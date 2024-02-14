from django.db import models






class staff(models.Model):
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phonenumber=models.IntegerField(null=True)
    department=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    is_approved = models.BooleanField(default=False)
   

    def __str__(self):
        return self.firstname
    

# Create your models here.
    
class cust(models.Model):
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phonenumber=models.IntegerField(null=True)
    state=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    

    def __str__(self):
        return self.username
    

    
class data(models.Model):
      room_id=models.IntegerField(null=True)
      amount=models.IntegerField(null=True)
      bed_space=models.CharField(max_length=200,null=True)
      details=models.CharField(max_length=200,null=True)
      type=models.CharField(max_length=200,null=True)
      image=models.ImageField(null=True,blank=True,upload_to="images/")
    


     

