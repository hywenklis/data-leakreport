from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choose-identity/', views.choose_identity, name='choose_identity'),
    path('report/identified/', views.create_report, name='identified_report'),
    path('report/anonymous/', lambda r: views.create_report(r, anonymous=True), name='anonymous_report'),
    path('report/success/<uuid:uuid>/', views.report_success, name='report_success'),
]
