/* If you're feeling fancy you can add interactivity 
    to your site with Javascript */
"use strict"
const ORGS_URL = "https://api.airtable.com/v0/appW8sadHSpo3ifKG/Food%20Insecurity";
const KEY_QUERY = "key1QI3yN9GjIzfgT";
const SUMMARY_QUERY = "fields%5B%5D=Name&fields%5B%5D=Link&fields%5B%5D=Phone";

function fetchorgs() {
  let OrgResultElement = document.getElementById("org-container");
  
fetch(`${ORGS_URL}?${KEY_QUERY}&${SUMMARY_QUERY}`)
    .then(response => response.json())
    .then(data => {
      console.log(data); // response is an object w/ .records array
  
      OrgResultElement.innerHTML = "";
      let newHtml = "";
  for (let i = 0; i < data.records.length; i++) {
        let orgName = data.records[i].fields["Name"];
        let orgLink = data.records[i].fields["Link"];
        
        newHtml += `
          <div class="row">
  <div class="col-sm-6 mb-3 mb-sm-0">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">${orgName}</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="${orgLink}" class="btn btn-primary">${orgLink}</a>
      </div>
    </div>
  </div>
        `;
      }

      OrgResultElement.innerHTML = newHtml;
    });
}