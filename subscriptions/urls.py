from django.urls import path

from .views import SubscriptionView, PackageView

urlpatterns = [
    path('subscription/', SubscriptionView.as_view()),
    path('package/', PackageView.as_view()),
]
