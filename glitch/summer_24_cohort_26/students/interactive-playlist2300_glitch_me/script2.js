"use strict";

// function for our list view
async function getAllRecords() {
  let getResultElement = document.getElementById("music");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patpSjqWHaVdpBN3e.20043c39be44d7de229d635335848ae200a4c13f3bf105105e7e691ca8ed8e40`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/appkKsrQMRSVa49cJ/Artist`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      getResultElement.innerHTML = ""; // clear brews

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let logo = data.records[i].fields["Artist"];
        let cover = data.records[i].fields["Cover"];// here we are getting column values
        

        newHtml += `
         
         <div class="carousel-item">
      ${cover ? `<img class="covers" src="${cover[0].url}">` : ``}
    </div>
    
  
        `;
      }

      getResultElement.innerHTML = newHtml;
    });
}



// function for our detail view
async function getOneRecord(id) {
  let jobsResultElement = document.getElementById("music");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patpSjqWHaVdpBN3e.20043c39be44d7de229d635335848ae200a4c13f3bf105105e7e691ca8ed8e40`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/appkKsrQMRSVa49cJ/Artist/${id}`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is a single object

      // let logo = data.fields["Artist"];
      let cover = data.fields["Cover"];
      // let song = data.fields["Song"];
      // let zip = data.fields["Zip"];
      // let neighborhood = data.fields["Neighborhood"];
     

      let newHtml = `
         
   
    <div class="carousel-item">
      ${cover ? `<img src="${cover[0].url}">` : ``}
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>

      `;

      jobsResultElement.innerHTML = newHtml;
    });
}
 // function to filter records by neighborhood
function searchFunction() {
  let input, filter, cardimagetext, i, x; // declare all four at once

  input = document.getElementById("myinput");
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
// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into an array
// ["?id=", "receHhOzntTGZ44I5"] and then we only choose the second one
let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // call function to hide search bar
 
  // has at least ["?id=", "OUR ID"]
  getOneRecord(idParams[1]); // create detail view HTML w/ our id
} else {
  // Call listener function to hide search bar for mobile devices

  getAllRecords(); // no id given, fetch summaries
}