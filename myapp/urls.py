from django.urls import path
from . import views
from .views import AnnouncementList, AnnouncementDetail, AnnouncementCreate, AnnouncementDelete

urlpatterns = [
    path('', views.index, name='home'),
    path('announcements/', AnnouncementList.as_view(), name='announcements'),
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement'),
    path('create/', AnnouncementCreate.as_view(), name='create'),
    path('delete/', AnnouncementDelete.as_view(), name='delete'),
    path('work_room/', views.work_room, name='work_room'),

]
