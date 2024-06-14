$(document).ready(function () {
    var popoverTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="popover"]')
    );
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        var popover = new bootstrap.Popover(popoverTriggerEl);
        popoverTriggerEl.addEventListener("shown.bs.popover", function () {
            document
                .querySelector(".btn-logout")
                .addEventListener("click", function () {
                    var modalLogout = new bootstrap.Modal(
                        document.getElementById("modalLogout"),
                        {
                            backdrop: "static", // Evita que el modal se cierre cuando se hace clic fuera de él
                        }
                    );
                    modalLogout.show();
                    setTimeout(function () {
                        window.location.href = "/logout/";
                    }, 300);
                });
        });
        return popover;
    });
});