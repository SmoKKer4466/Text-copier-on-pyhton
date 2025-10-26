from PIL import Image
import pytesseract
import pyperclip
import os
import urllib.request

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_available_languages():
    """Checks which languages are available in Tesseract"""
    tessdata_path = r"C:\Program Files\Tesseract-OCR\tessdata"
    available = []
    
    if os.path.exists(tessdata_path):
        for file in os.listdir(tessdata_path):
            if file.endswith('.traineddata') and file != 'osd.traineddata':
                lang_code = file.replace('.traineddata', '')
                available.append(lang_code)
    
    return available

def download_language_pack(lang_code):
    """Downloads language pack for Tesseract"""
    tessdata_path = r"C:\Program Files\Tesseract-OCR\tessdata"
    url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
    file_path = os.path.join(tessdata_path, f"{lang_code}.traineddata")
    
    try:
        print(f"Downloading {lang_code}.traineddata...")
        urllib.request.urlretrieve(url, file_path)
        print(f"✅ Language {lang_code} successfully installed!")
        return True
    except PermissionError:
        print(f"❌ No write permissions for {tessdata_path}")
        print("💡 Solutions:")
        print("1. Run PowerShell/CMD as administrator")
        print("2. Or download file manually:")
        print(f"   URL: {url}")
        print(f"   Save as: {file_path}")
        print("3. Or use English only (choice 0)")
        return False
    except Exception as e:
        print(f"❌ Error downloading {lang_code}: {e}")
        return False

def manual_language_setup():
    """Shows instructions for manual language installation"""
    print("\n=== Manual Language Pack Installation ===")
    print("1. Open PowerShell as administrator:")
    print("   - Press Win + X")
    print("   - Select 'Windows PowerShell (Admin)'")
    print("\n2. Execute commands to download languages:")
    
    languages = {
        "rus": "Russian",
        "ukr": "Ukrainian", 
        "deu": "German",
        "fra": "French"
    }
    
    for code, name in languages.items():
        print(f"\n# {name} ({code}):")
        print(f'Invoke-WebRequest -Uri "https://github.com/tesseract-ocr/tessdata/raw/main/{code}.traineddata" -OutFile "C:\\Program Files\\Tesseract-OCR\\tessdata\\{code}.traineddata"')
    
    print("\n3. After installation, restart this script")
    input("\nPress Enter to continue...")

available_langs = get_available_languages()
print(f"Installed languages: {', '.join(available_langs)}")
language_info = {
    "1": ("eng", "English"),
    "2": ("rus", "Russian"),
    "3": ("ukr", "Ukrainian"),
    "4": ("deu", "German"),
    "5": ("fra", "French"),
    "6": ("spa", "Spanish"),
    "7": ("ita", "Italian"),
    "8": ("pol", "Polish"),
    "9": ("chi_sim", "Chinese (Simplified)"),
    "10": ("jpn", "Japanese"),
    "0": ("eng", "English only (installed)")
}

print("\n=== Language Selection for Recognition ===")
for key, (code, name) in language_info.items():
    status = "✅" if code in available_langs or code == "eng" else "❌ (need to download)"
    print(f"{key}. {name} {status}")

print("\nYou can select multiple languages separated by commas (e.g.: 1,2)")
print("Or enter language codes with + (e.g.: rus+eng)")
print("Enter 'help' for manual language installation instructions")

choice = input("\nSelect languages (0 - English): ").strip()

if choice.lower() == "help":
    manual_language_setup()
    print("\n=== Language Selection for Recognition ===")
    for key, (code, name) in language_info.items():
        status = "✅" if code in available_langs or code == "eng" else "❌ (нужно скачать)"
        print(f"{key}. {name} {status}")
    choice = input("\nSelect languages (0 - English): ").strip()

if choice == "0" or choice == "":
    selected_lang = "eng"
elif "+" in choice:
    selected_lang = choice
elif "," in choice:
    selected_codes = []
    for num in choice.split(","):
        num = num.strip()
        if num in language_info:
            lang_code = language_info[num][0]
            if lang_code not in available_langs and lang_code != "eng":
                download = input(f"Language {lang_code} not installed. Download? (y/n): ")
                if download.lower() == 'y':
                    if download_language_pack(lang_code):
                        available_langs.append(lang_code)
                    else:
                        continue
                else:
                    continue
            selected_codes.append(lang_code)
    selected_lang = "+".join(selected_codes) if selected_codes else "eng"
else:
    if choice in language_info:
        lang_code = language_info[choice][0]
        if lang_code not in available_langs and lang_code != "eng":
            download = input(f"Язык {lang_code} не установлен. Скачать? (y/n): ")
            if download.lower() == 'y':
                if download_language_pack(lang_code):
                    selected_lang = lang_code
                else:
                    selected_lang = "eng"
            else:
                selected_lang = "eng"
        else:
            selected_lang = lang_code
    else:
        print("Invalid choice, using English")
        selected_lang = "eng"

print(f"Selected languages: {selected_lang}")

image_path = input("\nEnter image path: ").strip('"\'')

try:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=selected_lang)
    
    print("\n=== Recognized Text ===\n")
    print(text)
    try:
        pyperclip.copy(text)
        print("\n✅ Text copied to clipboard.")
    except ImportError:
        print("\nℹ️ Install 'pyperclip' if you want text to be copied automatically: pip install pyperclip")

except FileNotFoundError:
    print("❌ File not found. Check the image path.")
except pytesseract.TesseractError as e:
    print(f"❌ Tesseract error: {e}")
    print("💡 Try using English only (choice 0)")
except Exception as e:
    print(f"❌ An error occurred: {e}")
