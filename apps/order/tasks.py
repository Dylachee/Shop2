from django.core.mail import send_mail

def send_confirmation_mail(instance):
    message = f"""
    Fuck you ,{instance.user.username}!
    Accept this shit son of bitch{instance.address}
    any way just suck
    http://localhost:2003/order/{instance.pk}/confirm

    """
    send_mail(
        subject='Accept order',
        message=message,
        from_email= 'test@example.com',
        recipient_list=[instance.user.email],
        fail_silently= False,
    )