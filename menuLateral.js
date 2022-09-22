function aparecerMenuLateral(){
    var a = document.getElementById('menuLateral');
    a.style.left = '0'; 
    a.style.transition = '1s';

    var b = document.getElementById('fecharMenuLateral');
    b.style.display = 'block';

    var c = document.getElementById('campoFutebol');
    c.style.filter = 'blur(2px)'; 
    c.style.transition = '.5s';

    var d = document.getElementById('cabecalho');
    d.style.boxShadow = '0px 0px 0px 3000px rgba(0, 0, 0, 0.2)';
}

function sairMenuLateral(){
    var a = document.getElementById('menuLateral');
    a.style.left = '-260px'; 
    a.style.transition = '1s';

    var b = document.getElementById('fecharMenuLateral');
    b.style.display = 'none';

    var c = document.getElementById('campoFutebol');
    c.style.filter = 'blur(0px)'; 
    c.style.transition = '.5s';

    var d = document.getElementById('cabecalho');
    d.style.boxShadow = '0px 0px 0px 0px rgba(0, 0, 0, 0.2)';
}