"use strict";
// link to airtable
const BREEDS_URL = "https://api.airtable.com/v0/appxRkskcvYqVZw7B/Reviews";
// api key
const KEY_QUERY = "api_key=keyhp4WPZbqrXjv8s";
// fields
const SUMMARY_QUERY =
  "fields%5B%5D=Name&fields%5B%5D=Rating&fields%5B%5D=Feedback&fields%5B%5D=Created";

// created a function to add stars according to given rating
function stars(rating) {
  if (rating === 1) {
    return "⭐";
  } else if (rating === 2) {
    return "⭐⭐";
  } else if (rating === 3) {
    return "⭐⭐⭐";
  } else if (rating === 4) {
    return "⭐⭐⭐⭐";
  } else if (rating === 5) {
    return "⭐⭐⭐⭐⭐";
  }
}

function fetchDogs() {
  let dogResultElement = document.getElementById("reviews-container");

  fetch(`${BREEDS_URL}?${KEY_QUERY}&${SUMMARY_QUERY}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      dogResultElement.innerHTML = ""; // clear dogs

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let rating = data.records[i].fields["Rating"];
        let name = data.records[i].fields["Name"];
        let comment = data.records[i].fields["Feedback"];
        let dateObj = new Date(data.records[i].fields["Created"]);
        let created = dateObj.toDateString();
        newHtml += `
          <div class="list-group">
  <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1"></h5>
    </div>
    <p class="mb-1">Rating: ${stars(rating)}</p>
    <p><medium>Name: ${name}</medium></p>
    <small>Comment: ${comment}</small>
    <p><small class = "create">Review Created: ${created}</small></p>
  </a>
  </div>
        `;
      }

      dogResultElement.innerHTML = newHtml;
    });
}


let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
 
} else {
  fetchDogs(); 
}


