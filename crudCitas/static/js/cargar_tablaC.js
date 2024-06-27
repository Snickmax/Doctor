$(document).ready(function () {
    $("#table-cita").DataTable({
        processing: true,
        dom: 'rtip',
        orderable: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.13.7/i18n/es-CL.json",
        },
        columnDefs: [{ orderable: false, targets: 4 }],
        order: [[0, "asc"]],
    });
    $('#search-input').on('keyup', function () {
        $('#table-cita').DataTable().search(this.value).draw();
    });
});
