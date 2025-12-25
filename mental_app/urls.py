from django.urls import path
from . import views

urlpatterns = [
    path("patients_t/", views.patients_table, name="patients_tables"),
    path('predict/', views.predict_view, name='predict'),
]

