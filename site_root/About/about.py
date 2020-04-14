#этот файл будет отвечать за вывод страницы About на сайте
import django.http as httpDj
import site_root.html_pre_post_factory as htmlHelper

def about_simple(request):
    return httpDj.HttpResponse(htmlHelper.html_tag_center()+ #отцентруем все
                               htmlHelper.html_return2main()+#добавим ссылку на главную страницу
                               "<br>"
                               "О сайте: здесь могла бы быть ваша реклама"+
                               htmlHelper.html_tag_center(True)#закроем тег центровки
                               )
