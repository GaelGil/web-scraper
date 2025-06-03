"use strict";

async function fetchStoreInfo() {
  let storeInfoResult = document.getElementById("card-container"); //Div to put the cards in 

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patqR1FZX0fwt1XOx.0d21207428c3d941ef820561ac8ec3e85df6ea73c3e02b99e2fa1f5db517f4bb`,
    },
  };

  const summary =
    "fields%5B%5D=nameOfStore&fields%5B%5D=frontOfStore&fields%5B%5D=city"; //spesific fields for card view

  await fetch(
    `https://api.airtable.com/v0/appHBW4OWD4DfQ5Xz/Stores?&${summary}`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      storeInfoResult.innerHTML = ""; 

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {          //forloop that places simple view cards
        let storeName = data.records[i].fields["nameOfStore"];
        let storeFront = data.records[i].fields["frontOfStore"];
        let storeArea = data.records[i].fields["city"];

        newHtml += `
          <div class="col-xl-4 storeCards d-flex justify-content-center">
            <div class="card">
              ${
                storeFront
                  ? `<img class="cardImage" src="${storeFront[0].url}">`
                  : ``
              }
              <div class="card-body">
              <h4 class="card-title generalText">${storeName}</h4>
               <h5 class="generalText">${storeArea}</h5> 
              <a class="btn btn-primary generalText" 
                href="index.html?id=${data.records[i].id}"
                >View More</a>
            </div>
            </div>
          </div>
        `;
      }

      storeInfoResult.innerHTML = newHtml;
    });
}

//detail page
async function fetchOneStoreInfo(jobsId) {
  let storeInfoResult = document.getElementById("card-container"); //Div to put the cards in PUTTHEMIN
  let newHtml = "";
  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patqR1FZX0fwt1XOx.0d21207428c3d941ef820561ac8ec3e85df6ea73c3e02b99e2fa1f5db517f4bb`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/appHBW4OWD4DfQ5Xz/Stores/${jobsId}`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is a single object
      let storeImg = data.fields["frontOfStore"];
      let storeName = data.fields["nameOfStore"];
      let website = data.fields["website"];
      let phoneNum = data.fields["phoneNumber"];
      let eventCal = data.fields["EventCallender"];
      let address = data.fields["Adress"];
      let city = data.fields["city"];
      let draft = data.fields["Draft"];
      let sellSingles = data.fields["sellSingles"];
      let buySingles = data.fields["buySingles"];
      let opentables = data.fields["openTables"];

      newHtml = `  <div class="container detailView my-5">
      <div class="card row flex-row">
        <img
          class="col-lg-4 card-img-start img-fluid p-0"
          src="${storeImg[0].url}"
        />
        <div class="col-lg-8 card-body">
          <h1 class="card-title">${storeName}</h1>
          <p class="card-text">${city}<br />${address}</p>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">${phoneNum}</li>
            <li class="list-group-item">Regular Drafts? | ${draft}</li>
            <li class="list-group-item">Buys singles? | ${buySingles}</li>
            <li class="list-group-item">Sells singles? | ${sellSingles}</li>
            <li class="list-group-item">Open Tables? | ${opentables}</li>
            
          </ul>
          <div class="card-body">
          <p>Website:</p>
            <a href="#" class="card-link">${website}</a>
            <p>Event Cal:</p>
            <a href="#" class="card-link">${eventCal}</a>
          </div>
        </div>
      </div>
      <div class="back">
        <p><a href="index.html" class="btn btn-primary">Back</a></p>
      </div>
    </div> `;
    });

  storeInfoResult.innerHTML = newHtml;
}



let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id=", "OUR ID"]
  fetchOneStoreInfo(idParams[1]); // create detail view HTML w/ our id
} else {
  fetchStoreInfo(); // no id given, fetch summaries
}

// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the back to top button
window.onscroll = function () {
  scrollFunction();
};
//function that tracks how far scrolled for back to top button
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
