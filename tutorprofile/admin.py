from django.contrib import admin
from .models import (
        TutorProfile,
        Subject,
        City,
        Availability,
        Time,
        School
    )

admin.site.register(TutorProfile)
admin.site.register(Subject)
admin.site.register(City)
admin.site.register(Availability)
admin.site.register(Time)
admin.site.register(School)
