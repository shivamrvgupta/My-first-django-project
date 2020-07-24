from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from .models import Listing
from .choices import bedroom_choices, state_choices, price_choices
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings 
    }
        
    

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

# Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        print('Keywords ---- {}'.format(keywords))
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
        else:
            print("keyword Not Found")    

# City
    if 'city' in request.GET:
        city = request.GET['city']
        print("City --- {}".format(city))
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
        else:
            print("City Not Found")    

# State
    if 'state' in request.GET:
        state = request.GET['state']
        print("State is {}".format(state))
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
        else:
            print("State Not Found")    

# Bedroom
    if 'bedrooms' in request.GET:
        Bedroom = request.GET['bedrooms']
        print('Bedroom ---- {}'.format(Bedroom))
        if Bedroom:
            queryset_list = queryset_list.filter(bedroom__lte=Bedroom)
        else:
            print("Bedroom Not Found")    

# Price
    if 'price' in request.GET:
        Price = request.GET['price']
        print("The price is {}".format(Price))
        if Price:
            queryset_list = queryset_list.filter(price__lte=Price)
        else:
            print("Price Not Found")    



    context ={
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "price_choices": price_choices,
        "listings": queryset_list,
        "values": request.GET 
    }

    return render(request, 'listings/search.html', context)    

