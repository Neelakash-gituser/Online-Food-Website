from django.shortcuts import render
from django.http import HttpResponse
from Food.models import Food,Contact,Buy


# Create your views here.
def index(request):
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def contact(request):
	if request.method=="POST":
		name=request.POST.get('name',())
		email=request.POST.get('email',())
		message=request.POST.get('message',())
		print(name,email,message)
		contact=Contact(name=name,email=email,message=message)
		contact.save()
	return render(request,'contact.html')	
def testimonials(request):
	return render(request,'testimonials.html')	
def privacy(request):
	return render(request,'privacy.html')	
def achieve(request):
	return render(request,'achieve.html')		
def productview(request,id):
	#fetch the food item using the id
	a=Food.objects.all()
	return render(request,'productview.html',{'q':a})
def buy(request):
	if request.method=="POST":
		quantity=request.POST.get('quantity',())
		payment_method=request.POST.get('payment_method',())
		price=request.POST.get('price',())
		name=request.POST.get('name',())
		mobile=request.POST.get('mobile',())
		address=request.POST.get('address',())
		city=request.POST.get('city',())
		print(name,quantity,price)
		buy=Buy(quantity=quantity,payment_method=payment_method,price=price,name=name,mobile=mobile,address=address,city=city)
		buy.save()
	return render(request,'buy.html')		
def search(request):
	return render(request,'search.html')			