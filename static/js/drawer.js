const navLinks = document.querySelectorAll(".nav-link");
const offcanvas = document.querySelector(".offcanvas");
const header = document.querySelector("header");

console.log(offcanvas);

const offcanvasInstance = new bootstrap.Offcanvas(offcanvas);

navLinks.forEach((link) => {
    // Add event listener to each navigation link
    link.addEventListener("click", (e) => {
      // Close offcanvas
      e.preventDefault();
      const targetSectionId = e.target.getAttribute("href").substring(1);

      // Calculate the top position to scroll to, accounting for the header height
      const targetSection = document.getElementById(targetSectionId);

      const targetScrollPosition =
        targetSection.offsetTop - header.offsetHeight * 1.5;

      console.log(targetSection.offsetTop);

      // Scroll to the target position
      window.scrollTo({
        top: targetScrollPosition,
        behavior: "smooth",
      });

      offcanvasInstance.hide();
    });
  });