from django.db import models
# Create your models here.
class user_registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    username=models.CharField(max_length=50)
    def __str__(self):
        return self.username

# class employee_registration(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     gender=models.CharField(max_length=10)
#     phone_no=models.IntegerField()
#     location = models.CharField(max_length=50)
#     category=models.CharField(max_length=50)
#     specialised_skill=models.CharField(max_length=50)
#     experience=models.CharField(max_length=50)
#     username=models.CharField(max_length=50)
#     action = models.CharField(max_length=99)
#     status = models.CharField(max_length=99)
#     def __str__(self):
#         return self.username

class log_in(models.Model):
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    # action=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
    def __str__(self):
        return self.username

class payment(models.Model):
    username = models.CharField(max_length=50)
    email=models.EmailField()
    employee_name=models.CharField(max_length=50)
    advAmound=models.IntegerField()
    booking=models.CharField(max_length=50)
    pay_status=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class employee_registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    gender=models.CharField(max_length=10)
    phone_no=models.IntegerField()
    license=models.FileField()
    photo=models.FileField()
    # biodata=models.FileField()
    # specialised_skill = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    action = models.CharField(max_length=99)
    status = models.CharField(max_length=99)
    def __str__(self):
        return self.username

class emp_gallery(models.Model):
    username = models.CharField(max_length=100)
    work1 = models.FileField()
    work2 = models.FileField()
    work3 = models.FileField()
    # work4 = models.FileField()
    # work5 = models.FileField()
    # work6 = models.FileField()

    def __str__(self):
        return self.username

class feedback1(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField()
    employee_name = models.CharField(max_length=10)
    review = models.CharField(max_length=150)

class common_feedback(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.CharField(max_length=150)


class Mesage(models.Model):
    employee_name=models.CharField(max_length=10)
    email=models.EmailField()
    messages= models.CharField(max_length=100)

class booking(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_no = models.IntegerField()
    date=models.DateField()
    address=models.CharField(max_length=100)
    employee_name=models.CharField(max_length=50)
    action=models.CharField(max_length=99)
    payment=models.CharField(max_length=99)
    day=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PasswordReset(models.Model):
    user_registration = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    token = models.CharField(max_length=4)

class amountdetails(models.Model):
    username = models.CharField(max_length=50)
    fullamount = models.IntegerField()
    advAmound = models.IntegerField()
    def __str__(self):
        return self.username




