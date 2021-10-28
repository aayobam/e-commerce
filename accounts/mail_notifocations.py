from django.core.mail import send_mail
from e_commerce.settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.models import User


# helper class to send mail to users and admins upon registeration.
class MailNotificationForRegisteration():

    def __init__(self, recipient_email, sender_email, mail_subject, message_body):
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.mail_subject = mail_subject
        self.message_body = message_body

    # send main to customers
    def mail_new_customer(self):
        send_mail(
            from_email=self.sender_email,
            recipient_list=[str(self.recipient_email)],
            subject=self.mail_subject,
            message=self.message_body,
            fail_silently=False
        )

    # send mails to admins
    def mail_admin(self):
        message_body = f"<h1>Hello {self.recipient_email}, You got a newly registered customer</h1>",
        mail_subject = f"<h1>New customer registeration</h1>"
        sender_email = DEFAULT_FROM_EMAIL

        users = User.objects.filter(is_superuser=True)
        for user in users:
            self.sender_email = sender_email
            self.recipient_email = user.email
            self.mail_subject = mail_subject
            self.message_body = message_body,
            send_mail(
                from_email=self.sender_email,
                recipient_list=[self.recipient_email],
                subject=self.mail_subject,
                html_message=self.message_body,
                fail_silently=False
            )


# helper class for sending order notifications to customers and admin
class MailNotificationForOrders():

    def __init__(self, recipient_email, sender_email, mail_subject, message_body):
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.mail_subject = mail_subject
        self.message_body = message_body

    # send mail to customers
    def mail_new_customer(self):
        send_mail(
            from_email=self.sender_email,
            recipient_list=[str(self.recipient_email)],
            subject=self.mail_subject,
            message=self.message_body,
            fail_silently=False
        )

    # send mail to admins
    def mail_admin(self):
        message_body = f"<h1>Hello {self.recipient_email}, You got a new order </h1>",
        mail_subject = f"<h1>New customer registeration</h1>"
        sender_email = DEFAULT_FROM_EMAIL

        users = User.objects.filter(is_superuser=True)
        for user in users:
            self.sender_email = sender_email
            self.recipient_email = user.email
            self.mail_subject = mail_subject
            self.message_body = message_body,
            send_mail(
                from_email=self.sender_email,
                recipient_list=[self.recipient_email],
                subject=self.mail_subject,
                html_message=self.message_body,
                fail_silently=False
            )