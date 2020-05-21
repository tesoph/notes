
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


$(document).click(function(e) {
    console.log('clicked');
    var heading = document.getElementById("firstHeading");
    document.getElementById("pageFrame").name = heading;
    console.log('h: ' + heading);
 });