from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, 
            message, 
            message_email,
            ['e-mail'],
            fail_silently=False, # if the email is not sent, it will raise an error
        )
             
         
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})