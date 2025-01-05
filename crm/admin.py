from django.contrib import admin
from .models import Lead, Contact, Note, Reminder

admin.site.register(Lead)
admin.site.register(Contact)
admin.site.register(Note)
admin.site.register(Reminder)
