const layers = document.querySelectorAll('.layer');

function parallax() {
  const y = window.scrollY;
  for (let i = 1; i < layers.length; i++) {
    layers[layers.length-i].style.transform = `translateY(${(i*0.1) * y}px)`;
  }
}

window.addEventListener('scroll',parallax,false);

var slideIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  x[slideIndex-1].style.display = "block";
  setTimeout(carousel, 2000); // Change image every 2 seconds
}