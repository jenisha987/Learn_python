        
#--Merge the PDF--

from pypdf import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf") #name of merged pdf file
merger.close()

# --Exercise 9, Shoutouts to Everyone using win32 API--
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    s = input("Type what you want to say : ")
    speaker.Speak(s)