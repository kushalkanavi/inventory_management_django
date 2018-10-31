from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect ,HttpResponse
from django.urls import reverse, reverse_lazy
from django import forms
from .forms import InventoryForm
from .models import userRole, invetoryRecord, permisionsAddInventory, permisionsEditInventory

import json
from django.http import JsonResponse
from django.core import serializers

from django.db.models import Q
from django.contrib import messages

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request,'my_app/index.html')


class main(View):
	def get(self, request, *args, **kwargs):
		form = InventoryForm()

		role = userRole.objects.get(UserID_id = request.user.id)

		inventory_detail = serializers.serialize('json', invetoryRecord.objects.all())
		inventory_data = [d['fields'] for d in json.loads(inventory_detail)]
		inventory_ID = [d['pk'] for d in json.loads(inventory_detail)]

		data = zip(inventory_ID,inventory_data)

		context = {
			'form'	:form,
			'data'	:data,
			'role'	:role
			}

		return render(request,'my_app/main.html',context)

class saveInventory(View):
	def post(self, request, *args, **kwargs):
		form = InventoryForm(self.request.POST)
		if form.is_valid():
			fform = form.save()
			invetoryRecord.objects.filter(id=fform.id).update(User = request.user.id)

		return redirect('intro:main')

def inventorySearch(request):
	if request.method == 'POST':
		srch  = request.POST['search']

		if srch:
			match = invetoryRecord.objects.filter(Q(Product_ID__icontains = srch) | Q(Product_Name__icontains = srch) | Q(Vendor__icontains = srch) | Q(Status__icontains = srch))

			if match:
				form = InventoryForm()
				inventory_detail = serializers.serialize('json', invetoryRecord.objects.all())
				inventory_data = [d['fields'] for d in json.loads(inventory_detail)]
				inventory_ID = [d['pk'] for d in json.loads(inventory_detail)]

				data = zip(inventory_ID,inventory_data)
				
				context = {
					'srch':match,
					'form':form,
				}
				return render(request,'my_app/main.html',context)
			else:
				messages.error(request,'No Result Found.')

		else:
			return render(request,'my_app/main.html')

	return render(request,'my_app/main.html')

class editInventory(View):
	def get(self, request, *args, **kwargs):
		iid = kwargs['id']

		inventory_detail = serializers.serialize('json', invetoryRecord.objects.filter(id = iid).all())
		inventory_data = [d['fields'] for d in json.loads(inventory_detail)]
		inventory_ID = [d['pk'] for d in json.loads(inventory_detail)]

		print()
		
		context = {
			'data'	: inventory_data,
			'id'	: inventory_ID
			 }
		role = userRole.objects.get(UserID_id = request.user.id)

		if role.Store_Manager == True:
			return render(request,'my_app/manager_edit.html',context)
		
		elif permisionsEditInventory.objects.filter(Inventory__id = kwargs['id']).exists():
			if permisionsEditInventory.objects.get(Inventory__id = kwargs['id']).Approval_Status == 'Accepted':
				return render(request,'my_app/manager_edit.html',context)
		
		else:
			return render(request,'my_app/assistant_edit.html',context)

class approveInventory(View):
	def get(self, request, *args, **kwargs):
		iid = kwargs['id']
		invetoryRecord.objects.filter(id = iid).update(Status = 'Approved')
		return redirect('intro:main')

class managerPermissions(View):
	def get(self, request, *args, **kwargs):
		add_permissions = permisionsAddInventory.objects.filter(Approval_Status = 'Pending').all()
		edit_permissions = permisionsEditInventory.objects.filter(Approval_Status = 'Pending').all()
		
		context = {
			'add_permissions'	: add_permissions,
			'edit_permissions'	: edit_permissions
			}
		return render(request,'my_app/permissions.html',context)

class assistantPermissions(View):
	def get(self, request, *args, **kwargs):
		form = InventoryForm()
		context = {
			'add_permissions' 	: permisionsAddInventory.objects.filter(User_id=request.user.id).all(),
			'add_permissions' 	: permisionsEditInventory.objects.filter(User_id=request.user.id).all(),
			'form'	: form
		}
		return render(request,'my_app/permissions_requested.html',context)

class addInventoryPermission(View):
	def post(self, request, *args, **kwargs):
		permisionsAddInventory.objects.create(User_id = request.user.id)
		return redirect('intro:main')

class acceptPermissions(View):
	def get(self, request, *args, **kwargs):
		permisionsAddInventory.objects.filter(id=kwargs['id']).update(Approval_Status = 'Accepted')
		return redirect('intro:main')

class rejectPermissions(View):
	def get(self, request, *args, **kwargs):
		permisionsAddInventory.objects.filter(id=kwargs['id']).update(Approval_Status = 'Rejected')
		return redirect('intro:main')

class editInventoryPermission(View):
	def get(self, request, *args, **kwargs):
		permisionsEditInventory.objects.create(
				User_id = request.user.id,
				Inventory_id = kwargs['id']
				)
		return redirect('intro:main')

class acceptEditPermissions(View):
	def get(self, request, *args, **kwargs):
		permisionsEditInventory.objects.filter(id=kwargs['id']).update(Approval_Status = 'Accepted')
		return redirect('intro:main')

class rejectEditPermissions(View):
	def get(self, request, *args, **kwargs):
		permisionsEditInventory.objects.filter(id=kwargs['id']).update(Approval_Status = 'Rejected')
		return redirect('intro:main')

