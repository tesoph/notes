
//https://stackoverflow.com/questions/13667533/getelementsbyclassname-onclick-issue
let btns = document.getElementsByClassName("deleteNoteButton");
for (let i = 0; i < btns.length; i++) {
    btns[i].onclick = function () {
        console.log('clickt button');
        if (confirmDelete()) {
            console.log('clicked yes');
            window.location.href=this.href;

        }
        else {
            console.log('cliocked no');
            return false;
        }

    }
}

function confirmDelete() {
    if (confirm("Do you want to permanently delete this note?")) {
        return true;
    }
    else {
        return false;
    }
}  

//var url2 = document.getElementById('pageFrame').contentDocument.location;  // All good browsers

function getURL(){
    return url2;
}

/*
$(document).click(function(e) {
  
    var t = document.getElementById("note_timestamp");
    console.log('hi');
    console.log(t);
 });*/

 ///////new from base.html

 $(document).ready(function () {
    $('.collapsible').collapsible();
})

$(document).ready(function () {
    $('.sidenav').sidenav();
});