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
