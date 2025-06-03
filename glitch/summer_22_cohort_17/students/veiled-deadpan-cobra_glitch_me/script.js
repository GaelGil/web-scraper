// Airtable
var CARS_URL = "https://api.airtable.com/v0/app0Sx2zD8KCtf9BO/fastest%20cars";
var KEY_QUERY = "api_key=keyqNaRFBJZo2IKsJ";
var SUMMARY_QUERY = "fields%5B%5D=Car%20Name&fields%5B%5D=Price&fields%5B%5D=Top%20Speed&fields%5B%5D=pictures"
;

function getCars() {
  var carResultElement = document.getElementById("cars");

  fetch(`${CARS_URL}?${KEY_QUERY}&view=car&${SUMMARY_QUERY}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      carResultElement.innerHTML = ""; // clear student

      var newHtml = "";

      for (var i = 0; i < data.records.length; i++) {
        var picture = data.records[i].fields["pictures"];
        var name = data.records[i].fields["Car Name"];
        var speed = data.records[i].fields["Top Speed"];
       var price = data.records[i].fields["Price"];
       
        newHtml += `
        
          <div class="col-md-4 cardImageText">
          <div class="card">
            <a href="index.html?id=${data.records[i].id}">
              ${picture ? `<img class="head" src="${picture[0].url}">` : ``}
        
      </a>

            <div class="card-body">
              <p class="card-text card-key">${name}</p>
              <p class="card-text card-key">${speed}</p>
            </div>
          </div>
        </div>
        
        `;
      }

      carResultElement.innerHTML = newHtml;
    });
}
              
    //<p/P> %the9867L.....b
   // <p/> eQ=



function fetchSingleCar(carId) {
  var carResultElement = document.getElementById("cars");
fetch(`${CARS_URL}/${carId}?${KEY_QUERY}`)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is a single object

      var picture = data.fields["pictures"];
      var carName = data.fields["Car Name"];
      var carPrice = data.fields["Price"];
      var carTop  = data.fields["Top Speed"];
      var carNumber = data.fields["Produced"];
      var carEngine = data.fields["Engine"];
      var carTime= data.fields["Time"];
      
  


     /* var newHtml = `
        <div class="col-9">
        ${picture ? `<img class="head" src="${picture[0].url}">` : ``}
          <div class="card">
            <h4 class="card-title">${carName}</h4>
            <h5></h5>

            <h4 <p> numbers of cars produced </p>${carNumber}</h4>
            <h4 ${carTop}</h4>
            <p>${carPrice}</p>
          </div>
        </div>
        <div class="col">
       
          
         
      </a>
     </div>
         
      `*/;
var newHtml = `
        <div class="col-9">
        ${picture ? `<img class="head" src="${picture[0].url}">` : ``}
          <div class="card">
            <h4 class="card-title car_name">${carName}</h4>
            <h5></h5>

            <h4 <p> -Numbers of Cars Produced </p>${carNumber}</h4>
            <h4 ${carTop}</h4>
            <h4 <p> -Car Price </p>${carPrice}</h4>
            <h4 <p> -Type Of Engine </p>${carEngine}</h4>
          <h4 <p> -0 TO 60 Time  </p>${carTime}</h4>
          </div>
        </div>
        <div class="col">
       
          
         
      </a>
     </div>
         
      `;
      carResultElement.innerHTML = newHtml;
    });
}
 
// function getSingleDirectory(programsId) {
//   var programsResultElement = document.getElementById("student");

//   fetch(`${DIRECTORY_URL}/${programsId}?${KEY_QUERY}`)
//     .then((response) => response.json())
//     .then((data) => {
//       console.log(data); // response is a single object

//       var progName = data.fields["Name"];
//       var progDescription = data.fields["Description"];
//       var progGrade = data.fields["Grade"];
//       var progTime = data.fields["Time Duration"];
//       var progLink = data.fields["Program URL"];

//       var newHtml = `
        
//         <div class="col-12">
//           <div class="card">
    
//             <h4 class="card-title">${progName}</h4>
           
//             <p class="progDescription">${progDescription}</p>
//             <h5 class="descriptionTitle">Description:</h5>
            
//         </div>
//       `;

//       programsResultElement.innerHTML = newHtml;
//     });
// }

// function searchFunction() {
//   var input, filter, cardimagetext, i, x;
//   input = document.getElementById("myinput");
//   filter = input.value.toUpperCase();
//   cardimagetext = document.getElementsByClassName("cardImageText");

//   for (x = 0; x < cardimagetext.length; x++) {
//     i = cardimagetext[x].getElementsByClassName("card-key")[0];
//     if (i.innerHTML.toUpperCase().indexOf(filter) > -1) {
//       cardimagetext[x].style.display = "";
//     } else {
//       cardimagetext[x].style.display = "none";
//     }
//   }
// }

// look up window.location.search and split, so this would take
// https://dmspr2021-airtable-app.glitch.me/index.html?id=receHhOzntTGZ44I5
// and look at the ?id=receHhOzntTGZ44I5 part, then split that into an array
// ["id?=", "receHhOzntTGZ44I5"] and then we only choose the second one
var idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id?", "OUR ID"]
 fetchSingleCar(idParams[1]); // create detail view HTML w/ our id
} else {
  getCars(); // no id given, fetch summaries
}

