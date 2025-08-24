# Invoice & Purchase Order Document Generator

This project generates sample Invoice and Purchase Order documents in PDF, PNG, and JPG formats using Python. It is useful for testing document processing systems or for generating synthetic data for demos and development.

## Features
- Generates random Invoice and Purchase Order PDFs
- Converts PDFs to PNG and JPG images
- Uses realistic fake data for vendors, dates, and items

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
python generate_docs.py
```

This will create 50 sample Invoice and Purchase Order documents in the `sample_docs` folder, each in PDF, PNG, and JPG formats.

## Customization
- To change the number of documents generated, edit the last line in `generate_docs.py`:
  ```python
  generate_bulk_docs(50)  # Change 50 to desired number
  ```

## Output
- All generated files will be saved in the `sample_docs` directory.

## License
This project is for educational and testing purposes.
