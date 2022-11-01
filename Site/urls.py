from django.conf.urls import url
from django.conf.urls.static import static

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
from Site.controllers.control.social.add import add as social_add
from Site.controllers.control.social.confirm import confirm as social_confirm
from Site.controllers.control.social.reject import reject as social_reject
from Site.controllers.control.analysis.post.confirm import confirm as analysis_post_confirm
from Site.controllers.control.analysis.post.reject import reject as analysis_post_reject
from Site.controllers.control.analysis.video.confirm import confirm as analysis_video_confirm
from Site.controllers.control.analysis.video.reject import reject as analysis_video_reject
from Site.controllers.control.analysis.group.confirm import confirm as analysis_group_confirm
from Site.controllers.control.analysis.group.reject import reject as analysis_group_reject
from Site.controllers.control.analysis.photo.confirm import confirm as analysis_photo_confirm
from Site.controllers.control.analysis.photo.reject import reject as analysis_photo_reject
from Site.controllers.control.analysis.inf.confirm import confirm as analysis_inf_confirm
from Site.controllers.control.analysis.inf.reject import reject as analysis_inf_reject

from Site.controllers.corrupt.corrupt_get import corrupt_get
from Site.controllers.corrupt.corrupt_remove import corrupt_remove
from Site.controllers.corrupt.corrupt_table import corrupt_table
from Site.controllers.corrupt.corrupt_work import corrupt_work
from Site.controllers.place.city.place_city_remove import place_city_remove
from Site.controllers.place.city.place_city_work import place_city_work
from Site.controllers.place.country.place_countries_remove import place_countries_remove
from Site.controllers.place.country.place_countries_work import place_countries_work
from Site.controllers.place.country.get import get as place_countries_get
from Site.controllers.place.regions.get import get as place_regions_get
from Site.controllers.place.city.get import get as place_city_get
from Site.controllers.place.place_info import place_info
from Site.controllers.place.regions.place_regions_remove import place_regions_remove
from Site.controllers.place.regions.place_regions_work import place_regions_work
from Site.controllers.place.place_table import place_table
from Site.controllers.table.table_info import table_info
from Site.controllers.vch.vch_get import vch_get
from Site.controllers.vch.vch_remove import vch_remove
from Site.controllers.vch.vch_table import vch_table
from Site.controllers.vch.vch_work import vch_work
from Site.controllers.archive.table import table as archive_table
from Site.controllers.archive.remove.post import post as archive_remove_post
from Site.controllers.archive.remove.video import video as archive_remove_video
from Site.controllers.archive.remove.group import group as archive_remove_group
from Site.controllers.archive.remove.photo import photo as archive_remove_photo
from Site.controllers.archive.remove.inf import inf as archive_remove_inf
from Site.views import index, control, actions, reports, config, place, login, tester, vch, corrupt, archive
from mysite import settings

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

                  url(r'^control/social/add/$', social_add, name='social_add'),
                  url(r'^control/social/confirm/$', social_confirm, name='social_confirm'),
                  url(r'^control/social/reject/$', social_reject, name='social_reject'),

                  url(r'^control/analysis/post/confirm/$', analysis_post_confirm, name='analysis_post_confirm'),
                  url(r'^control/analysis/post/reject/$', analysis_post_reject, name='analysis_post_reject'),
                  url(r'^control/analysis/video/confirm/$', analysis_video_confirm, name='analysis_video_confirm'),
                  url(r'^control/analysis/video/reject/$', analysis_video_reject, name='analysis_video_reject'),
                  url(r'^control/analysis/group/confirm/$', analysis_group_confirm, name='analysis_group_confirm'),
                  url(r'^control/analysis/group/reject/$', analysis_group_reject, name='analysis_group_reject'),
                  url(r'^control/analysis/inf/confirm/$', analysis_inf_confirm, name='analysis_inf_confirm'),
                  url(r'^control/analysis/inf/reject/$', analysis_inf_reject, name='analysis_inf_reject'),
                  url(r'^control/analysis/photo/confirm/$', analysis_photo_confirm, name='analysis_photo_confirm'),
                  url(r'^control/analysis/photo/reject/$', analysis_photo_reject, name='analysis_photo_reject'),

                  url(r'^corrupt/$', corrupt, name='corrupt'),
                  url(r'^corrupt/get/$', corrupt_get, name='corrupt_get'),
                  url(r'^corrupt/table/$', corrupt_table, name='corrupt_table'),
                  url(r'^corrupt/work/$', corrupt_work, name='corrupt_work'),
                  url(r'^corrupt/remove/$', corrupt_remove, name='corrupt_remove'),

                  url(r'^archive/$', archive, name='archive'),
                  url(r'^archive/table/$', archive_table, name='archive_table'),
                  url(r'^archive/get/$', archive_table, name='archive_table'),
                  url(r'^archive/remove/post/$', archive_remove_post, name='archive_remove_post'),
                  url(r'^archive/remove/video/$', archive_remove_video, name='archive_remove_video'),
                  url(r'^archive/remove/group/$', archive_remove_group, name='archive_remove_group'),
                  url(r'^archive/remove/photo/$', archive_remove_photo, name='archive_remove_photo'),
                  url(r'^archive/remove/inf/$', archive_remove_inf, name='archive_remove_inf'),

                  url(r'^actions/$', actions, name='actions'),

                  url(r'^reports/$', reports, name='reports'),

                  url(r'^config/$', config, name='config'),
                  url(r'^config/place/$', place, name='place'),
                  url(r'^config/place/info/$', place_info, name='place_info'),
                  url(r'^config/place/table/$', place_table, name='place_table'),
                  url(r'^config/place/countries/get/$', place_countries_get, name='place_countries_get'),
                  url(r'^config/place/countries/work/$', place_countries_work, name='place_countries_work'),
                  url(r'^config/place/countries/remove/$', place_countries_remove, name='place_countries_remove'),
                  url(r'^config/place/regions/get/$', place_regions_get, name='place_regions_get'),
                  url(r'^config/place/regions/work/$', place_regions_work, name='place_regions_work'),
                  url(r'^config/place/regions/remove/$', place_regions_remove, name='place_regions_remove'),
                  url(r'^config/place/city/get/$', place_city_get, name='place_city_get'),
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

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
