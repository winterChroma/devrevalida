const uploadImageForm = document.getElementById("upload-image-form");
const inputFile = document.getElementById("input-file");
const classifierSelect = document.getElementById("classifier-select");
const uploadedImage = document.getElementById("uploaded-image");
const resultText = document.getElementById("result-text");
let imgURL = ""

uploadImageForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  let reader = new FileReader();
  reader.onloadend = function () {
    uploadedImage.src = reader.result
  }

  reader.readAsDataURL(inputFile.files[0]);

  formData = new FormData()
  formData.append("inputFile", inputFile.files[0])
  formData.append("classifierSelect", classifierSelect.value)
  console.log(formData)

  let loc = window.location

  fetch(`${loc.protocol}//${loc.hostname}:${loc.port}/classify`, {
    method: 'POST',
    body: formData
  }).then(response => {
    return response.json()
  }).then(text => {
    console.log(text)
    resultText.innerHTML = `This image is a ${text.result}!`
  })

});



