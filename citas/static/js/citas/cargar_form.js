$(document).ready(function () {
    // Inicializa los tooltips
    $('.tooltip-trigger').tooltip();

    $(".btn-open-form").click(function (e) {
        e.stopPropagation();

        var target = $(this).data("bs-target");
        $(target).modal('show');

        var formType = $(this).data("form-type"); // Obtiene el tipo de formulario
        var patientId = $(this).data("patient-id"); // Obtiene el ID del usuario, si está presente
        var requestData = { form_type: formType }; // Inicializa los datos de la solicitud

        // Agrega el ID del usuario a los datos de la solicitud si está presente
        if (patientId) {
            requestData.patient_id = patientId;
        }
        $.ajax({
            url: "/home/cargar_formulario/", // Ruta a la vista que devuelve el formulario
            type: "GET",
            data: requestData, // Envía el tipo de formulario y, opcionalmente, el ID del usuario a la vista
            success: function (response) {
                $("#modalBase .modal-body").html(response.form_html); // Carga el formulario en el cuerpo del modal
                $("#modalBase .modal-title").html(response.titulo_modal);
                $("#editarForm").attr("data-patient-id", patientId);
            },
            error: function (xhr, errmsg, err) {
            },
        });
    });
});