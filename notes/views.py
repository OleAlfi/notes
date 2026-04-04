from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.defaultfilters import title

from notes.models import Category, Notes
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from .forms import CategoryForm, NotesForm, LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def index(request):
    message = "Hello from Notes app"
    return render(request, "notes/index.html", {"message": message})


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NotesForm
    template_name = "notes/notes_form.html"
    success_url = reverse_lazy("notes:list_notes")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotesListViews(LoginRequiredMixin, ListView):
    model = Notes
    template_name = "notes/notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = Notes.objects.all()
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = "notes/note_details.html"


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = "notes/notes_form.html"
    success_url = reverse_lazy("notes:list_notes")

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)


class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("notes:list_notes")

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "notes/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome, {username}")
                return redirect("notes:list_notes")
    return render(request, "notes/login.html", {"form": form})


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "notes/register.html", {"form": form})

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("notes:list_notes")
    return render(request, "notes/register.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You quit from the system")
    return redirect("notes:login")
