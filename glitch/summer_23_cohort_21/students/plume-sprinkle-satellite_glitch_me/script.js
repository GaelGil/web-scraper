document.addEventListener("DOMContentLoaded", function () {
  const startButton = document.getElementById("start-button");
  const startMenu = document.getElementById("start-menu-content");
  const taskbarIcons = document.querySelectorAll(".taskbar-icon");
  const desktopIcons = document.querySelectorAll(".desktop-icon");

  const backgroundIcon = document.getElementById("background-icon");
  const goalsIcon = document.getElementById("goals-icon");
  const linkedinIcon = document.getElementById("linkedin-icon");

  startButton.addEventListener("click", function () {
    startMenu.style.display =
      startMenu.style.display === "none" ? "block" : "none";
  });

  // Event listener for Background icon
  backgroundIcon.addEventListener("click", function () {
    window.open("path_to_background_page.html", "_blank");
  });

  // Event listener for Goals icon
  goalsIcon.addEventListener("click", function () {
    window.open("path_to_goals_page.html", "_blank");
  });

  // Event listener for LinkedIn icon
  linkedinIcon.addEventListener("click", function () {
    window.open("https://www.linkedin.com/in/fshaikh2/");
  });

  taskbarIcons.forEach(function (icon) {
    icon.addEventListener("click", function () {
      taskbarIcons.forEach(function (item) {
        item.classList.remove("active");
      });
      icon.classList.add("active");
    });
  });

  desktopIcons.forEach(function (icon) {
    icon.addEventListener("click", function () {
      desktopIcons.forEach(function (item) {
        item.classList.remove("active");
      });
      icon.classList.add("active");
    });
  });

  const draggableIcons = document.querySelectorAll(".draggable");

  draggableIcons.forEach(function (icon) {
    icon.addEventListener("mousedown", function (event) {
      const startX = event.clientX;
      const startY = event.clientY;
      const startLeft = icon.offsetLeft;
      const startTop = icon.offsetTop;

      function handleDrag(event) {
        const newLeft = startLeft + event.clientX - startX;
        const newTop = startTop + event.clientY - startY;

        icon.style.left = newLeft + "px";
        icon.style.top = newTop + "px";
      }

      function handleRelease() {
        document.removeEventListener("mousemove", handleDrag);
        document.removeEventListener("mouseup", handleRelease);
      }

      document.addEventListener("mousemove", handleDrag);
      document.addEventListener("mouseup", handleRelease);
    });
  });
});

console.log("Hello, world!");
