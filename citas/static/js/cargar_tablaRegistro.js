$(document).ready(function () {
    $("#table-events").DataTable({
        processing: true,
        dom: "rtip",
        orderable: true,
        language: {
            url: "//cdn.datatables.net/plug-ins/1.13.7/i18n/es-CL.json",
        },
        order: [[0, "desc"]],
    });
    $("#search-input").on("keyup", function () {
        $("#table-events").DataTable().search(this.value).draw();
    });
});