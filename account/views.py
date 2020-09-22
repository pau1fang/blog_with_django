from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, get_list_or_404

from django.shortcuts import render, reverse
from .forms import RegisterForm, LoginForm
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.http import is_safe_url
from .models import BlogUser


class RegisterView(generic.FormView):
    form_class = RegisterForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            # user = form.save(False)
            # user.is_active = False
            # user.save(True)
            return HttpResponseRedirect(reverse('account:login'))
        else:
            return self.render_to_response({
                'form': form
            })


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = '/blog'
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)

        if form.is_valid():
            login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        else:
            return self.render_to_response({'form': form})

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=[self.request.get_host()]):
            redirect_to = self.success_url
        return redirect_to

    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = '/'
        kwargs['redirect_to'] = redirect_to
        return super().get_context_data(**kwargs)


class LogoutView(generic.RedirectView):
    url = '/account/login/'

    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ProfileView(generic.TemplateView):
    template_name = 'account/profile.html'


