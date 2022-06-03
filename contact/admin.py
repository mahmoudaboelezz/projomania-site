from django.contrib import admin
from .models import Contact1,Booking,Ticket,Ticket_reply,datebaseTickets,Ai_Reply


class ReplyAdmin(admin.StackedInline):
    model = Ticket_reply
    extra = 0
    readonly_fields = ['ticket','timestamp']
    #raw_id_fields = ['author']
    
class auto_replyAdmin(admin.StackedInline):
    model = Ai_Reply
    extra = 0
    # readonly_fields = ['ticket','aiReply']
    
class TicketAdmin(admin.StackedInline):
    model = Ticket
    extra = 0
    
    list_display = ['issueTitle','status','timestamp','updates']
    list_editable = ['status']
    readonly_fields = ['issueTitle','issueContent','user','snapShot','timestamp','updates']
    
class TicketAdmin1(admin.ModelAdmin):
    model = Ticket
    extra = 0
    inlines = [ReplyAdmin,auto_replyAdmin]
    list_display = ['issueTitle','status','dbRelated','timestamp','updates']
    list_editable = ['status']
    #readonly_fields = ['issueTitle','issueContent','user','snapShot','timestamp','updates']
    
class dbAdmin(admin.ModelAdmin):
    inlines = [TicketAdmin]
    extra = 0

# Register your models here.
admin.site.register(Contact1)
admin.site.register(Booking)
admin.site.register(Ticket,TicketAdmin1)
admin.site.register(datebaseTickets,dbAdmin)

admin.site.site_header = 'ProjoMania Admin Panel'
admin.site.site_title = 'ProjoMania C-Panel'
admin.site.index_title = 'ProjoMania C-Panel'