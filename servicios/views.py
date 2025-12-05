
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .models import Servicio


# Página de inicio
def paginaInicio(request):
    servicios = Servicio.objects.all()[:6]
    return render(request, 'paginaInicio.html', {'servicios': servicios})


# Página de Servicios
def Servicios(request):
    modeloservicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'modeloservicios': modeloservicios})


# Páginas estáticas
def privacidad(request):
    return render(request, 'privacidad.html')

def noticias(request):
    return render(request, 'noticias_list.html')


# Página de Contacto con envío de email
def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        asunto = f'Contacto desde Terapy - {nombre}'
        cuerpo = f'De: {nombre} <{email}>\n\n{mensaje}'

        try:
            send_mail(
                asunto,
                cuerpo,
                'no-reply@terapy.local',
                ['fa21-0936@unphu.edu.do']
            )
            messages.success(request, 'Mensaje enviado correctamente. Gracias por contactarnos.')
        except Exception:
            messages.error(request, 'Ocurrió un error al enviar el mensaje. Intenta más tarde.')

        return redirect('contacto')

    return render(request, 'contacto.html')


# Login personalizado
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('/admin/')

            return redirect('paginaInicio')
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
            return redirect('login_page')

    return render(request, 'registration/login.html')


# Logout personalizado
def custom_logout(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('paginaInicio')


# Reservar un servicio
def reservar_servicio(request):
    if request.method == 'POST':
        servicio = request.POST.get('servicio')
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        fecha = request.POST.get('fecha')

        # Validar fecha ingresada
        try:
            fecha_reserva = timezone.datetime.strptime(fecha, "%Y-%m-%d").date()
        except:
            messages.error(request, "La fecha no es válida.")
            return redirect('Servicios')

        # Validar fecha no en el pasado
        hoy = timezone.localdate()
        if fecha_reserva < hoy:
            messages.error(request, "No puedes reservar una fecha en el pasado.")
            return redirect('Servicios')

        asunto = f'Reserva de servicio: {servicio}'
        cuerpo = (
            f'Servicio: {servicio}\n'
            f'Cliente: {nombre} <{email}>\n'
            f'Fecha preferida: {fecha}\n'
        )

        try:
            send_mail(
                asunto,
                cuerpo,
                'no-reply@terapy.local',
                ['fa21-0936@unphu.edu.do']
            )
            messages.success(request, 'Tu reserva fue enviada. Te contactaremos pronto.')
        except Exception:
            messages.error(request, 'Error al enviar la reserva. Intenta más tarde.')

        return redirect('Servicios')

    return redirect('Servicios')