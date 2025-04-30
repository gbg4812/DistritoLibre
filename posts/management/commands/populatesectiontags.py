from django.core.management.base import BaseCommand
from posts.models import Tag

tag_names = [
    "ANARQUISMOCRISTIANO",
    "COMUNALISMOTRADICIONALISTA",
    "PAELOLIBERTARISMO",
    "SOCIALISMOCRISTIANO",
    "LIBERALISMOCONSERVADOR",
    "NACIONALBOLCHEVISMO",
    "FASCISMOCLERICAL",
    "NEOREACCIONNRX",
    "ANARCOCOMUNISMO",
    "MUTUALISMO",
    "LIBERTARISMO",
    "SOCIALISMODEMOCRATICO",
    "LIBERALISMOCLASICO",
    "MARXISMOLENINISMO",
    "FASCISMOCLASICO",
    "CAPITALISMOILIBERAL",
    "POSANARQUISMO",
    "ANARQUISMOEGOISTA",
    "IZQUIERDALIBERTARIA",
    "LUXEMBURGISMO",
    "SOCIOLIBERALISMO",
    "COMUNISMOPOSMARXISTA",
    "TECNOCRACIAPROGRESISTA",
    "JACOBINISMO",
]


class Command(BaseCommand):
    help = "Populates db with predefined tag names"

    def handle(self, *args, **kwargs):
        created_count = 0

        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created TagSeccio: {name}"))
            else:
                self.stdout.write(f"TagSeccio already exists: {name}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone. {created_count} new TagSeccio entries created."
            )
        )
