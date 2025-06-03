"use strict";

// function for our list view
async function getAllRecords() {
  let getResultElement = document.getElementById("strat");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patx0vreaSL7ZeM0P.20303e2cd658eac81e83001ff56195067e9a5ed58ab4a7b004a0f9f7c731af9a`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/apprtPOXLY4tAWnbK/strat`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      getResultElement.innerHTML = ""; // clear brews

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let image = data.records[i].fields["Image"]; // here we are getting column values
        let name = data.records[i].fields["Name"];
        

        newHtml += `
       <div class="mx-auto">
      <p class="text-center" id="strategyname">${name}</p>
      <a href="index.html?id=${
            data.records[i].id
          }">
      ${image ? `<img id="str" class="mx-auto" src="${image[0].url}">` : ``}</a>
</div>
    
        `;
      }

      getResultElement.innerHTML = newHtml;
    });
}



// function for our detail view
async function getOneRecord(id) {
  let jobsResultElement = document.getElementById("strat");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patx0vreaSL7ZeM0P.20303e2cd658eac81e83001ff56195067e9a5ed58ab4a7b004a0f9f7c731af9a`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/apprtPOXLY4tAWnbK/strat/${id}`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is a single object

      let image = data.fields["Image"];
      let name = data.fields["Name"];
      let prosAndCons = data.fields["prosandcons"];
      let desc = data.fields["description"];
      let link = data.fields["link"];
      let mentor = data.fields["mentor"];
     
      let newHtml = `
     
    


     
     <div id="cards" class="card mb-3" style="max-width: 900px; height: 500px;">
  <div class="row g-0">
    <div class="col-md-4">
      ${image ? `<img id="str" class="mx-auto" src="${image[0].url}">` : ``}
    </div>
    <div class="col-md-6">
      <div class="card-body ">
        <h5 id="titlecard" class="card-title">${name}</h5>
        <p id="desccard" class="card-text">${desc}</p>
        <p id="prosandcons" class="card-text">${prosAndCons}</p>
         <p id="mentorname" class="card-text">${mentor}</p>
         <a id="moreinfolink" href="${link} class="card-text">more info</a>
      </div>
    </div>
  </div>
</div>
     
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