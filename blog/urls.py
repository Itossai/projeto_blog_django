"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from blog.views import page,post,CategoryListView,TagByListView,search,PostListView, CreatedByListView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(),name='index'),
    path('page/<slug:slug>/', page,name='page'),
    path('post/<slug:slug>/', post,name='post'),
    path('category/<slug:slug>/',
         CategoryListView.as_view(), 
         name='category'),
    path('created_by/<int:author_pk>/',
         CreatedByListView.as_view(), 
         name='created_by'),
    path('tag/<slug:slug>/',
         TagByListView.as_view(),
        name='tag'),
    path('search/',search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
