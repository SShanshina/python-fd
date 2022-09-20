from django.core.mail import send_mail

EMAIL = 'valid_email@example.org'

SUBJECTS = [
    'Registration confirmation',
    'Password reset',
    'Order confirmation'
]

MESSAGES = [
    'New user has been registered successfully',
    'Your password has been reset successfully',
    'Dear customer, thank you for order. Our manager will contact you soon to confirm order details'
]


def send_custom_mail(user, subject, message):
    return send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
