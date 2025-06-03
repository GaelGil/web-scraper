console.log("Mariah wuz here");


const container = document.getElementById(".team");
const getAirtableData = async () => {
  const apiKey = "patnXDBYo167dIUT6.5588f408fdbdfaf046383c199db6ccab54c2137dd9a2fd4374809de8ee7d56ae";
  const baseId = "appaJy7kRkg2YVS6r";
  const tableName = "Trainees";
  const url = `https://api.airtable.com/v0/${baseId}/${tableName}`;
  const options = {
    method: "GET",
    headers: {
      Authorization: `Bearer ${apiKey}`,
    },
  };
  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error("Failed to fetch data from Airtable.");
    }
    const data = await response.json();
    // Sort the records alphabetically by name before processing
    data.records.sort((a, b) => a.fields.name.localeCompare(b.fields.name));
    //console.log(data);
    let content = "";
    
    
      
    for (const record of data.records) {
      const name = record.fields.name || "Name not available";
      const email = record.fields.email || "Email not available";
      const linkedIn = record.fields.linkedIn || "#";
      const headshot = record.fields.headshot;
      const title = record.fields.title || "Maverick";
      const skills = record.fields.skills || "no skill";
      const Testimonials = record.fields.Testimonials;
      // Check if the trainee has a picture (headshot) and set the URL accordingly
      const headshotUrl = headshot ? headshot[0]?.url : "https://example.com/default-avatar.jpg";
      
      
 /*     
      content += `
      <div class="details d1">
            <div class="Sub-text">${email}</div>
						<div class="headline col1">
            <div class="name">${name}</div>
            </div>
						<div class="title">${title}</div>
						<div class="skills">${Testimonials}</div>
					</div>
          <button class="View-btn" src="${linkedIn}">
              View Me
            </button>
      `;
      
  }*/
      
       content += `
      <div class="flex flex-wrap -m-4">
      <div class="p-4 lg:w-1/4 md:w-1/2">
        <div class="h-full flex flex-col items-center text-center">
          <img alt="team" class="flex-shrink-0 rounded-lg w-full h-56 object-cover object-center mb-4" src="https://dummyimage.com/200x200">
          <div class="w-full">
            <h2 class="title-font font-medium text-lg text-gray-900">${name}</h2>
            <h3 class="text-gray-500 mb-3">${title}</h3>
            <p class="mb-4">DIY tote bag drinking vinegar cronut adaptogen squid fanny pack vaporware.</p>
            <span class="inline-flex">
              <a class="text-gray-500">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                  <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
                </svg>
              </a>
              <a class="ml-2 text-gray-500">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                  <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"></path>
                </svg>
              </a>
              <a class="ml-2 text-gray-500">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                  <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"></path>
                </svg>
              </a>
            </span>
          </div>
        </div>
      </div>
    </div>
      `;
      
  }
    container.innerHTML = content;
    
    
  } catch (error) {
    console.log("Error:", error);
    container.innerHTML = "<p>Failed to fetch data. Please try again later.</p>";
  }
};
getAirtableData();

