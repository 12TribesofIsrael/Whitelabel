import re
import os

def clean_repeated_sections(text):
    """Remove repeated disclaimer sections and clean up formatting."""
    # Get unique paragraphs while preserving order
    seen_paragraphs = set()
    unique_paragraphs = []
    
    # Split by double newline to separate paragraphs
    paragraphs = text.split('\n\n')
    
    for para in paragraphs:
        # Clean up the paragraph
        para = para.strip()
        if not para:
            continue
            
        # Skip page markers and dividers
        if re.match(r'^={10,}.*?={10,}$', para) or re.match(r'^Page \d+$', para):
            continue
            
        # Skip repeated disclaimers
        if "Disclaimer This E-book" in para and para in seen_paragraphs:
            continue
            
        # Skip page numbers
        if para.strip().isdigit():
            continue
            
        # Skip website URL if it appears alone
        if para.strip().startswith('Visit us @'):
            continue
            
        # Add to unique paragraphs if not seen before
        if para not in seen_paragraphs:
            seen_paragraphs.add(para)
            unique_paragraphs.append(para)
    
    return unique_paragraphs

def format_section_headers(text):
    """Format section headers in all caps with proper spacing."""
    # Add extra newlines before all-caps headers
    text = re.sub(r'(?m)^([A-Z][A-Z\s]{10,}[A-Z])$', r'\n\n\1\n', text)
    return text

def format_lists(text):
    """Format numbered lists and bullet points."""
    # Format numbered lists (e.g., "1.Something" to "1. Something")
    text = re.sub(r'(?m)^(\d+\.)([^\s])', r'\1 \2', text)
    
    # Format bullet points
    text = re.sub(r'(?m)^[-•]\s*', '• ', text)
    return text

def format_contact_info(text):
    """Format contact information blocks with proper spacing."""
    # Add proper spacing for address blocks
    text = re.sub(r'([A-Z]{2}\s+\d{5}(?:-\d{4})?)\n(?=[A-Za-z])', r'\1\n\n', text)
    return text

def format_text(input_file, output_file):
    """Format the text according to book formatting standards."""
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove page markers and metadata
    text = re.sub(r'={20} Page \d+ ={20}', '', text)
    text = re.sub(r'^Extracted text from:.*?\n', '', text)
    text = re.sub(r'={50,}', '', text)
    
    # Get unique paragraphs
    paragraphs = clean_repeated_sections(text)
    
    # Join paragraphs with proper spacing
    text = '\n\n'.join(paragraphs)
    
    # Apply formatting
    text = format_section_headers(text)
    text = format_lists(text)
    text = format_contact_info(text)
    
    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    # Write the formatted text
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Created formatted text file: {output_file}")

def main():
    input_dir = 'Extracted_Text'
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    
    # Process each extracted text file
    for filename in os.listdir(input_dir):
        if filename.endswith('_extracted.txt'):
            input_path = os.path.join(input_dir, filename)
            output_filename = filename.replace('_extracted.txt', '_formatted.txt')
            output_path = os.path.join(input_dir, output_filename)
            
            format_text(input_path, output_path)

if __name__ == '__main__':
    main() 