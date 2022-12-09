from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})

# def home(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ThingForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             # return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     # else:
#     #     form = ThingForm()

#     return render(request, 'name.html', {'form': form})