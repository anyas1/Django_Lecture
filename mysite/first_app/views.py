from django.shortcuts import render
from django.http.response import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
)

# Create your views here.

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR")  # 404.HTML


# domain.com/first_app/0 ---> domain.com/fist_app/sports


def num_page_view(request, num_page):
    topics_list = list(articles.keys())  # ['sports','finance','politics']
    topic = topics_list[num_page]

    return HttpResponseRedirect(topic)
