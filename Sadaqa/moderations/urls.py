from django.urls import path
from .views import report_comment
urlpatterns = [
    
    path('report_comment/', report_comment, name='report_comment'),
]