from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def home(request):
    return render(request, 'reports/home.html')

def choose_identity(request):
    return render(request, 'reports/choose_identity.html')

def create_report(request, anonymous=False):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.is_anonymous = anonymous
            report.save()
            return redirect('report_success', correlationId=report.correlationId)
    else:
        form = ReportForm()
    return render(request, 'reports/create_report.html', {'form': form})

def report_success(request, correlationId):
    return render(request, 'reports/report_success.html', {'correlationId': correlationId})

def about(request):
    return render(request, 'reports/about.html')

def view_reports(request):
    return render(request, 'view_reports.html')

import re
from django.shortcuts import render
from .models import Report

def view_identified_reports(request):
    reports = None
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(email_regex, identifier):
            reports = Report.objects.filter(email=identifier)
        else:
            reports = Report.objects.filter(correlationId=identifier)

    return render(request, 'reports/view_reports.html', {'reports': reports})
