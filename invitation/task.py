from time import sleep
from django.core.mail import send_mail

from celery import shared_task



# In celery producer and the consumer/worker refer to same function
@shared_task # worker notices every call from producer
def send_email_task(details):
    sleep(3)
    print("Sending email", details.get('email'))
    send_mail(
        "You are invited",
        f"Hi {details.get('full_name')}\n You are invited for grant event!\n \n See you soon!",
        "wearelearning@django.com",
        [details.get('email')],
        fail_silently=True

    )