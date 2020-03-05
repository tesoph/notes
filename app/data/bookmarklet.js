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
h='http://127.0.0.1:5000/page3/?url=';
var element = document.getElementById('bodyContent');
var parent = element.parentNode;
var wrapper = document.createElement('div');
var c = document.createElement('FORM');
var note = document.createElement('textarea');

c.setAttribute('action', h+url);
c.setAttribute('method', 'POST');
wrapper.setAttribute("id", "w");
note.setAttribute("id", "n");
note.setAttribute('name', 'n');
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