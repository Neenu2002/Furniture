from django.shortcuts import render,redirect
from Newapp.models import ProductDB
from WebApp.models import ContactDB
from Newapp.models import CategoryDB
from WebApp.models import SignupDB
from WebApp.models import CartDB
from WebApp.models import orderDb
from django.contrib import messages
import razorpay
# Create your views here.
def homepage(request):
    Categories=CategoryDB.objects.all()
    return render(request,"homepage.html",{'Categories':Categories})

def productspage(request):
    products=ProductDB.objects.all()
    return render(request,"products.html",{'products':products})

def contactspage(request):
    return render(request,"contacts.html")

def aboutus(request):
    return render(request,"aboutus.html")

def savecontact(request):
    if request.method == "POST":
        Fname=request.POST.get('f_name')
        Lname=request.POST.get('l_name')
        Email_id=request.POST.get('e_value')
        Mess=request.POST.get('msg')
        obj=ContactDB(First_Name=Fname, Last_Name=Lname, Email=Email_id,Message=Mess)
        obj.save()
        return redirect(contactspage)

def productsfilter(request,cat_name):
    data=ProductDB.objects.filter(Product_Category=cat_name)
    return render(request,"products_filter.html",{'data':data})

def Singleproduct(request,proid):
    pro=ProductDB.objects.get(id=proid)
    return render(request,"Single_product.html",{'pro':pro})

def loginspage(request):
    return render(request,"Signup.html")

def Signinpage(request):
    return render(request,"Signin.html")

def save_signup(request):
    if request.method=="POST":
        name = request.POST.get('name')
        mail=request.POST.get('email')
        mobile = request.POST.get('mobile')
        pswd = request.POST.get('pass')
        rpswd = request.POST.get('re_pass')
        obj=SignupDB(Name=name,Mail=mail,Mobile=mobile,Password=pswd,Confirm=rpswd)
        obj.save()
        return redirect(Signinpage)

def User_login(request):
    if request.method=="POST":
        un=request.POST.get('your_name')
        pswd=request.POST.get('your_pass')
        if SignupDB.objects.filter(Name=un,Password=pswd).exists():
            request.session['Name']=un
            request.session['Password']=pswd
            messages.success(request,"Welcome")
            return redirect(homepage)

        else:
            messages.warning(request, "Invalid user name")
            return redirect(Signinpage)
    else:
        messages.error(request, "Invalid Password")
        return redirect(Signinpage)

def User_logout(request):
        del request.session['Name']
        del request.session['Password']
        messages.success(request,"Logged out successfully")
        return redirect(homepage)

def save_to_cart(request):
    if request.method == "POST":
        usnm=request.POST.get('name')
        price=request.POST.get('pc')
        pro=request.POST.get('pn')
        qty=request.POST.get('qty')
        total=request.POST.get('tp')
        obj=CartDB(Username=usnm,Price=price,Product_Name=pro,Quantity=qty,Total_Price=total)
        obj.save()
        return redirect(homepage)

def cart(request):
    data = CartDB.objects.filter(Username=request.session['Name'])
    subtotal=0
    shipping_amount=0
    total_amount=0

    for i in data:
        subtotal = subtotal + i.Total_Price

        if subtotal>20000:
            shipping_amount=500
        else:
            shipping_amount=1000

        total_amount = shipping_amount+subtotal

    return render(request,"cart.html",{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})

def checkout(request):
    data = CartDB.objects.filter(Username=request.session['Name'])
    subtotal = 0
    shipping_amount = 0
    total_amount = 0

    for i in data:
        subtotal = subtotal + i.Total_Price

        if subtotal > 20000:
            shipping_amount = 500
        else:
            shipping_amount = 1000

        total_amount = shipping_amount + subtotal
    return render(request,"checkout.html",{'data':data,'subtotal':subtotal,'total_amount':total_amount})

def save_checkout(req):
    if req.method == "POST":
        na = req.POST.get('uname')
        pri = req.POST.get('c_total_price')
        plc = req.POST.get('place')
        add= req.POST.get('c_address')
        ms = req.POST.get('c_order_notes')
        mb=req.POST.get('c_phone')
        em=req.POST.get('c_email_address')

        obj = orderDb(Username=na, Total_price=pri, Message=ms, Mobile=mb, Email=em,Address=add,Place=plc)
        obj.save()
        return redirect(payment_page)

def payment_page(request):
    customer=orderDb.objects.order_by('-id').first()
    payy=customer.Total_price
    amount=int(payy*100)
    payy_str=str(amount)
    # for i in payy_str:
    #     print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_cdbNnD2ZSBzrFm', '2jP3TlSRCBcKKyiwZb3Zun3M'))
        payment=client.order.create({'amount':amount, 'currency':order_currency})
    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})

def remove_cart(request,ctid):
    cat=CartDB.objects.filter(id=ctid)
    cat.delete()
    return redirect(cart)






