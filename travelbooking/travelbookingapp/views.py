from django.shortcuts import render,redirect
from .models import bookingdata
import faker
fake = faker.Faker()
def homeview(request):
    data = bookingdata.objects.all().order_by('-id')
    return render(request, 'home.html',{'data':data})
def ticketform(request):
    if request.method == 'GET':
        return render(request, 'ticketform.html')
    else:
        bookingdata(
        name = request.POST['name'],
        from_to = request.POST['from_to'],
        froms = request.POST['froms'],
        date = request.POST['date'],
        number = request.POST['number'],
        sit_nmuber = fake.random_element(elements = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60))
        ).save()
        return redirect(homeview)
def candiateview(request,id):
    data = bookingdata.objects.get(id=id)
    return render(request, 'canddata.html',{'data':data})
def deleteview(request,id):
    data = bookingdata.objects.get(id=id)
    data.delete()
    return redirect(homeview)
def bookingview(request):
        data = bookingdata.objects.all()
        return render(request,'bookinglist.html',{'abc':data})
