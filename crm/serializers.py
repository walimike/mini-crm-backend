from rest_framework import serializers
from .models import Lead, Contact, Note, Reminder

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField()
    notes = NoteSerializer(many=True, read_only=True)
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'

    def get_contact(self, obj):
        """Returns a simplified contact representation."""
        if obj.contact:
            return {
                "id": obj.contact.id,
                "name": obj.contact.name,
                "email": obj.contact.email,
            }
        return None  # Handle cases where the contact is None


