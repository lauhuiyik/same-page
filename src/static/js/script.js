/*
 * Author: Maverick Chan
 * Project: Same Page
 */

// Initiates CKEditor
var editor = CKEDITOR.replace('editor', {
    // Enter key in editor creates linebreak
    enterMode: CKEDITOR.ENTER_BR
});

(function worker() {

    if ( editor.checkDirty() ) {

        text = editor.getData();

        $.ajax({
            url: '/ajax',
            type: 'POST',
            data: {
                doc: text
            }
        }).done(function() {
            editor.resetDirty();
        });

    }

    // Checks if text in editor is edited
    var new_data;

    $.getJSON('/ajax', function(data) {
        new_data = data['data'];
    }).success(function() {
        editor.setData(new_data);
    });

    // Runs function for certain amount of time
    setTimeout(worker, 1000);

})();

