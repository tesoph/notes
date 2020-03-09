/*function hello(){

}

hello();

//how do oyu call an anonymous function?
// in the case of bookmarklet
//javascript://

javascript:(function (){alert('hello');})();//thisis execute the function that's inside these parenthesies 
javascript:location.href='http://127.0.0.1:5000/page/?url='+location.href+'&title='+document.title;
*/
/*
    width: 40%;
    height: 200px;
    background-color: blue;
    position: fixed;
    padding: 2em;
    bottom: 0%;
    left: 60%;
    transform: translateY(-50%);
*/
(function () {
    console.log("bookmarklet starting");
    var element = document.getElementById('bodyContent');
    var parent = element.parentNode;
    var wrapper = document.createElement('div');
    var c = document.createElement('div');
    var note = document.createElement('textarea');
    wrapper.setAttribute("id", "w");
    note.setAttribute("id", "n");
    c.setAttribute("id", "c");
    c.appendChild(note);
    parent.replaceChild(wrapper, element);
    wrapper.appendChild(element);
    wrapper.appendChild(c);
    var btn = document.createElement("BUTTON");   // Create a <button> element
    btn.innerHTML = "CLICK ME";                   // Insert text
    c.appendChild(btn);
    var style = document.createElement('style');
    style.innerHTML = `
    #w {
  
    }
    #bodyContent{
        width:60%;
    }

    #c{
        top: 15%;
        width: 35%;
        height: 80vh;
        background-color: blue;
        position: fixed;
        right: 0;
    }
    #note{
        width:100%;
        min-height:90%;
        overflow-y:scroll;
    }
    `;
    document.head.appendChild(style);
})();

//form action='/page/?url={{ url }}' method='POST' id='noteForm'
//javascript:location.href='http://127.0.0.1:5000/page/?url='+location.href+'&title='+document.title;
//  <button class="btn btn-info" id='submitNote' type="submit">Save Note</button>
console.log("bookmarklet starting");
var url=location.href;
var title=document.title;
h='wiki-note.herokuapp.com/page3/?url=';
var element = document.getElementById('bodyContent');
var parent = element.parentNode;
var wrapper = document.createElement('div');
var c = document.createElement('FORM');
var note = document.createElement('textarea');

c.setAttribute('action', h+url);
c.setAttribute('method', 'POST');
wrapper.setAttribute("id", "w");
note.setAttribute("id", "n");
note.setAttribute('name', 'body');
if(typeof nbody !== 'undefined'){
note.innerHTML = nbody;    }
c.setAttribute("id", "c");
c.appendChild(note);
parent.replaceChild(wrapper, element);
wrapper.appendChild(element);
wrapper.appendChild(c);
var btn = document.createElement("BUTTON");
btn.setAttribute('type', 'submit');
btn.innerHTML = "CLICK ME";       
c.appendChild(btn);
var style = document.createElement('style');
style.innerHTML = `
#w {

}
#bodyContent{
    width:60%;
}

#c{
    top: 15%;
    width: 35%;
    height: 80vh;
    background-color: blue;
    position: fixed;
    right: 0;
}
#note{
    width:100%;
    min-height:90%;
    overflow-y:scroll;
}
`;
document.head.appendChild(style);

/*
 note.setAttribute("class", "resizable draggable");
 #n{
        width: 35%;
        height: 100vh;
        background-color: blue;
        position: fixed;
        padding: 2em;
        bottom: 0%;
        left: 60%;
        transform: translateY(-50%);
    }
 $('#n').resizable();
    $('#n').draggable()
var style = document.createElement('style');
    style.innerHTML = `
    #w {
    display:flex;
    width:100%
    }

    #n{
        height:200px;
        width:50%
        float:right;
        background-color:blue;
    }
    `;
    document.head.appendChild(style);
javascript:(function(){let script = document.createElement('script');script.src='bookmarklet.js'; document.body.appendChild(script);})

*/

/*



'''
class Bookmark(db.Model):
    url = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
    image = CharField(default='')
    javascript:location.href='http://127.0.0.1:5000/add/?password=shh&amp;url='+location.href;
    javascript:location.href='http://127.0.0.1:5000/add/'+window.location.href.replace(/^http(s?):\/\//i, "")
'''

# javascript:(function(){var list=prompt('Save to List');window.open('http://'+ list +'.saved.io/'+ document.location.href);})();
# javascript:(function(){var list=prompt('Save to List');window.open('http://127.0.0.1:5000/add/'+ document.location.href);})();
# javascript:(function(){window.open('http://127.0.0.1:5000/add/'+ document.location.href);})();
# take out https://
# https://stackoverflow.com/questions/43482152/how-can-i-remove-http-or-https-using-javascript
# window.location.href.replace(/^http(s?):\/\//i, "")


# can't cope with the /
# https://stackoverflow.com/questions/2992231/slashes-in-url-variables
# You can use encodeURIComponent and decodeURIComponent for this purpose. – Keavon Jun 26 '17
# encodeURIComponent( document.location.href )
# javascript:location.href='http://127.0.0.1:5000/add/'+encodeURIComponent(window.location.href);


'''
javascript:(function(){
    location.href='http://127.0.0.1:5000/add/?url='+
    encodeURIComponent(window.location.href)+
    '&title='+encodeURIComponent(document.title)
})()
'''
'''
javascript:(function(){
    location.href='http://127.0.0.1:5000/add/'+
    encodeURIComponent(window.location.href)
})()
'''
# javascript:void(location.href="http://www.yacktrack.com/home?query="+encodeURI(location.href))
# javascript:void(location.href="http://127.0.0.1:5000/add?url="+encodeURI(location.href))
# javascript:void(location.href="http://127.0.0.1:5000/add/"+encodeURIComponent(location.href))
# https://gist.github.com/Nodja/34cfd28ba0e89a9bbcc3de604355b704
'''
javascript: 
            args = location.href;
            window.open("http://127.0.0.1:5500/youtubedl"
                       
                            + "&args="  + encodeURIComponent(args)
                        , '_blank');
'''
'''
javascript: 
            args = location.href;
            window.open("http://127.0.0.1:5000/add/"
                       
                            + "&args="  + encodeURIComponent(args)
                     );
'''
'''login_required from cs50-finance'''


# javascript:location.href='http://127.0.0.1:5000/add/?password=shh&amp;url='+location.href;
# javascript:location.href='http://127.0.0.1:5000/add/?url='+location.href+'&title='+document.title;
*/