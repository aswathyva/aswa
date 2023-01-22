from django.shortcuts import render
from . models import Place
from . models import Customer

def demo(request):
    obj=Place.objects.all()
    obj2=Customer.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x*y
#     res3=x-y
#     res4=x/y
#     return render(request,"result.html",{'addresult':res1,'mulresult':res2,'subresult':res3,'divresult':res4})