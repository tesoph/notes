//fORCE RELOAD ON BACK PAGE TO SHOW THE MOST RECENT WORK
//https://stackoverflow.com/questions/43043113/how-to-force-reloading-a-page-when-using-browser-back-button
/*if(performance.navigation.type == 2){
    location.reload(true);
 }*/
 window.addEventListener( "pageshow", function ( event ) {
    var historyTraversal = event.persisted || 
                           ( typeof window.performance != "undefined" && 
                                window.performance.navigation.type === 2 );
    if ( historyTraversal ) {
      // Handle page restore.
      window.location.reload();
    }
  });

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

function confirmDelete() {
    if (confirm("Do you want to permanently delete this note?")) {
        return true;
    }
    else {
        return false;
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
    //Code on how to to initialize the Materialize sidenav from : https://stackoverflow.com/questions/51355020/materialize-css-sidenav-options-not-defined
   // $('.sidenav').sidenav();
   var elems = document.querySelectorAll('.sidenav');
   var instances = M.Sidenav.init(elems, {
    edge: 'left',
    draggable: false,
    inDuration: 250,
    outDuration: 200,
    onOpenStart: null,
    onOpenEnd: null,
    onCloseStart: null,
    onCloseEnd: null,
    preventScrolling: true
   });
});