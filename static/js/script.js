/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.dropdown-trigger').dropdown({
        constrainWidth: true, 
        coverTrigger: false 
      });
});
