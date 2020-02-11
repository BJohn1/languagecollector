from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Language
from .forms import UpskillForm

# Define the home view
def home(request):
  return HttpResponse('<h1>DO YOU EVEN CODE BRUH?</h1>')

def about(request):
  return render(request, 'about.html')

def languages_index(request):
  languages = Language.objects.all()
  return render(request, 'languages/index.html', { 'languages': languages })

def languages_detail(request, language_id):
  language = Language.objects.get(id=language_id)
  upskill_form = UpskillForm()
  return render(request, 'languages/detail.html', {
    'language': language, 'upskill_form': upskill_form
  })

def add_upskill(request, language_id):
  # create the ModelForm using the data in request.POST
  form = UpskillForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_upskill = form.save(commit=False)
    new_upskill.language_id = language_id
    new_upskill.save()
  return redirect('detail', language_id=language_id)


class LanguageCreate(CreateView):
  model = Language
  fields = ['name','years_experience']
  success_url = '/languages/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  

class LanguageUpdate(UpdateView):
  model = Language
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['years_experience']

class LanguageDelete(DeleteView):
  model = Language
  success_url = '/languages/'