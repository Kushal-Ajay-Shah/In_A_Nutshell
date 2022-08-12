function load() {
  console.log("load");
  console.log(new Date().getTime());
  // console.log(document.querySelector(".loaded"));
  document.querySelector(".loaded").style.visibility = "hidden";
  setTimeout(() => {
    console.log(new Date().getTime());
    document.querySelector("#pulse-wrapper").style.visibility = "visible";
  }, 1000);
}
