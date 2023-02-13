from Utils import Utils 
from bs4 import BeautifulSoup
import urllib.parse
class HtmlWriter:
    
    # list.htmlを更新する
    def update_list(read_file,write_file):
        with open(read_file, mode='rt', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        html_basenames = Utils.get_html_base_names()
        for html_basename in html_basenames:
            li = soup.new_tag('li')
            # htmlファイル名をパーセントエンコーディングしURLを作成
            html_url = f"./books/{urllib.parse.quote(html_basename)}.html"
            a = soup.new_tag('a',href=html_url)
            a.append(html_basename)
            li.append(a)
            soup.ul.append(li)
        with open(write_file, mode='w', encoding='utf-8') as f:
            f.write(soup.prettify())
    
    # templateファイルをベースに取得したhtmlリストを書き込み、list.html生成
    update_list(read_file=f"{Utils.ROOT_DIR}template.html",write_file=f"./htdocs/list.html")