$(document).ready(function(){
    $('.slider').slider();
    $('.parallax').parallax();
    $('.materialboxed').materialbox();
	$('.carousel.carousel-slider').carousel({fullWidth: true});
	autoplay()   
	function autoplay() {
    	$('.carousel.carousel-slider').carousel('next');
    	setTimeout(autoplay, 4500);
	}
});

        