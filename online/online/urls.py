"""online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main.views import *
from django.template.defaulttags import url
from django.urls import path
from django.views.static import serve
from django.urls import re_path as url

from online import settings

urlpatterns = [
    path('', indexHandler),
    path('about/', aboutHandler),
    path('courses/', coursesHandler),
    path('teacher/', teacherHandler),
    path('blog/', blogHandler),
    path('blog/<int:blog_id>/', blogsingleHandler),
    path('contact/', contactHandler),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
    })
]
