import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PageObject
from PyPDF2 import Transformation

# Set padding size
PADDING = 20

def merge_pages(pdf_path, output_path):

    pdf_reader = PdfReader(pdf_path)
    pdf_writer = PdfWriter()
    num_pages = len(pdf_reader.pages)

    for i in range(0, num_pages, 4):

        # Create output page
        output_page = PageObject.create_blank_page(
            width=pdf_reader.pages[0].mediabox.width,
            height=pdf_reader.pages[0].mediabox.height
        )

        # Calculate scaled page size with padding 
        page_width = (output_page.mediabox.width - 3*PADDING) / 2
        page_height = (output_page.mediabox.height - 3*PADDING) / 2

        if i < num_pages:
            # Page 1
            pdf_reader.pages[i].add_transformation(
                Transformation().scale(page_width/pdf_reader.pages[0].mediabox.width))
            pdf_reader.pages[i].add_transformation(
                Transformation().translate(PADDING, page_height + 2*PADDING))
            output_page.merge_page(pdf_reader.pages[i])

        if i + 1 < num_pages:
            # Page 2
            pdf_reader.pages[i+1].add_transformation(
                Transformation().scale(page_width/pdf_reader.pages[0].mediabox.width))
            pdf_reader.pages[i+1].add_transformation(
                Transformation().translate(page_width + 2*PADDING, page_height + 2*PADDING))
            output_page.merge_page(pdf_reader.pages[i+1])

        if i + 2 < num_pages:  
            # Page 3
            pdf_reader.pages[i+2].add_transformation(
                Transformation().scale(page_height/pdf_reader.pages[0].mediabox.height))
            pdf_reader.pages[i+2].add_transformation(
                Transformation().translate(PADDING, PADDING))
            output_page.merge_page(pdf_reader.pages[i+2])

        if i + 3 < num_pages:
            # Page 4
            pdf_reader.pages[i+3].add_transformation(
                Transformation().scale(page_height/pdf_reader.pages[0].mediabox.height))
            pdf_reader.pages[i+3].add_transformation(
                Transformation().translate(page_width + 2*PADDING, PADDING))
            output_page.merge_page(pdf_reader.pages[i+3])

        pdf_writer.add_page(output_page)

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)


def process_directory(input_directory, output_directory):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            merge_pages(input_path, output_path)


if __name__ == "__main__":

    input_directory = "./input_pdfs"
    output_directory = "./output_pdfs"

    process_directory(input_directory, output_directory)
