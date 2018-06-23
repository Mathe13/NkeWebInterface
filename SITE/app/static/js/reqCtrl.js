function submeter(){
    var arquivo=document.getElementById('InputArquivo');
    if (verifica_extensao(String(arquivo.value))){
        // document.getElementById('formulario').submit();
        return true;
    }else{
        alert('Envie rar,zip ou tar apenas');
        return false;
    }
}
function verifica_extensao(fileName) {
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
