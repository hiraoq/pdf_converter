from Utils import Utils 
from bs4 import BeautifulSoup

class HtmlWriter:
    
    # list.htmlを更新する
    def update_list(read_file,write_file):
        with open(read_file, mode='rt', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        li = soup.new_tag('li')
        li.append
        html_basenames = Utils.get_html_base_names()
        elems = ""
        for html_basename in html_basenames:
            a = soup.new_tag('a',href=f"./books/{html_basename}")
            li.append(a)
            li.append(html_basename)
        soup.ul.append(li)
        with open(write_file, mode='w', encoding='utf-8') as f:
            f.write(soup.prettify())

    # TODO:呼び出し方は検討
    # update_list("list.html",utils.HTML_DIR)