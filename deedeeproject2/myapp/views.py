from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

def index(request):
    all_person = Person.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        all_person = all_person.filter(name__icontains=query)
    return render(request, 'index.html', {'persons': all_person})

def form_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Person.objects.create(name=name, age=age)
        return redirect('/')
    return render(request, 'form.html')

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect("/")
    return render(request, "edit.html", {"person": person})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")