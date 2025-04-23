from django.core.management.base import BaseCommand
from posts.models import (
    TagSeccio,
    SubTagEdifici,
)  # Replace 'yourapp' with your app name

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
    help = (
        "Populates TagSeccio with predefined tag names and assigns Escola to edificis"
    )

    def handle(self, *args, **kwargs):
        # Ensure "Escola" exists
        escola, _ = SubTagEdifici.objects.get_or_create(name="Escola")
        created_count = 0

        for name in tag_names:
            tag_seccio, created = TagSeccio.objects.get_or_create(name=name)
            tag_seccio.edificis.add(escola)

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created TagSeccio: {name} and linked to Escola"
                    )
                )
            else:
                self.stdout.write(
                    f"TagSeccio already exists: {name}, ensured link to Escola"
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone. {created_count} new TagSeccio entries created."
            )
        )

