const RESTAURANTS_URL =
  "https://api.airtable.com/v0/appuowFe3eShTFR2a/Restaurants";
const KEY_QUERY = "api_key=keyt2LT37669Y577t";
const SUMMARY_QUERY =
  "fields%5B%5D=Name&fields%5B%5D=Pictures&fields%5B%5D=Address&fields%5B%5D=Cuisine&fields%5B%5D=Rating&fields%5B%5D=Hours&fields%5B%5D=Service";

function fetchRestaurants() {
  let restaurantsResultElement = document.getElementById(
    "restaurants-container"
  );

  fetch(`${RESTAURANTS_URL}?${KEY_QUERY}&${SUMMARY_QUERY}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      restaurantsResultElement.innerHTML = ""; // clear dogs

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let restaurantsPic = data.records[i].fields["Pictures"];
        let restaurantsName = data.records[i].fields["Name"];
        let restaurantsAddress = data.records[i].fields["Address"];
        let restaurantsCuisine = data.records[i].fields["Cuisine"];
        let restaurantsRating = data.records[i].fields["Rating"];

        newHtml += `
          <div class="col-4 restaurants-card">
            <div class="card">
              ${restaurantsPic ? `<img src="${restaurantsPic[0].url}">` : ``}
              <div class="card-body">
              <h10 class="card-title">${restaurantsCuisine}</h10>
              <h5 class="card-title name">${restaurantsName}</h5>
              <h6 class="card-title">${restaurantsAddress}</h6>
              <a class="btn btn-primary" 
                href="index.html?id=${data.records[i].id}"
                target="_blank">Restaurant Details</a>
            </div>
            </div>
          </div>
        `;
      }

      restaurantsResultElement.innerHTML = newHtml;
    });
}

function fetchSingleRestaurant(restaurantId) {
  let restaurantResultElement = document.getElementById(
    "restaurants-container"
  );

  fetch(`${RESTAURANTS_URL}/${restaurantId}?${KEY_QUERY}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is a single object

      let restaurantPic = data.fields["Pictures"];
      let restaurantName = data.fields["Name"];
      let restaurantCuisine = data.fields["Cuisine"];
      let restaurantWebsite = data.fields["Website"];
      let restaurantNumber = data.fields["Number"];
      let restaurantHours = data.fields["Hours"];
      let restaurantService = data.fields["Service"];

      let newHtml = `
        <div class="card" id="detail-card">
          <div class="row align-items-center">
            <div class="col">
             ${restaurantPic ? `<img src="${restaurantPic[0].url}">` : ``}
            </div>
            <div class="col">
              <h4 class="card-title">${restaurantName}</h4>
              <h5>Cuisine</h5>
              <p>${restaurantCuisine}</p>
              <h5>Service</h5>
              <p>${restaurantService}</p>
              <h5>Website</h5>
              <p>${restaurantWebsite}</p>
              <h5>Number</h5>
              <p>${restaurantNumber}</p>
              <h5>Hours</h5>
              <p>${restaurantHours}</p>
            </div>
          </div>
        </div>
      `;

      restaurantResultElement.innerHTML = newHtml;
    });
}

function filterRestaurants() {
  let input, restaurantsFilter, restaurantsCard, i, x; // declare all four at once

  input = document.getElementById("search");
  restaurantsFilter = input.value.toUpperCase(); // ignore case/capitalization
  restaurantsCard = document.getElementsByClassName("restaurants-card");

  for (x = 0; x < restaurantsCard.length; x++) {
    i = restaurantsCard[x].getElementsByClassName("name")[0];
    if (i.innerHTML.toUpperCase().indexOf(restaurantsFilter) > -1) {
      restaurantsCard[x].style.display = ""; // '' means show
    } else {
      restaurantsCard[x].style.display = "none";
    }
  }
}

// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into am array
// ["id?=", "receHhOzntTGZ44I5"] and then we only choose the second one
let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id?", "OUR ID"]
  fetchSingleRestaurant(idParams[1]); // create detail view HTML w/ our id
} else {
  fetchRestaurants(); // no id given, fetch summaries
}
