from django.db import models


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

    def __str__(self):
        return self.name
