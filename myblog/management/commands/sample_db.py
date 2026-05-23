from django.core.management.base import BaseCommand

from myblog.hardcoded import VAULTS
from myblog.models import Vault


class Command(BaseCommand):

    def handle(self, *args, **options):
        for v_data in VAULTS:
            v = Vault.objects.create(name=v_data["name"])
            for f_data in v_data["folders"]:
                f = v.folder_set.create(name=f_data["name"])
                for n_data in f_data["notes"]:
                    f.note_set.create(name=n_data["name"])
