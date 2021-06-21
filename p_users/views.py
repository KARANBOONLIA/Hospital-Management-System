from django.shortcuts import render, redirect
from p_users.forms import PatientModelForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from patient.models import Patient
from django.contrib.auth.models import User

class PatientFormView(generic.View):
    form_class = PatientModelForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user.save()

            user = authenticate(username=username, password=password)

            if user is None:
                login(request, user)
                return redirect('add')


        context = {'patient': Patient.objects.all()}
        return render(request, 'patient/index.html', context)


