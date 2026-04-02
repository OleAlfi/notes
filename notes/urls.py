from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.NotesListViews.as_view(), name="list_notes"),

    path("create/", views.NotesCreateView.as_view(), name="note_create"),
    path("<int:pk>/details/", views.NotesDetailView.as_view(), name="note_details"),
    path("<int:pk>/edit/", views.NotesUpdateView.as_view(), name="note_edit"),
    path("<int:pk>/delete/", views.NotesDeleteView.as_view(), name="note_delete"),

]