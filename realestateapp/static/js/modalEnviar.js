document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('form-contacto');
    var loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    var mensajeModal = new bootstrap.Modal(document.getElementById('mensajeModal'));

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Evitar el envío del formulario por defecto

            var formData = new FormData(form);

            // Limpiar mensajes de error anteriores
            document.querySelectorAll('.alert.alert-danger').forEach(function(element) {
                element.remove();
            });

            // Mostrar modal de carga
            loadingModal.show();

            fetch(window.location.href, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                // Ocultar modal de carga
                loadingModal.hide();

                if (data.status === 'ok') {
                    // Mostrar modal de mensaje enviado
                    mensajeModal.show();

                    // Limpiar el formulario después de enviar
                    form.reset();
                } else if (data.status === 'invalid') {
                    console.log('Errores de validación:', data.errors);
                    
                    // Mostrar errores en el formulario
                    var errors = JSON.parse(data.errors);
                    for (var field in errors) {
                        var errorMessages = errors[field];
                        var fieldElement = document.querySelector('[name=' + field + ']');
                        if (fieldElement) {
                            var errorElement = document.createElement('div');
                            errorElement.className = 'alert alert-danger';
                            errorMessages.forEach(function(error) {
                                var errorText = document.createTextNode(error.message);
                                errorElement.appendChild(errorText);
                            });
                            fieldElement.parentElement.appendChild(errorElement);
                        }
                    }
                }
            })
            .catch(error => {
                // Ocultar modal de carga en caso de error
                loadingModal.hide();
                console.error('Error al enviar el formulario:', error);
            });
        });
    }
});