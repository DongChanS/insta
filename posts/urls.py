from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.list, name="list"),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/update/', views.update, name="update"),
    path('<int:post_id>/like/', views.like, name="like"),
    path('<int:post_id>/comment/create', views.create_comment, name="create_comment"),
    path('<int:comment_id>/comment/delete', views.delete_comment, name="delete_comment"),
]