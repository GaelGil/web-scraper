//keykhpXeAOAcG9gOT -airtable API key

const JTOWN_URL = "https://api.airtable.com/v0/applqq6DytTPfdzNL/Japantown%20Plaza";
const KEY_QUERY = "api_key=keykhpXeAOAcG9gOT";
const SUMMARY_QUERY = "fields%5B%5D=name&fields%5B%5D=photos&fields%5B%5D=description&fields%5B%5D=address&fields%5B%5D=food";

function fetchName() {
  let dogResultElement = document.getElementById("doggo-container");
  
  fetch(`${JTOWN_URL}?${KEY_QUERY}&${SUMMARY_QUERY}`)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is an object w/ .records array

      dogResultElement.innerHTML = ""; // clear places

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let photos = data.records[i].fields["photos"];
        let name = data.records[i].fields["name"];
        let placeAddress = data.records[i].fields["address"];
      
        
        
        newHtml += `
        <div class="col-4 jtown-card">
            <div class="card">
               ${photos ? `<img src="${photos[0].url}">` : ``}
              <div class="card-body">
              <h5 class="card-title">${name}</h5>
              <h6 class="card-title">${placeAddress}</h6>
              <a class="btn btn-primary" 
                href="index.html?id=${data.records[i].id}"
                target="_blank">Description</a>
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

  fetch(`${JTOWN_URL}/${dogId}?${KEY_QUERY}`)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is a single object

      let dogPic = data.fields["Picture URL"];
      let dogName = data.fields["name"];
      let dogDescription = data.fields["Description"];
    let description = data.fields["description"];
    let photos = data.fields["food"];
 
      let colorsHtml = "";
      if ("name" in data.fields) {
        colorsHtml += "<ul>";
        let dogColors = data.fields["name"].split(", ");
        for (let i = 0; i < dogName.length; i++) {
          colorsHtml += `<li>${dogColors[i]}</li>`;
        }
        colorsHtml += "</ul>";
      }

      let newHtml = `
        <div class="col-4 wholeCard">
          <div class="newCard">
            <h4 class="card-title">${name}</h4>
            ${name}
            <h5>Description</h5>
            <p>${description}</p>
          </div>
        </div>
        <div class="col-7 picCard" >
          ${photos ? `<img src="${photos[0].url}">` : ``}
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


let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id?", "OUR ID"]
  fetchSingleDog(idParams[1]); // create detail view HTML w/ our id
} else {
  fetchName(); // no id given, fetch summaries
}
