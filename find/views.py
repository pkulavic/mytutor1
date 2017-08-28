from django.shortcuts import render, HttpResponse
from .forms import FindForm, PaymentForm
from tutorprofile.models import TutorProfile
from django.views.generic import DetailView
from django import forms

def find(request):
    template = 'find/find.html'
    if request.method=="POST":
        form = FindForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            city = form.cleaned_data['city']
            queryset = TutorProfile.objects.filter(subject=subject, city=city)
            count = queryset.count()

            if count == 0:
                availability_set = []
            else:
                for obj in queryset:
                    availability_set = obj.availability.all()

            context = {'form': FindForm(request.POST), 'queryset': queryset, 'count': count, 'availability_set': availability_set}
    else:
        context = {'form': FindForm()}

    return render(request, template, context)





def find_detail_view(request, slug):
    tutor = TutorProfile.objects.get(slug=slug)
    availability_set = tutor.availability.all()


    TIME_CHOICES = []
    for time in availability_set:
        TIME_CHOICES.append((time, time))

    class TimeForm(forms.Form):
        for time in availability_set:
            times = forms.ChoiceField(choices=TIME_CHOICES, widget=forms.RadioSelect)

    if request.method == "POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['times']
            BoundPaymentForm = PaymentForm({'tutor': tutor, 'parent_name': '', 'student_name': '', 'time': time})
            template = 'payment/checkout.html'
            context = {'time': time, 'tutor': tutor, 'BoundPaymentForm': BoundPaymentForm}

    else:
        template = 'find/find_detail.html'
        context = {'tutor': tutor, 'availability_set': availability_set, 'form': TimeForm}

    return render(request, template, context)
