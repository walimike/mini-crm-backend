import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from crm.models import Contact, Lead, Note, Reminder
from datetime import datetime, timedelta

def run():
    # Create contacts
    contacts = [
        Contact(name="John Doe", email="john@example.com", phone="1234567890", location="New York"),
        Contact(name="Jane Smith", email="jane@example.com", phone="0987654321", location="Los Angeles"),
        Contact(name="Bob Johnson", email="bob@example.com", phone="5555555555", location="Chicago"),
        Contact(name="Alice Williams", email="alice@example.com", phone="1111111111", location="Houston"),
    ]
    Contact.objects.bulk_create(contacts)

    # Fetch contacts and users
    contacts = Contact.objects.all()
    user = User.objects.last()  # Ensure you have at least one user created

    # Create leads
    leads = [
        Lead(contact=contacts[0], status="open", found_by=user),
        Lead(contact=contacts[1], status="closed", found_by=user),
        Lead(contact=contacts[2], status="open", found_by=user),
        Lead(contact=contacts[3], status="closed", found_by=user),
    ]
    Lead.objects.bulk_create(leads)

    # Fetch leads
    leads = Lead.objects.all()

    # Create notes
    notes = [
        Note(lead=leads[0], content="First note for John"),
        Note(lead=leads[1], content="First note for Jane"),
        Note(lead=leads[2], content="First note for Bob"),
        Note(lead=leads[3], content="First note for Alice"),
    ]
    Note.objects.bulk_create(notes)

    # Create reminders
    reminders = [
        Reminder(lead=leads[0], title="Follow up with John", reminder_date=datetime.now() + timedelta(days=1)),
        Reminder(lead=leads[1], title="Email Jane", reminder_date=datetime.now() + timedelta(days=2)),
        Reminder(lead=leads[2], title="Call Bob", reminder_date=datetime.now() + timedelta(days=3)),
        Reminder(lead=leads[3], title="Meet Alice", reminder_date=datetime.now() + timedelta(days=4)),
    ]
    Reminder.objects.bulk_create(reminders)

    print("Database seeded successfully!")

if __name__ == "__main__":
    run()
