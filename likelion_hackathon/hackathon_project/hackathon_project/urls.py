"""hackathon_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import * #view의 모든 함수 불러옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('select/', select, name = "select"),
    path('new_fiction/', new_fiction, name="new_fiction"),
    path('new_poetry/', new_poetry, name="new_poetry"),
    path('new_nonfiction/', new_nonfiction, name="new_nonfiction"),
    path('new_essay/', new_essay, name="new_essay"),
    path('new_free/', new_free, name = "new_free"),
    path('create_fiction/', create_fiction, name="create_fiction"),
    path('create_poetry/', create_poetry, name="create_poetry"),
    path('create_nonfiction/', create_nonfiction, name="create_nonfiction"),
    path('create_essay/', create_essay, name="create_essay"),
    path('create_free', createFree, name="createFree"),
    path('<str:id>',detail,name="detail"),

    path("editBook/<str:id>", editBook, name = "editBook"),
    path('updateBook/<str:id>', updateBook, name = "updateBook"),
    path('delete/<str:id>', deleteBook, name='deleteBook'),

    path('editFree/<str:id>', editFree, name = "editFree"),
    path('updateFree/<str:id>', updateFree, name = "updateFree"),
    path('deleteFree/<str:id>', deleteFree, name = "deleteFree"),
    
    path('free/<str:id>',detailFree,name="detailFree"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('signup/',register_view,name="signup"),
]
