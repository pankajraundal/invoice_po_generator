# Invoice & Purchase Order Document Generator

This project generates sample Invoice and Purchase Order documents in PDF, PNG, and JPG formats using Python. It is useful for testing document processing systems or for generating synthetic data for demos and development.

## Features
- Generates random Invoice and Purchase Order PDFs
- Converts PDFs to PNG and JPG images
- Uses realistic fake data for vendors, dates, and items
- Allows customization of vendor, owner, GST, date, and logo per document
- Accepts number of documents to generate as a command-line argument

## Prerequisites
- Python 3.7+

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pankajraundal/invoice_po_generator.git
   cd invoice_po_generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script to generate documents:
```bash
python generate_docs.py -n 20
```
This will create 20 sample Invoice and Purchase Order documents in the `sample_docs` folder, each in PDF, PNG, and JPG formats.

If you omit the `-n` argument, it will default to 5 documents:
```bash
python generate_docs.py
```

## Customization
- To use your own logo, set the `logo_path` variable in `generate_bulk_docs`.
- You can also pass your own vendor, owner, GST, and date values to `generate_invoice_pdf`.

## Output
- All generated files will be saved in the `sample_docs` directory.

## Cleaning Up Generated Files
To delete all generated files in the `sample_docs` directory, run:
```bash
rm -rf sample_docs/*
```
This will remove all PDFs, PNGs, and JPGs created by the script.

## License
This project is for educational and testing purposes.
