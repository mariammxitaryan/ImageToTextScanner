import argparse
import easyocr
import os
import sys

# ==========================
#   OCR CLI TOOL MODULE
# ==========================
# This module provides a command-line interface for performing Optical Character Recognition (OCR)
# on image files using EasyOCR. It reads the specified image, processes it according to user-provided
# parameters, and outputs the recognized text (and optional bounding box details) to a .txt file.


def text_recognition(file_path, languages, detail, paragraph, contrast_ths, adjust_contrast):
    """
    Perform OCR on the given image file and save results to a text file.

    Parameters:
        file_path (str): Path to the input image file.
        languages (list of str): List of language codes for OCR (e.g., ['en', 'ru']).
        detail (int): 0 for text only, 1 for text with bounding boxes.
        paragraph (bool): Whether to group text into paragraphs.
        contrast_ths (float): Contrast threshold for preprocessing.
        adjust_contrast (float): Contrast adjustment factor.

    Returns:
        str: Path to the output text file containing OCR results.
    """
    # Validate input file
    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    # Initialize the OCR reader
    try:
        reader = easyocr.Reader(languages)
    except Exception as e:
        print(f"Error initializing OCR reader: {e}")
        sys.exit(1)

    # Perform OCR
    try:
        result = reader.readtext(
            file_path,
            detail=detail,
            paragraph=paragraph,
            contrast_ths=contrast_ths,
            adjust_contrast=adjust_contrast
        )
    except Exception as e:
        print(f"OCR failed: {e}")
        sys.exit(1)

    # Prepare output file
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base_name}_ocr_result.txt"

    # Write results
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for entry in result:
                if detail == 1 and isinstance(entry, (list, tuple)):
                    # Pretty-print bounding box and text
                    bbox, text = entry[0], entry[1]
                    f.write(f"Bounding Box: {bbox}\nText: {text}\n\n")
                else:
                    f.write(f"{entry}\n\n")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

    return output_file


def main():
    """
    Parse command-line arguments and invoke the OCR function.

    Arguments:
        image (str): Path to the input image file.
        -l, --languages (list): Languages for OCR (default: ['en']).
        --detail (int): 0 or 1 for level of detail (default: 0).
        --paragraph (flag): Group text into paragraphs.
        --contrast_ths (float): Contrast threshold (default: 0.1).
        --adjust_contrast (float): Contrast adjustment factor (default: 1.0).
    """
    parser = argparse.ArgumentParser(
        description="Perform OCR on an image and save results to a text file."
    )
    parser.add_argument("image", help="Path to the input image file.")
    parser.add_argument(
        "-l", "--languages", nargs='+', default=["en"],
        help="Languages to use for OCR (e.g., en ru)."
    )
    parser.add_argument(
        "--detail", type=int, choices=[0, 1], default=0,
        help="0: text only, 1: text with bounding boxes."
    )
    parser.add_argument(
        "--paragraph", action="store_true",
        help="Group recognized text into paragraphs."
    )
    parser.add_argument(
        "--contrast_ths", type=float, default=0.1,
        help="Contrast threshold for preprocessing."
    )
    parser.add_argument(
        "--adjust_contrast", type=float, default=1.0,
        help="Contrast adjustment factor."
    )

    args = parser.parse_args()

    print("Starting OCR...")
    output_file = text_recognition(
        args.image,
        args.languages,
        args.detail,
        args.paragraph,
        args.contrast_ths,
        args.adjust_contrast
    )
    print(f"OCR complete. Results saved to: {output_file}")


if __name__ == "__main__":
    main()
