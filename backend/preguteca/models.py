from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)


class Building(models.Model):
    name = models.CharField(max_length=128, primary_key=True)


class BuildingInSection(models.Model):
    pk = models.CompositePrimaryKey("building_id", "section_id")
    building = models.ForeignKey(Building, models.CASCADE)
    section = models.ForeignKey(Building, models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=128, primary_key=True)


class Post(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    date = models.DateField()
    author = models.ForeignKey(User, models.CASCADE)
    section = models.ForeignKey(Section, models.CASCADE)
    building = models.ForeignKey(Building, models.CASCADE)

    logo = models.CharField(max_length=256)
