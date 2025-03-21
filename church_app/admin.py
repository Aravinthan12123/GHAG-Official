from django.contrib import admin
from . models import PortfolioItem
from .models import Verse_of_the_day
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from .models import Ministry
from .models import Certificate

# Register your models here.

#gallery
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display=('title','category',)
    search_fields=('title','category',)

admin.site.register(PortfolioItem,PortfolioItemAdmin)


#daily verse
class VerseOfTheDayAdmin(admin.ModelAdmin):
    list_display = ('date','englishname', 'tamilname', 'chapter', 'versecount', 'verse', 'kjv')
    search_fields = ('date','englishname', 'chapter', 'versecount')
    list_filter = ('englishname', 'date')
    ordering = ('date',)
    date_hierarchy = 'date'

    def get_queryset(self, request):
        # Get the current date and the date 60 days ahead
        today = make_aware(datetime.today())
        end_date = today + timedelta(days=60)

        # Return only the records from today to 60 days from today
        return super().get_queryset(request).filter(date__range=[today.date(), end_date.date()])

admin.site.register(Verse_of_the_day, VerseOfTheDayAdmin)



from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile_number', 'address', 'message')
    search_fields = ('name', 'mobile_number', 'address')


from django.contrib import admin
from .models import Sermons

@admin.register(Sermons)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description')
    search_fields = ('title', 'author')



#ministry
class MinistryAdmin(admin.ModelAdmin):
    list_display=('title','category',)
    search_fields=('title','category',)

admin.site.register(Ministry,MinistryAdmin)

#our teams
from .models import Team
class TeamAdmin(admin.ModelAdmin):
    list_display=('author','role',)
    search_fields=('author','role',)

admin.site.register(Team,TeamAdmin)

#events

from .models import Event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('title','date','venue')
    search_fields=('title','date','venue')


#membership
from .models import ChurchMember
class ChurchMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name','profile_image', 'email', 'phone', 'gender', 'city', 'occupation')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('gender', 'marital_status', 'city')

admin.site.register(ChurchMember, ChurchMemberAdmin)

#admin status

from .models import Usersstatus

class UserstatusAdmin(admin.ModelAdmin):
    list_display = ('username',)
admin.site.register(Usersstatus,UserstatusAdmin)


#certificate
admin.site.register(Certificate)