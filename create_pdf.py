from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.colors import black, gray
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import os
import re

def clean_text(text):
    """Clean the text by removing sequence numbers and formatting disclaimer."""
    # Remove sequence numbers (more aggressive pattern)
    text = re.sub(r'\b\d+[\.-]\s*', '', text)  # Matches numbers followed by . or - and spaces
    text = re.sub(r'\b\d+\s+(?=[A-Z])', '', text)  # Matches standalone numbers before capital letters
    
    # Format disclaimer by adding line breaks and extra spacing after each sentence
    if "Disclaimer" in text:
        disclaimer_pattern = r'(Disclaimer.*?purposes\.)'
        disclaimer_match = re.search(disclaimer_pattern, text, re.DOTALL)
        if disclaimer_match:
            disclaimer = disclaimer_match.group(1)
            # Add double line breaks after each sentence in disclaimer
            formatted_disclaimer = re.sub(r'([.!?])\s+', r'\1\n\n', disclaimer)
            # Ensure proper spacing between disclaimer sections
            formatted_disclaimer = formatted_disclaimer.replace('\n\n\n', '\n\n')
            text = text.replace(disclaimer, formatted_disclaimer)
    
    return text

def create_formatted_pdf(input_file, output_file):
    # Read the formatted text
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Clean the text
    text = clean_text(text)
    
    # Create PDF document with 1-inch margins
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=inch,
        bottomMargin=inch
    )
    
    # Create custom style
    styles = getSampleStyleSheet()
    normal_style = ParagraphStyle(
        'CustomNormal',
        fontName='Times-Roman',  # Using built-in Times-Roman font
        fontSize=12,
        leading=18,  # 1.5 line spacing (12pt * 1.5 = 18)
        alignment=0,  # 0=left, 1=center, 2=right, 4=justified
        spaceAfter=12,
        spaceBefore=0,
    )
    
    # Process text into paragraphs
    story = []
    paragraphs = text.split('\n\n')
    
    for para in paragraphs:
        if para.strip():
            p = Paragraph(para.strip(), normal_style)
            story.append(p)
            story.append(Spacer(1, 12))
    
    # Build the PDF
    doc.build(story)

def main():
    # Create output directory if it doesn't exist
    if not os.path.exists('Extracted_Text'):
        os.makedirs('Extracted_Text')
    
    # Process each formatted text file
    input_dir = 'Extracted_Text'
    for filename in os.listdir(input_dir):
        if filename.endswith('_formatted.txt'):
            input_path = os.path.join(input_dir, filename)
            output_filename = filename.replace('_formatted.txt', '.pdf')
            output_path = os.path.join(input_dir, output_filename)
            
            create_formatted_pdf(input_path, output_path)
            print(f"Created PDF: {output_filename}")

if __name__ == '__main__':
    main() 