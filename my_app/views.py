from django.shortcuts import render
import requests
from .models import Product


def telegram_bot_sendtext(bot_message):
	bot_token = '5607564433:AAEgCOh9bQZrhT73-2b-lLveCq4FvpmXjs4'
	bot_chatID = '1470735667'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&text='+bot_message
	requests.get(send_text)


def IndexPageView(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		message = request.POST.get('message', None)
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nXabar:{message}")

	return render(
	request=request,
	template_name='index.html')


def CenterPageView(request):
	if request.method == 'POST':

		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		message = request.POST.get('message', None)
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nXabar:{message}")
	return render(
	request=request,
	template_name='center.html')



def ProductPageView(request, slug):

	product = Product.objects.get(slug=slug)

	if request.method == 'POST':
		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		message = request.POST.get('message', None)
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nXabar:{message}")

	return render(
			request=request,
			template_name='product.html',
			context={'product': product}
		)



def CatalogPageView(request, slug):

	products = Product.objects.all().filter(category__slug=slug)


	if request.method == 'POST':
		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		message = request.POST.get('message', None)
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nXabar:{message}")



	return render(
	request=request,
	template_name = 'catalog.html',
	context = {'products': products})



def ServisePageView(request):
	if request.method == 'POST':

		name = request.POST.get('name', None)
		phone = request.POST.get('phone', None)
		message = request.POST.get('message', None)
		telegram_bot_sendtext(f"Ismi:{name}\nTelefon raqami:{phone}\nXabar:{message}")

	return render(
	request=request,
	template_name='service.html')

