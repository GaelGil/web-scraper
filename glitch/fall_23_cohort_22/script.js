"use strict";


async function getAllRecords() {
  
  let getResultElement = document.getElementById("insertHTML");
  

  const options = {
    
    method: "GET",
    headers: { Authorization: `Bearer patdWVIPROwamj7g4.f90712990c3621c8df93fedf4ee02c64dfbaf3b137108373f2a11bde89d47ee4`, },
  
  };

  
  await fetch(
    `https://api.airtable.com/v0/appqP8MnguXP3AEB1/tbl5bHZgwWAjqPmEu`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
    console.log(data); // response is an object w/ .records array

    getResultElement.innerHTML = ""; // clear student

    let newHtml = "";

    for (let i = 0; i < data.records.length; i++) {
      
      let picture = data.records[i].fields["Picture"]; // here we are getting column values
      let name = data.records[i].fields["Name"];
      let career = data.records[i].fields["Career"];
      let description = data.records[i].fields["Description"];
      let linkedin = data.records[i].fields["Linkedin"];
      let aboutme = data.records[i].fields["Aboutme"];



      newHtml += `
        <center>
          <div class="card mb-3" style="max-width: 65%;">
            <div class="row g-0">
              <div class="col-md-4">
              
                ${
                  picture
                  ? `<img src="${picture[0].url}" class="img-fluid rounded-start" alt="Image">`: ``
                }
                
              </div>
              <div class="col-md-8">
                <div class="card-body">
                
                  <h1 class="card-title card-key"><p href="index.html?id=${data.records[i].id}">${name}</p></h1>
                  <p class="card-text careerText">${career}</p>
                  <p class="card-text" >${description}</p>
                  <a href="${aboutme}" target="_blank" class="card-text link" style="color: blue"><small  class="text-body-secondary" >About Me  |  </small></a>
                  <a href="${linkedin}" target="_blank" class="card-text link" style="color: blue"><small  class="text-body-secondary" >LinkedIn</small></a>

                </div>
              </div>
            </div>
          </div>

        <center>
        <div class="myDivider"></div>
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

  async function getOneRecord(jobsId) {
    let jobsResultElement = document.getElementById("job");

    const options = {
      method: "GET",
      headers: {
        Authorization: `Bearer patyxFwydN1umVWRB.a71c65f85b76352ea9b881aa685c0808e1014dffe74412f83dd6d5c9abfd3ca6`,
      },
    };

    await fetch(
      `https://api.airtable.com/v0/appGoA98d9s6dxCa5/JobList/${jobsId}`,
      options
    )
      .then((response) => response.json())
      .then((data) => {
        console.log(data); // response is a single object

        let name = data.fields["Name"];
        let career = data.fields["Career"];
        let picture = data.fields["Picture"];
        let aboutme = data.fields["Aboutme"];
        let linkedin = data.fields["Linkedin"];

        let newHtml = `

          <div class="info">
            <div class="card-deck">
              <div class="card detail border-dark" ;">
                <div class="card-body">
                
                   <h2 class="card-title">${name}</h2> 
                      ${picture ? `<img src="${picture[0].url}">` : ``}

                    <br><br>
                    
                    <p class="card-text"><u>Annual Salaries</u> <br> Low Salary: $${toCommas(
                      lowRate * 26
                    )} <br> High Salary: $${toCommas(
                    highRate * 26
                  )} <br> (Average Salary: $${toCommas(avgRate * 26)})</p>
                  
                  </div> 
              </div>

               <div class="card detail border-dark" style="width:450px;">
                <div class="card-body">
                  <h2 class="card-title">Job Description</h2> 
                  <p class="card-text">${description}</p>
                </div>
               </div>    
               <div class="card detail border-dark" style="width:450px;">
                <div class="card-body">   
                  <h2 class="card-title">Description</h2>
                  <p class="card-text">${formattedString(description)}</p>
                 </div> 
               </div>  
             </div>   
            </div>  
              <div class="back">
              <p><a href="index.html" class="btn btn-primary">Back</a>
              </div> 
    
        `;

        jobsResultElement.innerHTML = newHtml;
      });
  }

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
  // ["id?=", "receHhOzntTGZ44I5"] and then we only choose the second one
  let idParams = window.location.search.split("?id=");
  if (idParams.length >= 2) {
    // has at least ["id?", "OUR ID"]
    getOneRecord(idParams[1]); // create detail view HTML w/ our id
  } else {
    getAllRecords(); // no id given, fetch summaries
  }





















// <div class="card mb-3" style="max-width: 540px;">
//   <div class="row g-0">
//     <div class="col-md-4">
//        ${picture ? `<img src="${picture[0].url}">` : ``}
//     </div>
//     <div class="col-md-8">
//       <div class="card-body">
//         <h5 class="card-title">Card title</h5>
//                   <p class="card-text">${description}</p>
//       </div>
//     </div>
//   </div>
// </div>








