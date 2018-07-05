from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'item'

urlpatterns = [

    # 演習6
    url(r'^calc/view$', views.view, name='calc_in'),
    url(r'^calc/execute$', views.execute, name='calc_res'),

    # 演習8
    url(r'^calc/confirm$', views.confirm, name='calc_con'),
    url(r'^calc/mozaiku$', views.mozaiku, name='calc_mozaiku'),
    url(r'^calc/tamp$', views.tamp, name='calc_tamp'),

]