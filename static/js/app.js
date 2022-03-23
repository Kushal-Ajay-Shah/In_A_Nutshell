// Close onclick outside
document.addEventListener("click", (e) => {
  const toggle = document.querySelector(".search__toggle");
  const input = document.querySelector(".search__input");
  const clickedElement = e.target;

  if (clickedElement == toggle) {
    input.value = "";
    return;
  }

  const isSearchField = clickedElement.closest(".search__field");

  if (!isSearchField) {
    toggle.checked = false;
    input.value = "";
  }
});
console.log("Hello");
