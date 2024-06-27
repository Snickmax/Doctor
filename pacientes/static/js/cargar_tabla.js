$(document).ready(function () {
    $("#table-patient").DataTable({
        processing: true,
        dom: 'rtip',
        orderable: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.13.7/i18n/es-CL.json",
        },
        columnDefs: [{ orderable: false, targets: 9 }],
        order: [[0, "asc"]],
    });
    $('#search-input').on('keyup', function () {
        $('#table-patient').DataTable().search(this.value).draw();
    });
});
