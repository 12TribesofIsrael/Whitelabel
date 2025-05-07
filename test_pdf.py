import fitz
import os

def test_pdf_extraction():
    # Path to the PDF file
    pdf_path = os.path.join("Orginal", "Master CR_Funding.pdf")
    
    # Check if file exists
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return
    
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        
        # Get the first page text as a test
        first_page = doc[0]
        text = first_page.get_text()
        
        # Print first 500 characters as a preview
        print("\nFirst 500 characters of text from the first page:")
        print("-" * 50)
        print(text[:500])
        print("-" * 50)
        
        # Print some document information
        print(f"\nDocument Information:")
        print(f"Number of pages: {len(doc)}")
        print(f"PDF Version: {doc.metadata.get('format', 'Unknown')}")
        
        # Close the document
        doc.close()
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")

if __name__ == "__main__":
    print("Starting PDF extraction test...")
    test_pdf_extraction()
    print("\nTest completed!") 