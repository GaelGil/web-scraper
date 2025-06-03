"use strict"


async function fetchTrainees() {
  let traineeResultElement = document.getElementById("card-container");
  
  const options = {
    method: 'GET',
    headers: {
      Authorization: `Bearer patyxFwydN1umVWRB.a71c65f85b76352ea9b881aa685c0808e1014dffe74412f83dd6d5c9abfd3ca6`
    }
  };
  
  const SUMMARY_QUERY = "fields%5B%5D=name&fields%5B%5D=linkedIn&fields%5B%5D=bio&fields%5B%5D=link&fields%5B%5D=email&fields%5B%5D=headshot&fields%5B%5D=title&fields%5B%5D=thumbnail";

  await fetch(`https://api.airtable.com/v0/appVopZTmpCPJVkDz/Trainees?&view=order&${SUMMARY_QUERY}`, options)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is an object w/ .records array

      traineeResultElement.innerHTML = "";

      let newHtml = "";

      for (let i = 0; i < data.records.length; i++) {
        let name = data.records[i].fields["name"];
        let email = data.records[i].fields["email"];
        let linkedIn = data.records[i].fields["linkedIn"];
        let bio = data.records[i].fields["bio"];
        let link = data.records[i].fields["link"];
        let pic = data.records[i].fields["headshot"];
        let title = data.records[i].fields["title"];
        let thumbnail = data.records[i].fields["thumbnail"];
        
        newHtml += `
              <div class="flip-card col-3">
                <div class="flip-card-inner">
                  <div class="flip-card-front shadow rounded-5">   <br>
                    ${pic ? `<img class="card-img-front rounded-circle" src="${pic[0].url}">` : ``}
                    <div class="card-body text-center">
                    <br>  <br>
                      <h4 class="card-title"><strong>&lt; ${name} &gt;</strong></h4>
                      <p class="card-text">${title}</p>
                    </div>
                  </div>
                  <div class="flip-card-back shadow rounded-5">
                  <h3 class="p1">About Me</h3>
                    <a
                      href="${link}"
                      target="_blank"
                      style="text-decoration: none"
                    >
                    ${thumbnail ? `<img class="card-img-back" src="${thumbnail[0].url}">` : ``}
                    </a>
                    <div class="card-body text-center">
                      <p class="card-text" id="bio">
                        ${bio}
                      </p>

                      <div class="links">
                        <ul class="icons">
                          <a
                            href="${linkedIn}"
                            target="_blank"
                            style="text-decoration: none"
                          >
                            <li><i class="fa-brands fa-linkedin"></i></li>
                          </a>
                          <a
                            href="mailto:${email}"
                            target="_blank"
                            style="text-decoration: none"
                          >
                            <li><i class="fa-solid fa-envelope"></i></li>
                          </a>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
        `;
      }

      traineeResultElement.innerHTML = newHtml;
    });
}

let idParams = window.location.search.split("?id=");
if (idParams.length >= 2) {
  // has at least ["id=", "OUR ID"]
  //fetchSingleDog(idParams[1]); // create detail view HTML w/ our id
} else {
  fetchTrainees(); // no id given, fetch summaries
}
