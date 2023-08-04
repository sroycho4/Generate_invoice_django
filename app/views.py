from django.shortcuts import render
from  . models import producat,seller,buyer
import datetime

# Create your views here.
def index(request):
    pro = producat.objects.all()
    slr = seller.objects.all()
    return render(request,'index.html',{'products':pro,'seller':slr})

def buy(request,pk):
    print(pk)
    pro = producat.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])
        
        by = buyer(name=name,address=address,phone=phone)
        by.save()
        amount = float(pro.price)
        pn = pro.name
        dis = pro.dis
        price = amount
        pro_quantity =quantity
        pro_total = amount*quantity         
        slr = seller.objects.all()
        data = {'pname':pn,'pprice':price,'bname':name,'baddress':address,'bphone':phone,'pdis':dis,'pquantity':pro_quantity, 'ptotal':pro_total}
        return render(request, 'pdf.html', {'data': data, 'seller': slr})

    return render(request, 'buy.html')


def pdf(request):
    slr = seller.objects.all()
    return render(request,'pdf.html',{'seller':slr})

