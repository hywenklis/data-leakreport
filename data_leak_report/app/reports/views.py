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
            return redirect('report_success', uuid=report.uuid)
    else:
        form = ReportForm()
    return render(request, 'reports/create_report.html', {'form': form})

def report_success(request, uuid):
    return render(request, 'reports/report_success.html', {'uuid': uuid})
