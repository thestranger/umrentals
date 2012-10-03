from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # other fields besides generic User fields  

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

ROOM_CHOICES = (
    ('Commons', (
            ("4BR2BA", "4 Bedroom/ 2 Bath"),
            ("2BR2BA", "2 Bedroom/ 2 Bath"),
            )
     ),
    ('Courtyards', (
            ("4BR2BA", "4 Bedroom/ 2 Bath"),
            ('4BR4BA', '4 Bedroom/ 4 Bath'),
            ('2BR2BA', '2 Bedroom/ 2 Bath'),
            )
     ),
    ('View', (
            ('2BR2BA', '2 Bedroom/ 2 Bath'),
            ("4BR2BA", "4 Bedroom/ 2 Bath"),
            ('4BR4BA', '4 Bedroom/ 4 Bath'),
            )
     ),
    ('Varsity', (
            ('2BR2BA', '2 Bedroom/ 2 Bath'),
            ("4BR3BA", "4 Bedroom/ 3 Bath"),
            ('4BR4BA', '4 Bedroom/ 4 Bath'),
            ('3BR3BA', '3 Bedroom/ 3 Bathroom'),
            ('1BR1BA', '1 Bedroom/ 1 Bathroom'),
            )
     )
)
class Listing(models.Model):
    building = models.ForeignKey('Building')
    room = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add = True)
    start_lease = models.DateField()
    end_lease = models.DateField()
    posters_email = models.EmailField(max_length=254)
    price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    negotiable = models.BooleanField(default=True)
    description = models.TextField()
    num_rooms = models.IntegerField()

    room_type = models.CharField(max_length=30, choices = ROOM_CHOICES)

    class Meta:
        ordering = ['-pub_date']

class Building(models.Model):
    BUILDING_CHOICES = (
        ('Commons', ' South Campus Commons'),
        ('Courtyards', 'The Courtyards'),
        ('Varsity', 'The Varsity'),
        ('View', 'The University View')
    )
    name = models.CharField(max_length = 20, choices = BUILDING_CHOICES)
    website = models.URLField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
                
class ListingForm(ModelForm):
    class Meta:
        model = Listing

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()
    email = forms.EmailField()
    lid = forms.IntegerField()
