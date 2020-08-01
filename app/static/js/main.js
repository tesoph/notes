//Force relod on back page to display the new note after creation/display updated version of edited note
//https://stackoverflow.com/questions/43043113/how-to-force-reloading-a-page-when-using-browser-back-button
window.addEventListener("pageshow", function (event) {
    var historyTraversal = event.persisted ||
        (typeof window.performance != "undefined" &&
            window.performance.navigation.type === 2);
    if (historyTraversal) {
        // Handle page restore.
        window.location.reload();
    }
});

//Confirm to delete a note when clicking on the delete button
function confirmDelete() {
    if (confirm("Do you want to permanently delete this note?")) {
        return true;
    }
    else {
        return false;
    }
}

let btns = document.getElementsByClassName("deleteNoteButton");
for (let i = 0; i < btns.length; i++) {
    btns[i].onclick = function () {
        if (confirmDelete()) {
            window.location.href = this.href;
        }
        else {
            return false;
        }
    }
}

//Confirm to delete a note when clicking on the delete button
function confirmCategoryDelete() {
    if (confirm("Do you want to delete this tag from your list of tags? The notes under this tag will remain but they will be untagged.")) {
        return true;
    }
    else {
        return false;
    }
}

let deleteCatButton = document.getElementById("deleteCategoryButton");
if (deleteCatButton) {
    deleteCatButton.onclick = function () {
        if (confirmCategoryDelete()) {
            window.location.href = this.href;
        }
        else {
            return false;
        }
    }
}

$(document).ready(function () {
    $('.collapsible').collapsible();
})

//Make the flashed messages disappear after a set time 
//https://stackoverflow.com/questions/51822192/trying-javascript-to-have-my-flash-my-message-disappear-after-a-few-seconds-afte
$(document).ready(function() {
    setTimeout(function() {
        $('.alert-saved').fadeOut('slow');
    }, 3000); // <-- time in milliseconds
});
//Materialize sidenav initialization settings
$(document).ready(function () {
    //Code on how to to initialize the Materialize sidenav from: 
    //https://stackoverflow.com/questions/51355020/materialize-css-sidenav-options-not-defined
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {
        edge: 'left',
        draggable: true,
        inDuration: 250,
        outDuration: 200,
        onOpenStart: null,
        onOpenEnd: null,
        onCloseStart: null,
        onCloseEnd: null,
        preventScrolling: true
    });
});