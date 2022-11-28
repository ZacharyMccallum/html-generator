from airium import Airium
import webbrowser


a = Airium()

a('')
with a.html(lang="pl"):
    with a.head():
        a.meta(charset='utf-8')
        a.title(_t="GeneratingHTML")
    
    with a.body():
        with a.h3(id="id23409321", klass='main_header'):
            a('Alec Brown')
        

html = str(a)

html_bytes = bytes(a)


file_object = open("C:/Users/arb2/Visual Studios/index.html","w")
file_object.write(html)
file_object.close()

webbrowser.open("C:/Users/arb2/Visual Studios/index.html")