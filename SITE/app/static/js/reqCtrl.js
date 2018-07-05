const apiLink ='http://localhost/NkeWebInterface/API/index.php/Api/';
function submeter(){
    var arquivo=document.getElementById('InputArquivo');
    if (verificaExtensao(String(arquivo.value))){
        document.getElementById('fileName').value = new Date().getTime() + salt(2)
        document.getElementById('formulario').submit();
        // alert('rolou submit');
    }else{
        alert('Envie rar,zip ou tar apenas');
        return false;
    }
}
function verificaExtensao(fileName) {
    if (
        (fileName.match('.rar')) || 
        (fileName.match('.zip')) || 
        (fileName.match('.tar'))
    ) {
        console.log('verdadiro');
        return true;
    }
    console.log('false');
    return false;
}
// function sendFile(arquivo){
    // var payload=new FormData();
    // var name = new Date().getTime()+salt(2);
    // payload.append("arquivo", arquivo.files[0]);
    // payload.append("nome",name);
    // var xhr = new XMLHttpRequest();
    // xhr.open("POST", apiLink +'salvar');
    // xhr.send(formData);
// }
function salt(tamanho){
    var text;
    var  possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (var i = 0; i < tamanho; i++)
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
}
