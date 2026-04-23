import pdfplumber 
#open pdf, reads each text and extract redeable text

def extract_text(pdf_path):
    text = "" #We create an empty container to store all text from the PDF

    with pdfplumber.open(pdf_path) as pdf: #Open the PDF file safely and Automatically close it after reading
        for page in pdf.pages: #read page by page
            if page.extract_text(): #Get readable text from each page
                text += page.extract_text() #Add all pages together into one big text

    return text #Send extracted text back to main program