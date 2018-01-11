from __future__ import unicode_literals
from datetime import datetime

from django.db import models

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class List(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_to = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
