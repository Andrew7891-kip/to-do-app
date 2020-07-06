from django.urls import path 
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.index,name='index'),
    path('addTodoItem/',views.addTodoView,name='add'),
    path('deleteTodoItem/<int:pk>',views.deleteTodo,name='del'),
    # path('add/',views.TodoCreate.as_view(),name='add'),
]