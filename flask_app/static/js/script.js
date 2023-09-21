const themeToggler = document.querySelector(".theme-toggler");
const sideMenu = document.querySelector("sidebar");


// Change Theme

themeToggler.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme-variables");
    
    themeToggler.querySelector("span:nth-child(1)").classList.toggle("active");
    themeToggler.querySelector("span:nth-child(2)").classList.toggle("active")
})

sideMenu.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme-variables");
    sideMenu.querySelector("span").classList.toggle("active");
})