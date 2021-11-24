const observer = new IntersectionObserver(entries =>{
    entries.forEach(entry =>{

    if(entry.isIntersecting){
      document.querySelectorAll(".animated1")[0].classList.add("fadein");
      document.querySelectorAll(".animated2")[1].classList.add("fadeout");
    }
}) 
})
observer.observe(document.querySelector("animationcontainer"))