var file_upload = document.getElementById('file_upload');
var submit_button = document.getElementById('submit_button');

file_upload.onchange = function () {
  if (file_upload.value == '') {
    submit_button.disabled = true;
  }
  else {
    submit_button.disabled = false;
  }
}