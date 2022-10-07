from django.shortcuts import render, redirect
from .forms import (AddressForm, CustomerForm, PriceListForm, ProductForm,
	NakladForm, ZakazForm)

from .models import Products, Addresses, Naklads, Customers, PriceLists, Zakaz


def index_buh(request):
	context = {
		'products': Products.objects.all(),
	}
	return render(request, template_name='buh/index_buh.html', context=context)
	

def raznos(request):
    return render(request, 'buh/raznos.html')


def settings(request):
    return render(request, 'buh/settings.html')


#Addresses
def list_address(request):
	context = {'addresses':Addresses.objects.all(),}
	return render(request, template_name='buh/catalog/addresses/address.html', context=context)


def create_address(request):
	form = AddressForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_address')
	return render()


def delete_address(request):
	return render()


def save_address(request):
	return render()


#Customers
def list_customer(request):
	context = {'customers':Customers.objects.all()}
	return render()


def create_customer(request):
	form = CustomerForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_customer')
	return render()


def delete_customer(request):
	return render()


def save_customer(request):
	return render()



#PriceLists
def list_pricelist(request):
	context = {'pricelists':PriceLists.objects.all()}
	return render()

def create_pricelist(request):
	form = PriceListForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_pricelist')
	return render()

def delete_pricelist(request):
	return render()

def save_pricelist(request):
	return render()



#Products
def list_product(request):
	context = {'products':Products.objects.all()}
	return render()

def create_product(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_product')
	return render()

def delete_product(request):
	return render()

def save_product(request):
	return render()


#Naklad + Zakaz
def list_naklad(request):
	context = {	'naklads':Naklads.objects.all(),
				'zakaz':Zakaz.objects.all()
	}
	return render(request, template_name='buh/naklads/naklad.html', context=context)


def create_naklad(request):
	print("NEW")
	template = 'buh/naklads/new_naklad.html'
	form_naklad = NakladForm(request.POST or None)
	form_zakaz = ZakazForm(request.POST or None)
	context = {
		'form_naklad': form_naklad,
		'form_zakaz': form_zakaz,
	}
	if form_naklad.is_valid() and form_zakaz.is_valid():
		new_naklad = form_naklad.save()
		zakaz = form_zakaz.save(commit=False)
		zakaz.naklad = new_naklad
		zakaz.save()
		return redirect('buh:list_naklad')
	return render(request, template, context)


def delete_naklad(request):
	return render()


def save_naklad(request):
	return render()
