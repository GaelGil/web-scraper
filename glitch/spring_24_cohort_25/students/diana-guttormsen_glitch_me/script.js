


const button = document.getElementById("button"),
      svg = document.getElementById("svg");

let count = 0;

const fill = "rgb(249, 24, 128)";

const t1 = 'gsap'.timeline({ repeat: 1, yoyo: true }),
      t2 = 'gsap'.timeline(),
      main = 'gsap'.timeline();

const ease = "elastic.out(1, 0.4)";

t1.to(["#heart", "#heart-filled"], 0.5, { morphSVG: "#x", ease })  
  .to("#svg", 0.5, { scale: 1.25, ease }, "<");

t2.to("#heart", 0.25, { fill })
  .to("#heart-filled", 0.25, { opacity: 1 }, "<");

main.add(t1);
main.add(t2, "<85%");
main.pause();

$(document).ready(function(){
  var animTime = 300,
      clickPolice = false;
  
  $(document).on('touchstart click', '.acc-btn', function(){
    if(!clickPolice){
       clickPolice = true;
      
      var currIndex = $(this).index('.acc-btn'),
          targetHeight = $('.acc-content-inner').eq(currIndex).outerHeight();
   
      $('.acc-btn h1').removeClass('selected');
      $(this).find('h1').addClass('selected');
      
      $('.acc-content').stop().animate({ height: 0 }, animTime);
      $('.acc-content').eq(currIndex).stop().animate({ height: targetHeight }, animTime);

      setTimeout(function(){ clickPolice = false; }, animTime);
    }
    
  });
  
});