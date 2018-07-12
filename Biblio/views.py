from django.shortcuts import render    

def Livro_list(request):
    return render(request, 'Biblio/Livro_list.html', {})