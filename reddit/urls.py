
from django.urls import path, include
from .views import Postlist, VoteCreate


app_name = 'reddit'
urlpatterns = [
    path('', Postlist.as_view()),
    path('vote/<int:pk>/', VoteCreate.as_view()),

]
