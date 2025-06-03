"use strict";
// read token for airtable directory
const very_secret_token = 'patCd9XaHXn1QiqKV.5d4572f549c38c9e562d06e08091a6f252a51e17f4ab486aacbec2dbb083be7c';

// function for our list view
async function getAllRecords() {
  // TODO: change to ID of HTML Element where class directory cards will be made
  let getResultElement = document.getElementById("cohort-container");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer ${very_secret_token}`,
    },
  };

  await fetch(
    `https://api.airtable.com/v0/appHa1LrG80RqCCoJ/Participants?&view=order`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      getResultElement.innerHTML = ""; // clear brews

      let newHtml = "";
      for (let i = 0; i < data.records.length; i++) {
        // TODO: Get access to all records
        // let field = data.records[i].fields;
        let name = data.records[i].fields["Name"];
        let email = data.records[i].fields["Email"];
        let headshot = data.records[i].fields["Headshot"];
        let aboutMe = data.records[i].fields["About Me"];
        let linkedIn = data.records[i].fields["Linked-in"];
        let project = data.records[i].fields["Project"];
        let groupPhotos = data.records[i].fields["Group Photos"]
        let quote = data.records[i].fields["Quote"];
        // TODO: Create an element to store all the records
        newHtml += 
//         `
//         <div class="card mx-auto" style="width: 18rem;">
//            <img class="card-img-top rounded-circle mx-auto my-2" style="height: 200px; width: 200px;"src="${headshot[0].url}">
//            <div class="card-body">
//             <h5 class="card-title text-center">${name}</h5>
//           </div>
//         </div>
        
//         `;
          `
		<div class="">
			<div class="col-lg-4 col-md-4 ">
				<div class="flip-card">
					<div class="flip-card-inner">
						<div class="flip-card-front">
							<div class="card">
                <img class="card-img-top rounded-circle mx-auto my-2" style="height: 200px; width: 200px;" src="${headshot[0].url}">
								<div class="card-body">
									<h5 class="card-title">${name}</h5>
									<p class="card-text">${quote}</p>
								</div>
							</div>
						</div>
						<div class="flip-card-back">
							<div class="card">
								<img src=
                  "https://devmission.org/wp-content/uploads/2022/11/cropped-DM-Full-Logo-01.png"
									class="card-img-top pt-2" alt="Back Image">
								<div class="card-body d-flex flex-column">
									<a class="card-text btn btn-primary mt-1 mx-auto fw-bold" href="${aboutMe}" target="_blank">About Me</a>
									<a class="card-text btn btn-primary mt-1 mx-auto" href="${project}" target="_blank">Favorite Project</a>
                  <a class="link-dark fs-1" target="_blank" href="${linkedIn}"><i class="fa-brands fa-linkedin"></i></a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>          
          `
      }
        
      getResultElement.innerHTML = newHtml;
    
      
    });
}



// function for our detail view
async function getOneRecord(id) {
  // TODO: change to ID of HTML Element where class directory cards will be made
  let jobsResultElement = document.getElementById("brews");

  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer ${very_secret_token}`,
    },
  };

  await fetch(
    //TODO: Change fetch link to class directory link
    `https://api.airtable.com/v0/appHa1LrG80RqCCoJ/Participants/${id}`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is a single object
      // TODO: Get access to one record
      let field = data.fields;
    
      // TODO: Create an expanded information page or element
      let newHtml = `
      
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
  // has at least ["?id=", "OUR ID"]
  getOneRecord(idParams[1]); // create detail view HTML w/ our id
} else {
  getAllRecords(); // no id given, fetch summaries
}