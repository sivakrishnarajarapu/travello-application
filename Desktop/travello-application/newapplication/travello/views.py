from django.shortcuts import render

# Create your views here.
from travello.models import Destination


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Vijayawada'
    # dest1.desc = 'Colorfull city'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 800
    # dest1.offer = True
    #
    # dest2 = Destination()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'Biryani is famous'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 650
    # dest2.offer = False
    #
    # dest3 = Destination()
    # dest3.name = 'Guntur'
    # dest3.desc = 'Beautiful city'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 700
    # dest3.offer = True
    #
    # dest4 = Destination()
    # dest4.name = 'Kakinada'
    # dest4.desc = 'mona born city'
    # dest4.img = 'destination_4.jpg'
    # dest4.price = 500
    # dest4.offer = True
    #
    # dest5 = Destination()
    # dest5.name = 'Huzurnagar'
    # dest5.desc = 'Biscuit placing city'
    # dest5.img = 'destination_5.jpg'
    # dest5.price = 700
    # dest5.offer = False
    #
    # dest6 = Destination()
    # dest6.name = 'Sattenapalli'
    # dest6.desc = 'Phaphu boughtup city'
    # dest6.img = 'destination_6.jpg'
    # dest6.price = 700
    # dest6.offer = False
    #
    # dests = [dest1,dest2,dest3,dest4,dest5,dest6]

    dests = Destination.objects.all()

    return render(request,'index.html',{'dests':dests})