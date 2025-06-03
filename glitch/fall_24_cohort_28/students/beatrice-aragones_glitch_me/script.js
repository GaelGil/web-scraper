function toggleDarkMode() {
    var element = document.body;
    var modeIcon = document.getElementById("modeIcon").querySelector("i");
    var headshot = document.getElementById("beatrice-headshot");

    element.classList.toggle("dark-mode");

    if (element.classList.contains("dark-mode")) {
        modeIcon.classList.remove("fa-moon");
        modeIcon.classList.add("fa-sun");

        headshot.src = "https://cdn.glitch.global/ce29cf64-aa3b-447a-b634-d3a4c1562c3e/beatrice-dark-headshot.jpg?v=1728963181514";
    } else {
        modeIcon.classList.remove("fa-sun");
        modeIcon.classList.add("fa-moon");

        headshot.src = "https://cdn.glitch.global/ce29cf64-aa3b-447a-b634-d3a4c1562c3e/beatrice-light-headshot.jpeg?v=1728461065045";
    }
}