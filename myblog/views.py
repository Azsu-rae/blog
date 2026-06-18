
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Vault, Folder, Note


def vaults(request):
    return HttpResponse(loader.get_template("blog/items.html").render({
        "item_type": "vaults",
        "item_content": "folders",
        "content_url": "blog:folders",
        "items": Vault.objects.all()
    }, request))


def folders(request, vault_id):
    try:
        return HttpResponse(loader.get_template("blog/items.html").render({
            "item_type": "folders",
            "item_content": "notes",
            "content_url": "blog:notes",
            "items": Folder.objects.filter(vault=Vault.objects.get(id=vault_id))
        }, request))
    except Vault.DoesNotExist:
        raise Http404("Requested Vault doesn't exist!")


def notes(request, folder_id):
    try:
        return HttpResponse(loader.get_template("blog/items.html").render({
            "item_type": "notes",
            "item_content": "detail",
            "content_url": "blog:detail",
            "items": Note.objects.filter(folder=Folder.objects.get(id=folder_id))
        }, request))
    except Folder.DoesNotExist:
        raise Http404("Requested Folder doesn't exist!")


def detail(request, note_id):
    try:
        return HttpResponse(f"requesting content for note '{Note.objects.get(id=note_id)}'.")
    except Note.DoesNotExist:
        raise Http404("Requested Note doesn't exist!")


def favorite(request):
    return HttpResponse("Success.")
