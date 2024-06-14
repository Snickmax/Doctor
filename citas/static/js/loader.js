document.onreadystatechange = function () {
    if (document.readyState !== "complete") {
        document.querySelector("table").style.visibility = "hidden"; // Ocultar la tabla en lugar de la etiqueta "table"
        document.querySelector("#loader").style.visibility = "visible";
    } else {
        setTimeout(function () {
            document.querySelector("#loader").style.display = "none";
            document.querySelector("table").style.visibility = "visible";
        }, 300);
    }
};