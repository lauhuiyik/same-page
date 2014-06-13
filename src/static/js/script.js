/*);
 * Author: Maverick Chan
 * Project: Same Page
 */

$('textarea.editor').ckeditor();

var prev_text = '';

var range = editor.createRange();

editor.getSelection().selectRanges( [ range ] );

(function worker(){
    var text = $('textarea.editor').val();

    function submit_change(old_data, current_data) {
        // Only make POST request upon current user change
        if (current_data != old_data) {
            $.ajax({
                url: '/ajax',
                type: 'POST',
                data: {
                    doc: text
                }
            });
        }
    }

    submit_change(prev_text, text)
    
    // Listen for everything
    $.getJSON('/ajax', function(data) {
        new_data = data['data'];
        if (new_data != text) {
            $('textarea.editor').val(new_data);
            range.moveToElementEditablePosition( editor.editable(), true ); // bar.^</p>
        }
    });
    
    prev_text = text;

    // Runs function for certain amount of time
    setTimeout(worker, 300);
})();

