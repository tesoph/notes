
//When text is input to either the title bar or the note body for the first time, the autosave function is called
//Closure to make sure the function is only called once from:
//https://stackoverflow.com/questions/12713564/function-in-javascript-that-can-be-called-only-once
var autoSave = (function () {
    var executed = false;
    return function () {
        if (!executed) {
            executed = true;
            setInterval(function () {
                let ed = tinyMCE.get('note_body');
                var body = ed.getContent();
                var title = document.getElementById('note_title').value;
                var category = document.getElementById('note_category').value;
                var timestamp = document.getElementById('note_timestamp').value;
                
                var post = {
                    "body": body,
                    "title": title,
                    "category": category,
                    "timestamp": timestamp,
                }
                
                //https://stackoverflow.com/questions/52459953/passing-variable-from-javascript-to-flask-using-ajax
                $.ajax({
                    type: 'POST',
                    url: "/autosave/",
                    contentType: 'application/json;charset=UTF-8',
                    dataType: "json",
                    data: JSON.stringify(post, null, '\t')
                });
            }, 3000);
        }
    };
})();

//When text is input to either the title bar or the note body for the first time, the autosave function is called
//JQuery to only fire an event once
//https://stackoverflow.com/questions/3393686/only-fire-an-event-once
//#tinymce-livepreview is a hidden div on the note page. The html is changed when text is input to the editor to allow this event to be detected.
$('body').one("DOMSubtreeModified", '#tinymce-livepreview', autoSave);
$('#note_title').one('input', autoSave);