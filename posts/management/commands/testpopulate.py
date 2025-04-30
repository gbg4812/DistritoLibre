from django.core.management.base import BaseCommand
from posts.models import TagBuilding, Post


building_list = ["SCHOOL", "CINEMA", "UNIVERSITY", "THEATER", "LIBRARY", "PARLAMENT"]


class Command(BaseCommand):
    def handle(self, *args, **options) -> str | None:
        count = 0
        for b in building_list:
            _, created = TagBuilding.objects.get_or_create(name=b)
            if created:
                print(f"Adding {b} Building Tag")
                count += 1
            else:
                print(f"{b} Building Tag alreadey exists")

        print(f"{count} new building tags added")

        return
