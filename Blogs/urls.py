"""
URL configuration for Blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from BApp.views import Registration,logins,dashboard,logouts,create,blogspost,post_detail,post_dlt,post_upd,comment_dlt,admin_dashboard,blogs,post_aupd,post_adlt,adashboard,comment_adlt,users,user_adlt,post_adlt,posts
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
a = '/dasboard/'
urlpatterns = [
    path('registration/', Registration , name='Registration'),
    path('logins/', logins , name='logins'),
    path('logouts/', logouts , name='logouts'),
    path('create/', create , name='create'),
    path('dashboard/', dashboard , name='dashboard'),
    path('blogspost/<author_id>/', blogspost , name='blogspost'),
    path('post/<post_id>/', post_detail , name='post_detail'),
    path('post_dlt/<id>/', post_dlt , name='post_dlt'),
    path('post_upd/<id>/', post_upd , name='post_upd'),
    path('comment_dlt/<id>/', comment_dlt , name='comment_dlt'),
    path('admins/', admin_dashboard,name='admin_dashboard'),
    path('adashboard/', adashboard , name='adashboard'),
    path('post_aupd/<id>/', post_aupd , name='post_aupd'),
    path('post_adlt/<id>/', post_adlt , name='post_adlt'),
    path('comment_adlt/<id>/', comment_adlt , name='comment_adlt'),
    path('users/', users , name='users'),
    path('user_adlt/<id>/', user_adlt , name='user_adlt'),
    path('posts/', posts , name='posts'),
    path('post_adlt/<id>/', post_adlt , name='post_adlt'),
    
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
