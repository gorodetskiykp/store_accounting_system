from django.db import models
from datetime import datetime, date, timedelta


class Naklads(models.Model):
	date = models.DateField(default=date.today()+timedelta(days=1), verbose_name="Дата")
	date_update = models.DateTimeField(auto_now=True)
	customer = models.ForeignKey('Customers', on_delete=models.PROTECT, verbose_name="Покупатель")
	
	class Meta:
		verbose_name = "Накладная"
		verbose_name_plural = "Накладные"
		ordering = ['-date']

			
class Zakaz(models.Model):
	product = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name = "Товар")
	quantity = models.IntegerField()
	naklad = models.ForeignKey('Naklads', on_delete=models.CASCADE, verbose_name = "Накладная")
	price = models.IntegerField() # СВЯЗАТЬ ПРАЙС-ЛИСТ 
	
	@property
	def summa(self):
		return self.price*self.quantity

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"
		ordering = ['id']


class PriceLists(models.Model):
	customer = models.ForeignKey('Customers', on_delete=models.PROTECT, verbose_name = "Покупатель")
	product = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name = "Товар")
	price = models.IntegerField()
	date_update = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name = "Прайс-лист"
		verbose_name_plural = "Прайс-листы"
		ordering = ['id']
		
	#def __str__(self):         не выводит имя----------------------------------------
		#return self.customer


class Products(models.Model):
	product_name = models.CharField(max_length=50, unique=True, verbose_name = "Наименование")
	volume = models.ForeignKey('Volumes', on_delete=models.PROTECT, verbose_name = "Объем")
	netto = models.DecimalField(max_digits=5, decimal_places=1, verbose_name = "Чистый вес")
	brutto = models.DecimalField(max_digits=5, decimal_places=1, verbose_name = "Грязный вес")
	
	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
		ordering = ['id']
		
	def __str__(self):
		return self.product_name


class Volumes(models.Model):
	volume = models.CharField(max_length=50, verbose_name = "Объем ведра")
	
	class Meta:
		verbose_name = "Объем ведра"
		verbose_name_plural = "Объемы ведер"
		ordering = ['id']
	
	def __str__(self):
		return self.volume


class Customers(models.Model):
	customer_name = models.CharField(max_length=50, verbose_name = "Имя покупателя")
	type_of_customer = models.BooleanField
	address = models.ForeignKey('Addresses', on_delete=models.PROTECT)

	class Meta:
		verbose_name = "Покупатель"
		verbose_name_plural = "Покупатели"
		ordering = ['id']
			
	def __str__(self):
		return self.customer_name


class Addresses(models.Model):
	address = models.CharField(max_length=50, verbose_name = "Адрес")
	
	class Meta:
		verbose_name = "Адрес"
		verbose_name_plural = "Адреса"
		ordering = ['id']
		
	def __str__(self):
		return self.address
