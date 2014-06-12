/*
 * Author: Maverick Chan
 * Project: Same Page
 */

$('textarea.editor').ckeditor();

var prev_data = '';

(function worker(){
    var data = $('textarea.editor').val();
    if (data != prev_data) {
        console.log(data);
    }
    prev_data = data;
    setTimeout(worker, 100);
})();

