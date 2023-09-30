from django.shortcuts import render, redirect
from .models import Lugares, NaoKennedy, Tabela
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    lugares = Lugares.objects.all()
    naokennedy = NaoKennedy.objects.all()
    tabela = Tabela.objects.all()

    return render(request,
                  "home.html",
                  context={
                      "Lugares": lugares,
                      "NaoKennedy": naokennedy,
                      "Tabela": tabela
                  })

@login_required
def create_lugar(request):
    if request.method == "POST":
        Lugares.objects.create(title=request.POST["titulo"],
                               nota_geral=request.POST["nota_geral"],
                               frequencia=request.POST["frequencia"],
                               problema=request.POST["problema"])

        return redirect("home")
    return render(request, "forms.html", context={"action":"Adicionar"})

@login_required
def update_lugar(request, id):
  lugar = Lugares.objects.get(id = id)
  if request.method == "POST":
    lugar.title=request.POST["titulo"]
    lugar.nota_geral=request.POST["nota_geral"]
    lugar.frequencia=request.POST["frequencia"]
    lugar.problema=request.POST["problema"]
    lugar.save()
        
    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar" ,"lugar": lugar})

@login_required
def delete_lugar(request, id):
  lugar = Lugares.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      lugar.delete()
        
    return redirect("home")
  return render(request, "are_you_sure.html", context={"action": "Atualizar" ,"lugar": lugar})



@login_required
def create_kennedy(request):
    if request.method == "POST":
        NaoKennedy.objects.create(title=request.POST["titulo"],
                               nivel_ruim=request.POST["nivel_ruim"],
                               regularidade=request.POST["regularidade"],
                               insatisfacao=request.POST["insatisfacao"])

        return redirect("home")
    return render(request, "forms2.html", context={"action":"Adicionar"})

@login_required
def update_kennedy(request, id1):
  kennedy = NaoKennedy.objects.get(id1 = id1)
  if request.method == "POST":
    kennedy.title=request.POST["titulo"]
    kennedy.nivel_ruim=request.POST["nivel_ruim"]
    kennedy.regularidade=request.POST["regularidade"]
    kennedy.insatisfacao=request.POST["insatisfacao"]
    kennedy.save()
        
    return redirect("home")
  return render(request, "forms2.html", context={"action": "Atualizar" ,"kennedy": kennedy})

@login_required
def delete_kennedy(request, id1):
  kennedy = NaoKennedy.objects.get(id1 = id1)
  if request.method == "POST":
    if "confirm" in request.POST:
      kennedy.delete()
        
    return redirect("home")
  return render(request, "are_you_sure2.html", context={"action": "Atualizar" ,"kennedy": kennedy})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(request.POST["username"],request.POST["email"],request.POST["password"])
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action":"Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(username=request.POST["username"],password=request.POST["password"])
    if user != None:
      login(request,user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")