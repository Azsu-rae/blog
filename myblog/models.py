from django.db import models
from django.contrib.auth.models import User


class Vault(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Folder(models.Model):
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    @property
    def is_favorite(self):
        return len((self.favoritenote_set.filter(id=self.id))) > 0

    def __str__(self):
        return self.name


class FavoriteNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes '{self.note.name}'"
