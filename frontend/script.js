document.getElementById('clear-button').addEventListener('click', function () {
    document.getElementById("preview").src = 'default-image.png';
    document.getElementById("result-image").src = 'default-image.png';
});

document.getElementById("imageFile").onchange = evt => {
  const [file] = evt.target.files
  if (file) {
    document.getElementById("preview").src = URL.createObjectURL(file)
  }
}

document.getElementById("detect-button").addEventListener('click', function (e) {
    document.getElementById("detect-button").disabled = true
    let request = new XMLHttpRequest();   // new HttpRequest instance
    request.open("POST", 'api/detect');
    request.responseType = 'blob';
    request.onload = function () {
        let status = request.status;
        if (status === 200) {
            document.getElementById("result-image").src = URL.createObjectURL(request.response);
        } else {
            console.log(status);
        }
        document.getElementById("detect-button").disabled = false
    };
    let formData = new FormData();
    formData.append("imagefile", document.getElementById("imageFile").files[0]);
    request.send(formData);
})