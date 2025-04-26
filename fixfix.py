import os
import shutil
from bs4 import BeautifulSoup
import random

preloader='''<link href="static/img/favicon.ico" rel="icon">
<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();
   for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(101414766, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/101414766" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
</head>
'''
for d in os.listdir('lockandkey'):
    try:
        for c in os.listdir(f'lockandkey/{d}'):
            try:
                for b in os.listdir(f'lockandkey/{d}/{c}'):
                    try:
                        search_categories = open(f'lockandkey/{d}/{c}/{b}', "r", encoding="utf8").read()
                        op= search_categories.replace("﻿", '')
                        op= op.replace('</head>', preloader.replace('"static/img', '"../../static/img'))
                        fp = open(f'lockandkey/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except:
                        pass
            except:
                pass
    except:
        pass
for d in os.listdir('lockandkey'):
    try:
        search_categories = open(f'lockandkey/{d}/index.html', "r", encoding="utf8").read()
        op= search_categories.replace("﻿", '')
        
        op= op.replace('</head>', preloader.replace('"static/img', '"../static/img'))
        fp = open(f'lockandkey/{d}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(op)
        fp.close()
    except:
        pass
try:
    search_categories = open(f'lockandkey/index.html', "r", encoding="utf8").read()
    op= search_categories.replace("﻿", '')
    op= op.replace('</head>', preloader)
    fp = open(f'lockandkey/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass
try:
    search_categories = open(f'index.html', "r", encoding="utf8").read()
    op= search_categories.replace("﻿", '')
    op= op.replace('</head>', preloader)
    fp = open(f'index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass
