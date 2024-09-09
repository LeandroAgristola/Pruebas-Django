document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('form-contacto');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            // Verifica si el formulario es válido antes de mostrar el modal
            if (form.checkValidity()) {
                // Si el formulario es válido, mostrar el modal
                event.preventDefault();  // Detener el envío para mostrar el modal
                var mensajeModal = new bootstrap.Modal(document.getElementById('mensajeModal'));
                mensajeModal.show();

                // Enviar el formulario después de mostrar el modal
                mensajeModal._element.addEventListener('hidden.bs.modal', function() {
                    form.submit();  // Enviar el formulario una vez que se cierra el modal
                });
            } else {
                // Si no es válido, evitar el envío y mostrar errores
                event.preventDefault();
                form.reportValidity();
            }
        });
    }
});