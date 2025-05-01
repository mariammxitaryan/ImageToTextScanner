## EasyOCR CLI Tool

A simple command-line interface for performing Optical Character Recognition (OCR) on images using [EasyOCR](https://github.com/JaidedAI/EasyOCR).

### Features

- Specify one or more languages (e.g., `en`, `ru`, `fr`).
- Choose output detail level: plain text or text with bounding boxes.
- Optionally group detected text into paragraphs.
- Preprocess image contrast via threshold and adjustment parameters.
- Writes results to a text file named `<imagename>_ocr_result.txt`.

### Requirements

- Python 3.7 or higher
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- PyTorch (required by EasyOCR)
- NumPy

### Installation

1. **Clone the repository**

2. **Create & activate a virtual environment (recommended)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .\.venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

```bash
python ocr_tool.py <image_path> [options]
```

#### Options

- `-l, --languages`: List of language codes (default: `en`).
- `--detail`: `0` for text only, `1` for text with bounding boxes (default: `0`).
- `--paragraph`: Group recognized text into paragraphs.
- `--contrast_ths`: Contrast threshold for preprocessing (default: `0.1`).
- `--adjust_contrast`: Contrast adjustment factor (default: `1.0`).

#### Example

```bash
python ocr_tool.py sample.jpg -l en fr --detail 1 --paragraph --contrast_ths 0.2 --adjust_contrast 1.5
```

### Output

The OCR results will be saved to `sample_ocr_result.txt` in the current directory.

### Project Structure

```
ocr-cli/
├── ocr_tool.py      # Main OCR script
├── requirements.txt # Dependencies
├──README.md         # This file
└── .gitignore       # Ignored files
```

### .gitignore

```
__pycache__/
*.pyc
*.pyo
*.txt
.venv/
```

