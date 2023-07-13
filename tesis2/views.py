from django.shortcuts import render

def home(request):
    username = 'John'  # Puedes obtener el nombre de usuario desde la autenticación o desde cualquier otra fuente de datos
    return render(request, 'home.html', {'username': username})
