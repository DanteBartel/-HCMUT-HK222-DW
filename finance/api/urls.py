from django.urls import path, include
from .views import SectorView, TickerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('sector/', SectorView.as_view()),
    path('sector/<int:pk>', SectorView.as_view()),
    path('ticker/', TickerView.as_view()),
    path('ticker/<int:pk>', TickerView.as_view()),
]