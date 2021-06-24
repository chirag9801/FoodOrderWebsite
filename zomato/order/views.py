from django.shortcuts import render,redirect
from .forms import kim,jim
from .models import order
from .models import userregister

# Create your views here.
def home(request):
    order_list=order.objects.all()
    context={
        "order_list":order_list
    }
    print(context)
    return render(request,'order/home.html',context)

def add(request):
    if request.method=="POST":
        form=kim(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:

        form =  kim()
    context={
        'form':form
    }
    return render(request,'order/add.html')

def index(request):
    return render(request,'order/index.html')


def useraccount(request):
    if request.method=="POST":
        form=jim(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:

        form =  jim()
    context={
        'form':form
    }
    return render(request,'order/register.html')
