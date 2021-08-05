from django.template.loader import render_to_string

from final_project_crm.celery import app
from django.core.mail import send_mail

from organization.models import Organization
from quote.models import Quote


@app.task
def send_quote(quote_id, organization_id):
    organization = Organization.objects.get(id=organization_id)
    quote = Quote.objects.get(id=quote_id)
    subject = f'Quote no. {quote_id}'
    message = f'Dear {organization.contact_name}' \
              f'Here is Your Quote And Attached Pdf.'
    mail_sent = send_mail(subject, message, 'admin@HighTechStore.com', [organization.contact_email, ],
                          html_message=render_to_string('quote/pdf_template.html', {'quote': quote}))
