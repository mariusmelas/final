const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".meny");
const links = document.querySelectorAll(".meny li");

hamburger.addEventListener("click", () => {
  meny.classList.toggle("open");
  links.forEach(link => {
    link.classList.toggle("fade");
  });
})