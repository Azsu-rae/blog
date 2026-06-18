from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.vaults, name="vaults"),
    path("vault/<int:vault_id>/", views.folders, name="folders"),
    path("folder/<int:folder_id>/", views.notes, name="notes"),
    path("note/<int:note_id>/", views.detail, name="detail"),

    path("favorite/", views.favorite, name="favorite"),
]
