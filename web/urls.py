from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="hinglish"),
    path("about/", views.about),
    path("english/", views.english),
    path("suggest/",views.suggestion),
    path("feedback/",views.feedback),
    path("404",views.error_404),
    # path("addword",views.AddHinglishWord),
    # path("set<str:word>", views.setcookie,name="set")
]
