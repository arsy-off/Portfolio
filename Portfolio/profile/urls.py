from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompaniesListCreate.as_view()),
    path('positions/', views.PositionsListCreate.as_view()),
    path('tasks/', views.TasksListCreate.as_view()),
    path('technologies/', views.TechnologiesListCreate.as_view()),
]