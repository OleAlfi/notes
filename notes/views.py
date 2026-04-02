from django.shortcuts import render
from django.http import HttpResponse
from notes.models import Category, Notes
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .forms import CategoryForm, NotesForm
from django.utils.timezone import now

def index(request):
    message = "Hello from Notes app"
    return render(request, "notes/index.html", {"message": message})

# def get_notes(request):
#     notes = Notes.objects.all()
#     return render(request, "notes/notes.html", {"notes": notes})

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    template_name = "notes/notes_form.html"
    success_url = reverse_lazy("notes:list_notes")

class NotesListViews(ListView):
    model = Notes
    template_name = "notes/notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search")

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

class NotesDetailView(DetailView):
    model = Notes
    template_name = "notes/note_details.html"

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = "notes/notes_form.html"
    success_url = reverse_lazy("notes:list_notes")

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("notes:list_notes")


# class CategoryCreateView(CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = "notes/category_form.html"
#     success_url = reverse_lazy("notes")