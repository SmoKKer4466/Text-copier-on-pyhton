# Text Copier - OCR Image to Text Converter

A Python script that uses Tesseract OCR to extract text from images and copy it to clipboard. Supports multiple languages with automatic language pack download.

## Features

- 🖼️ **Image to Text Conversion**: Extract text from images using OCR
- 🌍 **Multi-language Support**: Support for 10+ languages including English, Russian, Ukrainian, German, French, Spanish, Italian, Polish, Chinese (Simplified), and Japanese
- 📋 **Automatic Clipboard Copy**: Extracted text is automatically copied to clipboard
- 📦 **Auto-download Language Packs**: Automatically downloads missing Tesseract language packs
- 🛠️ **Easy Setup**: Step-by-step installation guide with manual fallback options

## Prerequisites

### Required Software
1. **Python 3.6+** - Download from [python.org](https://www.python.org/downloads/)
2. **Tesseract OCR** - Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

### Python Dependencies
```bash
pip install pillow pytesseract pyperclip
```

## Installation

### 1. Install Tesseract OCR
- Download Tesseract installer for Windows from [here](https://github.com/UB-Mannheim/tesseract/wiki)
- Install to default location: `C:\Program Files\Tesseract-OCR\`
- Make sure to check "Additional language data" during installation if you need non-English languages

### 2. Install Python Dependencies
Open Command Prompt or PowerShell and run:
```bash
pip install pillow pytesseract pyperclip
```

### 3. Download the Script
Save the `textcopier.py` file to your desired location.

## Usage

### Basic Usage
1. Open Command Prompt or PowerShell
2. Navigate to the script directory
3. Run the script:
   ```bash
   python textcopier.py
   ```

### Step-by-Step Process

1. **Language Selection**
   - The script will show available installed languages
   - Choose from the menu (0-10) or enter custom language codes
   - Multiple languages can be selected:
     - Comma-separated numbers: `1,2` (English + Russian)
     - Plus-separated codes: `rus+eng`
   - If a language is not installed, the script will offer to download it automatically

2. **Image Input**
   - Enter the full path to your image file
   - Supported formats: PNG, JPG, JPEG, TIFF, BMP, GIF
   - Example: `C:\Users\YourName\Pictures\screenshot.png`

3. **Text Extraction**
   - The script will process the image and extract text
   - Extracted text will be displayed in the console
   - Text is automatically copied to clipboard for easy pasting

## Language Support

| Code | Language | Auto-download |
|------|----------|---------------|
| eng | English | ✅ (pre-installed) |
| rus | Russian | ✅ |
| ukr | Ukrainian | ✅ |
| deu | German | ✅ |
| fra | French | ✅ |
| spa | Spanish | ✅ |
| ita | Italian | ✅ |
| pol | Polish | ✅ |
| chi_sim | Chinese (Simplified) | ✅ |
| jpn | Japanese | ✅ |

## Manual Language Installation

If automatic download fails (permission issues), you can install languages manually:

### Option 1: PowerShell as Administrator
1. Press `Win + X` and select "Windows PowerShell (Admin)"
2. Run commands for desired languages:

```powershell
# Russian
Invoke-WebRequest -Uri "https://github.com/tesseract-ocr/tessdata/raw/main/rus.traineddata" -OutFile "C:\Program Files\Tesseract-OCR\tessdata\rus.traineddata"

# Ukrainian
Invoke-WebRequest -Uri "https://github.com/tesseract-ocr/tessdata/raw/main/ukr.traineddata" -OutFile "C:\Program Files\Tesseract-OCR\tessdata\ukr.traineddata"

# German
Invoke-WebRequest -Uri "https://github.com/tesseract-ocr/tessdata/raw/main/deu.traineddata" -OutFile "C:\Program Files\Tesseract-OCR\tessdata\deu.traineddata"

# French
Invoke-WebRequest -Uri "https://github.com/tesseract-ocr/tessdata/raw/main/fra.traineddata" -OutFile "C:\Program Files\Tesseract-OCR\tessdata\fra.traineddata"
```

### Option 2: Manual Download
1. Go to [Tesseract Language Data Repository](https://github.com/tesseract-ocr/tessdata)
2. Download the `.traineddata` files for your languages
3. Copy them to `C:\Program Files\Tesseract-OCR\tessdata\`

## Troubleshooting

### Common Issues

**"Tesseract not found" error:**
- Ensure Tesseract is installed in `C:\Program Files\Tesseract-OCR\`
- If installed elsewhere, update the path in the script:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"YOUR_PATH\tesseract.exe"
  ```

**Permission denied when downloading languages:**
- Run the script as administrator
- Or download language files manually (see Manual Installation)

**Poor text recognition:**
- Ensure image has good quality and contrast
- Try using multiple languages: `eng+rus` for mixed text
- Use images with clear, readable text

**"File not found" error:**
- Check the image path is correct
- Use full absolute path
- Remove quotes if copying path from file explorer

### Supported Image Formats
- PNG (recommended for screenshots)
- JPEG/JPG
- TIFF
- BMP
- GIF

### Tips for Better OCR Results
- Use high-resolution images
- Ensure good contrast between text and background
- Avoid rotated or skewed text
- Use images with clear, readable fonts
- For screenshots, use PNG format

## Examples

### Single Language (English)
```
Select languages (0 - English): 0
Enter image path: C:\Users\SmoKKer\Pictures\english_text.png
```

### Multiple Languages (Russian + English)
```
Select languages (0 - English): 2,1
Enter image path: C:\Users\SmoKKer\Pictures\mixed_text.png
```

### Custom Language Codes
```
Select languages (0 - English): rus+eng+deu
Enter image path: C:\Users\SmoKKer\Pictures\multilingual.png
```

## License

This script is provided as-is for educational and personal use. Make sure to comply with Tesseract OCR license terms.

## Dependencies Credits

- **Tesseract OCR** - Google's open source OCR engine
- **Pillow** - Python Imaging Library fork
- **pytesseract** - Python wrapper for Tesseract
- **pyperclip** - Cross-platform clipboard functionality
