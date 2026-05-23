from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.vaults, name="vaults"),
    path("folders/<int:vault_id>/", views.folders, name="folders"),
    path("notes/<int:folder_id>/", views.notes, name="notes"),
    path("content/<int:note_id>/", views.content, name="content"),
]
