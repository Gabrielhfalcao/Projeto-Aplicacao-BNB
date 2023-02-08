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