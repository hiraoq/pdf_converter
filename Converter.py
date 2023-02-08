import os,subprocess,asyncio
from Utils import Utils
from HtmlWriter import HtmlWriter


ROOT_DIR = Utils.CONVERTED_DIR # './'
PDF_DIR = Utils.PDF_DIR # f'{ROOT_DIR}pdf/'
HTML_DIR = Utils.HTML_DIR # f'{ROOT_DIR}htdocs/html/'
CONVERTED_DIR = Utils.CONVERTED_DIR # f'{ROOT_DIR}converted/'
DOC_ROOT = Utils.DOC_ROOT
# LIST_FILE = Utils.LIST_FILE

def main():
    html_base_names = get_html_base_names()
    pdfs = os.listdir(PDF_DIR)
    
    # pdfフォルダ内すべてのpdfファイルを変換
    for file in pdfs:
        pdf_base_name, ext = os.path.splitext(file)
        if ext == '.pdf' and pdf_base_name not in html_base_names:
            pdf_path=f'{PDF_DIR}{file}'
            html_path=f'{HTML_DIR}{pdf_base_name}.html'
            
            # 変換処理
            subprocess.run(['pdf2htmlEX',pdf_path,html_path])
            
            # 変換済のPDFは移動する
            if f'{pdf_base_name}' in get_html_base_names():
                # 移動先に同名ファイルあれば強制上書き
                subprocess.run(['mv','-f',pdf_path,CONVERTED_DIR])
    HtmlWriter.update_list(read_file=f"{DOC_ROOT}list.html",write_file=f"./htdocs/list.html")
            
def get_html_base_names():
    return [os.path.splitext(i)[0] for i in os.listdir(HTML_DIR)]

if __name__ == "__main__":
    main()