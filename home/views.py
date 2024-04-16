from django.shortcuts import render
from .models import*
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

# Create your views here.
def user(request):
    return render(request,'login.html')

def create_acc(request):
    if request.method=="POST":
        Username=request.POST["Username"]
        fn=request.POST['fn']
        ln=request.POST['ln']
        e_id=request.POST['e_id']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(Username,e_id,pass1)
        myuser.first_name=fn
        myuser.last_name=ln

        myuser.save()

        messages.success(request,"Your account succesfully created:::")

        return redirect("signin")

    return render(request,"create_acc.html")

def signin(request):
    if request.method=="POST":
        Username=request.POST['Username']
        pass1=request.POST['pass1']

        user=authenticate(Username=Username,password=pass1)

        if user is not None:
            login(request,user)
            fn=user.first_name
            return render(request,"login.html",{"fn":fn})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect("login")

    return render(request,"signin.html")

def index(request):
    context={'amenties':Amenitites.objects.all()}
    return render(request,'index.html',context)

def get_hotel(request):
    try:
        hotel_objs=Hotel.objects.all()
        #ascending order
        if request.GET.get('sort_by'):
            sort_by_value =request.GET.get('sort_by')
            if sort_by_value == 'asc':
                hotel_objs= hotel_objs.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                hotel_objs=hotel_objs.order_by('-hotel_price')

        if request.GET.get('amount'):
            amount =request.GET.get('amount')
            hotel_objs=hotel_objs.filter(hotel_price__lte=amount)

        if request.GET.get('name'):
            name=request.GET.get('name')
            hotel_objs=hotel_objs.filter(hotel_name=name)

        if request.GET.get('amenities'):
            amenities=request.GET.get('amenities')
            amenities=str(amenities).split(',')
            am=[]
            for amenity in amenities:
                am.append(int(amenity))
            
            hotel_objs=hotel_objs.filter(amenitites__in=am).distinct()

        payload=[]
        for hotel_obj in hotel_objs:
            payload.append({
                'hotel_name':hotel_obj.hotel_name,
                'hotel_price':hotel_obj.hotel_price,
                'hotel_description':hotel_obj.hotel_description,
                'banner_image':'/media/'+str(hotel_obj.banner_image),
                'amenitites':hotel_obj.get_amenities(),
            })

        return JsonResponse(payload,safe=False)
    
    except Exception as e:
        print(e)

    return JsonResponse({'message':'Something went Wrong:'})