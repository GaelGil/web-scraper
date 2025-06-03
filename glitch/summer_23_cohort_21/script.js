
/*
const container = document.getElementById("container");

const getAirtableData = async () => {
  const apiKey = "patwSsvy7Hvo5mSGS.9799e293a34039bfd554077a19779c0bc8b47f161fcda595acaa76f6b26ee9a4";
  const baseId = "appPABgKKuNzeb4l6";
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

    let content = "";
    for (const record of data.records) {
      const name = record.fields.name || "Name not available";
      const email = record.fields.email || "Email not available";
      const linkedIn = record.fields.linkedIn || "#";
      const headshot = record.fields.headshot;

      // Check if the trainee has a picture (headshot) and set the URL accordingly
      const headshotUrl = headshot ? headshot[0]?.url : "https://example.com/default-avatar.jpg";

      content += `
        <div>
          <img src="${headshotUrl}" />
          <h1>Name: ${name}</h1>
          <p>Email: ${email}</p>
          <p><a href="${linkedIn}" target="_blank">LinkedIn</a></p>
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
*/


/* siding bar */
function menuOnClick() {
  document.getElementById("menu-bar").classList.toggle("change");
  document.getElementById("nav").classList.toggle("change");
  document.getElementById("menu-bg").classList.toggle("change-bg");

  function resetMenu() {
    if (window.innerWidth >= 900) {
      document.getElementById(menu - bar).style.display = 'flex'
    }
  }
}




/*Toggle dark mode */
const darkModeToggle = document.getElementById("darkModeToggle");


const prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;


document.body.classList.toggle("dark-mode", prefersDarkMode);
/*
// Function to toggle dark mode
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}
darkModeToggle.addEventListener("click", toggleDarkMode); */



/*Cards option*/
$(function () {
  $(".material-card > .mc-btn-action").click(function () {
    var card = $(this).parent(".material-card");
    var icon = $(this).children("i");
    icon.addClass("fa-spin-fast");

    if (card.hasClass("mc-active")) {
      card.removeClass("mc-active");

      window.setTimeout(function () {
        icon
          .removeClass("fa-arrow-left")
          .removeClass("fa-spin-fast")
          .addClass("fa-bars");
      }, 800);
    } else {
      card.addClass("mc-active");

      window.setTimeout(function () {
        icon
          .removeClass("fa-bars")
          .removeClass("fa-spin-fast")
          .addClass("fa-arrow-left");
      }, 800);
    }
  });
});



/*Search option */
