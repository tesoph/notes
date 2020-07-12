
//https://www.tiny.cloud/docs-4x/plugins/autosave/
/*document.getElementById('subBtn').addEventListener('click', function () {
    // Perform your ajax request
    console.log('autosaved new');
  tinymce.get('about').save();
});
*/
//changed = tinymce.get('note_body').getContent();

//JQuery to only fire an event once
//https://stackoverflow.com/questions/3393686/only-fire-an-event-once
$('body').one("DOMSubtreeModified", '#tinymce-livepreview', function (e) {
    // use e.whic
    console.log('tinymce changed');
//function autosave(){
    console.log('triggered');
//https://stackoverflow.com/questions/37073010/checkbox-value-true-false
$("#public").on('change', function() {
    console.log('help');
    if ($(this).is(':checked')) {
      $(this).attr('value', 'true');
    } else {
      $(this).attr('value', 'false');
    }
});

setInterval(function(){ 
    console.log("timer x");
    let ed = tinyMCE.get('note_body');
    var d = ed.getContent();
    //console.log("aaa: " + d);
    var body = d;
    var title = document.getElementById('note_title').value;
    var category = document.getElementById('note_category').value;
    var timestamp = document.getElementById('note_timestamp').value;
    var public = document.getElementById('public').value;
    console.log('category check:  ' + category);
  /*  if (public=='true'){
        public == True;
    }else{
        public == False;
    }*/

    var post = {
        "body": body,
        "title":title,
        "category": category,
        "timestamp": timestamp,
        "public": public,
    }
    console.log("post: " + post['body']+ "x:" +post['public']);
    //let nb = $('my_id').html($(this).text());
    //console.log("aaa:" + nb);
    //https://stackoverflow.com/questions/52459953/passing-variable-from-javascript-to-flask-using-ajax
    $.ajax({
        type : 'POST',
        url : "/autosave/",
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        //data : {'data':d}
        //data: JSON.stringify(data, null, '\t')
        //data: {body: bod}
        data: JSON.stringify(post, null, '\t')
        
      });
}, 3000);

//};
});



/*$(document).ready(function(){
    var timer;
    var timeout = 5000; // Timout duration
    $('#postTitle,#note_body').keyup(function(){
    
     if(timer) {
      clearTimeout(timer);
     }
     timer = setTimeout(saveData, timeout); 
    
    });
    
    $('#submit').click(function(){
     saveData();
    });
   });*/
   /*
   // Save data
   function saveData(){
    
   // var postid = $('#postid').val();
    //var title = $('#postTitle').val().trim();
    var content = $('#note_body').val().trim();
   
    if(title != '' || content != ''){
     // AJAX request
     $.ajax({
      url: 'autosave.php',
      type: 'post',
      data: {postid:postid,title:title,content:content},
      success: function(response){
       $('#postid').val(response);
      } 
     });
    } 
   }
*/
//From https://stackoverflow.com/questions/931252/ajax-autosave-functionality

/*
('$note_body').onChange = function(){
    //myAutoSavedTextbox_onTextChange();
    console.log('autosav');
}

*/
/*
myAutosavedTextbox_onTextChanged();

function myAutosavedTextbox_onTextChanged()
{
    console.log("sdffffffffff")
    if (!autosaveOn)
    {
        autosaveOn = true;

        $('note_body').everyTime("300000", function(){
             $.ajax({
                 type: "POST",
                 url: "autosavecallbackurl",
                 data: "id=1",
                 success: function(msg) {
                     $('#autosavenotify').text(msg);
                 }
             });
        }); //closing tag
    }
}*/
/*
//https://blog.carbonfive.com/an-ajax-auto-save-implementation/
function save(event) {
    event.target.form['version_number'].value++;
    var request = new XMLHttpRequest();
    request.open(event.target.form.method, event.target.form.action);
    request.send(new FormData(event.target.form));
}*/