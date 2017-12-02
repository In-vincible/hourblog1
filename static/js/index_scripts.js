$(document).ready(function(){
    $('.slider').slider();
    $('.parallax').parallax();
	$('.carousel.carousel-slider').carousel({fullWidth: true});
	autoplay()   
	function autoplay() {
    	$('.carousel.carousel-slider').carousel('next');
    	setTimeout(autoplay, 4500);
	}
});
        