from PyPDF3 import PdfFileReader
import sys
from gtts import gTTS
import os

def extract_information(pdf_path):
    testread = ""
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        testread = pdf.getPage(92).extractText().strip()
        print(pdf.getPage(92).extractText().strip())
        number_of_pages = pdf.getNumPages()

    # txt = f"""
    # Information about {pdf_path}: 

    # Author: {information.author}
    # Creator: {information.creator}
    # Producer: {information.producer}
    # Subject: {information.subject}
    # Title: {information.title}
    # Number of pages: {number_of_pages}
    # """
    print(testread)

    # define variables
    s = testread.strip()
    file = "file.mp3"

    # initialize tts, create mp3 and play
    tts = gTTS(s, 'en')
    tts.save(file)
    #os.system("mpg123 " + file)

    
    return information

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("Argument 1: {}".format(sys.argv[0]))
        print("Argument 2: {}".format(sys.argv[1]))
        print("Argument 2: {}".format(sys.argv[3]))
    else:
        print("No arguments passed.")

    path = '/home/dass/Downloads/Linux Bible Ninth Edition avxhome.se.pdf'
    extract_information(path)
