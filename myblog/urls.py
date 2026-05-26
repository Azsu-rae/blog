from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.vaults, name="vaults"),
    path("folders/<int:vault_id>/", views.folders, name="folders"),
    path("notes/<int:folder_id>/", views.notes, name="notes"),
    path("detail/<int:note_id>/", views.detail, name="detail"),

    path("search_results/", views.search_results, name="search_results"),
    path("favorite/", views.favorite, name="favorite"),
]
