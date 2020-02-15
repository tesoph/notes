document.addEventListener("click", function () {
    document.getElementById("demo").innerHTML = "Hello World";
});

//https://stackoverflow.com/questions/13667533/getelementsbyclassname-onclick-issue
let btns = document.getElementsByClassName("deleteNoteButton");
for (let i=0;i<btns.length;i++){
    btns[i].onclick=function(){
        console.log('clicked')
        var result = confirm("Are you sure you want to delete this note?");
        if (result) {
            console.log('yes')
           window.location.href=this.href;
        }
        return false;
    }
}







/*
document.getElementsByName("deleteNoteButton").onclick = function () {
    console.log('clicked')
    var result = confirm("Want to delete?");
    if (result) {
        console.log('yes')
        var link = this
        link.setAttribute("href", "{{url_for('delete_note', note_id=note._id)}}");
    }
    return false;
}
*/
/*
let btn = document.getElementById("deleteNoteBtn");
btn.addEventListener("click", () => {
print('clicked')
var result = confirm("Want to delete?");
if (result) {
    this.href="{{url_for('delete_note', note_id=note._id)}}"
}
else{
    this.href=""
}
});*/
/*
//More information modal button
let btn = document.getElementById("submitNote");
btn.addEventListener("click", () => {
   //this.toggleInfo();
   submitNote();
});
//this.toggleInfo=
submitNote = function () {
   // let vis = record if settings menu was open when more information button was clicked.
   let vis = $("#settings-menu").is(":visible");
   //Show the modal
   if ($("#information-modal").is(":hidden")) {
       $('#information-modal').modal('show');
   }
   //Pause sketch while modal is showing.
   audioVisualizer.noLoop();
   //If settings menu was open when the information button was clicked, hide it
   if (vis) {
       $("#settings-menu").hide();
   }
   $('#information-modal').on('hidden.bs.modal', function () {
       //if the settings menu was open when more information button was clicked, show it again.
       if (vis === true) {
           $("#settings-menu").show();
       }
       //reset vis to false on close
       vis = false;
       //Play sketch when modal is closed.
       audioVisualizer.loop();
   });
};
*/