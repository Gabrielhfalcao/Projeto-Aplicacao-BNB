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
    e.style.border = '3px solid rgb(36, 36, 54)';
    e.style.top = '50%';
    e.style.left = '50%';
    e.style.transform = 'translate(-50%, -50%)';
    e.style.zIndex = '0';
    e.style.transition = '.5s';
}

function mostrarFotoUsuario(){
    var a = document.getElementById('espacoImagemUsuarioEmFoco');
    a.style.top = '50%';
    a.style.left = '50%';
    a.style.transform = 'translate(-50%, -50%)';
    a.style.boxShadow = '1px 1px 1px 1000px rgba(0, 0, 0, 0.7)';
    a.style.transition = '.5s';

    var b = document.getElementById('menuLateral');
    b.style.left = '-260px'; 
    b.style.transition = '1s';

    var c = document.getElementById('desabilitarBtnMenuLateral');
    c.style.display = 'block';
    c.style.zIndex = '1000';

    var a1 = document.getElementById('imagemUser');
    a1.style.transform = 'translate(-50%, -50%)';
    a1.style.width = '50px';
    a1.style.transition = '.5s';

    var b1 = document.getElementById('quadroMenuUsuario');
    b1.style.transform = 'translate(-50%, -50%)';
    b1.style.transition = '.5s';

    var c1 = document.getElementById('menuOpcoesUsuario');
    c1.style.width = '1px';
    c1.style.height = '1px';
    c1.style.transition = '.5s';

    var d1 = document.getElementById('arrow-left');
    d1.style.transform = 'translate(-50%, -50%)'; 
    d1.style.borderRight = '10px solid rgb(36, 36, 54)';
    d1.style.transition = '.5s';

    var e1 = document.getElementById('sairMenuUsuario');
    e1.style.transform = 'translate(-50%, -50%)'
    e1.style.color = 'rgb(36, 36, 54)';
    e1.style.backgroundColor = 'rgb(36, 36, 54)';
    e1.style.border = '3px solid rgb(36, 36, 54)';
    e1.style.top = '50%';
    e1.style.left = '50%';
    e1.style.transform = 'translate(-50%, -50%)';
    e1.style.zIndex = '0';
    e1.style.transition = '.5s';
}

function sairFotoUsuarioEmFoco(){
    var a = document.getElementById('espacoImagemUsuarioEmFoco');
    a.style.top = '-500px';
    a.style.left = '50%';
    a.style.transform = 'translate(-50%, -50%)';
    a.style.boxShadow = '1px 1px 1px 1px rgba(0, 0, 0, 0.7)';
    a.style.transition = '.5s';

    var c = document.getElementById('desabilitarBtnMenuLateral');
    c.style.display = 'none';
    c.style.zIndex = '0';

    var b = document.getElementById('fecharMenuLateral');
    b.style.display = 'none';
}
