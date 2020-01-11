from django.views.generic import ListView
from .models import Person
from django_tables2 import SingleTableView
from .tables import PersonTable


class PersonListView(ListView):
    model = Person
    template_name = 'tutorial/index.html'


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tutorial/index.html'
