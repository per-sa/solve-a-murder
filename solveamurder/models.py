from tabnanny import verbose
from django.db import models

# Create your models here.

class Suspect(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = "Suspects"

    def __str__(self):
        return f"{self.name} ({self.date_of_birth})"
    

class Victim(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    date_of_death = models.DateField()
    cause_of_death = models.CharField(max_length=100)
    main_suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Victims"

    def __str__(self):
        return f"{self.name} ({self.date_of_birth})"

class Cases(models.Model):
    case_id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=255)
    case_date = models.DateTimeField()
    case_description = models.TextField()
    case_victims = models.ManyToManyField(Victim)
    case_main_suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    is_unsolved = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Cases"

    def __str__(self):
        return f"{self.case_name} ({self.case_date}) - {self.case_main_suspect}"