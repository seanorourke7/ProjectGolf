from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.PostCreate.as_view(), name='postcreate'),
    path('<int:id>', views.PostLike.as_view(), name='post_like'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('remove/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
    path('edit/<int:id>', views.EditPost.as_view(), name='edit_post'),

]
