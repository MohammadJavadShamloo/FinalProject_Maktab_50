from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from organization.forms import ReportForm
from organization.models import Organization


@login_required
def add_report(request, pk):
    """
        a View for creating new report using a form
    """
    organization = get_object_or_404(Organization,
                                     id=pk)
    if request.method == 'POST' and request.is_ajax():
        followup = organization.followups.create(registrar=request.user,
                                                 organization=organization,
                                                 report=request.POST.get('report'))
        return JsonResponse({
            'Status': 'Ok',
            'registrar': str(followup.registrar),
            'number': str(organization.followups.count()),
            'report': str(followup.report),
            'date': followup.date.strftime("%b. %d, %Y, %H:%M %P"),
        })
    else:
        form = ReportForm()
        return render(request,
                      'followup/report_from.html',
                      {'form': form,
                       'organization': organization})
