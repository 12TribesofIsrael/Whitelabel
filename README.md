# PDF Text Extraction and Reformatting Application

## Overview
This application allows you to extract text from PDF files, edit the content, and create new PDFs with proper formatting. The workflow is designed to be flexible, allowing for manual text editing between automated processing steps.

## Project Structure
```
White Label/
├── Original/                 # Place your source PDFs here
│   └── Master CR_Funding.pdf
├── Extracted_Text/          # Output directory
│   ├── *_extracted.txt      # Raw extracted text
│   ├── *_formatted.txt      # Formatted text
│   └── *.pdf               # Final formatted PDFs
├── pdf_extractor.py        # Text extraction script
├── format_text.py          # Text formatting script
└── create_pdf.py           # PDF creation script
```

## Requirements
- Python 3.x
- Required packages (install using pip):
  ```bash
  pip install PyMuPDF reportlab
  ```

## Step-by-Step Workflow

### 1. Prepare Your PDF
- Place your PDF file in the `Original` folder
- The file name will be preserved throughout the process
- Example: `Original/Master CR_Funding.pdf`

### 2. Extract Text (Step 1)
```bash
python pdf_extractor.py
```
This will:
- Read the PDF from the `Original` folder
- Extract all text content
- Create `*_extracted.txt` in the `Extracted_Text` folder
- Example: `Extracted_Text/Master CR_Funding_extracted.txt`

### 3. Edit Text Content (Manual Step)
- Open the `*_extracted.txt` file in your preferred text editor
- Make any necessary changes to the content:
  - Fix formatting issues
  - Correct text errors
  - Remove unwanted content
  - Add new content
- Save your changes

### 4. Format Text (Step 2)
```bash
python format_text.py
```
This will:
- Read your edited `*_extracted.txt` file
- Apply formatting rules:
  - Remove duplicate sections
  - Clean up spacing
  - Format paragraphs
  - Handle special sections (e.g., disclaimers)
- Create `*_formatted.txt` in the `Extracted_Text` folder

### 5. Create Final PDF (Step 3)
```bash
python create_pdf.py
```
This will:
- Read the `*_formatted.txt` file
- Apply PDF styling:
  - Set fonts and sizes
  - Apply paragraph spacing
  - Format headers and body text
- Create the final PDF in the `Extracted_Text` folder

## Tips and Best Practices

### Iterative Editing
1. You can repeat steps 3-5 as many times as needed
2. After editing the extracted text, just run:
   ```bash
   python format_text.py
   python create_pdf.py
   ```
3. Check the output PDF and repeat if necessary

### File Management
- Keep original PDFs in the `Original` folder
- Don't modify files in `Extracted_Text` except for `*_extracted.txt`
- Each new run will overwrite previous output files

### Common Tasks
1. **To start fresh with a new PDF:**
   - Place PDF in `Original` folder
   - Run all three scripts in sequence

2. **To make adjustments to existing text:**
   - Edit the `*_extracted.txt` file
   - Run format_text.py and create_pdf.py

3. **To process multiple PDFs:**
   - Place all PDFs in `Original` folder
   - Run scripts for each file

## Troubleshooting

### Common Issues
1. **Missing Text in Output**
   - Check the original PDF for searchable text
   - Ensure PDF is not scanned/image-based

2. **Formatting Issues**
   - Edit the extracted text file manually
   - Check for special characters or formatting marks

3. **Script Errors**
   - Ensure all required packages are installed
   - Check file permissions
   - Verify file paths and names

### Getting Help
- Check script error messages for specific issues
- Ensure all files are in the correct folders
- Verify file names match expected patterns

## Maintenance
- Keep Python packages updated
- Regularly backup your original files
- Clean up old output files as needed 