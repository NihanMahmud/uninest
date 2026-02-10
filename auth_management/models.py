from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    roll_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def get_section(self):
        """Automatically determine section based on roll number"""
        roll = self.roll_number
        # A/B
        if 1 <= roll <= 60:
            main_section = "A"
        elif 61 <= roll <= 121:
            main_section = "B"
        else:
            main_section = "Unknown"

        # Subsection A1/A2/B1/B2
        if 1 <= roll <= 30:
            sub_section = "A1"
        elif 31 <= roll <= 60:
            sub_section = "A2"
        elif 61 <= roll <= 90:
            sub_section = "B1"
        elif 91 <= roll <= 121:
            sub_section = "B2"
        else:
            sub_section = "Unknown"

        return {"main": main_section, "sub": sub_section}