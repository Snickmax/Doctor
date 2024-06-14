$(document).ready(function () {
    $("#table-user").DataTable({
        processing: true,
        "dom": 'rtip',
        orderable: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.13.7/i18n/es-CL.json",
        },
        columnDefs: [{ orderable: false, targets: 6 }],
        order: [[5, "asc"], [3, "asc"], [2, "asc"]],
    });
    $('#search-input').on('keyup', function () {
        $('#table-user').DataTable().search(this.value).draw();
    });
});
