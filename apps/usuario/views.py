from django.contrib.auth import login, logout
from django.core.serializers import serialize
from django.http.response import (HttpResponse, HttpResponseRedirect,
                                  JsonResponse)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.edit import FormView

from apps.usuario.models import Usuario

from .forms import FormularioLogin, FormularioUsuario


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    # adds CSRF protection,it can be used on a per view basis
    @method_decorator(csrf_protect)
    # adds headers to a response so that it will never be cached
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class ListadoUsuario(ListView):
    model = Usuario

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('usuario:inicio_usuario')


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'

    # does the same as the method that is in Forms.py
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    name=form.cleaned_data.get('name'),
                    last_name=form.cleaned_data.get('last_name')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuario:inicio_usuario')


class EditarUsuario(UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/editar_usuario.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuario:inicio_usuario')


class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuario/eliminar_usuario.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.is_active = False
            usuario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuario:inicio_usuario')
