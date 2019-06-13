from django.contrib import admin
from . import views
from django.urls import path

app_name = 'music' 

urlpatterns = [
   # music/
   path('', views.IndexView.as_view() , name = 'index' ) ,

   #music/71/
   path('<int:pk>/', views.DetailView.as_view(), name='detail' ),

   #music/album/add/
   path('album/add' , views.AlbumCreate.as_view() , name= 'album-add'  ) ,

   #music/album/71/       #update
   path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update' ),

   #music/album/71/            #delete
   path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete' ),


   path('register/' , views.UserFormView.as_view() , name = 'register'  ) ,
  
   #path('<int:pk>/favorite/', views.favorite, name='favorite' ),

]
