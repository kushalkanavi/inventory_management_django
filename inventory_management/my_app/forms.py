from django import forms 
from .models import userRole, invetoryRecord, STATUS_CHOICES

class InventoryForm(forms.ModelForm):
	class Meta:
		model=invetoryRecord
		
		fields = [
		'Product_ID',
		'Product_Name',
		'Vendor',
		'MRP',
		'Batch_Num',
		'Batch_Date',
		'Quantity',
		'Status',
		]

		labels = {
		'Product_ID'	: '',
		'Product_Name'	: '',
		'Vendor'		: '',
		'MRP'			: '',
		'Batch_Num'		: '',
		'Batch_Date'	: '',
		'Quantity'		: '',
		'Status'		: '',
		}

		widgets = {
		'Product_ID'	:forms.TextInput(attrs={'name':'productid','class':'form-control','placeholder':'Product_ID',}),
		'Product_Name'	:forms.TextInput(attrs={'name':'productname','class':'form-control','placeholder':'Product_Name',}),
		'Vendor'		:forms.TextInput(attrs={'name':'vendor','class':'form-control','placeholder':'Vendor'}),
		'MRP'			:forms.TextInput(attrs={'name':'mrp','class':'form-control','placeholder':'MRP'}),
		'Batch_Num'		:forms.TextInput(attrs={'name':'batchnum','class':'form-control','placeholder':'Batch_Num'}),
		'Batch_Date'	:forms.DateInput(attrs={'type':'date','name':'batchdate','class':'form-control','placeholder':'Batch_Date'}),
		'Quantity'		:forms.TextInput(attrs={'name':'quantity','class':'form-control','placeholder':'Quantity'}),
		'Status'		:forms.Select(attrs={'name':'status','class':'form-control','placeholder':'Status'}),
		}