from django.shortcuts import render
from django.views import View
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView ,View, TemplateView, DeleteView
from .forms import CreateNoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class Index(ListView):
    model = Note

    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(publish_as =2).order_by('-created_on')

        context ={
            'notes' : notes,
        }
        return render(request, 'baseapp/note_list.html', context)

    
class CreateNoteView(LoginRequiredMixin,View):
    
    def get(self, request,  *args, **kwargs):
        form = CreateNoteForm

        context = {
            'form' : form
        }
        return render(request, 'baseapp/create_note.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateNoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
       
        return HttpResponseRedirect(reverse('index'))


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PrivateNoteView(ListView):
    model = Note

    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(publish_as =1).order_by('-created_on')

        context ={
            'notes' : notes,
        }
        return render(request, 'baseapp/private_note.html', context)

class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')

        note_list =Note.objects.filter(
            Q(body__icontains=query)
        )
        context={
            'note_list' : note_list,
            'query' : query,
        }
        return render(request, 'baseapp/search.html', context)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = "baseapp/note_confirm_delete.html"

    def get_success_url(self):
        return reverse('index')