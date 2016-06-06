from django.shortcuts import render

def celeste(request):
	return render(request, 'index.html')
	
def moda(request):
	return render(request, 'index-1.html')

def sobre(request):
	return render(request, 'sobre.html')

def tienda(request):
	return render(request, 'index-3.html')

def contacto(request):
	return render(request, 'contacto.html')
	


