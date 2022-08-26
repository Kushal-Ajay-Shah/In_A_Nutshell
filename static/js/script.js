// SPLASH SCREEN

splash = ()=>{

    let i = 0;
    let speed = 200;
    typing_effect = (parent,i,speed) => {
        Array.from(parent.children).forEach(li => {
            setTimeout(()=>{
                li.style.visibility = "visible";
            },i*speed);
            i = i+1;
        });
    }

    let parent = document.getElementsByClassName("splash-element")[0];
    typing_effect(parent,i,speed);

    setTimeout(()=>{
        cont = document.getElementsByClassName("splash")[0];
        cont.style.top = "-100vh"
        document.getElementsByClassName("index")[0].style.top = "0";
        document.getElementsByClassName("splash")[0].style.display = "none";

    },15*speed);
}





// --------------------------------------------------------
// Start Loading
// --------------------------------------------------------
load = () => {
    console.log("start loading");
    
    document.getElementsByClassName("loading")[0].style.display = "flex";
}

// --------------------------------------------------------
// Search Anim
// --------------------------------------------------------
function searchAnim(){
    
    document.getElementById("searchAnim").textContent = "Search";
    inpultHolder = document.getElementById("searchInput");
    inpultHolder.setAttribute('id','search');
    // inpultHolderStyle. = "black";
    // inpultHolderStyle.display = "block";
}
upload_input = document.getElementById("upload");
upload_input.addEventListener("change",()=>{
    if(upload_input.value){
        document.getElementById("upload-sec").style.backgroundColor = "#1f4467";
        document.getElementById("upload-sec").style.color = "white";
        document.getElementById("upload-label").innerText = "Uploaded ✓";

        document.getElementById("upload-submit").disabled = false;
    }
});

// --------------------------------------------------------
// Form Validation
// --------------------------------------------------------
function validateForm1() {
    var x = document.forms["searchForm"]["keyword"].value;
    if (x == "") {
        document.getElementById("searchInput").style.boxShadow = "0 0 2px red";
        document.getElementsByClassName("loading")[0].style.display = "none";
        document.getElementById("searchInput").style.border = "1px red solid";
      return false;
    }
    document.getElementById("searchInput").style.boxShadow = "0";
    document.getElementById("searchInput").style.border = "1px #1f4467 solid";
    
  }
function validateForm2() {
    var x = document.forms["uploadForm"]["file"].value;
    if (x) {
      return true;
    }
    document.getElementById("upload-sec").style.backgroundColor = red;
    document.getElementById("upload-sec").style.color = "white";
    document.getElementById("upload-label").innerText = "Select a file first";

    return false;
  }