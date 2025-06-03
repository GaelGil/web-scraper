"use strict";

const options = {
  method: "GET",
  headers: {
    Authorization: "Bearer patfH34R278rH97od.200cfcb36491d49a3c9af8a9f53c9970ced5f171c2a27e420ab346a3868d3f1e",
  },
};

fetch("https://api.airtable.com/v0/appYBYqd9KS9OqEE5/Directory", options)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    const cardsContainer = document.getElementById('cards-container');
    data.records.forEach(record => {
      const picture = record.fields["Picture"];
      const name = record.fields["Name"];
      const linkedin = record.fields["Linkedin"];
      const description = record.fields["Description"];
      const aboutMePage = record.fields["About Me Page"];
      const thumbnail = record.fields["Picture"] ? record.fields["Picture"][0].url : "";
      

      const card = document.createElement('div');
      card.classList.add('card', 'col-md-4');

      const front = document.createElement('div');
      front.classList.add('front');
      front.innerHTML = `<img src="${thumbnail}" alt="${name}" style="width: 100%;"><h2>${name}</h2>`;
      
      const back = document.createElement('div');
      back.classList.add('back');
      back.innerHTML = `<p>${description}</p><a href="${linkedin}" target="_blank" class="btn btn-primary"><i class="fab fa-linkedin"></i> LinkedIn</a> <a href="${aboutMePage}" target="_blank" class="btn btn-secondary"><i class="fas fa-info-circle"></i> About Me</a>`;
      
      card.appendChild(front);
      card.appendChild(back);
      cardsContainer.appendChild(card);
    });
  })
  .catch(error => console.error('Error fetching data:', error));
