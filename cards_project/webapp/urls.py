from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('add.html', views.add, name='add'),
    path('subtract.html', views.subtract, name='subtract'),
    path('multi.html', views.multi, name='multi'),
    path('divide.html', views.divide, name='divide'),

]
