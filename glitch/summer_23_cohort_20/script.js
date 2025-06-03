"use strict";

const fetchPeople = async () => {
  // This is the function to get the list of people
  let getResultElement = document.getElementById("person-card");

  const options = {
    method: "GET",
    headers: {
      Authorization:
        "Bearer patZ4NnYJhygrXxkj.7c2f66794f7c8c6c194768f2c61019735a2a500c1bef241a2960f582e7fe8c32", // TODO: BACKEND Fill in with PAT
    },
  };

  const params = "?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc";
  let data = {};

  try {
    const response = await fetch(
      `https://api.airtable.com/v0/appOVo3a1nsgzxQvv/Trainees${params}`,
      options
    ); // TODO: BACKEND Fill in with AirTable URL
    data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }

  let newHTML = "",
    image = "",
    name = "",
    title = "",
    url = "",
    description = "";

  data.records.map((record) => {
    //forloop that fetches info from airtable
    if (record.fields.Image == undefined) {
      image =
        "https://i0.wp.com/theperfectroundgolf.com/wp-content/uploads/2022/04/placeholder.png?fit=1200%2C800&ssl=1";
    } else {
      image = record.fields.Image[0].thumbnails.large.url;
    }
    name = record.fields.Name;
    title = record.fields.Title;
    description = record.fields.Description;
    url = record.fields.Url;
    
    // TODO: FRONTEND Add styling, use template literals to use image, name, title, and description variables. Eg. `My name is ${name}`.
    //Card is currently a placeholder, have front end make sure it's to their liking.
    newHTML += `
    
    <div class="col">
      <div class="card cardpadding" style="border-radius: 5rem">    
        <img id="images" src="${image}" class="card-img-top" alt="Image of " +${name}/>
          <div class="card-body ">
            <h5 class="card-title">${name}</h5>
            <p class="card-text jobTitle"> ${title} </p>
            <div class="overflow-y-scroll">
              <p id="description" class="card-text">${description}</p>
            </div>
            <div class="button-center">
            <a class="btn btn-secondary" target="_blank" href="${url}">About Me</a>
            </div>
          </div>
      </div>
    </div>
    `;
    getResultElement.innerHTML = newHTML;
  });
};

const searchBar = async (e) => {
  // Search bar to filter people.
  e.preventDefault();
  let input, filter, cardimagetext, i, x; // declare all four at once

  input = document.getElementById("myinput");
  filter = input.value.toUpperCase(); // ignore case/capitalization
  cardimagetext = document.getElementsByClassName("card");

  for (x = 0; x < cardimagetext.length; x++) {
    i = cardimagetext[x].getElementsByClassName("card-text")[0];
    if (i.innerHTML.toUpperCase().indexOf(filter) > -1) {
      cardimagetext[x].style.display = ""; // '' means show
    } else {
      cardimagetext[x].style.display = "none";
    }
  }
};

// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into an array
// ["id?=", "receHhOzntTGZ44I5"] and then we only choose the second one
// let idParams = window.location.search.split("?id=");
// if (idParams.length >= 2) {
//   // has at least ["id?", "OUR ID"]
//   fetchPerson(idParams[1]); // create detail view HTML w/ our id
// } else {
//   fetchPeople(); // no id given, fetch summaries
// }
fetchPeople();
