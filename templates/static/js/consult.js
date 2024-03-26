//Exibe o arquivo selecionado nas importações de planilhas csv

function updateFileName() {
  var fileInput = document.getElementById('csv_file');
  var fileName = document.getElementById('csv_label');
  var submitButton = document.getElementById('submitButton');

  if (fileInput.files.length > 0) {
    fileName.textContent = fileInput.files[0].name;
    submitButton.style.display = 'inline-block';
  } else {
    fileName.textContent = 'Importação de planilha csv';
    submitButton.style.display = 'none';
  }
}