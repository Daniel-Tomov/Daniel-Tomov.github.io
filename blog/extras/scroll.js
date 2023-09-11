function changeCss () {
  var headerElement = document.getElementById("header");
  if (this.scrollY > 144) {
    headerElement.style.backgroundColor = "rgba(36,38,41,0.95)";
  } else {
    headerElement.style.backgroundColor = "rgba(36,38,41,0.6)";
  }
}

window.addEventListener("scroll", changeCss , false);
