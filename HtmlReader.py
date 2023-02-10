from Utils import Utils 

class HtmlReader:
    HTML_DIR = Utils.HTML_DIR
    COVER_IMG_DIR = Utils.COVER_IMG_DIR
    def __init__(self,html_path) -> None:
        # 書籍名とカバー画像のパスの辞書かタプル
        extract_cover_image(html_path)
        cover = get_cover_img_path(html_path)
        name_with_cover = (html_path,cover)
        pass
        
    def get_cover_img_path(html_path):
        # return 画像のパス
        pass     
    def extract_cover_image(html_path):
        # 画像をCOVER_IMG_DIRにコピー
        return 1
