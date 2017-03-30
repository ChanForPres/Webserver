from django.db import models

# Create your models here.

# Inheriting from models.Model gives built in methods to use
# Each class is a database table, its columns represent data fields

#/Users/marcus/PycharmProjects/untitled/DB_start/models.py
class Artist(models.Model):
    name = models.CharField("artist", max_length=50) #will display "artist" in front of artist-name
    year_formed = models.PositiveIntegerField()

#   Initialization Example
#     newArtist = Artist(name = 'Artist Name', year_formed = 2015);
#     newArtist.save();




# Album will be a foreign key
# Many to 1 relation ie (Single artist -> many albums)
class Album(models.Model):
    name = models.CharField("album", max_length=50) #will display "album" in front of album-name
    artist = models.ForeignKey(Artist)


