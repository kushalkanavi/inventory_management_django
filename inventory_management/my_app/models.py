from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class userRole(models.Model):

    Store_Assistant	= models.BooleanField(default=False)
    Store_Manager  	= models.BooleanField(default=False)
    UserID		 	= models.ForeignKey(User,on_delete=models.CASCADE,to_field='id',null = True)

    def __str__(self):
        return str(self.Store_Manager)

STATUS_CHOICES = (
	('Pending', 'Pending'),
    ('Approved','Approved'),
)

APPROVAL_STATUS = (
	('Pending', 'Pending'),
    ('Accepted','Accepted'),
    ('Rejected','Rejected'),
)


class invetoryRecord(models.Model):
	Product_ID 		=	models.CharField(max_length = 120, null = True)
	Product_Name	=	models.CharField(max_length = 120, null = True)
	Vendor			=	models.CharField(max_length = 120, null = True)
	MRP     		=	models.IntegerField(null = True)
	Batch_Num  		=	models.IntegerField(null = True)
	Batch_Date  	=	models.DateField(max_length = 120, null = True)
	Quantity 		=	models.IntegerField(null = True)
	Status			=	models.CharField(max_length = 20, choices=STATUS_CHOICES, default='Pending')
	User			= 	models.ForeignKey(User,on_delete=models.CASCADE,to_field='id',null = True)

	def __str__(self):
		return self.Product_Name

class permisionsAddInventory(models.Model):
	User			= 	models.ForeignKey(User,on_delete=models.CASCADE,to_field='id',null = True)
	Approval_Status	=	models.CharField(max_length = 20, choices=APPROVAL_STATUS, default='Pending')
	date_time		=	models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return str(self.User)

class permisionsEditInventory(models.Model):
	Inventory 		=	models.ForeignKey(invetoryRecord,on_delete=models.CASCADE,to_field='id',null = True)
	User			= 	models.ForeignKey(User,on_delete=models.CASCADE,to_field='id',null = True)
	Approval_Status	=	models.CharField(max_length = 20, choices=APPROVAL_STATUS, default='Pending')
	date_time		=	models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return str(self.User)