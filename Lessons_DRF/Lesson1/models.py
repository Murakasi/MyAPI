from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    prica = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField()

    def __str__(self):
        return self.title
    

    class Meta:
        db_table = 'books'
        indexes = [
            models.Index(fields=['available']),
        ]