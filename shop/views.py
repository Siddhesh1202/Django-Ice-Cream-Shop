from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('product_name')
    cats = {item['product_name'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_name=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides ), nSlides])
    params = {'allProds': allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html') 

 
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse(e)
        
    return render(request, 'shop/tracker.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name , email=email , phone=phone , desc=desc)
        contact.save()
    return render(request,'shop/contact.html') 

def search(request):
    return render(request,'shop/search.html') 

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodview.html',{'product':product[0]}) 

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address_1 = request.POST.get('address_1','')
        address_2 = request.POST.get('address_2','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Order(items_json=items_json,name=name , email=email , address_1=address_1, address_2=address_2, phone=phone , city=city, state=state, zip_code=zip_code)
        order.save() 
        update = OrderUpdate(order_id=order.order_id, update_desc="The Order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id': id})
    return render(request,'shop/checkout.html') 