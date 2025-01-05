from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, ContactViewSet, NoteViewSet, ReminderViewSet

router = DefaultRouter()
router.register('leads', LeadViewSet)
router.register('contacts', ContactViewSet)
router.register('notes', NoteViewSet)
router.register('reminders', ReminderViewSet)

urlpatterns = router.urls
