from django.shortcuts import render,redirect
from Newapp.models import CategoryDB
from Newapp.models import ProductDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from WebApp.models import ContactDB
# Create your views here.
def index(request):
    return render(request,"index.html")
def addcategory(request):
    return render(request,"AddCategory.html")

def savecategory(request):
    if request.method=="POST":
        Name=request.POST.get('c_name')
        Image = request.FILES['c_img']
        Desc=request.POST.get('c_desc')
        obj=CategoryDB(Category_Name=Name,Category_Image=Image,Description=Desc)
        obj.save()
        return redirect(addcategory)

def displaycategory(request):
    cat=CategoryDB.objects.all()
    return render(request,"DisplayCategory.html",{'cat': cat})

def editcategory(request,catid):
    cat=CategoryDB.objects.get(id=catid)
    return render(request,"EditCategory.html",{'cat':cat})

def updatecategory(request,catid):
    if request.method=="POST":
        Name=request.POST.get('c_name')
        Desc=request.POST.get('c_desc')
        try:
            img = request.FILES['c_img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=catid).Category_Image
        CategoryDB.objects.filter(id=catid).update(Category_Name=Name, Description=Desc, Category_Image=file)
        return redirect(displaycategory)

def deletecategory(request,catid):
    x = CategoryDB.objects.filter(id=catid)
    x.delete()
    return redirect(displaycategory)

def addproduct(request):
    cat=CategoryDB.objects.all()
    return render(request,"AddProduct.html",{'cat':cat})

def saveproduct(request):
    if request.method == "POST":
        Prod_cat = request.POST.get('p_cat')
        Prod_name= request.POST.get('p_name')
        Quant=request.POST.get('p_quant')
        Pri = request.POST.get('p_price')
        Desc = request.POST.get('p_desc')
        Coo = request.POST.get('p_coo')
        Manu = request.POST.get('p_manu')
        Img1 = request.FILES['p_imgfirst']
        Img2 = request.FILES['p_imgsecond']
        Img3 = request.FILES['p_imgthird']
        obj=ProductDB(Product_Category=Prod_cat,Product_Name=Prod_name,Quantity=Quant,Price=Pri,Description=Desc,Country_of_origin=Coo,Manufactured_by=Manu,Image1=Img1,Image2=Img2,Image3=Img3)
        obj.save()
        return redirect(addproduct)

def displayproduct(request):
    pro=ProductDB.objects.all()
    return render(request,"DisplayProduct.html",{'pro':pro})

def editproduct(request,proid):
    cat=CategoryDB.objects.all()
    pro=ProductDB.objects.get(id=proid)
    return render(request,"EditProduct.html",{'pro':pro,'cat':cat})

def updateproduct(request,proid):
    if request.method == "POST":
        Prod_cat = request.POST.get('p_cat')
        Prod_name= request.POST.get('p_name')
        Quant=request.POST.get('p_quant')
        Pri = request.POST.get('p_price')
        Desc = request.POST.get('p_desc')
        Coo = request.POST.get('p_coo')
        Manu = request.POST.get('p_manu')
        try:
            img1 = request.FILES['p_imgfirst']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file1 = ProductDB.objects.get(id=proid).Image1
        try:
            img2 = request.FILES['p_imgsecond']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = ProductDB.objects.get(id=proid).Image2

        try:
            img3 = request.FILES['p_imgthird']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3 = ProductDB.objects.get(id=proid).Image3
        ProductDB.objects.filter(id=proid).update(Product_Category=Prod_cat,Product_Name=Prod_name,Quantity=Quant,Price=Pri,Description=Desc,Country_of_origin=Coo,Manufactured_by=Manu,Image1=file1,Image2=file2,Image3=file3)
        return redirect(displayproduct)

def deleteproduct(request,proid):
    x = ProductDB.objects.filter(id=proid)
    x.delete()
    return redirect(displayproduct)
def Admin_login(request):
    return render(request,"AdminLogin.html")

def loginpage(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pswd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pswd
                return redirect(index)
            else:
                return redirect(Admin_login)
        else:
            return redirect(Admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Admin_login)

def contact_display(request):
    data=ContactDB.objects.all()
    return render(request,"contact_data.html",{'data':data})

def delete_contact(request,con):
    x=ContactDB.objects.filter(id=con)
    x.delete()
    return redirect(contact_display)


