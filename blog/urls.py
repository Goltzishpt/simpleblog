from django.urls import path
from blog.renders.views import (HomeView, ArticleDetailView, AddPostView, UpdatePostView,
                                DeletePostView, AddCategoryView, CategoryView, CategoryListView, like_view,
                                AddCommentView, DeleteCommentView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('article/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('article/<int:pk>/del_com', DeleteCommentView.as_view(), name='delete_comment'),
]
