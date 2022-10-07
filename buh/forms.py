from django import forms

from .models import Products, Addresses, PriceLists, Customers, Naklads, Zakaz


class AddressForm(forms.ModelForm):
	class Meta:
		model = Addresses
		fields = ['address']


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customers
		fields = ['customer_name']
		
		
class PriceListForm(forms.ModelForm):
	class Meta:
		model = PriceLists
		fields = ['customer','product', 'price']
		
		
class ProductForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ['product_name', 'volume', 'netto', 'brutto']


class NakladForm(forms.ModelForm):
	class Meta:
		model = Naklads
		fields = 'customer',
		widgets = {
			'customer': forms.Select(attrs={'class': 'input'}),
		}


class ZakazForm(forms.ModelForm):

	class Meta:
		model = Zakaz
		fields = 'product', 'quantity', 'price'
		widgets = {
			'product': forms.Select(attrs={'class': 'input'}),
			'quantity': forms.TextInput(attrs={'class': 'input'}),
			'price': forms.TextInput(attrs={'class': 'input'}),
		}

