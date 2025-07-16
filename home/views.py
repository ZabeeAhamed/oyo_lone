from django.shortcuts import render,redirect
from accounts.models import Hotel,Booking,HotelUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.

def index(request):
    hotels = Hotel.objects.all()
    if request.GET.get('search'):
        hotels = hotels.filter(hotel_name__icontains = request.GET.get('search'))

    if request.GET.get('sort_by'):
        sort_by = request.GET.get('sort_by')
        if sort_by == "sort_low":
            hotels = hotels.order_by('hotel_offer_price')
        elif sort_by == "sort_high":
            hotels = hotels.order_by('-hotel_offer_price')
    return render(request, 'index.html', context = {'hotels' : hotels[:50]})

@login_required
def hotel_details(request, slug):
    hotel = get_object_or_404(Hotel, hotel_slug=slug)
    hotel_user = HotelUser.objects.get(pk=request.user.pk)


    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        if not start_date or not end_date:
            messages.error(request, "Please select both start and end dates.")
            return redirect(request.path)

        # Check for overlapping bookings
        existing = Booking.objects.filter(
            hotel=hotel,
            booking_start_date__lt=end_date,
            booking_end_date__gt=start_date
        )
        if existing.exists():
            messages.error(request, "This hotel is already booked for the selected dates.")
        else:
            Booking.objects.create(
                user=hotel_user,
                hotel=hotel,
                booking_start_date=start_date,
                booking_end_date=end_date
            )
            messages.success(request, "Hotel booked successfully!")
            return redirect(request.path)

    return render(request, "hotel_detail.html", {"hotel": hotel})

