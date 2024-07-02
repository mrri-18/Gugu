from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name="countapp"
urlpatterns = [
    path('', views.index, name='index'),
    # path('stop-tracking/', views.stop_tracking, name='stop_tracking'),  # 걷기 기록 종료 시
    path('record/<int:record_id>/upload/', views.upload_walk_certification, name='upload_walk_certification'),  # 인증샷 업로드 페이지
    path('record/<int:record_id>/upload_archive/', views.upload_archive, name='upload_archive'),  # 인증샷 업로드 페이지
    path('record/<int:record_id>/upload/success/', views.upload_success, name='upload_success'),  # 인증샷 업로드 성공 페이지
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
