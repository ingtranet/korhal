#-*- coding: utf-8 -*-

test_text = '집에 가서 잠을 자고 싶다'

def test_tokenize():
    import korhal.hannanum as hannanum
    import korhal.komoran as komoran
    import korhal.openkoreantext as openkoreantext

    hannanum.tokenize(test_text)
    komoran.tokenize(test_text)
    openkoreantext.tokenize(test_text)

def test_aio_tokenize():
    import korhal.hannanum as hannanum
    import korhal.komoran as komoran
    import korhal.openkoreantext as openkoreantext

    hannanum.tokenize(test_text)
    komoran.tokenize(test_text)
    openkoreantext.tokenize(test_text)
