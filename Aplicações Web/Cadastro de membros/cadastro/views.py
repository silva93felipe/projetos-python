from django.shortcuts import render, get_object_or_404, redirect

from . forms import InsereMembro, InsereCargo, InsereDepartamento

from .models import Cargo, Membro, Departamento

def index(request):
    return render(request, 'base.html')

    
# Módulos de cargos (cadastrar, editar, consultar e excluir)
def cargos(request):
    cargo = Cargo.objects.all()
    return render(request, "cadastro/cargos.html", {'cargos': cargo})

def insereCargo(request):
        if request.method == 'POST':
            formCargo = InsereCargo(request.POST)

            if formCargo.is_valid():
                formCargo.save()
                return redirect ('/')
        else:
            formCargo = InsereCargo()
            return render(request, 'cadastro/inserecargo.html', {'formsCargo': formCargo})

def deletaCargo(request, id):
    cargo = get_object_or_404(Cargo, pk=id)
    cargo.delete()
    return redirect('/')





# Módulos de membros (cadastrar, editar, consultar e excluir)
def membros(request):
    membro = Membro.objects.all()
    return render(request, "cadastro/membros.html", {'membros': membro})

def insereMembro(request):
        if request.method == 'POST':
            form = InsereMembro(request.POST)

            if form.is_valid():
                form.save()
                return redirect ('/')
        else:
            form = InsereMembro()
            return render(request, 'cadastro/inseremembro.html', {'forms': form})


# Módulos de departamentos (cadastrar, editar, consultar e excluir)
def departamento(request):
    departamento = Departamento.objects.all()
    return render(request, "cadastro/departamento.html", {'departamentos': departamento})

def insereDepartamento(request):
        if request.method == 'POST':
            formsDepartamento = InsereDepartamento(request.POST)

            if formsDepartamento.is_valid():
                formsDepartamento.save()
                return redirect ('/')
        else:
            formsDepartamento = InsereDepartamento()
            return render(request, 'cadastro/inseredepartamento.html', {'formsDepartamento': formsDepartamento})
        
        
    


