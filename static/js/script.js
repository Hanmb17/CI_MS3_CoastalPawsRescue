/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.dropdown-trigger').dropdown({
        constrainWidth: true,
        coverTrigger: false
    });

    $('.tabs').tabs();

    $('#dropdown2').on('click', 'li', function(){
        var target = $(this).find('a').attr('href');

        // Activate the tab using Materialize function
        M.Tabs.getInstance($('.tabs')).select(target.slice(1));
    });


    $('.tooltipped').tooltip();
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        minDate: new Date('2000-01-01'),
        maxDate: new Date(),
        yearRange: [2000, new Date().getFullYear()],
    });

     /*
     Show search results for dogs when searched by name
    */
     var searchResults = $("#searchDogsNameResults");
     var displayResultsFlag = searchResults.data("display-results");

    if (displayResultsFlag === "False") {
        searchResults.addClass("hide");
        } else {
            searchResults.removeClass("hide"); 
        }

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

    var otherDogsYes = $("#otherDogsYes");
        var otherDogsNo = $("#otherDogsNo");
        var otherCatsYes = $("#otherCatsYes");
        var otherCatsNo = $("#otherCatsNo");
        var otherPetsYes = $("#otherPetsYes");
        var otherPetsNo = $("#otherPetsNo");
        var childrenYes = $("#childrenYes");
        var childrenNo = $("#childrenNo");

        var otherDogsDetails = $("#other_dogs_details");
        var otherCatsDetails = $("#other_cats_details");
        var otherPetsDetails = $("#other_pets_details");
        var childrenDetails = $("#children_details");

        
        toggleDetailsInput(otherDogsYes, otherDogsDetails);
        toggleDetailsInput(otherCatsYes, otherCatsDetails);
        toggleDetailsInput(otherPetsYes, otherPetsDetails);
        toggleDetailsInput(childrenYes, childrenDetails);

        // Attach event listeners to "Yes" and "No" radio buttons
        otherDogsYes.change(function () {
            toggleDetailsInput(otherDogsYes, otherDogsDetails);
        });
        otherDogsNo.change(function () {
            toggleDetailsInput(otherDogsYes, otherDogsDetails);
        });

        otherCatsYes.change(function () {
            toggleDetailsInput(otherCatsYes, otherCatsDetails);
        });
        otherCatsNo.change(function () {
            toggleDetailsInput(otherCatsYes, otherCatsDetails);
        });

        otherPetsYes.change(function () {
            toggleDetailsInput(otherPetsYes, otherPetsDetails);
        });
        otherPetsNo.change(function () {
            toggleDetailsInput(otherPetsYes, otherPetsDetails);
        });

        childrenYes.change(function () {
            toggleDetailsInput(childrenYes, childrenDetails);
        });
        childrenNo.change(function () {
            toggleDetailsInput(childrenYes, childrenDetails);
        });

        function toggleDetailsInput(option, detailsInput) {
            var input = detailsInput.find('input[type="text"]');

            if (option.is(":checked")) {
                detailsInput.removeClass("hide");
                input.prop("required", true); 
            } else {
                detailsInput.addClass("hide");
                input.prop("required", false); 
            }
        }


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

     // Update min and max values when the slider changes
    slider.noUiSlider.on("update", function(values, handle) {
        document.getElementById("minAge").value = values[0];
        document.getElementById("maxAge").value = values[1];
      });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
    console.log("Collapsed")

    
  });

