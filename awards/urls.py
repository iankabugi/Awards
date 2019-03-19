from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='landing'),
    url(r'^upload/$', views.new_project, name='newPro'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^viewproject/(\d+)$', views.view_project, name='viewpro'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'search/', views.search_results, name='search_results'),
    url(r'^api/profiles/$', views.ProfList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^project/(\d+)/review_design/$', views.add_design,
        name='add_design'),
    url(r'^project/(\d+)/review_usability/$',
        views.add_usability,
        name='review_usability'),
    url(r'^project/(\d+)/review_content/$',
        views.add_content,
        name='review_content'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
