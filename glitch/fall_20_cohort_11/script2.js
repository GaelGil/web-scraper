"use strict"

async function getDirectory() {
  let studentResultElement = document.getElementById("student");

  const options = {
    method: 'GET',
    headers: {
      Authorization: `Bearer patyxFwydN1umVWRB.a71c65f85b76352ea9b881aa685c0808e1014dffe74412f83dd6d5c9abfd3ca6`
    }
  };
  
  await fetch(`https://api.airtable.com/v0/appOV9Fu3N4LNDlPM/Directory?&view=order`, options)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      studentResultElement.innerHTML = ""; // clear student

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let name = data.records[i].fields["Name"];
        let link = data.records[i].fields["Link"];
        let picture = data.records[i].fields["Pictures"];

        newHtml += `
        
          <div class="col-md-4 cardImageText">
          <div class="card">
            <a href="${link}" target="_blank"
              >${picture ? `<img class="head" src="${picture[0].url}">` : ``}
            </a>

            <div class="card-body">
              <p class="card-text card-key">${name}</p>
            </div>
          </div>
        </div>
        
        `;
      }

      studentResultElement.innerHTML = newHtml;
    });
}

async function getSingleDirectory(programsId) {
  let studentResultElement = document.getElementById("student");
  
  const options = {
    method: 'GET',
    headers: {
      Authorization: `Bearer patyxFwydN1umVWRB.a71c65f85b76352ea9b881aa685c0808e1014dffe74412f83dd6d5c9abfd3ca6`
    }
  };

//   await fetch(`https://api.airtable.com/v0/appOV9Fu3N4LNDlPM/Directory/${programsId}`, options)
//     .then((response) => response.json())
//     .then((data) => {
//       console.log(data); // response is a single object

//       let progName = data.fields["Name"];
//       let progDescription = data.fields["Description"];
//       let progGrade = data.fields["Grade"];
//       let progTime = data.fields["Time Duration"];
//       let progLink = data.fields["Program URL"];

//       let newHtml = `
        
//         <div class="col-12">
//           <div class="card">
    
//             <h4 class="card-title">${progName}</h4>
           
//             <p class="progDescription">${progDescription}</p>
//             <h5 class="descriptionTitle">Description:</h5>
            
//         </div>
//       `;

//       studentResultElement.innerHTML = newHtml;
//     });
}

//function used to search through the cards by name
function searchFunction() {
  let input, filter, cardimagetext, i, x;
  input = document.getElementById("myinput");
  filter = input.value.toUpperCase();
  cardimagetext = document.getElementsByClassName("cardImageText");

  for (x = 0; x < cardimagetext.length; x++) {
    i = cardimagetext[x].getElementsByClassName("card-key")[0];
    if (i.innerHTML.toUpperCase().indexOf(filter) > -1) {
      cardimagetext[x].style.display = "";
    } else {
      cardimagetext[x].style.display = "none";
    }
  }
}

// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into an array
// ["id?=", "receHhOzntTGZ44I5"] and then we only choose the second one
let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id?", "OUR ID"]
  getSingleDirectory(idParams[1]); // create detail view HTML w/ our id
} else {
  getDirectory(); // no id given, fetch summaries
}
               
               
