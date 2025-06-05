
from fpdf import FPDF
from datetime import datetime

def generate_verification_report(doc_id, fingerprint, output_path="verification_report.pdf"):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.set_text_color(40, 40, 40)
    pdf.cell(200, 10, txt="Digital Verification Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    report_text = f"""
Document ID: {doc_id}

SHA-256 Fingerprint:
{fingerprint}

Result: Signature Verified Successfully
Issuer: Aur Digital Verification
Date: {date}
"""
    pdf.multi_cell(0, 10, txt=report_text)

    pdf.output(output_path)
    return output_path

# Test
if __name__ == "__main__":
    doc_id = "8EKDPLB*adecgh+"
    fingerprint = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
    path = generate_verification_report(doc_id, fingerprint)
    print("Report generated at:", path)
