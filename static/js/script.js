/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.dropdown-trigger').dropdown({
        constrainWidth: true,
        coverTrigger: false
    });

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
