from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
# Create your views here.
import math

def data(request):
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.filter().aggregate(Sum('Payment'))['Payment__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	}
	return render(request,'main.html',context)
@login_required(login_url='/login/')
def investmentpage(request):
	if request.method=='GET':
		form=investform()
	else:
		
		form=investform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Entry successfully inserted ')
		

	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	returninvestment=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'invtotal':investment-returninvestment,
	'investdata':Investment.objects.all(),
	'retinvestdata':Returninvestment.objects.all(),
	'form':form,
	
	}
	return render(request,'investment.html',context)
@login_required(login_url='/login/')
def retpay(request,id):
	if request.method=='GET':
		form=returninvestform()
	else:
		form=returninvestform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Entry successfully inserted ')
			return redirect('investment')
		else:
			messages.info(request, 'Failed ')

	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	returninvestment=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	idreturn=Returninvestment.objects.filter(id1=id).aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	idinvest=Investment.objects.filter(id=id).aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	context={
	'invlogs':Investment.objects.get(id=id),
	'idavail':idinvest-idreturn,
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'invtotal':returninvestment,
	'investment':investment-returninvestment,
	'retinvestdata':Returninvestment.objects.all(),
	'form':form,
	
	}
	return render(request,'retpay.html',context)
@login_required(login_url='/login/')
def bankint(request):
	if request.method=='GET':
		form=bankintform()
	else:
		form=bankintform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Entry successfully inserted ')
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	totamount=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'totamount':totamount,
	'bankintdata':Bankinterest.objects.all(),
	'form':form,
	
	}
	
	return render(request,'bankint.html',context)
@login_required(login_url='/login/')
def stats(request):
	if request.method=='GET':
		form=addcomform()
	else:
		form=addcomform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Company Name added successfully ')
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'interest':Logs_Table.objects.all().aggregate(Sum('Interest')),
	'companydata':Company.objects.all(),
	'form':form,
	
	}
	return render(request,'stats.html',context)
@login_required(login_url='/login/')
def logs(request):
	
	if request.method=='GET':
		form=logsform()
	else:
		form=logsform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Entry successfully Inserted ')
	
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'companies':Company.objects.all(),
	'alldata':Logs_Table.objects.all(),
	'form':form,
	}		
	return render(request,'logs.html',context)
@login_required(login_url='/login/')
def update(request,id):
	if request.method == 'GET':
		form = logsform1()

	else:
		returndate=request.POST['Return_Pay_Date']
		total_days=request.POST['Total_Days']
		interestrate =request.POST['Rate_Of_Interest']
		interest = request.POST['Interest']
		total = request.POST['Total']
		logs=Logs_Table.objects.get(id=id)
		logs.Return_Pay_Date=returndate
		logs.Total_Days=total_days
		logs.Rate_Of_Interest=interestrate
		logs.Interest=interest
		logs.Total=total
		logs.save()
		messages.success(request, 'Entry successfully Updated ')
		return redirect('alldata')
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0 
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={

	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'logs':Logs_Table.objects.get(id=id),
	'form':form,
	}
	return render(request,'update.html',context)
@login_required(login_url='/login/')
def alldata(request):
	
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	context={
	
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'alldata':Logs_Table.objects.all(),
	}
	return render(request,'alldata.html',context)
@login_required(login_url='/login/')
def statistics(request):
	investment=Investment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	payment=Logs_Table.objects.all().aggregate(Sum('Payment'))['Payment__sum'] or 0
	interest=Logs_Table.objects.all().aggregate(Sum('Interest'))['Interest__sum'] or 0
	bankinterest=Bankinterest.objects.all().aggregate(Sum('Amount'))['Amount__sum'] or 0
	paycom=Logs_Table.objects.all().aggregate(Sum('Total'))['Total__sum'] or 0
	retpays=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	returninvestment=Returninvestment.objects.all().aggregate(Sum('Investment_amount'))['Investment_amount__sum'] or 0
	context={
	'interest':math.floor(interest),
	'payment':payment,
	'investment':investment,
	'bankinterest':bankinterest,
	'retinv':returninvestment,
	'availbalance':math.floor(investment+paycom-payment-retpays-bankinterest),
	'profit':math.floor(interest-bankinterest),
	}
	return render(request,'statistics.html',context)