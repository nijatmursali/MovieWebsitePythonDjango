from django.db import models

CATEGORY_CHOICES = (
    ('A', 'ACTION'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)
LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
)

STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)

LINK_CHOICES = (
    ('T', 'WATCH TRAILER'),
    ('W', 'WATCH MOVIE'),
    ('D', 'DOWNLOAD LINK'),
)

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    yearofprod = models.DateField()
    countryofprod = models.CharField(max_length=100, default="")
    movieDirector = models.CharField(max_length=100, default="")
    movieWriter = models.CharField(max_length=100, default="")
    runtime = models.CharField(max_length=100, default= "")
    view_count = models.IntegerField(default=0)
    ratings = models.FloatField(default=0)
    trailerlink = models.URLField()

    def __str__(self):
        return  self.title


class MovieLink(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    #movielink = models.URLField()
    trailerlink = models.URLField()

    def __str__(self):
        return str(self.movie) + " | | " + str(self.type)
    