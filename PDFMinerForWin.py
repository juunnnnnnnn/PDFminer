from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from glob import glob

file_list = glob(r'C:\Users\160800\Documents\OriXLifeInsurance\030_Digi-C\006_first_test_of_prottype\AI-OCR/*.pdf')

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True
    device = TextConverter(rsrcmgr , retstr , codec=codec,laparams=laparams)
    fp = open(path , 'r+b')
    interpreter = PDFPageInterpreter(rsrcmgr , device)
    maxpages = 0
    caching = True
    pagenos=set()
    fstr = ''
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        
        str = retstr.getvalue()
        fstr += str
    
    fp.close()
    device.close()
    retstr.close()
    return fstr

result_list = []
for item in file_list:
    result_txt = convert_pdf_to_txt(item)
    result_list.append(result_txt)
    
allText = ','.join(result_list)

file = open(r'C:\Users\160800\Documents\OriXLifeInsurance\030_Digi-C\006_first_test_of_prottype\AI-OCR\result\pdf.txt','w' , encoding='UTF-8')
file.write(allText)
print(allText)
