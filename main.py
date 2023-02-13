from PyPDF2 import PdfReader
import csv
from io import StringIO
import re
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox


# creating a pdf reader object
def main(FILENAME):
    reader = PdfReader(FILENAME)

    # getting a specific page from the pdf file
    page = reader.pages[0]

    # extracting text from page
    lines= page.extract_text()
    text = re.sub(r'\xa0', ' ', lines)
    text = text.splitlines()
    criteria = [
        "Area",
        "Image quality",
        "Total hair count",
        "Hair density",
        "Anagen hairs",
        "Telogen hairs",
        "Hair length median",
        "Hair mass",
        "Hair thickness median",
        "Hair thickness mean",
        "Density vellus hairs",
        "Density terminal hairs",
        "Ratio vellus hairs",
        "Ratio terminal hairs"
    ]
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for sentence in text:
            # check if any of the words are in the sentence
            if any(word in sentence for word in criteria):
                # write the sentence to the CSV file
                if '²' in sentence:
                    sentence =sentence.replace("²", "SQ")
                if 'µm' in sentence:
                    sentence =sentence.replace("µm", "micrometer")
                writer.writerow([sentence])
                print(sentence)

def choose_file():
    file_path = filedialog.askopenfilename(title = "Select file", filetypes = (("PDF files", "*.pdf"), ("all files", "*.*")))
    if file_path:
        main(file_path)
        tkinter.messagebox.showinfo("Completed", "File processing completed!")

root = tk.Tk()
root.title("PDF File Processor")

choose_file_button = tk.Button(text="Choose File", command=choose_file)
choose_file_button.pack()

root.mainloop()
