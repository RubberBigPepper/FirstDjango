#этот файл будет отвечать за вывод страницы по умолчанию на сайте
import django.http as httpDj
import site_root.html_pre_post_factory as htmlHelper

def default(request):
    return httpDj.HttpResponse(htmlHelper.html_tag_center()+ #отцентруем все
                                "Начальная страница"
                               "<br>"
                               "<a href='/contacts'>Контакты</a>"
                               "<br>"
                               "<a href='/about'>О сайте</a>"+
                                htmlHelper.html_tag_center(True)#закроем тег центровки
                               )