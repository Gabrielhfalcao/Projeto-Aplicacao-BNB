function menuOpcoesUsuario(){
    var a = document.getElementById('imagemUser');
    a.style.transform = 'translate(-160%, -50%)';
    a.style.width = '65px';
    a.style.transition = '.5s';

    var b = document.getElementById('quadroMenuUsuario');
    b.style.transform = 'translate(-20%, -50%)';
    b.style.transition = '.5s';

    var c = document.getElementById('menuOpcoesUsuario');
    c.style.width = '110px';
    c.style.height = '80px';
    c.style.transition = '.5s';

    var d = document.getElementById('arrow-left');
    d.style.transform = 'translate(-700%, -50%)'; 
    d.style.borderRight = '10px solid rgba(0, 0, 0, 0.3)';
    d.style.transition = '.5s';

    var e = document.getElementById('sairMenuUsuario');
    e.style.top = '20px';
    e.style.left = '210px'
    e.style.color = 'white';
    e.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
    e.style.border = '3px solid white'
    e.style.transition = '.5s';
}

function sairMenuUsuario(){
    var a = document.getElementById('imagemUser');
    a.style.transform = 'translate(-50%, -50%)';
    a.style.width = '50px';
    a.style.transition = '.5s';

    var b = document.getElementById('quadroMenuUsuario');
    b.style.transform = 'translate(-50%, -50%)';
    b.style.transition = '.5s';

    var c = document.getElementById('menuOpcoesUsuario');
    c.style.width = '1px';
    c.style.height = '1px';
    c.style.transition = '.5s';

    var d = document.getElementById('arrow-left');
    d.style.transform = 'translate(-50%, -50%)'; 
    d.style.borderRight = '10px solid rgb(36, 36, 54)';
    d.style.transition = '.5s';

    var e = document.getElementById('sairMenuUsuario');
    e.style.transform = 'translate(-50%, -50%)'
    e.style.color = 'rgb(36, 36, 54)';
    e.style.backgroundColor = 'rgb(36, 36, 54)';
    e.style.border = '3px solid rgb(36, 36, 54)'
    e.style.transition = '.5s';
}