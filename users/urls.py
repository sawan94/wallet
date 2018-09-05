from django.conf.urls import url
from users.views import *
urlpatterns = [
        url(r"^user/create/$",CreateUser.as_view(),name="create_user"),
        url(r"^user/login/$",LoginView.as_view(),name="login_user"),
        url(r"^user/logout/$",LogoutView.as_view(),name="logout_user"),
        url(r"^user/$",UserView.as_view(),name="logout_user"),
]