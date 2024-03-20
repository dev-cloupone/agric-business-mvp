document.addEventListener("DOMContentLoaded", function() {

  var inputFields = document.querySelectorAll('input[type="text"], input[type="email"]');

  function checkFormChanges() {
    var formChanged = false;
    inputFields.forEach(function(input) {
      if (input.defaultValue !== input.value) {
        formChanged = true;
      }
    });

    var submitButton = document.getElementById('botaoEnviar');
    submitButton.disabled = !formChanged;
  }


  inputFields.forEach(function(input) {
    input.addEventListener('input', checkFormChanges);
  });

  checkFormChanges();
});