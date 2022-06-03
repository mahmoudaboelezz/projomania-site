# Create your views here.
from django.forms.models import modelformset_factory
from .form import ContactUs,Services
from .form import Tickets as ticket1 ,Tickets_reply,datebaseTickets_Form
from .models import Booking,Ticket, Ticket_reply, User,datebaseTickets,image_upload_handler,Ai_Reply
from blog.models import Auto_Reply
from django.views.generic import ListView
from django.shortcuts import render ,get_object_or_404
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pyocr import ocrtest,ocrtest1
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView






def contactus(request):
    if request.method=='POST':
        formset = ContactUs(request.POST) 
        if formset.is_valid():
            formset.save()
            
    if request.method == 'POST':
        formset = Services(request.POST) 
        if formset.is_valid():
            formset.save()
            
    return render(request, 'contact/contact.html', {'contact':ContactUs , 'Services':Services})

@login_required
def Tickets(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login/')
    form = ticket1()
    db = datebaseTickets.objects.filter(user=request.user)
    context = {'form':form,"db":db}
    # if request.method == "POST":Ticket.objects.filter(user=request.user)
    #         # obj = form.save(commit=False)
    #         # obj.user = request.user
    #         # obj.save()
    #         if form.is_valid():
    #             form.save()
    #         else:
                # print("NO")
            #return redirect(obj.get_absolute_url())
            

    if request.method == "POST":
        title = request.POST.get("issueTitle")
        content = request.POST.get("issueContent")
        #snapShot = request.POST.get("snapShot")
        dbname = request.POST.get("db")
        dbrelation = request.POST.get("dbRelated")


        if dbname:
            db_object = datebaseTickets.objects.create(db=dbname,user = request.user)
            if db_object:
                ticket_object = Ticket.objects.create(dbRelated=db_object,issueTitle=title, issueContent=content,snapShot=request.FILES.get("snapShot"),user = request.user)
            print(f"media/{image_upload_handler(request,request.FILES.get('snapShot'))}")
        elif dbrelation == "0":

            if request.FILES.get("snapShot"):
                ticket_object = Ticket.objects.create(issueTitle=title, issueContent=content,user = request.user,snapShot=request.FILES.get("snapShot"))
            else:
                ticket_object = Ticket.objects.create(issueTitle=title, issueContent=content,user = request.user)
        else:
            print(f"media/{image_upload_handler(request,request.FILES.get('snapShot'))}")
            db_object = datebaseTickets.objects.get(id=dbrelation,user = request.user)
            # print(f"db name {dbname}, db relation {dbrelation},object {db_object}")
            ticket_object = Ticket.objects.create(dbRelated=db_object,issueTitle=title, issueContent=content,snapShot=request.FILES.get("snapShot"),user = request.user)
        ticket_object.save()
        context['object'] = ticket_object
        context['created'] = True
        #print(f"{image_upload_handler(request,request.FILES.get('snapShot'))}")
        est=Ticket.objects.filter(id=ticket_object.id)[0].snapShot
        extracted = ocrtest(est)
        print(extracted)
        # listofsolutions = []
        # listofslinks = []
        for x in extracted:
            try:
                toprint = Auto_Reply.objects.get(error = x)
                # print(f"to print :{toprint,ticket_object}")
                ai = Ai_Reply.objects.create(aiReply=toprint,ticket=ticket_object)
                # print(f"ai :{ai}")
            except:
                pass
        # for name, age in zip(listofslinks, listofsolutions):
        #     Ticket.objects.filter(id=ticket_object.id).update(solution=age,link=name)
        # print(listofslinks)
        

        return redirect(ticket_object.get_absolute_url())
   
    return render(request, "contact/tickets/ticket.html", {"context":context})

#view
def Ticketdetail(request,id):
    if request.user.id == 1:
        ticketmain = get_object_or_404(Ticket, id = id)
    
     
        #print(ticketmain.snapShot)
        
        extracted1 = ocrtest1(ticketmain.snapShot,request.user)
        print(extracted1)
    else:
        
        ticketmain = get_object_or_404(Ticket, id = id,user=request.user)
        #extracted = ocrtest(ticketmain.snapShot)
        #extracted1 = ocrtest1(ticketmain.snapShot,request.user)

    
    reply = Tickets_reply()
    if request.method == "POST":
        author = request.user
        replys = request.POST.get("reply")
        ticket_object = Ticket_reply.objects.create(ticket=ticketmain, author=author,reply = replys)
    context = {
        'ticket' : ticketmain,
        'reply' : reply,
        'extracted1':extracted1
    }
    return render(request, 'contact/tickets/ticketdetails.html', context)

#list
@login_required
def Ticket_list(request):
    qs = Ticket.objects.filter(user=request.user)
    ticketupdateFormset = modelformset_factory(Ticket, form=ticket1,extra=0,fields=['status'])
    formset = ticketupdateFormset(request.POST or None, queryset=qs)
    test = formset.get_queryset()
    context = {
        "formset": formset,
        "qs":qs,
        "test":test
               }
    return render(request,"contact/tickets/mytickets.html",context)

#update
def Ticket_update(request,id):
    
    # ticket = get_object_or_404(Ticket, id=id, user=request.user)
    # form = ticket1(request.POST or None, instance=ticket)
    # context = {
    #      "ticket" : ticket,
    #      "form" : form
    # }
    # if form.is_valid():
    #     form.save()
    #     context['message'] = 'Data saved.'
    ticket = get_object_or_404(Ticket, id = id,user=request.user)
    form = ticket1(instance=ticket)
    context= {
        "ticket" : ticket,
        "form" : form
    }
    if request.method == "POST":
        user = request.user
        status = request.POST.get("status")
        comment = request.POST.get("comment")
        issueTitle = ticket.issueTitle
        issueContent = ticket.issueContent
        ticket_object = Ticket.objects.filter(id=ticket.id).update(user=user,status=status,issueTitle = issueTitle,issueContent=issueContent,comment=comment)
        context['message'] = "Data Saved."
        return redirect(ticket.get_absolute_url())

    if form.is_valid():
        form.save()
        return redirect(ticket.get_absolute_url())
    return render(request, 'contact/tickets/update.html', context)

def mylist(request):
    qs = Ticket.objects.filter(user=request.user)
    ticketupdateFormset = modelformset_factory(Ticket, form=ticket1,extra=0,fields=['status'])
    formset = ticketupdateFormset(request.POST or None, queryset=qs)
    test = formset.get_queryset()
    context = {
        "formset": formset,
        "qs":qs,
        "test":test
               }
    if request.htmx:
         return render(request,"contact/tickets/mylistticket.html",context)
    return render(request,"contact/tickets/mytickets.html",context)



