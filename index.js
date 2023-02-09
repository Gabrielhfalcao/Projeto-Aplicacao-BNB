function mostrarOpcaoMenu(){
    var btnRelatorio1 = document.getElementById('btnRelatorio1')
    var btnRelatorio= document.getElementById('btnRelatorio')
    var opcaoMenu1 = document.getElementById('opcaoMenu1')
    opcaoMenu1.style.height = '160px'
    opcaoMenu1.style.transition = '.5s'
    btnRelatorio1.style.display = 'none'
    btnRelatorio.style.display = 'block'
}

function voltarOpcaoMenu(){
    var btnRelatorio1 = document.getElementById('btnRelatorio1')
    var btnRelatorio= document.getElementById('btnRelatorio')
    var opcaoMenu1 = document.getElementById('opcaoMenu1')
    opcaoMenu1.style.height = '40px'
    opcaoMenu1.style.transition = '.5s'
    btnRelatorio1.style.display = 'block'
    btnRelatorio.style.display = 'none'
}

function desfocarFundo(){
    var menuLateral = document.getElementById('menuLateral')
    var tituloPortal = document.getElementById('tituloPort')
    menuLateral.style.filter = 'blur(4px)'
    menuLateral.style.transition = '.5s'
    tituloPortal.style.filter = 'blur(4px)'
    tituloPortal.style.transition = '.5s'
}

function focarFundo(){
    var menuLateral = document.getElementById('menuLateral')
    var tituloPortal = document.getElementById('tituloPort')
    menuLateral.style.filter = 'blur(0px)'
    menuLateral.style.transition = '.5s'
    tituloPortal.style.filter = 'blur(0px)'
    tituloPortal.style.transition = '.5s'
}
