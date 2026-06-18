from django.core.management.base import BaseCommand

from myblog.hardcoded import VAULTS
from myblog.models import Vault, User

from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        u = get_user_model().objects.create_superuser(
            username='ilyas',
            password='ilyas123',
        )
        for v_data in VAULTS:
            v = Vault.objects.create(name=v_data["name"])
            for f_data in v_data["folders"]:
                f = v.folder_set.create(name=f_data["name"])
                for n_data in f_data["notes"]:
                    n = f.note_set.create(name=n_data["name"])
                    if n_data["is_favorite"]:
                        n.favoritenote_set.create(user=u)


