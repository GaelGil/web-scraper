const fillerRef = document.getElementById("filler-box");
const aboutMeRef = document.getElementById("about-me");
const originalTransitionDuration = fillerRef.style.transitionDuration;
const TRANSITION_DURATION = '500ms';

let originalHeight = fillerRef.offsetHeight;
let windowHeight = window.innerHeight;
let currentSlideHeight = fillerRef.offsetHeight;

const maxHeightScrollTo = 100;

// For Touchscreen
let startY = 0;



// Set To Top To Prevent Locking user on Page
window.scrollTo(0,0);
document.body.style.overflowY = 'hidden';
document.body.style.overflowX = "hidden";

// Keep Offset Proper When Resizing
window.addEventListener("resize", () => {
  console.log("resize");
  windowHeight = window.innerHeight;
  originalHeight = window.innerHeight;
});
// Detect MouseScrolling Direction
window.addEventListener("wheel", (event) => {
  if (event.deltaY > 0) {
    handleScroll(event, 'down');
  } else if (event.deltaY < 0) {
    handleScroll(event, 'up');
  }
});

// TouchScreen Detection Scrolling
window.addEventListener("touchstart", (event) => {
   startY = event.touches[0].clientY;
});

window.addEventListener("touchmove", (event) => {
 const currentY = event.touches[0].clientY; // Get the current touch position
      if (currentY > startY) {
        handleScroll(event, "up")
      } else if (currentY < startY) {
        handleScroll(event, "down")
      }
});

window.addEventListener("keydown", () => {
  if (event.key === 'ArrowUp') {
    handleScroll(event, "up");
  } else if (event.key === 'ArrowDown') {
    handleScroll(event, "down");
  }
})

// Update Current Slide when programatically sliding
window.addEventListener("scroll", () => {
  currentSlideHeight = fillerRef.offsetHeight;
  console.log(currentSlideHeight);
});
// Detect Div Handles
const aboutButtonRef = document.getElementById("about-button");
const skillsButtonRef = document.getElementById("skills-button");
const projectsButtonRef = document.getElementById("projects-button");
const contactButtonRef = document.getElementById("contact-button");
const resumeButtonRef = document.getElementById("resume-button");

aboutButtonRef.addEventListener("click", (e) => {
  const aboutMeRef = document.getElementById("about-me");
  fillerRef.style.transitionDuration = TRANSITION_DURATION;
  fillerRef.style.height = originalHeight + 'px';

  currentSlideHeight = originalHeight;

  scroll(aboutMeRef.offsetTop);
  
  fillerRef.style.transitionDuration = originalTransitionDuration;
});
skillsButtonRef.addEventListener("click", (e) => {
  const skillsRef = document.getElementById("skills");
  fillerRef.style.transitionDuration = TRANSITION_DURATION;
  fillerRef.style.height = maxHeightScrollTo + 'px';
  currentSlideHeight = maxHeightScrollTo;
  scroll(skillsRef.offsetTop);
  fillerRef.style.transitionDuration = originalTransitionDuration;
});
projectsButtonRef.addEventListener("click", (e) => {
  const projectsRef = document.getElementById("projects");
  fillerRef.style.transitionDuration = TRANSITION_DURATION;
  fillerRef.style.height = maxHeightScrollTo + 'px';
  currentSlideHeight = maxHeightScrollTo;
  
  scroll(projectsRef.offsetTop);
  fillerRef.style.transitionDuration = originalTransitionDuration;
});
contactButtonRef.addEventListener("click", (e) => {
  const contactRef = document.getElementById("contact");
  
  fillerRef.style.transitionDuration = TRANSITION_DURATION;
  fillerRef.style.height = maxHeightScrollTo + 'px';
  currentSlideHeight = maxHeightScrollTo;
  scroll(contactRef.offsetTop);
  fillerRef.style.transitionDuration = originalTransitionDuration;
});

// Opens Resume in Different Tab
resumeButtonRef.addEventListener("click", (e) => {
  window.open("https://cdn.glitch.global/240f1a21-7c66-4f90-8ed9-df90e242c06c/Simon_Resume.pdf?v=1729060269889", '_blank');
});

function clamp01(x) {
  if (x > 1)
    return 1;
  else if (x < 0)
    return 0;

  return x;
}

function handleScroll(e, direction) {
  const fillerDivHeight = fillerRef.offsetHeight; 
  const currentHeight = window.scrollY;
  

  adjustFadeBasedOnHeight();
  // Scaling Down About Me Section
  
  //   Heading Down
  if (direction === "down" && fillerDivHeight > maxHeightScrollTo) {
    fillerRef.style.height = (fillerDivHeight - (windowHeight/10)) + 'px';
  }
  // Heading Up
  else if (direction === "up" && fillerDivHeight < originalHeight && currentHeight < maxHeightScrollTo) {
    fillerRef.style.height = (fillerDivHeight + (windowHeight/10)) + 'px';
  }
  
  currentSlideHeight = fillerRef.offsetHeight;
}

function scroll(YPosition) {
  window.scrollTo(0, YPosition);
  adjustFadeBasedOnHeight();
}

function adjustFadeBasedOnHeight() {
  const fillerDivHeight = fillerRef.offsetHeight; 
    // Background 
  const percentFade = clamp01((currentSlideHeight+maxHeightScrollTo+50) / (originalHeight)); 
  
  console.log((maxHeightScrollTo / currentSlideHeight));
  aboutMeRef.style.transform = `scale(${percentFade})`;
  aboutMeRef.style.opacity = `${percentFade}`;
  // Scrolling main content over about me
  if (fillerDivHeight <= maxHeightScrollTo + 50){
    document.body.style.overflowY = 'scroll';
  } else if(fillerDivHeight >= originalHeight) {
    document.body.style.overflowY = 'hidden';
  }    

  
}