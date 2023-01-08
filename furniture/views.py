from django.shortcuts import render,redirect
from django.http import HttpResponse
from furniture.models import Contact
# Create your views here.
def home(request):
    return render(request,'index.html')


def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,description=desc,contactno=contact)
        contact.save()
        return redirect("home")