from PyPDF2 import PdfReader
import os


directory = "/run/user/1000/gvfs/smb-share:server=10.99.40.84,share=hackathon%20data/Medical Emergency Response Reports/"
local_copy = ""

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        text = ""
        try:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()

            with open(local_copy, "w") as f:
                f.write(text)
        except Exception as e:
            print(e)
