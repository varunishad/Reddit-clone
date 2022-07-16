
// USER_DROPDOWN
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


// Three dots ICON DROPDOWN
$(document).ready(function(){
  // $(".ppp").click(function(){
  //   $(this).parent('form').parent('div').parent('div').parent('div').parent('div').parent('div').remove()
  // });
  $('.dropbtnicon').click(function(){
    $(this).siblings().toggleClass('show')
  });
});
$(document).ready(function(){
  $('button.up').click(function(event){
    // event.preventDefault();
    location.reload();
    $(this).addClass('upvote')
    $(this).siblings('span').addClass('upvote')
    $(this).siblings('span').removeClass('downvote')
    $(this).siblings('.down').removeClass('downvote')
  });
  $('button.down').click(function(event){
    // event.preventDefault();
    location.reload();
    $(this).addClass('downvote')
    $(this).siblings('span').addClass('downvote')
    $(this).siblings('span').removeClass('upvote')
    $(this).siblings('.up').removeClass('upvote')
  });
  $('.up, .down, actions a, actions button').click(function(){

  })
});


  window.addEventListener("click",function(event) {
    if (!event.target.matches('.dropbtnicon')) {
      var dropdowns = document.getElementsByClassName("dropdown-contenticon");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  },true)



//Scroll to


// Vote buttons
