import argparse
import easyocr
import os

def text_recognition(file_path, languages, detail, paragraph, contrast_ths, adjust_contrast):
    reader = easyocr.Reader(languages)
    result = reader.readtext(
        file_path,
        detail=detail,
        paragraph=paragraph,
        contrast_ths=contrast_ths,
        adjust_contrast=adjust_contrast
    )

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = f"{base_name}_ocr_result.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in result:
            f.write(f"{line}\n\n")
    return output_file

def main():
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
        help="Group text into paragraphs."
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