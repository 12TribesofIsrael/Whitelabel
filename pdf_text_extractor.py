import os
import fitz  # PyMuPDF
import sys

def create_output_directory():
    """Create the Extracted_Text directory if it doesn't exist."""
    output_dir = "Extracted_Text"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    return output_dir

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        text = ""
        
        # Extract text from each page
        for page in doc:
            text += page.get_text()
        
        # Close the document
        doc.close()
        return text
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return None

def main():
    # Define input and output directories
    input_dir = "Orginal"  # Using the existing folder name
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' not found!")
        sys.exit(1)
    
    # Create output directory
    output_dir = create_output_directory()
    
    # Get list of PDF files
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir} directory!")
        sys.exit(1)
    
    # Process each PDF file
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file}")
        
        # Construct full path for input PDF
        pdf_path = os.path.join(input_dir, pdf_file)
        
        # Extract text from PDF
        extracted_text = extract_text_from_pdf(pdf_path)
        
        if extracted_text:
            # Create output filename (change extension from .pdf to .txt)
            txt_filename = os.path.splitext(pdf_file)[0] + '.txt'
            txt_path = os.path.join(output_dir, txt_filename)
            
            # Save extracted text to file
            try:
                with open(txt_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write(extracted_text)
                print(f"Successfully created: {txt_filename}")
            except Exception as e:
                print(f"Error saving {txt_filename}: {str(e)}")
        else:
            print(f"Failed to extract text from {pdf_file}")

if __name__ == "__main__":
    print("Starting PDF text extraction process...")
    main()
    print("Process completed!") 