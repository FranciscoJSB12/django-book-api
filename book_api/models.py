from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
    # If we ever want to see all the data inside of a table we're going to see the title in order to identify the book that we want