from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm
from .models import Perfil

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # CREAMOS EL PERFIL: Esto asegura que el usuario tenga donde guardar su avatar
            Perfil.objects.create(user=user) 
            
            login(request, user)
            return redirect('Login') # Por ahora mandamos al login hasta tener la Home
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})



@login_required
def editar_perfil(request):
    usuario = request.user
    # Intentamos obtener el perfil, si no existe lo creamos (por seguridad)
    perfil, created = Perfil.objects.get_or_create(user=usuario)

    if request.method == 'POST':
        # ¡IMPORTANTE! request.FILES es lo que recibe la imagen
        form = UserEditForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            # Guardamos datos de User
            form.save()
            
            # Guardamos el Avatar manualmente en el modelo Perfil
            if request.FILES.get('avatar'):
                perfil.avatar = request.FILES['avatar']
                perfil.save()
                
            return redirect('Home') # O a una vista de "Perfil" que crearemos
    else:
        form = UserEditForm(instance=usuario)

    return render(request, 'accounts/editar_perfil.html', {'form': form})