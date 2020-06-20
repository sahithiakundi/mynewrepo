from django.shortcuts import render,redirect
from app.forms import myStudent
from django.http import HttpResponse
from app.models import Student
# Create your views here.
def add_data(request):
	if request.method=="POST":
		data=myStudent(request.POST)
		data.save()
		#return HttpResponse("Data added Successfully")
		return redirect('/display')
	mydata=myStudent()
	return render(request,'app/add_data.html',{'form':mydata})
def display(request):
	data=Student.objects.all()
	return render(request,'app/display.html',{'data':data})
def trash(request,id):
	data=Student.objects.get(id=id)
	data.delete()
	return redirect('/display')
def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data=myStudent(request.POST)
		data.save()
		return redirect('/display')
	form=myStudent(instance=data)
	return render(request,'app/update.html',{'form':form,'data':data})