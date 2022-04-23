from django.urls import path
# from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("try", views.mytry, name="mytry"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_poll, name="create"),
    path("choose", views.choose, name="choose"),

    # path("registerforaaruush", views.registerAaruush, name="registerforaaruush"),
    # path("generatecertificate", views.generateCertificate, name="generatecertificate"),
    # path("getcertificate", views.getCertificate, name="getcertificate"),
    # path("viewcertificate/<str:token>", views.viewCertificate, name="viewcertificate"),
]
