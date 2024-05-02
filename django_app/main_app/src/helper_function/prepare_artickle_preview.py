from django.contrib.auth.models import User

from src.helper_function.text_cleaners import cleanhtml


def article_preview(article_object):
    img_start = article_object["body"].find("<img src=")
    if img_start == -1:
        article_object["img"] = None
    else:
        article_object["img"] = article_object["body"][article_object["body"].find("<img src=")+10:article_object["body"].find("\" ", article_object["body"].find("<img src="))]
    article_object["desc"] = cleanhtml(article_object["body"])
    article_object["desc"] = article_object["desc"][:article_object["desc"].find(".", 150, 300)]
    article_object["author"] = User.objects.get(id=article_object["user_author_id"])