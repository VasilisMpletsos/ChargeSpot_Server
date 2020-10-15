from django.urls import path
from .views import RegisterView

app_name = "productsadmin"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('register/', RegisterView.as_view()),
]
