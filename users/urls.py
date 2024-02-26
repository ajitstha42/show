from django.urls import path
from .views import SignUpView, UserProfileView, CustomLoginView, UpdateProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("profile/edit/<int:pk>/", UpdateProfileView.as_view(), name="edit_profile"),
]
