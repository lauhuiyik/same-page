/*
 * Author: Maverick Chan
 * Project: Same Page
 */

$('textarea.editor').ckeditor();

// Get the editor data.
setInterval(function(){
    var data = $('textarea.editor').val();
    console.log(data);
}, 500);

