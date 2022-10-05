from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from Site import views

# Список URL адресов сервиса
urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^control/$', views.control, name='control'),
                  url(r'^control/work/$', views.control_work, name='control_work'),
                  url(r'^control/work/img/$', views.control_work_img, name='control_work_img'),
                  url(r'^control/work/img/remove/$', views.control_work_img_remove, name='control_work_img_remove'),
                  url(r'^control/remove/$', views.control_remove, name='control_remove'),
                  url(r'^control/info/$', views.control_info, name='control_info'),
                  url(r'^actions/$', views.actions, name='actions'),
                  url(r'^reports/$', views.reports, name='reports'),

                  url(r'^config/$', views.config, name='config'),

                  url(r'^config/place/$', views.place, name='place'),
                  url(r'^config/place/info/$', views.place_info, name='place_info'),

                  url(r'^config/place/countries/work/$', views.place_countries_work, name='place_countries_work'),
                  url(r'^config/place/countries/remove/$', views.place_countries_remove, name='place_countries_remove'),

                  url(r'^config/place/regions/work/$', views.place_regions_work, name='place_regions_work'),
                  url(r'^config/place/regions/remove/$', views.place_regions_remove, name='place_regions_remove'),

                  url(r'^config/place/city/work/$', views.place_city_work, name='place_city_work'),
                  url(r'^config/place/city/remove/$', views.place_city_remove, name='place_city_remove'),

                  url(r'^config/vch/$', views.vch, name='vch'),
                  url(r'^config/vch/info/$', views.vch_info, name='vch_info'),

                  url(r'^config/vch/work/$', views.vch_work, name='vch_work'),
                  url(r'^config/vch/remove/$', views.vch_remove, name='vch_remove'),

                  url(r'^login/$', views.login, name='login'),

                  url(r'^table/info/$', views.table_info, name='table_info'),

                  url(r'^auth/login/$', views.auth_login, name='auth_login'),
                  url(r'^auth/logout/$', views.auth_logout, name='auth_logout'),

                  url(r'^tester/$', views.tester, name='tester'),

              ] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
