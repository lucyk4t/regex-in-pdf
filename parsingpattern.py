import fitz
import os
import shutil
import os.path
import glob
import re

# using PyMUPDF library
# for finding some pattern words in pdf files
# funcion what is extended excel, ppt, txt in other office will be released soon
# To-Be: PyQT5(GUI) + PyM
def pymu_search_text():
    filename = glob.iglob('./Spec/**/*.pdf', recursive=True)

    for file in filename:
        doc = fitz.open(file)
        # page = doc.loadPage(0)
        # page = doc[0]
        # content = page.getText()

        # print('file: ', file, 'content: ', content)
        global_spec_pattern_tuple = [
            (r'(ECE.?R+.+)|(ECE \d+)', 'ECE'),
            (r'(\d+ CFR.*)|(CFR \d*.+)', 'CFR'),
            (r'CMVSS \d+', 'CMVSS'),
            (r'FMVSS \w+', 'FMVSS'),
            (r'KMVSS \w+', 'KMVSS'),
            (r'(VDA \d+)|(VDA Volume .*)|(VDA Band .*)', 'VDA'),
            (r'\d+/\d+/EC', 'EC'),
            (r'\d+/\d+/EEC', 'EEC'),
            (r'(GB/T \w+)|(GB\d+)', 'GB')
        ]

        for current_page in range(len(doc)):
            page = doc.loadPage(current_page)
            content = page.getText()
            for pattern, value in global_spec_pattern_tuple:
                precomp = re.compile(pattern)
                if re.search(precomp, content):
                    try:
                        newdir = './' + value
                        os.mkdir(newdir)
                    except FileExistsError as e:
                        pass
                    finally:
                        shutil.copy(file, newdir)
                    # if page.searchFor('VDA'):  # fitz module provides searching method but it can't apply pattern.
                else:
                    continue
    else:
        print('done!')

if __name__ == '__main__':
    pymu_search_text()
