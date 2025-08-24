import random
from faker import Faker
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pdf2image import convert_from_path
import os
import argparse

fake = Faker()

OUTPUT_DIR = "sample_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_invoice_pdf(file_path, doc_type="Invoice", vendor_name=None, vendor_address=None, owner_name=None, owner_address=None, gst_number=None, date=None, logo_path=None):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Logo (pass logo_path as argument, draw placeholder if None)
    if logo_path:
        try:
            c.drawImage(logo_path, 50, height-90, width=80, height=40, preserveAspectRatio=True, mask='auto')
        except Exception:
            c.setFillColorRGB(0.8, 0.8, 0.8)
            c.rect(50, height-90, 80, 40, fill=1, stroke=0)
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(55, height-75, "LOGO")
    else:
        c.setFillColorRGB(0.8, 0.8, 0.8)
        c.rect(50, height-90, 80, 40, fill=1, stroke=0)
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(55, height-75, "LOGO")

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height-50, f"{doc_type}")
    c.setFont("Helvetica", 10)
    doc_number = random.randint(1000,9999)
    c.drawString(150, height-70, f"{doc_type} Number: {doc_number}")
    c.drawString(150, height-85, f"Date of Issue: {date}")
    c.drawString(350, height-85, f"Due Date: {fake.date_this_year()}")

    # Vendor/Buyer/Customer Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, height-110, "Vendor:")
    c.setFont("Helvetica", 10)
    c.drawString(120, height-110, vendor_name)
    c.drawString(120, height-125, vendor_address)
    c.drawString(120, height-140, f"GSTIN: {gst_number}")
    c.drawString(120, height-155, f"PAN: {fake.bothify('?????#####?')}")
    c.drawString(120, height-170, f"Contact: {fake.phone_number()} | {fake.email()}")

    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, height-190, "Owner/Customer:")
    c.setFont("Helvetica", 10)
    c.drawString(170, height-190, owner_name)
    c.drawString(170, height-205, owner_address)
    c.drawString(170, height-220, f"GSTIN: {fake.bothify('##AAAA####A1Z#')}")
    c.drawString(170, height-235, f"PAN: {fake.bothify('?????#####?')}")
    c.drawString(170, height-250, f"Contact: {fake.phone_number()} | {fake.email()}")

    # Bank Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(350, height-110, "Bank Details:")
    c.setFont("Helvetica", 10)
    c.drawString(350, height-125, f"A/C No: {fake.bban()}")
    c.drawString(350, height-140, f"IFSC: {fake.bothify('ABCD0#####')}")
    c.drawString(350, height-155, f"Bank: {fake.company()}")

    # Table Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height-280, "Description")
    c.drawString(200, height-280, "HSN/SAC")
    c.drawString(270, height-280, "Qty")
    c.drawString(320, height-280, "Unit Price")
    c.drawString(400, height-280, "Amount")

    c.setFont("Helvetica", 10)
    y = height-300
    total = 0
    for _ in range(random.randint(3,6)):
        desc = fake.bs().title()
        hsn = fake.bothify('######')
        qty = random.randint(1,10)
        price = round(random.uniform(10,200),2)
        amount = qty*price
        total += amount

        c.drawString(50, y, desc[:30])
        c.drawString(200, y, hsn)
        c.drawString(270, y, str(qty))
        c.drawString(320, y, f"{price:.2f}")
        c.drawString(400, y, f"{amount:.2f}")
        y -= 20

    # Subtotal, Discount, Tax, Shipping, Total
    subtotal = total
    discount = round(subtotal * 0.05, 2)
    taxable = subtotal - discount
    cgst = round(taxable * 0.09, 2)
    sgst = round(taxable * 0.09, 2)
    igst = round(taxable * 0.18, 2) if random.choice([True, False]) else 0
    shipping = round(random.uniform(50, 200), 2)
    grand_total = taxable + cgst + sgst + igst + shipping

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y-20, f"Subtotal: {subtotal:.2f}")
    c.drawString(200, y-20, f"Discount: {discount:.2f}")
    c.drawString(320, y-20, f"Taxable: {taxable:.2f}")
    c.drawString(50, y-40, f"CGST: {cgst:.2f}")
    c.drawString(200, y-40, f"SGST: {sgst:.2f}")
    c.drawString(320, y-40, f"IGST: {igst:.2f}")
    c.drawString(400, y-40, f"Shipping: {shipping:.2f}")
    c.drawString(320, y-60, f"Total: {grand_total:.2f}")

    # Payment Terms & Method
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y-80, "Payment Terms:")
    c.setFont("Helvetica", 10)
    c.drawString(170, y-80, "Net 30 days | Bank Transfer | UPI")

    # Authorized Signature
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y-100, "Authorized Signature:")
    c.setFont("Helvetica", 10)
    c.drawString(200, y-100, fake.name())

    # Notes/Terms & Conditions
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y-120, "Notes:")
    c.setFont("Helvetica", 10)
    c.drawString(120, y-120, "Thank you for your business. Subject to jurisdiction.")

    c.showPage()
    c.save()

def generate_bulk_docs(n=5):
    for i in range(n):
        doc_type = random.choice(["Invoice", "Purchase Order"])
        pdf_path = os.path.join(OUTPUT_DIR, f"{doc_type}_{i+1}.pdf")

        # Generate random values for each document
        vendor_name = fake.company()
        vendor_address = fake.address().replace("\n", ", ")
        owner_name = fake.company()
        owner_address = fake.address().replace("\n", ", ")
        gst_number = f"GSTIN: {fake.bothify('##AAAA####A1Z#')}"
        date = fake.date_this_year()
        logo_path = None  # Set to your logo file path if available

        generate_invoice_pdf(
            pdf_path,
            doc_type,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            owner_name=owner_name,
            owner_address=owner_address,
            gst_number=gst_number,
            date=date,
            logo_path=logo_path
        )

        # Convert to images
        images = convert_from_path(pdf_path)
        for j, img in enumerate(images):
            img.save(pdf_path.replace(".pdf", f"_{j+1}.png"), "PNG")
            img.save(pdf_path.replace(".pdf", f"_{j+1}.jpg"), "JPEG")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate sample Invoice and PO documents.")
    parser.add_argument("-n", "--num", type=int, default=5, help="Number of documents to generate")
    args = parser.parse_args()
    generate_bulk_docs(args.num)
