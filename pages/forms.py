from django import forms
from . models import *
class logsform(forms.ModelForm):
	class Meta:
		model=Logs_Table
		fields=[
		'Farmer',
		'Company_Name',
		'Date_of_Pay',
		
		'Payment',
		# 'Return_Pay_Date',
		# 'Total_Days',
		# 'Rate_Of_Interest',
		# 'Interest',
		]
class returninvestform(forms.ModelForm):
	class Meta:
		model=Returninvestment
		fields=[
		'id1',
		'To_Return_Investment',
		'Return_Investment_Date',
		'Investment_amount',
		
		]
class investform(forms.ModelForm):
	class Meta:
		model=Investment
		fields=[
		'From_Investment',
		'Investment_Date',
		'Investment_amount',
		
		]
		
class bankintform(forms.ModelForm):
	class Meta:
		model=Bankinterest
		fields=[
		'Pay_Name',
		'Paid_Date',
		'Amount',
		
		]
class addcomform(forms.ModelForm):
	class Meta:
		model=Company
		fields=[
		'Com_Name',
		
		]
class logsform1(forms.ModelForm):
	class Meta:
		model=Logs_Table
		fields=[
		'Farmer',
		'Company_Name',
		'Date_of_Pay',
		
		'Payment',
		'Return_Pay_Date',
		'Total_Days',
		'Rate_Of_Interest',
		'Interest',
		'Total',
		]