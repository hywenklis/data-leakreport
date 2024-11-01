from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choose-identity/', views.choose_identity, name='choose_identity'),
    path('about/', views.about, name='about'),
    path('report/identified/', views.create_report, name='identified_report'),
    path('report/anonymous/', lambda r: views.create_report(r, anonymous=True), name='anonymous_report'),
    path('report/success/<uuid:correlationId>/', views.report_success, name='report_success'),
    path('view-reports/', views.view_reports, name='view_reports'),
    path('view-identified-reports/', views.view_identified_reports, name='view_identified_reports'),
    # path('view-identified-reports/', views.view_anonymous_report, name='view_anonymous_report'),
]
