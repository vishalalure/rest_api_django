from django.db import models

class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    Project=models.CharField(max_length=25)

    def __str__(self):
        return self.firstname

class client(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email_id=models.CharField(max_length=25)
    client_id=models.CharField(max_length=25)
    Project=models.CharField(max_length=25)

    def __str__(self):
        return self.firstname

class Project(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email_id=models.CharField(max_length=25)
    client_id=models.CharField(max_length=25)
    Project=models.CharField(max_length=25)

    def __str__(self):
        return self.firstname
