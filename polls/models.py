# Create your models here.
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return 'Person(First_Name = ' + self.first_name + ', Last_Name = ' + self.last_name + ', Salary = ' \
               + str(self.salary) + ')'



