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

    const url="http://127.0.0.1:8000/plantas/get_Planta/?nombrePlanta=Diente+de+Leon";
    fetch(url)
    .then((response) => response.json())
    .then((responseData) => {
        console.log(responseData);
        var planta= responseData[0]
        divInformacion.innerHTML =  `<div class="tm-bg-gray-dark tm-box-2">
                                        <h4 class="tm-text-primary tm-h3 mb-4">Resultado:</h4>
                                        <p><strong>Nombre:</strong></p>
                                        <p>${planta.nombre}</p>
                                        <p><strong>Nombre Cientifico:</strong><p>${planta.nombreCientifico}</p></p>
                                        <p><strong>Descripción:</strong><p class="text-justify">${planta.descripcion}</p></p>
                                        <p><strong>Cuidados:<strong></p>

                                    </div>`;
  
    })



    
}


