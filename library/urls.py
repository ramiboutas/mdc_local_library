"""library URL Configuration

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
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
# Now let's redirect the root URL of our site (i.e. 127.0.0.1:8000) to the URL 127.0.0.1:8000/catalog/.
# This is the only app we'll be using in this project. To do this, we'll use a special view function,
# RedirectView, which takes the new relative URL to redirect to (/catalog/) as its first argument
# when the URL pattern specified in the path() function is matched (the root URL, in this case).
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Django does not serve static files like CSS, JavaScript, and images by default, but it can be useful for
# the development web server to do so while you're creating your site. As a final addition to this URL mapper,
# you can enable the serving of static files during development by appending the following lines.

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
