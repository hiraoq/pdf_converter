import os,subprocess,asyncio;

ROOT_DIR = './'
PDF_DIR = f'{ROOT_DIR}pdf/'
HTML_DIR = f'{ROOT_DIR}html/'
CONVERTED_DIR = f'{ROOT_DIR}converted/'

def main():
    html_base_names = get_html_base_names()
    pdfs = os.listdir(PDF_DIR)
    
    # pdfフォルダ内すべてのpdfファイルを変換
    for file in pdfs:
        pdf_base_name, ext = os.path.splitext(file)
        if ext == '.pdf' and pdf_base_name not in html_base_names:
            pdf_path=f'{PDF_DIR}{file}'
            html_path=f'html/{pdf_base_name}.html'
            
            # 変換処理
            subprocess.run(['pdf2htmlEX',pdf_path,html_path])
            
            # 変換済のPDFは移動する
            if f'{pdf_base_name}' in get_html_base_names():
                subprocess.run(['mv',pdf_path,CONVERTED_DIR])
            
def get_html_base_names():
    return [os.path.splitext(i)[0] for i in os.listdir(HTML_DIR)]

if __name__ == "__main__":
    main()