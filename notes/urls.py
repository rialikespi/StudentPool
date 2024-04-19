from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # base url of website, call views.home function
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('page/', views.page, name='page'),
    path('upload/', views.upload_note, name='upload_note'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    #path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    #path('notes/<int:note_id>/', views.get_note, name='get_note'),
    #path('download/', views.download_note, name='download_note'),
    #path('submit_review/', views.submit_review, name='submit_review')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)