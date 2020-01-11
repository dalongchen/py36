"""
"""
from django.conf.urls import url
from .views import PersonListView
app_name = 'tutorial'
urlpatterns = [
    # ex: /polls/
    url(r'^$', PersonListView.as_view()),
]
