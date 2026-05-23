from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Vault, Folder, Note


def vaults(request):
    vaults = Vault.objects.all()
    template = loader.get_template("blog/items.html")
    context = {
        "item_type": "vaults",
        "item_content": "folders",
        "content_url": "blog:folders",
        "items": vaults
    }
    return HttpResponse(template.render(context, request))


def folders(request, vault_id):
    folders = Folder.objects.filter(vault__id=vault_id)
    context = {
        "item_type": "folders",
        "item_content": "notes",
        "content_url": "blog:notes",
        "items": folders
    }
    return render(request, "blog/items.html", context)


def notes(request, folder_id):
    notes = Note.objects.filter(folder__id=folder_id)
    context = {
        "item_type": "notes",
        "item_content": "content",
        "content_url": "blog:content",
        "items": notes
    }
    return render(request, "blog/items.html", context)


def content(request, note_id):
    try:
        Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404("note doesn't exist")
    return HttpResponse(f"requesting content for note {note_id}.")
