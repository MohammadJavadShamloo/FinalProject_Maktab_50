from django.contrib.auth.decorators import login_required
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
    if request.method == 'POST':
        form = ReportForm(data=request.POST,
                          files=request.FILES)
        if form.is_valid():
            organization.followups.create(
                registrar=request.user,
                organization=organization,
                report=form.cleaned_data['report']
            )
            return redirect('organization:organization_detail', organization.id)
        else:
            return redirect('organization:organization_list')
    else:
        form = ReportForm()
        return render(request,
                      'organization/report_from.html',
                      {'form': form,
                       'organization': organization})
