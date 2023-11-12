/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.dropdown-trigger').dropdown({
        constrainWidth: true,
        coverTrigger: false
    });
s
    /*
    jQuery for removal of class on window resize
    */
    function handleClassOnResize() {
        var screenWidth = $(window).width();

        if (screenWidth < 992) {
            $('#nav').removeClass('side-padding');
            $('#features').removeClass('features-section');
            console.log('remove classes');
        } else {
            $('#nav').addClass('side-padding');
            $('#features').addClass('features-section');
        }

        if (screenWidth <= 600) {
            $('#hero-section').removeClass('left-margin-0');
        }else{
            $('#hero-section').addClass('left-margin-0');
        }

    }

    handleClassOnResize(); 

    $(window).resize(function () {
        handleClassOnResize(); 
    });


});


document.addEventListener("DOMContentLoaded", function(event) {
    var slider = document.getElementById('ageSlider');
    noUiSlider.create(slider, {
     start: [0, 10],
     connect: true,
     step: 1,
     range: {
       'min': 0,
       'max': 10
     },
     format: wNumb({
       decimals: 0
     })
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
    console.log("Collapsed")

    
  });

