$(document).ready(function () {
    $("#loginForm").on("submit", function (e) {
      //Previene recarga de pagina y deshabilita botones
      e.preventDefault();
      disableButtons();
  
      //Limpia clases de validacion
      $(".is-invalid").removeClass("is-invalid");
      $(".alert-danger").hide();
      $("#submitButton").removeClass("btn-danger");
      $("#submitButton").addClass("btn-primary");
  
      //Serializa el formulario
      var form = $(this);
      var formData = $(this).serialize();
  
      // Muestra spinner en boton
      $("#spinner").show();
  
      $.ajax({
        url: "/login/",
        type: "POST",
        data: formData,
        success: function (response) {
          form.find(".form-control").not(".is-valid").addClass("is-valid");
          $("#submitButton").addClass("btn-success");
  
          setTimeout(function () {
            location.reload();
          }, 300);
        },
  
        error: function (xhr, errmsg, err) {
          var errors = xhr.responseJSON.errors;
          form.find(".form-control").addClass("is-invalid");
          $("#submitButton").addClass("btn-danger");
          $(".alert-danger").show().text(errors);
  
          $("#spinner").hide();
          enableButtons();
        },
      });
    });
  
    function disableButtons() {
      Array.from(document.getElementsByTagName("button")).forEach(function (
        button
      ) {
        button.disabled = true;
      });
    }
    function enableButtons() {
      Array.from(document.getElementsByTagName("button")).forEach(function (
        button
      ) {
        button.disabled = false;
      });
    }
  });