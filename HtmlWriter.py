from Utils import Utils 
from bs4 import BeautifulSoup

class HtmlWriter:
    
    # list.htmlを更新する
    def update_list(read_file,write_file):
        with open(read_file, mode='rt', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        html_basenames = Utils.get_html_base_names()
        for html_basename in html_basenames:
            li = soup.new_tag('li')
            a = soup.new_tag('a',href=f"./books/{html_basename}.html")
            a.append(html_basename)
            li.append(a)
            soup.ul.append(li)
        with open(write_file, mode='w', encoding='utf-8') as f:
            f.write(soup.prettify())
    
    update_list(read_file=f"{Utils.DOC_ROOT}list.html",write_file=f"./htdocs/list.html")

    # TODO:呼び出し方は検討
    # update_list(read_file="Utils.DOC_ROOT/list.html",utils.HTML_DIR)