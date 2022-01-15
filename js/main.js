const chooseFile = document.getElementById("exampleInputFile");
const imgPreview = document.getElementById("img-preview");
const divInformacion = document.getElementById("divInformacion")

chooseFile.addEventListener("change", function () {
getImgData();
divInformacion.innerHTML="";
});

function getImgData() {
const files = chooseFile.files[0];
if (files) {
const fileReader = new FileReader();
fileReader.readAsDataURL(files);
fileReader.addEventListener("load", function () {
imgPreview.style.display = "block";
imgPreview.innerHTML = '<img src="' + this.result + '" />';
});    
}
}





function getInformacion(){

    divInformacion.innerHTML =  `<div class="tm-bg-gray-dark tm-box-2">
                                    <h4 class="tm-text-primary tm-h3 mb-4">Resultado</h4>
                                    <p class="mb-5"><strong>Nombre:<strong></p>
                                    <p class="mb-5"><strong>Nombre Cientifico:<strong></p>
                                    <p class="mb-5"><strong>Descripción:<strong></p>

                                </div>`;
    
}