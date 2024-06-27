$(document).ready(function () {
    $(".btn-reporte").click(function (e) {
      e.stopPropagation();
  
      var target = $(this).data("bs-target");
      $(target).modal('show');
    });
  
    $("#modalReport").on("submit", "#formReport", function (e) {
      e.preventDefault();
      disableButtons();
  
      var fecha = document.getElementById('date');
      $("#spinner").show();
      $("#submitButton").addClass("btn-success");
      console.log(fecha);
      setTimeout(function () {
        window.location.href = "/home/report/" + fecha.value + "/";
      }, 300);
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