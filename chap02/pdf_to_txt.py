import pymupdf
import os

pdf_path = '/Users/nicole/VisualStudioCode/learn-ai-agent/chap02/pdf/법제처_2025_법령해석사례집(상).pdf'
doc = pymupdf.open(pdf_path)

full_text = ''

for page in doc:
    text = page.get_text()
    full_text += text

pdf_file_name = os.path.basename(pdf_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

txt_file_name = f"/Users/nicole/VisualStudioCode/learn-ai-agent/chap02/output/{pdf_file_name}.txt"
with open(txt_file_name, 'w', encoding='utf-8') as txt_file:
    txt_file.write(full_text)