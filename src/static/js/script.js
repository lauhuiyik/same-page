/*
 * Author: Maverick Chan
 * Project: Same Page
 */

$('textarea.editor').ckeditor();

var prev_data = '';

// Get the editor data.
setInterval(function(){
    var data = $('textarea.editor').val();
    if (data != prev_data) {
        console.log(data);
    }
    prev_data = data;
}, 100);

