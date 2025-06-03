"use strict"

const BREEDS_URL = "https://api.airtable.com/v0/appiaaA19TrhMmrhm/All%20restaurants";
const KEY_QUERY = "api_key=keykad7N6XADbHjKX";
const SUMMARY_QUERY = "fields%5B%5D=Name&fields%5B%5D=Hours&fields%5B%5D=Address&fields%5B%5D=Dishes&fields%5B%5D=Reviews&fields%5B%5D=Prices&fields%5B%5D=Phonenumber";

function fetchDogs() {
  let dogResultElement = document.getElementById("doggo-container");
  
  fetch(`${BREEDS_URL}?${KEY_QUERY}&${SUMMARY_QUERY}`)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is an object w/ .records array

      dogResultElement.innerHTML = ""; // clear dogs

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let Name = data.records[i].fields["Name"];
        let Hours = data.records[i].fields["Hours"];
        let Address = data.records[i].fields["Address"];
        let Dishes = data.records[i].fields["Dishes"];
        let Reviews = data.records[i].fields["Reviews"];
        let Prices = data.records[i].fields["Prices"];
        let Phonenumber = data.records[i].fields["Phonenumber"];
        let dishname = data.records[i].fields["dishname"];
        
        
        newHtml += `
          <div class="col-xl-4 doggo-card d-flex justify-content-center">
            <div class="card">
            ${Dishes ? `<img src="${Dishes[0].url}">` : ``}
              <div class="card-body">
              <h5 class="card-title">${Name}</h5>
              <p>${Prices}</p>
              <a class="btn btn-primary" 
                href="index.html?id=${data.records[i].id}"
                target="_blank">Details</a>
            </div>
            </div>
          </div>
        `;
      }

      dogResultElement.innerHTML = newHtml;
    });
}

function fetchSingleDog(dogId) {
  let dogResultElement = document.getElementById("doggo-container");

  fetch(`${BREEDS_URL}/${dogId}?${KEY_QUERY}`)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is a single object

      let Name = data.fields["Name"];
      let Dishes = data.fields["Dishes"];
      let Hours = data.fields["Hours"];
      let Address = data.fields["Address"];
      let Prices = data.fields["Prices"];
      let Phonenumber = data.fields["Phonenumber"];
      let dishname = data.fields["dishname"];
      let Description = data.fields["Description"];
      let Directions = data.fields["Directions"];
    
      let colorsHtml = "";
      if ("Colors" in data.fields) {
        colorsHtml += "<ul>";
        let dogColors = data.fields["Colors"].split(", ");
        for (let i = 0; i < dogColors.length; i++) {
          colorsHtml += `<li>${dogColors[i]}</li>`;
        }
        colorsHtml += "</ul>";
      }

      let newHtml = `
      
      <div class="row">
  <div class="column 1">
    <h2 id="Detailtitle">${Name}</h2>
    <p>${Dishes ? `<img id="Detailviewimg" src="${Dishes[0].url}">` : ``}</p>
  <h5 id="Description">${Description}</h5>
  </div>
  
  
  <div class="column 2">
    <h1 id="Hoursbanner">Hours</h>
    <h5 id="Detailviewhrs">${Hours}</h5>
  <br>
  <br>
  <br>
  <br>
  <h1 id="Locationbanner">Location</h>
  <h5 id="Detailvieaddress" href="https://goo.gl/maps/s1yGmdqFVC8beYjL6">${Address}</h5>
  <h1 id="Contactbanner">Contact</h>
 <h5 id="Detailcontact">${Phonenumber}</h5>
</div>
</div>
        

  
      `;

      dogResultElement.innerHTML = newHtml;
    });
}

function filterDoggos() {
  let input, doggoFilter, doggoCard, i, x; // declare all four at once

  input = document.getElementById("search");
  doggoFilter = input.value.toUpperCase(); // ignore case/capitalization
  doggoCard = document.getElementsByClassName("doggo-card");

  for (x = 0; x < doggoCard.length; x++) {
    i = doggoCard[x].getElementsByClassName("card-title")[0];
    if (i.innerHTML.toUpperCase().indexOf(doggoFilter) > -1) {
      doggoCard[x].style.display = ""; // '' means show
    } else {
      doggoCard[x].style.display = "none";
    }
  }
}

// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into am array
// ["?id=", "receHhOzntTGZ44I5"] and then we only choose the second one
let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id=", "OUR ID"]
  fetchSingleDog(idParams[1]); // create detail view HTML w/ our id
} else {
  fetchDogs(); // no id given, fetch summaries
}

/**
           _.="""=._
         /`  \   /  `\
        /  / _} {_ \  \
       /  ; /o) (o\ ;  \
       \  |  / _ \  |  /
        \_/\| (_) |/\_/
          /`\_/=\_/`\
        /`    `"`    `\
       {               }
*/

