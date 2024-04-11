from django.core.mail import EmailMessage
from game.models import HomePage


def send_sms_code(email, data):
    das = HomePage.objects.all().first()
    das.text_for_email += f'\n{data}'
    try:
        message = EmailMessage(
            to=[email],
            subject='',
            body=das,
            # from_email='noreply@zherdesh.ru'
        )

        message.send()
    except:
        return False
    return True
