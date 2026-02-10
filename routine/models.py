from django.db import models

class Class(models.Model):
    section = models.CharField(max_length=2)  # A1, A2, B1, B2
    date = models.DateField()
    time = models.TimeField()
    teacher = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    credit = models.FloatField()
    assignment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.course} - {self.section} - {self.date}"


class Lab(models.Model):
    lab_group = models.CharField(max_length=2)  # A1/A2/B1/B2
    date = models.DateField()
    time = models.TimeField()
    teacher = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    credit = models.FloatField()

    def __str__(self):
        return f"{self.course} - {self.lab_group} - {self.date}"
