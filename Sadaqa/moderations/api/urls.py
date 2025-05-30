from django.urls import path
from .views import report_comment, report_project
urlpatterns = [
    path('report_comment/', report_comment, name='report_comment'),
    path('report_project/', report_project, name='report_project'),
]