from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Language
from .forms import UpskillForm

# Define the home view
def home(request):
  return HttpResponse('<h1>DO YOU EVEN CODE BRUH?</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def languages_index(request):
  languages = Language.objects.filter(user=request.user)
  # You could also retrieve the logged in user's cats like this
  # cats = request.user.cat_set.all()
  return render(request, 'languages/index.html', { 'languages': languages })

@login_required
def languages_detail(request, language_id):
  language = Language.objects.get(id=language_id)
  upskill_form = UpskillForm()
  return render(request, 'languages/detail.html', {
    'language': language, 'upskill_form': upskill_form
  })

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class LanguageCreate(LoginRequiredMixin, CreateView):
  model = Language
  fields = ['name','years_experience']
  success_url = '/languages/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  

class LanguageUpdate(LoginRequiredMixin, UpdateView):
  model = Language
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['years_experience']

class LanguageDelete(LoginRequiredMixin, DeleteView):
  model = Language
  success_url = '/languages/'