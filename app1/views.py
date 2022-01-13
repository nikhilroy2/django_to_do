from django.shortcuts import render, redirect
from .models import PersonInfo

# Create your views here.
def Index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        country = request.POST.get('country', '')
        PersonInfo.objects.create(
            name = name,
            country = country
        )
    list_text = PersonInfo.objects.all()
    context = {
        'list_text': list_text
    }
    return render(request, 'index.html', context=context)


def Delete(request, id):
    list_text = PersonInfo.objects.get(id=id)
    list_text.delete()
    return redirect('index')

def Edit(request, id):
    list_text = PersonInfo.objects.get(id=id)
    
    if request.method == 'POST':
        list_text.name = request.POST.get('name')
        list_text.country = request.POST.get('country')
        list_text.save()
        return redirect('index')
    return render(request, 'edit.html', {'list_text': list_text})