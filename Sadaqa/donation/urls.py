from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [
    path('donate/', views.create_donation, name='donate'),
    path('success/', views.donation_success, name='success'),
    path('history/', views.donation_history, name='donation_history'),

    # REST API endpoints
    path('api/donations/', views.DonationListCreateAPIView.as_view(), name='donation-list-create'),
    path('api/donations/<int:pk>/', views.DonationRetrieveUpdateDestroyAPIView.as_view(), name='donation-detail'),
]
