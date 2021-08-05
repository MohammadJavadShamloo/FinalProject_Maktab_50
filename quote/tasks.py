from django.template.loader import render_to_string

from final_project_crm.celery import app
from django.core.mail import send_mail

from organization.models import Organization
from quote.models import Quote
from services.models import EmailHistory


@app.task
def send_quote(quote_id, organization_id):
    """
    Task To Send Email By Provided Html
    :param quote_id: Id Of Quote
    :param organization_id: Id Of Organization
    :return: mail status
    """
    organization = Organization.objects.get(id=organization_id)
    quote = Quote.objects.get(id=quote_id)
    subject = f'Quote no. {quote_id}'
    message = f'Dear {organization.contact_name}' \
              f'Here is Your Quote And Attached Pdf.'
    mail_sent = send_mail(subject, message, 'admin@HighTechStore.com', [organization.contact_email, ],
                          html_message=render_to_string('quote/pdf_template.html', {'quote': quote}))
    EmailHistory.objects.create(name='Sending Quote',
                                report=f'Sending Quote to Organization_{organization.name}'
                                       f'and Quote_{quote.id}',
                                is_sent=mail_sent,)
    return mail_sent