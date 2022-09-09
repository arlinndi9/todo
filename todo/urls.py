from django.urls import path
from todo.views import index,create,update,delete,mark_as_completed
urlpatterns=[
    path('',index,name='home'),
    path('create', create, name="create"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('mark-as-completed/<int:id>',mark_as_completed, name="mark-as-completed"),
]

