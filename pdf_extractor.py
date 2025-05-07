import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_path):
    """Extract text from PDF and save to a text file."""
    print(f"Extracting text from: {pdf_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    
    # Extract text with page markers
    text_parts = ["Extracted text from: " + os.path.basename(pdf_path)]
    text_parts.append("=" * 50)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text_parts.append(f"\n\n{'=' * 20} Page {page_num + 1} {'=' * 20}\n\n")
        text_parts.append(page.get_text())
    
    # Close the PDF
    doc.close()
    
    # Write the extracted text to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_parts))
    
    print(f"Text extracted and saved to: {output_path}")

def main():
    # Define directories
    original_dir = 'Original'
    extracted_dir = 'Extracted_Text'
    
    # Create directories if they don't exist
    os.makedirs(original_dir, exist_ok=True)
    os.makedirs(extracted_dir, exist_ok=True)
    
    # Process each PDF in the Original directory
    for filename in os.listdir(original_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(original_dir, filename)
            output_filename = filename.replace('.pdf', '_extracted.txt')
            output_path = os.path.join(extracted_dir, output_filename)
            
            extract_text_from_pdf(pdf_path, output_path)

if __name__ == '__main__':
    main() 