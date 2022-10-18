from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# Список URL адресов сервиса
from Site.controllers.auth.auth_login import auth_login
from Site.controllers.auth.auth_logout import auth_logout
from Site.controllers.control.control_get import control_get
from Site.controllers.control.control_info import control_info
from Site.controllers.control.control_remove import control_remove
from Site.controllers.control.control_table import control_table
from Site.controllers.control.control_work import control_work
from Site.controllers.control.control_work_img import control_work_img
from Site.controllers.control.control_work_img_remove import control_work_img_remove
from Site.controllers.control.status.search import search as status_search
from Site.controllers.control.status.analysis import analysis as status_analysis
from Site.controllers.corrupt.corrupt_get import corrupt_get
from Site.controllers.corrupt.corrupt_remove import corrupt_remove
from Site.controllers.corrupt.corrupt_table import corrupt_table
from Site.controllers.corrupt.corrupt_work import corrupt_work
from Site.controllers.place.place_city_remove import place_city_remove
from Site.controllers.place.place_city_work import place_city_work
from Site.controllers.place.place_countries_remove import place_countries_remove
from Site.controllers.place.place_countries_work import place_countries_work
from Site.controllers.place.place_info import place_info
from Site.controllers.place.place_regions_remove import place_regions_remove
from Site.controllers.place.place_regions_work import place_regions_work
from Site.controllers.table.table_info import table_info
from Site.controllers.vch.vch_get import vch_get
from Site.controllers.vch.vch_remove import vch_remove
from Site.controllers.vch.vch_table import vch_table
from Site.controllers.vch.vch_work import vch_work
from Site.views import index, control, actions, reports, config, place, login, tester, vch, corrupt

urlpatterns = [
                  url(r'^$', index, name='index'),

                  url(r'^control/$', control, name='control'),
                  url(r'^control/get/$', control_get, name='control_get'),
                  url(r'^control/work/$', control_work, name='control_work'),
                  url(r'^control/work/img/$', control_work_img, name='control_work_img'),
                  url(r'^control/work/img/remove/$', control_work_img_remove, name='control_work_img_remove'),
                  url(r'^control/remove/$', control_remove, name='control_remove'),
                  url(r'^control/info/$', control_info, name='control_info'),
                  url(r'^control/table/$', control_table, name='control_table'),
                  url(r'^control/status/search/$', status_search, name='status_search'),
                  url(r'^control/status/analysis/$', status_analysis, name='status_analysis'),

                  url(r'^corrupt/$', corrupt, name='corrupt'),
                  url(r'^corrupt/get/$', corrupt_get, name='corrupt_get'),
                  url(r'^corrupt/table/$', corrupt_table, name='corrupt_table'),
                  url(r'^corrupt/work/$', corrupt_work, name='corrupt_work'),
                  url(r'^corrupt/remove/$', corrupt_remove, name='corrupt_remove'),

                  url(r'^actions/$', actions, name='actions'),

                  url(r'^reports/$', reports, name='reports'),

                  url(r'^config/$', config, name='config'),
                  url(r'^config/place/$', place, name='place'),
                  url(r'^config/place/info/$', place_info, name='place_info'),
                  url(r'^config/place/countries/work/$', place_countries_work, name='place_countries_work'),
                  url(r'^config/place/countries/remove/$', place_countries_remove, name='place_countries_remove'),
                  url(r'^config/place/regions/work/$', place_regions_work, name='place_regions_work'),
                  url(r'^config/place/regions/remove/$', place_regions_remove, name='place_regions_remove'),
                  url(r'^config/place/city/work/$', place_city_work, name='place_city_work'),
                  url(r'^config/place/city/remove/$', place_city_remove, name='place_city_remove'),
                  url(r'^config/vch/$', vch, name='vch'),
                  url(r'^config/vch/get/$', vch_get, name='vch_get'),
                  url(r'^config/vch/table/$', vch_table, name='vch_table'),
                  url(r'^config/vch/work/$', vch_work, name='vch_work'),
                  url(r'^config/vch/remove/$', vch_remove, name='vch_remove'),

                  url(r'^login/$', login, name='login'),

                  url(r'^table/info/$', table_info, name='table_info'),

                  url(r'^auth/login/$', auth_login, name='auth_login'),
                  url(r'^auth/logout/$', auth_logout, name='auth_logout'),

                  url(r'^tester/$', tester, name='tester'),

              ] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
