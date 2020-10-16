from django.urls import path
from .views import RegisterView, GetUserView

app_name = "productsadmin"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('find_user/', GetUserView.as_view()),
]
