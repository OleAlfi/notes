from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("notes:note_details", args=[self.pk])
