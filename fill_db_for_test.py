import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "distrito_libre_backend.settings"
)  # Replace 'your_project_name'
django.setup()

from django.contrib.auth.models import User
from posts.models import (
    Sections,
    Post,
    get_anonymus_user,
)  # Replace 'your_app_name'

fake = Faker("es_ES")  # Use Spanish locale for Faker if in Spain


def create_random_post(section, anonymous_user_id):
    """Creates a random Post instance for a given section."""
    title = fake.sentence()[:49]
    content = fake.paragraph(nb_sentences=random.randint(3, 10))
    coverimg = fake.image_url() if random.random() < 0.7 else ""
    author_id = (
        random.choice(User.objects.all()).id
        if random.random() < 0.9
        else anonymous_user_id
    )
    post = Post(
        title=title,
        author_id=author_id,
        section=section,
        content=content,
        coverimg=coverimg,
    )
    post.save()
    print(f"Created post '{title}' in section '{section}'")


def populate_database():
    """Fills the database with random Post instances."""
    anonymous_user_id = get_anonymus_user()

    # Ensure there's at least one regular user
    if not User.objects.exclude(username="anonymous").exists():
        User.objects.create_user(username="testuser", password="testpassword")
        print("Created a default test user.")

    for section in Sections:
        print(f"\nCreating 5 random posts for section: {section.label}")
        for _ in range(5):
            create_random_post(section.value, anonymous_user_id)

    print("\nDatabase population complete.")


if __name__ == "__main__":
    populate_database()
