//Force relod on back page to display the new note after creation/display updated version of edited note
//https://stackoverflow.com/questions/43043113/how-to-force-reloading-a-page-when-using-browser-back-button
 window.addEventListener( "pageshow", function ( event ) {
    var historyTraversal = event.persisted || 
                           ( typeof window.performance != "undefined" && 
                                window.performance.navigation.type === 2 );
    if ( historyTraversal ) {
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
            window.location.href=this.href;
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
if(deleteCatButton){
    deleteCatButton.onclick = function () {
        if (confirmCategoryDelete()) {
            window.location.href=this.href;
        }
        else {
            return false;
        }
    }
}
//Confrm to delete a category when clicking on the delete category button
/*
function confirmDeleteCategory() {
    if (confirm("Do you want to delete this tag from your list of tags? The notes under this tag will remain but they will be untagged")) {
        return true;
    }
    else {
        return false;
    }
}  

let deleteCategoryButton = document.getElementsByClassName("deleteCategoryButton");

    deleteCategoryButton.onclick = function () {
        console.log('clicked');
        if (confirmDeleteCategory()) {
            window.location.href=this.href;
        }
        else {
            return false;
        
    }

}*/



/*
let categoryBtns = document.getElementsByClassName("deleteCategoryButton");
for (let i = 0; i < categoryBtns.length; i++) {
    categoryBtns[i].onclick = function () {
        console.log('clickt button');
        if (confirmCategoryDelete()) {
            console.log('clicked yes');
            window.location.href=this.href;
        }
        else {
            console.log('cliocked no');
            return false;
        }
    }
}

function confirmCategoryDelete() {
    if (confirm("Do you want to permanently delete this category? Notes belonging to this category will still be kept")) {
        return true;
    }
    else {
        return false;
    }
}  
*/

 $(document).ready(function () {
    $('.collapsible').collapsible();
})

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