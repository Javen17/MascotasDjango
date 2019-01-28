
var estaAbierto = 0;

var buttomNavBar = document.getElementById("buttom-nav-bar").addEventListener("click",()=>{
    
    if (estaAbierto === 0) {
        document.querySelector(".nav-side-responsive").style.display = "block";
        estaAbierto = 1;
    }else{
        document.querySelector(".nav-side-responsive").style.display = "none";
        estaAbierto = 0;
    }

},false);