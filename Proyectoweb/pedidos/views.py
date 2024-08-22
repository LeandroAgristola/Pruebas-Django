from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineaPedidos, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedidos(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
        ))

    LineaPedidos.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
        carro=carro.carro  # Enviamos el carro para poder mostrar los productos en el correo
    )

    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por tu pedido"
    mensaje = render_to_string("emails/pedidos.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedidos": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
        "carro": kwargs.get("carro")  # Pasamos el carro al contexto para el email
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "leo_91_166@hotmail.com"
    # to = kwargs.get("emailusuario")  # Línea comentada si no está configurado el email del usuario
    to = "leoolp.91@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)