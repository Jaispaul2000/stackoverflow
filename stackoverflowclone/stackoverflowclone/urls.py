"""stackoverflowclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from stackoverflowapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.IndexView.as_view(),name='index'),
    path('register',views.SignUpView.as_view(),name="signup"),
    path('',views.LoginView.as_view(),name="signin"),
    path("question/<int:id>",views.QuestionDetailView.as_view(),name="questiondetail"),
    path('question/answer/add/<int:id>',views.add_answer,name="addanswer"),
    path('answer/<int:id>/upvote',views.upvote_view,name="upvote"),
    path('answer/<int:id>/remove',views.remove_answer,name="remove-answer"),
    path("accounts/logout",views.signout_view,name="signout"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
