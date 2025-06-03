/* If you're feeling fancy you can add interactivity 
    to your site with Javascript */
"use strict";
const GYMS_URL = "https://api.airtable.com/v0/appbYD3onOD9u7MSK/boxingInfo";
const KEY_QUERY = "api_key=keyqbPt30v6cm5XKB";
const SUMMARY_QUERY = "fields%5B%5D=name&fields%5B%5D=image";

function fetchBoxingInfo() {
  let ResultElement = document.getElementById("info-container");

  fetch(`${GYMS_URL}?${KEY_QUERY}&${SUMMARY_QUERY}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      ResultElement.innerHTML = ""; // clear dogs

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let gymPic = data.records[i].fields["image"];
        let gymName = data.records[i].fields["name"];

        newHtml += `
        
          <div class="col-4 gym-card">
            <div class=" card card-img-top card-body">
               ${gymPic ? `<img class="card-img-top img-fluid" src="${gymPic[0].url}">` : ``}
              <div class="card-body">
              <h5 class="card-title"><b>${gymName}</b></h5>
              <!-- HTML !-->
              <a href="index.html?id=${data.records[i].id}">
              <button class="button-82-pushable button-fluid" role="button">
              <span class="button-82-shadow"></span>
              <span class="button-82-edge"></span>
              <span class="button-82-front text">Gym Details</span>
              </button></a>
              
            </div>
            </div>
          </div>
        `;
      }

      ResultElement.innerHTML = newHtml;
    });
}

function fetchSingleGym(gymId) {
  let gymResultElement = document.getElementById("info-container");

  fetch(`${GYMS_URL}/${gymId}?${KEY_QUERY}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is a single object

      let gymPic = data.fields["image"];
      let gymName = data.fields["name"];
      let gymDescription = data.fields["description"];
      let gymAddy = data.fields["location"];
      let gymNum = data.fields["number"];

      let colorsHtml = "";
      if ("Hours" in data.fields) {
        colorsHtml += "<ul>";
        let gymHours = data.fields["Hours"].split(", ");
        for (let i = 0; i < gymHours.length; i++) {
          colorsHtml += `<li>${gymHours[i]}</li>`;
        }
        colorsHtml += "</ul>";
      }

      let newHtml = `
      <div class="cardDes mb-3" style="max-width: 2000px;">
  <div class="row g-0">
    <div class="col-md-4">
      ${gymPic ? `<img class="img-fluid" src="${gymPic[0].url}">` : ``}
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h4 class="card-title"><u><b>${gymName}</b></u></h4>
        <p class="card-text">${gymDescription}</p>
        <h5 class="card-title"><u><b>HOURS/LOCATION/CONTACT </b></u></h5>${colorsHtml}
        <li>${gymAddy}</li></a>
        <li>${gymNum} </li>
      </div>
    </div>
  </div>
</div`;

      gymResultElement.innerHTML = newHtml;
    });
}

let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id?", "OUR ID"]
  fetchSingleGym(idParams[1]); // create detail view HTML w/ our id
} else {
  fetchBoxingInfo(); // no id given, fetch summaries
}
