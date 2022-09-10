// Show one page and hides the other two
function showPage(page) {
  // Hide all of the divs
  document.querySelectorAll("div").forEach((div) => {
    div.style.display = "none";
  });
  // Show the div provided in the argument
  document.querySelector(`#${page}`).style.display = "block";
}

// Wait for page to be loaded
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("button").forEach((button) => {
    // When button clicked, switch to that page
    button.onclick = function () {
      showPage(this.dataset.page);
    };
  });
});
