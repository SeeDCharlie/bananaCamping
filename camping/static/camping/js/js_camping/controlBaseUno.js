function showToastMsj(title, msj){
    $('.titleToast').text(title);
    $('.textToast').text(msj);
  
    var x = document.getElementById("toastMsj")
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
  
}
  