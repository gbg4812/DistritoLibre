from django.core.management.base import BaseCommand, CommandError
from typing import Any

from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Creates dev user"

    def handle(self, *args: Any, **options: Any) -> str | None:
        user = User.objects.create_user(
            "guillem",
            "guillembaldi@gmail.com",
            "superadmin",
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        self.stdout.write(self.style.SUCCESS("Dev user created!"))
