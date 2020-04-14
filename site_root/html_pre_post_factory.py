# этот файл будет выдавать часто используемые заголовки и подвалы для формируемых страничек. Возможно, стоит сделать класс

def html_tag_center(close=False):
    if close:
        return "</center>"
    else:
        return "<center>"

def html_return2main():
    return "<a href='/'>На главную страницу</a>"