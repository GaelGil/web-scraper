"use strict"

// const api_url = `https://api.airtable.com/v0/appocFsfVnwXhJuMW/Description?api_key=keyXe4tmt8vfCsXCu`;
// //  URL for airtable is :https://api.airtable.com/v0/appocFsfVnwXhJuMW/
//    Then add name of base + ? : "Description?"
//       Then add API Key

// const apiToken = "patikw4Ya3HUxJqmA.2b955ab47ba7fc08254ca781b778ccab4f611544e887ed362de24c6e397d8a35";
const summary = "fields%5B%5D=studentName&fields%5B%5D=imageURL&fields%5B%5D=website";
const api_url_NEW = `https://api.airtable.com/v0/appocFsfVnwXhJuMW/Description?&${summary}` ;



const options = {
  method: 'GET',
  headers:{
    Authorization: "Bearer patikw4Ya3HUxJqmA.2b955ab47ba7fc08254ca781b778ccab4f611544e887ed362de24c6e397d8a35"
  }
};

// ^new token method 


fetch(api_url_NEW, options)
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.records.length; i++) {
      let student = document.getElementById("student");
      
      student.innerHTML += `
      <div class="headshot">
        <a href="${data.records[i].fields.website}" target="_blank">
          <div class="cropped">
            <img  src="${data.records[i].fields.imageURL}" ${data.records[i].fields.missing} class="headshot" placeholder="image of ${data.records[i].fields.studentName}">
          </div>
        </a>
          <p class="name">${data.records[i].fields.studentName}</p>
      </div>`;
      
    }
   console.log(data)
  });



// everything below here is unnessisary



// fetch(api_url_NEW, options)
//   .then(response => response.json())
//   .then(data => {
  
//     console.log(data)

// });

// fetch(`https://api.airtable.com/v0/appocFsfVnwXhJuMW/Description?&${summary}`, options)
//   .then(response => response.json())
//   .then(data => {
  
//     console.log(data)

// });