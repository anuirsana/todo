from django.contrib import admin
from django.urls import path,include

from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    #path('details/',views.details,name="details")
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:taskid>/',views.update,name="update"),
    path('listview/',views.TaskListiew.as_view(),name="listview"),
    path('detailview/<int:pk>/', views.Taskdetail.as_view(), name="detailview"),
    path('updateview/<int:pk>/',views.Taskupdate.as_view(),name="updatesview"),
path('deleteview/<int:pk>/',views.Taskdelete.as_view(),name="deleteview")
]

