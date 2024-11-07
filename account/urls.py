from django.urls import path
from .views import (
    create,
    get_users,
    get_user,
    Register,
    Login,
    GetToken,
    logout,
    UpdateUser,
)

urlpatterns = [
    path("Create/", view=create, name="CreateUser"),
    path("All/", view=get_users, name="GetUsers"),
    path("Single/<int:pk>/", view=get_user, name="GetUser"),
    path("register/", Register),
    path("login/", Login, name="login"),
    path("token/", GetToken),
    path("logout/", logout),
    path("Update/<int:pk>/", view=UpdateUser),
]
