from django.shortcuts import render, redirect, get_object_or_404
from .forms import Cliente_form, Autor_form, Proveedor_form, Producto_form
from .models import Cliente, Autor, Proveedor, Producto

def index(request):
    return render(request, 'index.html')

def autorlist(request):
    autores = Autor.objects.all()
    return render(request, 'autor_list.html', {'autores': autores})

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor_list.html', {'proveedores': proveedores})

def producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

def crud(request):
    form=Cliente_form()
    return render(request,'crud.html',{'form':form})

def agregar(request):
    if request.method == "POST":
        form=Cliente_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    return redirect('crud')

def editar(request, id):
    cliente=get_object_or_404(Cliente,pk=id)
    if request.method == "POST":
        form = Cliente_form(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form=Cliente_form(instance=cliente)
    return render(request,'editar.html',{'form': form})

def borrar(request, id):
    clientes=get_object_or_404(Cliente,pk=id)
    if request.method == "POST":
        clientes.delete()
        return('cliente')
    return render(request,'eliminar.html',{'clientes':clientes})


# def agregar(request, model):
#     if request.method == "POST":
#         if model == 'Cliente':
#             form = Cliente_form(request.POST)
#         elif model == 'Autor':
#             form = Autor_form(request.POST)
#         elif model == 'Proveedor':
#             form = Proveedor_form(request.POST)
#         elif model == 'Producto':
#             form = Producto_form(request.POST)
#         else:
#             # Manejar caso no válido
#             return redirect('index')

#         if form.is_valid():
#             form.save()
#             return redirect(f'{model.lower()}_list')
#     else:
#         # Manejar caso GET
#         if model == 'Cliente':
#             form = Cliente_form()
#         elif model == 'Autor':
#             form = Autor_form()
#         elif model == 'Proveedor':
#             form = Proveedor_form()
#         elif model == 'Producto':
#             form = Producto_form()
#         else:
#             # Manejar caso no válido
#             return redirect('index')

#     return render(request, 'crud.html', {'form': form, 'model': model})