
$('.btnContReq').on('click', function (evt) {
    // Initiate Variables With Form Content
    var name = $("#name").val();
    var email = $("#email").val();
    var cell = $("#cel").val();
    var message = $("#message").val();

    if (name == '' || cell == '' || message == ''){
        formError();
        showToastMsj('error', 'Llene los datos para enviar el formulario de contacto');
    }else{
        
    var datos = JSON.stringify({
        name, name,
        cell: cell,
        email: email,
        message: message
    });
    submitForm(datos);
    }

});

function submitForm(datos) {
    requestAjax('submitContact', datos);
}

function respuestaAjax(data) {
    showToastMsj('Muy Bien', data.msj);
    formSuccess();
}

function errorSucces(msj) {
    showToastMsj('Muy Mal', msj);
    formError();
}
function errorAjax() {
    formError();
    showToastMsj('Muy Mals', 'Compruebe su conexion a internet');
}

function formSuccess() {
    $("#contactForm")[0].reset();
    submitMSG(true, "Mensaje Enviado!")
}

function formError() {
    $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
        $(this).removeClass();
    });
    submitMSG(false, "Hay campos vacios en el formulario de contacto!");
}

function submitMSG(valid, msg) {
    if (valid) {
        var msgClasses = "h3 text-center tada animated text-success";
    } else {
        var msgClasses = "h3 text-center text-danger";
    }
    $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
}