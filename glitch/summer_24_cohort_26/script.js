/*
  This is your site JavaScript code - you can add interactivity!
*/

// Print a message in the browser's dev tools console each time the page loads
// Use your menus or right-click / control-click and choose "Inspect" > "Console"
"use strict";
console.log("Hello 🌎");
/* 
Make the "Click me!" button move when the visitor clicks it:
- First add the button to the page by following the steps in the TODO 🚧
*/
const btn = document.querySelector("button"); // Get the button from the page
if (btn) { // Detect clicks on the button
  btn.onclick = function () {
    // The 'dipped' class in style.css changes the appearance on click
    btn.classList.toggle("dipped");
  };
}


// ----- GLITCH STARTER PROJECT HELPER CODE -----

// Open file when the link in the preview is clicked
let goto = (file, line) => {
  window.parent.postMessage(
    { type: "glitch/go-to-line", payload: { filePath: file, line: line } }, "*"
  );
};
// Get the file opening button from its class name
const filer = document.querySelectorAll(".fileopener");
filer.forEach((f) => {
  f.onclick = () => { goto(f.dataset.file, f.dataset.line); };
});

// link airtable api key  
async function getStudentRecords() {
  let getResultElement = document.getElementById("students");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patwCaJB5U3UbCl4N.cd05b6274b622fe904c97b8abdf06b778391696b327e23829e3c9f8a212c52a2`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/apprpZZbeRQLi4EZ6/Directory`,
    options
  )
.then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      getResultElement.innerHTML = ""; // clear student

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let name = data.records[i].fields["Name"]; // here we are getting column values
        let project = data.records[i].fields["Project"];
        let text = data.records[i].fields["Text"];
        let picture = data.records[i].fields["Picture"];
        
        newHtml += `
        
      <div class="col-xl-4 cardImageText">
        <div class="flip-card card rounded">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              ${picture ? `<img class="hshot rounded" src="${picture[0].url}" alt="Avatar">` : `<div style="width:300px;height:300px;background-color:#ccc;"></div>`}

            </div>
            <div class="flip-card-back desc">
              <h1 class="bio">${name}</h1>
              <p class="bio">${text}</p>
              <a href="${project}" target="_blank"><button type="button" class="btn btn-light">Project</button></a>
            </div>
          </div>
        </div>
      </div>
        `;
      }

      getResultElement.innerHTML = newHtml;
    });
}



function searchFunction() {
  let input, filter, cardimagetext, i, x; // declare all four at once

  input = document.getElementById("searchBar");
  filter = input.value.toUpperCase(); // ignore case/capitalization
  cardimagetext = document.getElementsByClassName("cardImageText");

  for (x = 0; x < cardimagetext.length; x++) {
    i = cardimagetext[x].getElementsByClassName("card-key")[0];
    if (i.innerHTML.toUpperCase().indexOf(filter) > -1) {
      cardimagetext[x].style.display = ""; // '' means show
    } else {
      cardimagetext[x].style.display = "none";
    }
  }
}

getStudentRecords();
