from rest_framework import serializers
from .models import invetoryRecord

class inventoryserializer(serializers.ModelSerializer):
	class Meta:
		model = invetoryRecord

		fields = '__all__'