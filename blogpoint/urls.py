"""
URL configuration for blogpoint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.site.site_header="Blogpoint Admin"
admin.site.site_title="Admin Panel"
admin.site.index_title="Welcome to Blogpoint Admin Panel"
from django.contrib.sitemaps.views import sitemap 
from blog.sitemaps import BlogpostSitemap
sitemaps = {
    'items':BlogpostSitemap,
}

urlpatterns = [
    path("django-check-seo/", include("django_check_seo.urls")),
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap, {'sitemaps':sitemaps}),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()