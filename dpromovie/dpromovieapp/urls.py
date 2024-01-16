from . import views
from django.urls import path, include
app_name='dpromovieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path("add/",views.add_movie,name='add_movie'),
    path('edit/<int:movie_id>/',views.update,name='update'),
    path('delete/<int:movie_id>/',views.delete,name='delete')
]
