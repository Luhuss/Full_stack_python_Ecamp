document.getElementById("text2").style.display = "none"


function mostrarMensaje(){
    document.getElementById('text2').style.display = "block";
}

function ocultarMensaje(){
    document.getElementById('text2').style.display = "none";
}

function agrandar(){
    document.getElementById("img").style.width = "100%";
}
function achicar() {
    document.getElementById("img").style.width ="20%";

}
function agrandarTexto() {
    document.getElementById("caja3").style.fontSize = "xx-large";

}
function achicarTexto(evento) {
    document.getElementById("caja3").style.fontSize = "initial";
    evento.innerHTML = "nuevo texto";
}

