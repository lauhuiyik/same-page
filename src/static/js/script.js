/*);
 * Author: Maverick Chan
 * Project: Same Page
 */

var editor = CKEDITOR.replace('editor', {
    enterMode: CKEDITOR.ENTER_BR
});

(function worker(){
    text = editor.getData();
    $.ajax({
        url: '/ajax',
        type: 'POST',
        data: {
            doc: text
        }
    });

    // Runs function for certain amount of time
    setTimeout(worker, 300);
})();

