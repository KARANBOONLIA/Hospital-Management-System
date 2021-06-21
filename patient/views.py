from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Patient, Doc
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
    context = {'Patient': Patient.objects.all()}
    if not request.user.is_authenticated:
        context['loggedin']=True
        context['user']=request.user

    return render(request, 'patient/index.html', context)

'''class IndexView(generic.ListView):
    template_name = 'patient/index.html'
    context_object_name = 'patient'         # context_object_name by default is 'object_list'
    # get_context_data is used to add extra data to context dict
    # Call the base implementation first to get the normal min context
    # context = super().get_context_data(**kwargs)

    def get_queryset(self):
        return Patient.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['user']= request.user'''


def details(request,no):
    try:
        p1 = Patient.objects.get(pk=no)

    except Patient.DoesNotExist:
        raise Http404("patient does not exist")
    return render(request, 'patient/details.html',{'p1': p1,'non_docs':Doc.objects.exclude(all_pats=p1).all(),'all_docs':p1.all_pats_rel.all()})

class PatientCreate(CreateView):
    model = Patient
    fields = ['pat_name', 'pat_code', 'pat_illness']

class PatientUpdate(UpdateView):
    model = Patient
    fields = ['pat_name', 'pat_code', 'pat_illness']

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('indexOFpats')


def book(request,no):
    try:
        doc_id = str(request.POST['doc_object'])
        doc_object = Doc.objects.get(name=doc_id)
        patient = Patient.objects.get(pk=no)
    except KeyError:
        return render(request,"patient/error.html",{'msg':'no selection'})
    except Doc.DoesNotExist:
        return render(request, "patient/error.html",{'msg':'No such doctor exists'})
    except Patient.DoesNotExist:
        return render(request, "patient/error.html",{'msg':'No such patient exists'})
    doc_object.all_pats.add(patient)
    return HttpResponseRedirect(reverse("details",args=(no,)))

