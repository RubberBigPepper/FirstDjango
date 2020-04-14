#этот файл будет отвечать за вывод страницы Contacts на сайте
import django.http as httpDj
import site_root.html_pre_post_factory as htmlHelper

def contacts_simple(request):
    return httpDj.HttpResponse(htmlHelper.html_tag_center() + #отцентруем все
                               htmlHelper.html_return2main() +#добавим ссылку на главную страницу
                               "<br>"
                               "Тут могут быть ваши контакты:"
                               "<br>"
                               "телефон: 3322223322"
                               "<br>"
                               "или почта: на_деревню@дедушке"+
                               htmlHelper.html_tag_center(True)#закроем тег центровки
                               )