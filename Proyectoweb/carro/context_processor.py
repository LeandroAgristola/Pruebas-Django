def importe_total_carro(request):
    total = 0
    # Verifica si 'carro' está en la sesión
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"]) 

    return {"importe_total_carro": total}