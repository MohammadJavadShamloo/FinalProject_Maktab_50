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
        form = ReportForm()
        form.instance.registrar = request.user
        form.instance.organization = organization
        form.instance.report = request.POST.get('report')
        form.save()
        return JsonResponse({
            'Status': 'Ok'
        })
    else:
        form = ReportForm()
        return render(request,
                      'organization/report_from.html',
                      {'form': form,
                       'organization': organization})
