const buttons = document.getElementsByTagName("button");
const info = document.getElementsByClassName("info");
const infobox = document.querySelector("#infobox");

for (let button of buttons) {
  button.addEventListener("click", function (e) {
    e.preventDefault();
    let content = e.target.nextElementSibling;
    content.hidden ? (content.hidden = false) : (content.hidden = true);
  });
}

// for (let target of info) {
//   target.addEventListener("click", function () {
//     let content = target.dataset.desc;
//     let id = target.closest(".category").id;
//     document.querySelector(`#${id}-info`).hidden = false;
//     document.querySelector(`#${id}-info`).innerText = content;
//   });
// }

// function info() {
//   const popup = document.getElementById("popup");
//   popup.classList.toggle("show");
// }

for (let target of info) {
  target.addEventListener("click", function () {
    let content = target.dataset.desc;
    infobox.hidden = false;
    infobox.innerText = "(click to close)\n" + content;
  });
}

infobox.addEventListener("click", () => (infobox.hidden = true));
