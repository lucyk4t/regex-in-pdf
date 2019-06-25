import PyPDF2
import os
import shutil
import sys
import re

GM_folder = "./GM"

global_spec_pattern_tuple = [
    (r'(\d)* CFR (\w)*', 'CFR'),
    (r'ECE ((\w)*|(\d)*)', 'ECE'),
    (r'(\d)*/(\d)*/EEC', 'EEC'),
    (r'(\d)*/(\d)*/EC', 'EC'),
    (r'(\w)* NCAP', 'NCAP'),
    (r'FMVSS (\w)*', 'FMVSS'),
    (r'CMVSS (\w)*', 'CMVSS'),
    (r'KMVSS (\w)*', 'KMVSS'),
    (r'CONTRAN (\w)*', 'CONTRAN'),
    (r'(GB/(\w)*)|(GB(\d)*)', 'GB')
]

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


def mkcpfile(pattern, filepath):
    try:
        os.makedirs(r'./GM/' + pattern, exist_ok=True)
        shutil.copy(filepath, r'./GM/' + pattern)
    except FileExistsError:
        pass


def findpattern_pdf(content, filepath):
    for pattern, value in global_spec_pattern_tuple:
        pattern_compile = re.compile(pattern)

        if re.search(pattern_compile, content):
            mkcpfile(value, filepath)
        else:
            continue
    else:
        pass


def findpattern_docx(content, filepath):
    pass


def gatheringtext():
    for file in os.listdir(GM_folder):
        filepath = os.path.join(GM_folder, file)
        fp = open(filepath, 'rb')

        if file.endswith('.pdf'):
            readpdf = PyPDF2.PdfFileReader(filepath)
            numpages = readpdf.getNumPages()
            page = readpdf.getPage(0)
            content = page.extractText()
            findpattern_pdf(content, filepath)
        elif file.endswith('.doc'):
            pass
        else:
            continue
        fp.close()
    else:
        print(r'Done!')


gatheringtext()
