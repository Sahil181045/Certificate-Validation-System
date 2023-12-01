from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pdfplumber

def generate_certificate(output_path, uid, candidate_name, course_name, org_name, institute_logo_path):
    # Create a PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter)

    # Create a list to hold the elements of the PDF
    elements = []

    # Add institute logo and institute name
    if institute_logo_path:
        logo = Image(institute_logo_path, width=150, height=150)
        elements.append(logo)

    # Add institute name
    institute_style = ParagraphStyle(
        "InstituteStyle",
        parent=getSampleStyleSheet()["Title"],
        fontName="Helvetica-Bold",
        fontSize=15,
        spaceAfter=40,
    )
    institute = Paragraph(org_name, institute_style)
    elements.extend([institute, Spacer(1, 12)])

    # Add title
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=getSampleStyleSheet()["Title"],
        fontName="Helvetica-Bold",
        fontSize=25,
        spaceAfter=20,
    )
    title1 = Paragraph("Certificate of Completion", title_style)
    elements.extend([title1, Spacer(1, 6)])

    # Add recipient name, UID, and course name with increased line space
    recipient_style = ParagraphStyle(
        "RecipientStyle",
        parent=getSampleStyleSheet()["BodyText"],
        fontSize=14,
        spaceAfter=6,
        leading=18,
        alignment=1
    )

    recipient_text = f"This is to certify that<br/><br/>\
                     <font color='red'> {candidate_name} </font><br/>\
                     with UID <br/> \
                    <font color='red'> {uid} </font> <br/><br/>\
                     has successfully completed the course:<br/>\
                     <font color='blue'> {course_name} </font>"

    recipient = Paragraph(recipient_text, recipient_style)
    elements.extend([recipient, Spacer(1, 12)])

    # Build the PDF document
    doc.build(elements)

    print(f"Certificate generated and saved at: {output_path}")


def extract_certificate(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Extract text from each page
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        lines = text.splitlines()

        org_name = lines[0]
        candidate_name = lines[3]
        uid = lines[5]
        course_name = lines[-1]

        return (uid, candidate_name, course_name, org_name)
    