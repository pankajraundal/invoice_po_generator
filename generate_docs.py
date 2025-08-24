import random
from faker import Faker
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pdf2image import convert_from_path
import os

fake = Faker()

OUTPUT_DIR = "sample_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_invoice_pdf(file_path, doc_type="Invoice"):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height-50, f"{doc_type}")
    c.setFont("Helvetica", 10)
    c.drawString(50, height-70, f"{doc_type} Number: {random.randint(1000,9999)}")
    c.drawString(50, height-85, f"Date: {fake.date_this_year()}")
    c.drawString(50, height-100, f"Vendor: {fake.company()}")

    # Table
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height-140, "Description")
    c.drawString(250, height-140, "Qty")
    c.drawString(300, height-140, "Unit Price")
    c.drawString(400, height-140, "Amount")

    c.setFont("Helvetica", 10)
    y = height-160
    total = 0
    for _ in range(random.randint(3,6)):
        desc = fake.bs().title()
        qty = random.randint(1,10)
        price = round(random.uniform(10,200),2)
        amount = qty*price
        total += amount

        c.drawString(50, y, desc[:30])
        c.drawString(250, y, str(qty))
        c.drawString(300, y, f"{price:.2f}")
        c.drawString(400, y, f"{amount:.2f}")
        y -= 20

    # Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, y-20, "Total:")
    c.drawString(400, y-20, f"{total:.2f}")

    c.showPage()
    c.save()

def generate_bulk_docs(n=50):
    for i in range(n):
        doc_type = random.choice(["Invoice", "Purchase Order"])
        pdf_path = os.path.join(OUTPUT_DIR, f"{doc_type}_{i+1}.pdf")
        generate_invoice_pdf(pdf_path, doc_type)

        # Convert to images
        images = convert_from_path(pdf_path)
        for j, img in enumerate(images):
            img.save(pdf_path.replace(".pdf", f"_{j+1}.png"), "PNG")
            img.save(pdf_path.replace(".pdf", f"_{j+1}.jpg"), "JPEG")

# Generate 50 docs
generate_bulk_docs(50)
