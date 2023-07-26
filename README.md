# PDF-Grid-Composer

PDF-Grid-Composer is a Python utility for merging multiple PDF files into a grid-like layout. It allows you to take a collection of PDF pages and arrange them in a specified grid pattern on a new PDF page. This can be especially useful when you need to print multiple pages on a single sheet or when you want to create a booklet-style PDF.

## How It Works

The PDF-Grid-Composer script uses the PyPDF2 library to handle PDF operations. It takes a directory containing input PDF files and processes each file, creating a new PDF file with the pages arranged in a grid. The script automatically calculates the appropriate scale and positioning for each page to fit within the grid cells.

## Features

- Merge multiple PDF files into a single grid-style PDF page.
- Customizable padding between pages to ensure readability and aesthetics.
- Automatic scaling to fit pages within the grid cells while maintaining aspect ratio.
- Supports various grid configurations, including 2x2, 3x3, and more.
- Works with both portrait and landscape orientation pages.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. The script has been tested with Python 3.7 and above.

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/faisal-saddique/PDF-Grid-Composer.git
   ```

2. Install the required dependencies:

   ```
   pip install PyPDF2
   ```

### Usage

1. Prepare your input PDF files and place them in a directory (e.g., `input_pdfs`).

2. Open a terminal or command prompt and navigate to the repository's root directory.

3. Run the PDF-Grid-Composer script with the following command:

   ```
   python pdf_grid_composer.py
   ```

4. The script will process the PDF files from the `input_pdfs` directory and generate merged PDF files in a new directory called `output_pdfs`.

5. You can customize the grid layout and padding by modifying the `pdf_grid_composer.py` script according to your preferences.

## Example

Suppose you have a PDF file `document1.pdf` having 4 pages, after running the script, the resulting output might look like this:

![Example Output](/images/example_output.png)

## Contributing

Contributions to PDF-Grid-Composer are welcome! If you find a bug, have an enhancement in mind, or want to propose a new feature, please open an issue or submit a pull request.

## License

PDF-Grid-Composer is open-source software licensed under the [MIT License](/LICENSE).

## Acknowledgments

PDF-Grid-Composer was inspired by the need to efficiently merge and layout PDF pages for various printing and publishing needs.

---

Thank you for your interest in PDF-Grid-Composer. If you have any questions or feedback, please don't hesitate to get in touch. Happy PDF composing!