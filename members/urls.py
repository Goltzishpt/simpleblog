from django.urls import path
from members.renders.views import (UserRegisterView, UserEditView, ShowProfilePageView, EditProfilePageView,
                                   CreateProfilePageView)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserRegisterView.as_view(), name='login'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('registration/<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('registration/<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_user_profile_page', CreateProfilePageView.as_view(), name='create_user_profile_page'),
]
