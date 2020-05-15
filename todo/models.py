from django.db import models

# Create your models here.
class Item(models.Model):

    # Fields
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    # Methods
    def __str__(self):
        """String for representing the Item object (in Admin site etc.)."""
        return self.name