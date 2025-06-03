"use strict"

async function getAllRecords() {
  let getResultElement = document.getElementById("portfolio");
  let newCardElement = "";
  
   const options = {
    method: 'GET',
    headers: {
      Authorization: `Bearer patyxFwydN1umVWRB.a71c65f85b76352ea9b881aa685c0808e1014dffe74412f83dd6d5c9abfd3ca6`
    }
  };

  await fetch(`https://api.airtable.com/v0/appzWd2So8NZYmAZL/Portfolio%20Member?&view=Grid view`, options)
    .then((response) => response.json())
    .then((data) => {
      let numberOfPeople = data.records.length;

      for (let eachPerson = 0; eachPerson < numberOfPeople; eachPerson++) {
        let currentPersonRecord = data.records[eachPerson];

        //Current Member Object
        let currentMember = {
          fullName: currentPersonRecord.fields["Full Name"],
          teamMateImage: currentPersonRecord.fields["Teammate Picture"][0].url,
          devMissionQuote: currentPersonRecord.fields["Dev/Mission Quote"],
          linkToLinkedIn: currentPersonRecord.fields["LinkedIn Link"],
          portfolioLink: currentPersonRecord.fields["Portfolio Link"],
          projectTitle: currentPersonRecord.fields["Project Title"],
          projectImage: currentPersonRecord.fields["Project Image"],
          projectSourceLink: currentPersonRecord.fields["Project Source Link"],
        };

        console.log(currentMember);
        
       let nameSplit = currentMember.fullName.split(" ");

        //Fantastic work on the cards, Priya! thank you :)
        newCardElement += `
      <div class="card card-body p-0 col-lg-2 col-md-4 col-sm-4">
      
    
      <a href="${currentMember.portfolioLink}">
           <img
              src="${currentMember.teamMateImage}"
              class="member-image img-fluid rounded-4 shadow-2-strong"
              alt="member head shot picture"
            />
            <div class="d-flex justify-content-center m-2">
            
           <h5 class="card-title memberName text-center">${nameSplit[0]}</h5>
           <h5 class="card-title memberName text-center">${nameSplit[1]}</h5>
           
           <a  target="_blank" href="${currentMember.linkToLinkedIn}"><img class="linkedin-logo m-2" src="https://cdn3.iconfinder.com/data/icons/inficons/512/linkedin.png
           " alt="linkedin"/"></a>
           </div>
           <div class="text-center">
             <a href="${currentMember.portfolioLink}" class="text-center card-title portfolio" target="_blank">View Portfolio</a>
             <img class="linkedin-logo" src="https://static.vecteezy.com/system/resources/previews/003/355/184/original/autumn-falling-leaves-icon-free-vector.jpg" alt="icon of leave"/>
            </div>
          <div class="d-flex flex-column justify-content-center card-text quote">"${currentMember.devMissionQuote}"
            
            <h5 class="row justify-content-center project-title">Project Showcase - ${currentMember.projectTitle}</h5>
                <a href="${currentMember.projectSourceLink}" target="_blank"class="row view-project justify-content-center">View Project</a>
          </div>
          </a>
         
  </div>`;
      }
      getResultElement.innerHTML = newCardElement;
    });
}

getAllRecords();
