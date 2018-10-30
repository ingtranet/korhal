# Korhal
[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/ingtranet/korhal.svg?style=flat-square)](https://github.com/ingtranet/korhal)
[![PyPI](https://img.shields.io/pypi/v/korhal.svg?style=flat-square)](https://pypi.org/project/korhal/)
[![Travis (.com) branch](https://img.shields.io/travis/com/ingtranet/korhal/master.svg?style=flat-square)](https://travis-ci.com/ingtranet/korhal)
[![Codacy branch grade](https://img.shields.io/codacy/grade/b8ad24518efb4bec9a68b32eeb994d78/master.svg?style=flat-square)](https://app.codacy.com/project/cookieshake/korhal/dashboard)

Korhal(KOrean Rpc-based Handy Application for Language-processing) is a python wrapper for several korean Part-Of-Speech taggers.

## How to install

``` sh
pip install korhal
```

## Available taggers

- KOMORAN with `korhal.komoran`
- Hannanum with `korhal.hannanum`
- Open-source Korean Text Processor with `korhal.openkoreantext`

## How to use

``` python
from korhal.komoran import tokenize

result = tokenize("집에 가서 잠을 자고 싶다")
# result => Token(text=집,pos=NNG), Token(text=에,pos=JKB), Token(text=가,pos=VV), Token(text=아서,pos=EC), Token(text=잠,pos=NNG), Token(text=을,pos=JKO), Token(text=자,pos=VV), Token(text=고,pos=EC), Token(text=싶,pos=VX), Token(text=다,pos=EC)]

from korhal.aio.komoran import tokenize

future = tokenize("집에 가서 잠을 자고 싶다")
# future => <Future at 0x10a335d30 state=finished returned list>
result = future.result()
# result => [Token(text=집,pos=NNG), Token(text=에,pos=JKB), Token(text=가,pos=VV), Token(text=아서,pos=EC), Token(text=잠,pos=NNG), Token(text=을,pos=JKO), Token(text=자,pos=VV), Token(text=고,pos=EC), Token(text=싶,pos=VX), Token(text=다,pos=EC)]
```

## Thanks to

- [KOMORAN](http://www.shineware.co.kr/products/komoran/)
- [Hannanum](http://semanticweb.kaist.ac.kr/hannanum/index.html)
- [Open-source Korean Text Processor](https://github.com/open-korean-text/open-korean-text)
- [KoalaNLP](https://koalanlp.github.io/KoalaNLP-core/) 