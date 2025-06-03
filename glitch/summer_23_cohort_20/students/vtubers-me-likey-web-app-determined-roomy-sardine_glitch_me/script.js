//add bootstrap

"use strict";
// a+= 1

//a = a + 1
async function NameandLore() {
  let VtubersResultElement = document.getElementById("Vtuber-container");

  const options = {
    method: "GET",
    headers: {
      Authorization:
        "Bearer patfgPGFmZFaxzYIl.76f63ef21b04e155597783a6fde8c1ab7a371bd8b1c7bca5f737ce3358931c92",
    },
  };
  const summary = "fields%5B%5D=Vtubers&fields%5B%5D=Vtuber Portrait";

  await fetch(
    `https://api.airtable.com/v0/appUWFMPXnlAP93Wo/Vtubers?&${summary}&view=Vtubers`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      VtubersResultElement.innerHTML = ""; // clear student

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let vtuberportrait = data.records[i].fields["Vtuber Portrait"]; // here we are getting column values
        let name = data.records[i].fields["Vtubers"];

        newHtml += `
        
         <div class="col-md-4 cardlistview">
          <div class="card cardlistview list border-dark" style="width: 20rem; height: auto">
          ${ vtuberportrait ? `<img class="cardlistimage" src="${vtuberportrait[0].url}">`: ``  }
            <!--[0].url means go to object(the thing in brackets)0 and take out the url only for the picture-->
          <div class="card-body">
            <h3 class="card-title card-key cardlisttitle"><a class="cardlisttitlenormalcolor" href="index.html?id=${
              data.records[i].id
            }">${name}
            </a></h3>
          </div>
          </div>
        </div>
        
        `;
      }

      VtubersResultElement.innerHTML = newHtml;
    });
}

/*
       <div class="container">
        <div class="card mb-3 carddetailedview ">
          <div class="row g-0">
            <div class="col-md-5 translate-middle">
             <img src="${vtuberfullbody}" class="vtuberfullbodybigger">
             <img src="${mascotpicture}" class="carddetailedviewpicture cardimage picturecol img-fluid mascotpicturesmall ">
            </div>
                  <div class="col-md-7">
                    <div class="card-body overflow-y-scroll">
                      <h2 class="card-title card-key cardtitlenormal middletext carddetailedviewname">${name}</h2>
                      <h4 id="scrollspyHeading1" class="headingforinfo">Lore</h4>
                      <p class="card-text">${lore}</p>
                      <h4 id="scrollspyHeading2" class="headingforinfo">Personality</h4>
                      <p class="card-text">${personality}</p>
                      <h4 id="scrollspyHeading3" class="headingforinfo">Mascot</h4>
                      <p class="card-text">${mascotinfo}</p>
                      <h4 id="scrollspyHeading4" class="headingforinfo">Funny Quotes</h4>
                      <p class="card-text">${quotes}</p>
                    </div>
                  </div>
          </div>
        </div>
      </div>     
*/

async function DetailedView(vtuberId) {
  let VtubersResultElement = document.getElementById("Vtuber-container");

  const options = {
    method: "GET",
    headers: {
      Authorization:
        "Bearer patfgPGFmZFaxzYIl.76f63ef21b04e155597783a6fde8c1ab7a371bd8b1c7bca5f737ce3358931c92",
    },
  };

  await fetch(
    `https://api.airtable.com/v0/appUWFMPXnlAP93Wo/Vtubers/${vtuberId}`,
    options
  )
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // response is an object w/ .records array

      let newHtml = "";

      let mascotpicture = data.fields["Mascot Picture"] // here we are getting column values
      let vtuberfullbody = data.fields["Vtuber Full Body"][0].url;
      let name = data.fields["Vtubers"];
      let lore = data.fields["Lore"];
      let personality = data.fields["Personality"];
      let mascotinfo = data.fields["Mascot and Fans"];
      let quotes = data.fields["Fun Quotes"];
      console.log(vtuberfullbody); //try to see what is happening behind the scenes
    
      newHtml += `
                   
                <div class="container">
                  <div class="row">
                      <div class="card carddetailedview">
                      <div class="row">
                        <div class="col-md-5">
                         <div class="overflowscroll topofscrollbarpicdetailed">
                          <img class="vtuberfullbodybigger" src="${vtuberfullbody}">
                          ${mascotpicture ? `<img class="rounded mx-auto d-block carddetailedviewpicture mascotpicturesmall" src="${mascotpicture[0].url}">`: ``}  
                          </div>
                        </div>
                        <div class="col-md-7 infodetailedcardbgcolor"> 
                        <h2 class="card-title card-key cardtitlenormal middletext carddetailedviewname">${name}</h2>
                          <div class="card-body overflowscroll test bottomofscrollbarinfo">
                          <h4 id="scrollspyHeading1" class="headingforinfo">Lore</h4>
                          <p class="card-text">${lore}</p>
                          <h4 id="scrollspyHeading2" class="headingforinfo">Personality</h4>
                          <p class="card-text">${personality}</p>
                          <h4 id="scrollspyHeading3" class="headingforinfo">Mascot and Fans</h4>
                          <p class="card-text">${mascotinfo}</p>
                          <h4 id="scrollspyHeading4" class="headingforinfo">Funny Quotes</h4>
                          <p class="card-text">${quotes}</p>
                          </div>
                        </div>
                        </div>
                  </div>
                </div>
   
         
        
        `;

      VtubersResultElement.innerHTML = newHtml;
    });
}

let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id?", "OUR ID"]
  DetailedView(idParams[1]); // create detail view HTML w/ our id
} else {
  NameandLore();
} // no id given, fetch summaries
