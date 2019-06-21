import PyPDF2
import os
import shutil
import sys
import re

GM_folder = "./GM"
BMW_GS_folder = "./GS"

CFR_PATTERN = re.compile(r'(\d)* CFR (\w)*')
ECE_PATTERN = re.compile(r'ECE ((\w)*|(\d)*)')
EEC_PATTERN = re.compile(r'(\d)*/(\d)*/EEC')
EC_PATTERN = re.compile(r'(\d)*/(\d)*/EC')
NCAP_PATTERN = re.compile(r'(\w)* NCAP')
FMVSS_PATTERN = re.compile(r'FMVSS (\w)*')
CMVSS_PATTERN = re.compile(r'CMVSS (\w)*')
KMVSS_PATTERN = re.compile(r'KMVSS (\w)*')
CONTRAN_PATTERN = re.compile(r'CONTRAN (\w)*')
GB_PATTERN = re.compile(r'(GB/(\w)*)|(GB(\d)*)')

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
    if CFR_PATTERN.findall(content):
        mkcpfile('CFR', filepath)
    if ECE_PATTERN.findall(content):
        mkcpfile('ECE', filepath)
    if EEC_PATTERN.findall(content):
        mkcpfile('EEC', filepath)
    if EC_PATTERN.findall(content):
        mkcpfile('EC', filepath)
    if NCAP_PATTERN.findall(content):
        mkcpfile('NCAP', filepath)
    if CONTRAN_PATTERN.findall(content):
        mkcpfile('CORTRAN', filepath)
    if FMVSS_PATTERN.findall(content):
        mkcpfile('FMVSS', filepath)
    if CMVSS_PATTERN.findall(content):
        mkcpfile('CMVSS', filepath)
    if KMVSS_PATTERN.findall(content):
        mkcpfile('KMVSS', filepath)
    if GB_PATTERN.findall(content):
        mkcpfile('GB', filepath)
    else:
        pass


def findpattern_docx(content, filepath):
    pass


def gatheringtext():
    for file in os.listdir(GM_folder):
        filepath = os.path.join(GM_folder, file)
        fp = open(filepath, 'rb')

        if file.endswith('.pdf'):
            # filepath = os.path.join(GM_folder, file)
            # fp = open(filepath, 'rb')
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
