from django.shortcuts import render
from find.views import find_detail_view
from .models import StripeCustomer, MyTutorCustomer
from tutorprofile.models import TutorProfile
from django.core.mail import send_mail
import stripe

def checkout(request):
    stripe.api_key = "sk_live_lpFbrd5HLHskXwpotoxLOXK1"
    if request.method=="POST":
        token = request.POST['stripeToken']
        email = request.POST['stripeEmail']
        parent_name = request.POST['parent_name']
        student_name = request.POST['student_name']
        tutor = request.POST['tutor']
        time = request.POST['time']
        tutorinstance = TutorProfile.objects.get(name=tutor)
        tutoremail = tutorinstance.email
        tutorphone = tutorinstance.phone
        tutorschool = tutorinstance.school

        # create stripe customer
        customer = stripe.Customer.create(
            email = email,
            source = token
        )

        customer_id = customer['id']

        # subscribe the customer
        stripe.Subscription.create(
            customer = customer_id,
            items = [
                {
                    'plan': 'weekly'
                }
            ]
        )

        # add customer to the database
        StripeCustomer.objects.create(
            customer_id=customer_id,
            customer_email=email
        )

        MyTutorCustomer.objects.create(
            parent_name=parent_name,
            student_name=student_name,
            email=email,
            tutor=tutorinstance,
        )


        send_mail(
            'NEW CUSTOMER',
            "Parent name: %s. Student name: %s. Email: %s. // Tutor name: %s. Tutor Email: %s. Time: %s" % (parent_name, student_name, email, tutor, tutoremail, time),
            email,
            ['mytutorforward@gmail.com'],
            fail_silently=True,
        )

    context = {'email': email, 'tutoremail': tutoremail, 'tutorphone': tutorphone, 'tutor': tutor, 'tutorschool': tutorschool}
    template = 'payment/finish.html'
    return render(request, template, context)
