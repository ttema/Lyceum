from django.contrib import admin
from django.urls import path
from articles import settings
from office import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tape, name='tape'),
    path('add_article', views.write_article, name='write_art'),
    path('article/<int:pk>', views.view_article, name='article'),
    path('delete/<int:pk>', views.del_article, name='delete'),
    # path('edit/<int:pk>', views.edit_article, name='edit'),
    path('period_delete/<int:pk>', views.del_period, name='period_delete'),
    path('periods_manager', views.view_periods, name='periods_view'),
    path('timetable', views.view_timetable, name='timetable_view'),
    path('album/<int:pk>', views.view_album, name='view_album'),
    path('albums', views.add_album, name='albums'),
    path('de_album/<int:pk>', views.del_album, name='del_album')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
