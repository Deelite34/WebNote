from django.db import models


class Note(models.Model):
    content = models.CharField(max_length=160, blank=False)
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        return str(self.id)
