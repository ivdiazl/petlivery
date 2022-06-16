$("#cotizacionForm").validate({
    rules: {
        "nombre": {
            required: true
            
        },
        "apellido": {
            required: true
            
        },
        "telefono": {
            required: true,
            minlength: 9,
            maxlength: 9
        },
        "mail": {
            required: true,
            email: true
        }

    }, // --> Fin de reglas
    messages: {
        "nombre": {
            required: 'Ingrese su nombre!'
            
        },
        "apellido": {
            required: 'Ingrese su apellido'
            
        },
        "telefono": {
            required: 'Ingrese su telefono!',
            minlength: 'Ingrese 9 numeros',
            maxlength: 'no ingrese mas de 9 numeros'
        },
        "mail": {
            required: 'Ingrese email!!!',
            email: 'No cumple formato'
        }

    } //-->Fin de mensajes

});