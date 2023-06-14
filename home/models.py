from django.db import models
# Model creation
class Userngo(models.Model):
    name = models.TextField(max_length=122)
    email = models.TextField(max_length=122)
    phone = models.TextField(max_length=12)
    password = models.CharField(max_length=300)
    address = models.TextField(max_length=102)
    certification = models.TextField(max_length=102)

    def __str__(self):
        return self.name

class Userdonor(models.Model):
    name = models.TextField(max_length=122)
    email = models.TextField(max_length=122)
    phone = models.TextField(max_length=12)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Donations(models.Model):
    donor_name = models.TextField(max_length=122)
    medicine_name = models.TextField(max_length=122)
    pickup_address = models.TextField(max_length=120)
    purpose = models.TextField(max_length=30)
    expiry_date = models.DateField()
    phone = models.CharField(max_length=12)
    accepted_by=models.TextField(max_length=12)
    email = models.TextField(max_length=122,default='xyz')
    def __str__(self):
        return self.donor_name

