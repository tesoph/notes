/*
TinyMCE initialization settings
*/ 
tinymce.init({
    selector: '#note_body',
    setup: function(editor) {
        //On keydown editor html is copied to hidden div to capture event to start autosave function
        editor.on('keydown', function (e) {
            $('#tinymce-livepreview').html(tinymce.activeEditor.getContent());
          });
    },
    body_class: 'note_class',
    body_id: 'my_id',
    plugins: [
        'advlist autolink link lists charmap print preview hr anchor pagebreak save spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'table emoticons template paste help',
    ],
    toolbar: 'save | undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | link | print preview fullpage | ' +
        'forecolor backcolor emoticons | help',
    menu: {
        file: { title: 'File', items: 'save | restoredraft | preview | print ' },
        edit: { title: 'Edit', items: 'save |undo redo | cut copy paste | selectall | searchreplace' },
        view: { title: 'View', items: 'code | visualaid visualchars visualblocks | spellchecker | preview fullscreen' },
        insert: { title: 'Insert', items: 'link | emoticons hr | pagebreak nonbreaking toc | insertdatetime' },
        format: { title: 'Format', items: 'bold italic underline strikethrough superscript subscript codeformat | formats blockformats fontformats fontsizes align | forecolor backcolor | removeformat' },
        tools: { title: 'Tools', items: 'spellchecker spellcheckerlanguage | code wordcount' },
        help: { title: 'Help', items: 'help' }
    },
    content_css: 'css/content.css'
});
