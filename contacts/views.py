from django.shortcuts import render, redirect
from .models import Contact 
from django.core.mail import send_mail 
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        print('Enquiry Checking ---')

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            print("New Enquiry Sent ")
            if has_contacted:
                messages.error(request , 'You have Already made an inquiry for this listing')
                print("Error has been sended")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        print("Request been checked")
        contact.save()
        print("Request Saved")

        # Send Mail
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been inquiry for ' + listing + '. Sign into the admin pannel for more info',
        #     'shivamrvgupta@gmail.com',
        #     ['anil03gupta03@gmail.com'],
        #     fail_silently=False,
            
        # )
        # print("Email sended to ---- {}".format(send_mail))
        messages.success(request, 'Your request have been submitted, A realtor will get back to you soon ')
        print("Message has been Sent")

        return redirect('/listings/'+listing_id)
        print("Enquiry Sent & Redirecting to listing_id")

