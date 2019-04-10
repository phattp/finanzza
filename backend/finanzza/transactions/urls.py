from django.urls import path, include
from rest_framework import routers
from .views import TransactionView

router = routers.DefaultRouter()
router.register('api/transactions', TransactionView, 'transactions')

urlpatterns = [
    path('', include(router.urls))
]
