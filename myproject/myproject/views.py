from django.template import RequestContext, Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from listings.models import Listing, Building, ListingForm, ContactForm
from django.shortcuts import get_list_or_404, render
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.core import serializers

def home(request):
    template = loader.get_template('home.html')
    listings = Listing.objects
    dict = {"listings": listings}
    c = RequestContext(request, dict)
    return HttpResponse(template.render(c))

def presentation(request):
    template = loader.get_template('presentation.html')
    dict = {}
    c = RequestContext(request, dict)
    return HttpResponse(template.render(c))

def about(request):
    template = loader.get_template('about.html')
    dict = {}
    c = RequestContext(request, dict)
    return HttpResponse(template.render(c))

def listing(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']


            recipients = []
            recipients.append(listing.posters_email)
            recipients.append(sender)

            from django.core.mail import send_mail
            send_mail('You have a Prospective Renter from Campus Rentals', message, sender,
                      recipients, fail_silently=False)
            template= loader.get_template('contactAfter.html')
            dict = {"listingID": listing_id}
            c = RequestContext(request, dict)
            return HttpResponse(template.render(c))
    else:
        form = ContactForm()
    return render(request, 'listing_page.html', {
        'form': form,
        'listing': listing,
    })


def listing_by_building(request, location):
    buildingName = Building.objects.get(name = location)
    itemsList = get_list_or_404(Listing, building__exact = buildingName)
    

    return list_detail.object_list(
        request,
        queryset = itemsList,
        #template_name = ''
    )

def searchresults(request, commons, courtyards, varsity, view, startyear, startmonth, startday, endyear, endmonth, endday, pricerange, numrooms):
    listings = []
    for l in Listing.objects.all():
        building = l.building
        start_lease = l.start_lease
        end_lease = l.end_lease
        price = l.price
        if (building.name == "Commons" and commons == 'true') or (building.name == "Courtyards" and courtyards == 'true') or (building.name == "View" and view == 'true') or (building.name == "Varsity" and varsity == 'true'):
            if ((startyear == "any" or (str(start_lease.year) == startyear and (str(start_lease.month) == startmonth))) and (endyear=="any" or (str(end_lease.year) == endyear) and (str(end_lease.month) == endmonth))):
                if pricerange == 'all':
                    listings.append(l)
                elif price <= 500 and pricerange == 'less500':
                    listings.append(l)
                elif price <= 1000 and pricerange == 'less1000':
                    listings.append(l)
                elif price > 1000 and pricerange == 'great1000':
                    listings.append(l)
    resp = serializers.serialize('json', listings)
    return HttpResponse(simplejson.dumps(resp), mimetype="application/json")

def listing_by_price(request, max_price):
    itemsList = get_list_or_404(Listing, price__lte = max_price)

    return list_detail.object_list(
        request,
        queryset = itemsList,
        #template_name = ''
    )

def submitListing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            building = form.cleaned_data['building']
            room = form.cleaned_data['room']
            start_lease = form.cleaned_data['start_lease']
            end_lease = form.cleaned_data['end_lease']
            posters_email = form.cleaned_data['posters_email']
            price = form.cleaned_data['price']
            negotiable = form.cleaned_data['negotiable']
            description = form.cleaned_data['description']
            l = Listing(building = building,
                        room = room,
                        start_lease = start_lease,
                        end_lease = end_lease,
                        posters_email = posters_email,
                        price = price,
                        negotiable = negotiable,
                        description = description
                        )
            l.save()
            template = loader.get_template('submitAfter.html')
            dict = {"listingID": l.id, "listing":l}
            c = RequestContext(request, dict)
            return HttpResponse(template.render(c))
    else:
        form = ListingForm()

    return render(request, 'submit.html', {
            'form': form,
            })
