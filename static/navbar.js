
document.querySelector('.dropbtn').addEventListener("click",function(){
  document.getElementById("myDropdown").classList.toggle("show");
},false)
// Close the dropdown if the user clicks outside of it
window.addEventListener("click",function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
},true)

