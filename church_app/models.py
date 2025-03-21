from django.db import models

# Create your models here.
from django.db import models

#gallery
class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('church', 'Church'),
        ('ministry', 'Ministry'),
        ('celebration', 'Celebration'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/store/images/thumbimages' ,default="",blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


# daily verse
class Verse_of_the_day(models.Model):
    date=models.DateField()
    englishname=models.CharField(max_length=20)
    tamilname=models.CharField(max_length=20)
    chapter=models.IntegerField()
    versecount=models.IntegerField()
    verse=models.TextField()
    kjv=models.TextField()


# contact
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)  # Changed to CharField for flexibility
    address = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


#sermons
class Sermons(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    author=models.CharField(max_length=20)
    body=models.TextField()
    youtubecode=models.CharField(max_length=1200,default='')
    keywords=models.TextField()

#ministry
class Ministry(models.Model):
    CATEGORY_CHOICES = [
        ('childrens ministry', 'Childrens Ministry'),
        ('youths ministry', 'Youths Ministry'),
        ('sports ministry', 'Sports Ministry'),
        ('mens ministry', 'Mens Ministry'),
        ('womens ministry', 'Womens Ministry'),


    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/store/images/ministry' ,default="",blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    body=models.TextField()

    def __str__(self):
        return self.title
    

#our teams
class Team(models.Model):
    author=models.CharField(max_length=30)
    role=models.CharField(max_length=50)
    description=models.TextField()
    image = models.ImageField(upload_to='media/store/images/teams' ,default="",blank=True)


#Events
class Event(models.Model):
    image = models.ImageField(upload_to='media/store/images/event' ,default="",blank=True)
    title=models.CharField(max_length=100)
    date=models.DateField()
    venue=models.CharField(max_length=100)
    calendarcode=models.CharField(max_length=1200,default='')

#membership

class ChurchMember(models.Model):
    profile_image = models.ImageField(upload_to='media/store/images/profile' ,default="",blank=True)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Engaged', 'Engaged'),
    ]
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    
    phone = models.CharField(max_length=15)
    emergency_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    # Address Fields
    resident_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    door_number = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    # Church Transfer Fields
    CHURCH_TRANSFER_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    church_transfer = models.CharField(max_length=3, choices=CHURCH_TRANSFER_CHOICES, blank=True, null=True)
    previous_church = models.CharField(max_length=255, blank=True, null=True)

    # Areas of Interest in Ministry
    MINISTRY_CHOICES = [
        ('Worship Team', 'Worship Team'),
        ('Youth Ministry', 'Youth Ministry'),
        ('Children’s Ministry', 'Children’s Ministry'),
        ('Prayer Group', 'Prayer Group'),
        ('Outreach & Evangelism', 'Outreach & Evangelism'),
        ('Media & Technical Support', 'Media & Technical Support'),
        ('Teaching & Discipleship', 'Teaching & Discipleship'),
        ('Ushering & Hospitality', 'Ushering & Hospitality'),
    ]
    ministry_interest = models.CharField(max_length=50, choices=MINISTRY_CHOICES)

    occupation = models.CharField(max_length=255)
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    

#waiting login status
class Usersstatus(models.Model):
    username= models.CharField(max_length=100)
    status= models.IntegerField()  


###certificate
class Certificate(models.Model):
    name = models.CharField(max_length=255)
    certificate = models.FileField(upload_to="media/store/pdf/certificates")
    certificatestatus= models.IntegerField(default=0)

    def __str__(self):
        return self.name