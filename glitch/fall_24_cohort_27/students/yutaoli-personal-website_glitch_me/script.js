//       function adjustHeight() {
//         const header = document.querySelector('h1');
//         const container = document.querySelector('.container-fluid');
//         const headerHeight = header.offsetHeight; // Get the height of the header
//         const viewportHeight = window.innerHeight; // Get the height of the viewport
//         container.style.height = `calc(${viewportHeight}px - ${headerHeight}px)`; // Adjust height dynamically
//       }

//       // Call the function when the page loads
//       window.addEventListener('load', adjustHeight);
//       // Call the function when the window is resized
//       window.addEventListener('resize', adjustHeight);