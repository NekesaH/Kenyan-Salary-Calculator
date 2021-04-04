from django.db import models

# Create your models here.
class Taxes(models.Model):
    
    basic_salary = models.FloatField('BASIC SALARY', default='0.00' )
    
    allowances = models.FloatField('ALLOWANCES', default='0.00')

    nhif =models.BooleanField('DEDUCT NHIF')

    nssf =models.BooleanField('DEDUCT NSSF')

    






