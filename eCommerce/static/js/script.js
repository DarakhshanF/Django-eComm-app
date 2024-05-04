// function toggleMenu() {
//     var navigation = document.getElementById("navigation");
//     if (navigation.className === "navigation") {
//         navigation.className += " active";
//     } else {
//         navigation.className = "navigation";
//     }
// }
function toggleMenu() {
  var menu = document.getElementById("navMenu");
  var icon = document.querySelector(".hamburger");

  if (menu.style.display === "block") {
    menu.style.display = "none";
    icon.innerHTML = "&#9776;";
  } else {
    menu.style.display = "block";
    icon.innerHTML = "&times;";
  }
}
