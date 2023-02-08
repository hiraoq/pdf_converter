import os
class Utils:
    # TODO:テンプレート文字列使ってみる
    ROOT_DIR = './' 
    HTML_DIR = f'{ROOT_DIR}htdocs/books/'
    PDF_DIR = f'{ROOT_DIR}pdf/'
    CONVERTED_DIR = f'{ROOT_DIR}converted/'
    DOC_ROOT = '/mnt/c/Apache24/htdocs/'
    # write用とread用をテンプレートで分ける
    # LIST_FILE_TEMP = hogehoge
    
    def get_directry_of(dir):
        pass
    def get_base_name_of(files):
        pass
    @staticmethod
    def get_html_base_names():
        return [os.path.splitext(i)[0] for i in os.listdir(Utils.HTML_DIR) if os.path.splitext(i)[1] == '.html']