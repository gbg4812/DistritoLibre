from django.core.management.base import BaseCommand, CommandError
from typing import Any

from posts.models import Tag, TagBuilding


flattened_list = [
    "ANARQUISMO_CRISTIANO",
    "COMUNALISMO_TRADICIONALISTA",
    "PAELO_LIBERTARISMO",
    "SOCIALISMO_CRISTIANO",
    "LIBERALISMO_CONSERVADOR",
    "NACIONAL_BOLCHEVISMO",
    "FASCISMO_CLERICAL",
    "NEO_REACCIONNRX",
    "ANARCO_COMUNISMO",
    "MUTUALISMO",
    "LIBERTARISMO",
    "SOCIALISMO_DEMOCRATICO",
    "LIBERALISMO_CLASICO",
    "MARXISMO_LENINISMO",
    "FASCISMO_CLASICO",
    "CAPITALISMO_LIBERAL",
    "POS_ANARQUISMO",
    "ANARQUISMO_EGOISTA",
    "IZQUIERDA_LIBERTARIA",
    "LUXEMBURGISMO",
    "SOCIO_LIBERALISMO",
    "COMUNISMO_POSMARXISTA",
    "TECNOCRACIA_PROGRESISTA",
    "JACOBINISMO",
]

city_buildings_with_icons = [
    ("Hospital", "mdi:hospital"),
    ("Library", "mdi:library"),
    ("Police Station", "mdi:police-station"),
    ("Fire Station", "mdi:fire-truck"),
    ("City Hall", "mdi:town-hall"),
    ("Post Office", "mdi:email-outline"),
    ("School", "mdi:school"),
    ("University", "mdi:school-outline"),
    ("Museum", "mdi:bank"),
    ("Theater", "mdi:drama-masks"),
    ("Courthouse", "mdi:scale-balance"),
    ("Train Station", "mdi:train"),
    ("Bus Terminal", "mdi:bus"),
    ("Airport", "mdi:airplane"),
    ("Community Center", "mdi:account-group"),
    ("Sports Arena", "mdi:stadium"),
    ("Shopping Mall", "mdi:shopping"),
    ("Public Market", "mdi:store"),
    ("Power Plant", "mdi:transmission-tower"),
    ("Water Treatment Plant", "mdi:water-pump"),
]


class Command(BaseCommand):
    help = "Fills initial db data for the posts app"

    def handle(self, *args: Any, **options: Any) -> str | None:
        for item in flattened_list:
            if Tag.objects.filter(name=item).exists():
                tag = Tag.objects.create(name=item)
                self.stdout.write(self.style.SUCCESS(f"Tag {tag.name} created"))
                tag.save()

        self.stdout.write(self.style.SUCCESS("All section tags writen successfully"))

        for b in city_buildings_with_icons:
            if TagBuilding.objects.filter(name=b[0]).exists():
                build = TagBuilding.objects.create(name=b[0], icon=b[1])
                self.stdout.write(self.style.SUCCESS(f"Tag {build.name} created"))
                build.save()

        self.stdout.write(self.style.SUCCESS("All building tags writen successfully"))
