$(document).ready(function () {
    $("#modalBase").on("submit", "#editarForm", function (e) {
        //Previene recarga de pagina y deshabilita botones
        e.preventDefault();
        disableButtons();

        //Limpia clases de validacion
        $(".is-invalid").removeClass("is-invalid");
        $(".is-valid").removeClass("is-valid");
        $(".invalid-feedback").html("");
        $("#submitButton").removeClass("btn-danger");
        $("#submitButton").addClass("btn-primary");

        //Obtiene el ID de usuario y serializa el formulario
        var patientId = $(this).data("patient-id");
        var form = $(this);
        var formData = $(this).serialize();

        // Muestra spinner en boton
        $("#spinner").show();

        //Envio de datos por AJAX
        $.ajax({
            url: "/home/actualizar_cita/" + patientId + "/",
            type: "POST",
            data: formData,
            success: function (response) {
                form.find('.form-control').prop("disabled", true);
                form.find(".form-control").not(".is-valid").addClass("is-valid");
                $(".alert-success").show().text(response.success);
                $("#submitButton").addClass("btn-success");

                setTimeout(function () {
                    $("#modalBase").modal("hide"); // Close the modal
                    location.reload();
                }, 300);
            },
            error: function (xhr, errmsg, err) {
                var errors = xhr.responseJSON.errors;
                // Recorre todos los errores y los muestra en el lugar correcto
                for (var field in errors) {
                    var formField = $("#" + field);
                    var errorMessages = errors[field]
                        .map(function (error) {
                            return "<li>" + error + "</li>";
                        })
                        .join(" ");
                    formField.siblings(".invalid-feedback").html(errorMessages);
                    formField.addClass("is-invalid");
                }
                form.find(".form-control").not(".is-invalid").addClass("is-valid");
                $("#submitButton").addClass("btn-danger");

                // Ocultar el spinner y habilitar los botones
                $("#spinner").hide();
                enableButtons();
            },
        });
    });

    function disableButtons() {
        $("button").prop("disabled", true);

        $(".nav-link").click(function (e) {
            e.preventDefault();
        });
    }

    function enableButtons() {
        $("button").prop("disabled", false);

        $(".nav-link").off('click');
    }
});