from django.db import models

# Create your models here.

# Employee Model.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
