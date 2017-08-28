from django.db import models
from tutorprofile.models import TutorProfile, Availability
class StripeCustomer(models.Model):
    customer_id = models.CharField(max_length=120)
    customer_email = models.CharField(max_length=120)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_email

class MyTutorCustomer(models.Model):
    parent_name = models.CharField(max_length=120)
    student_name = models.CharField(max_length=120)
    email = models.EmailField()
    tutor = models.ForeignKey('tutorprofile.TutorProfile')
    def __str__(self):
        return self.parent_name
