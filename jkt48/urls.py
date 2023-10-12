from django.urls import path
from . import views
from .views import MemberListCreate, MemberRetrieveUpdateDelete

urlpatterns = [
    path('', views.home, name='home-page'),
    path('members/', views.members, name='members'),
    path('member', MemberListCreate.as_view(), name="Create-Member_list"),
    path('member/<int:pk>/', MemberRetrieveUpdateDelete.as_view(), name="member-Details")
]
