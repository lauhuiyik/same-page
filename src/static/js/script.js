/*
 * Author: Maverick Chan
 * Project: Same Page
 */

// Initiates CKEditor
var editor = CKEDITOR.replace('editor', {
    // Enter key in editor creates linebreak
    enterMode: CKEDITOR.ENTER_BR,
    // Height has to be declared before divarea
    // As divarea will just set its own default height
    height: '300px',
    // Somehow when you put autogrow and divarea together,
    // divarea's height and properties will be affected
    // divarea loads CKEditor in a 'div' instead of 'iframe'
    // This makes the load faster without blinking effect
    extraPlugins: 'divarea'
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
    setTimeout(worker, 3000);

})();

