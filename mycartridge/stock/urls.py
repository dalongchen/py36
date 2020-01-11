"""
"""
from django.conf.urls import url
from .views import DataListView
app_name = 'stock'
urlpatterns = [
    # ex: /stock/
    url(r'^$', DataListView.as_view()),
]
