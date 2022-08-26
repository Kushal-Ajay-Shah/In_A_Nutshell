# from unidecode import unidecode


def get_ascii(text) :
    return  ''.join([i if ord(i) < 128 else ' ' for i in text])
    #  return unidecode(unicode(text, encoding = "utf-8"))


def check_ascii(text) :
    return text.isascii()