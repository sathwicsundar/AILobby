from django.shortcuts import render, HttpResponse
from .models import Contact,contactForm,Project,DigitalNote


# Create your views here.
def index(request):
    return render(request, 'AIWeb/index.html')


def contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            concern = request.POST['desc']
            print(name, email, phone, concern)
            contactObj = Contact(name=name, email=email, phone=phone, desc=concern)
            contactObj.save()
            form = contactForm()
            return render(request, 'AIWeb/contact.html', {'form': form, 'submitted': True, 'try': True})
        else:
            form = contactForm()
            return render(request, 'AIWeb/contact.html', {'form': form, 'submitted': False, 'try': True})
    form = contactForm()
    return render(request, 'AIWeb/contact.html', {'form': form, 'submitted': False, 'Failed': False})


def projects(request):
    Projects = Project.objects.all()
    return render(request, 'AIWeb/projects.html', {'Projects': Projects})


def events(request):
    return render(request, 'AIWeb/events.html')


def academics(request):
    digitalNotes = {'allSubject':list(DigitalNote.objects.all())[::-1]}
    return render(request, 'AIWeb/academics.html',digitalNotes)
