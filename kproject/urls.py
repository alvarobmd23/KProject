"""
URL configuration for kproject project.

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
from django.urls import include, path

from modules.core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/',
         include('users.urls', namespace='users')),
    path('finance/accounts/',
         include('modules.finance.accounts.urls', namespace='accounts')),
    path('finance/entrys/',
         include('modules.finance.entrys.urls', namespace='entrys')),
    #   path('persons/',
    #         include('modules.foundation.persons.urls', namespace='persons')),

]
