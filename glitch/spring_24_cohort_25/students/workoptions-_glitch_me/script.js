const openNav = () => {
  document.getElementsByTagName("body")[0].classList.add("modal-open");
document.getElementById("theNav").style.height = "100%";}

const closeNav = () => {
  document.getElementsByTagName("body")[0].classList.remove("modal-open");
  document.getElementById("theNav").style.height = "0%";}

//AIR TABLE//
"use strict";

// function for our list view
async function getAllRecords() {
  let getResultElement = document.getElementById("CafeName");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer patL5GA4js0K0w5wX.99081ff52ae77a70bd2f4c90dc667f54df7d55eb2d69ca88296b2c2b8241c932`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/appZI39habaM1AkL4/Cafe%20Recccs`,
    options
  )

    .then((response) => response.json())
    .then((data) => {
      console.log(data); 
   getResultElement.innerHTML = ""; // clear student

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let location = data.records[i].fields["Location"]; // here we are getting column values
        let name = data.records[i].fields["Name"];
        
        newHtml += `
        
         <p>${location}</p>
         <p>${name}</p>
        
        `;
      }
getResultElement.innerHTML = newHtml;
    });
}

//adds a comma after the 3rd digit from the left
function toCommas(value) {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// changes the comma in the string into a list item <li>
function formattedString(value) {
  return value.split(",").join("<li>");
}



 


// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into an array
// ["?id=", "receHhOzntTGZ44I5"] and then we only choose the second one
let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["?id=", "OUR ID"]
  getOneRecord(idParams[1]); // create detail view HTML w/ our id
} else {
  getAllRecords(); // no id given, fetch summaries
}

