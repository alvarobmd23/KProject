from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (Analitic_Delete, Analitic_New, Analitic_Update,
                    Sintetic_Delete, Sintetic_New, Sintetic_Update,
                    accountsview)

app_name = 'accounts'

urlpatterns = [
    path('', login_required(accountsview), name='accounts'),
    path('sintetic_new/', login_required(Sintetic_New.as_view()),
         name='sintetic_new'),
    path('sintetic_update/<int:pk>', login_required(Sintetic_Update.as_view()),
         name='sintetic_update'),
    path('sintetic_delete/<int:pk>', login_required(Sintetic_Delete.as_view()),
         name='sintetic_delete'),
    path('analitic_new/', login_required(Analitic_New.as_view()),
         name='analitic_new'),
    path('analitic_update/<int:pk>', login_required(Analitic_Update.as_view()),
         name='analitic_update'),
    path('analitic_delete/<int:pk>', login_required(Analitic_Delete.as_view()),
         name='analitic_delete')

]
