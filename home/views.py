from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, generic.ListView):
    login_url = '/home/login/'
    redirect_field_name = '/home/index'
    template_name = 'home/index.html'
    context_object_name = 'users_list'


    def get_queryset(self):
        return self.request.user

class UserFormView(View):

    form_class = UserForm
    template_name = 'home/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home:index")
        return render(request, self.template_name, {"form":form})

