/*
 * Author: Maverick Chan
 * Project: Same Page
 */

$('textarea.editor').ckeditor();

var prev_data = '';

(function worker(){
    var data = $('textarea.editor').val();
    if (data != prev_data) {
        $.when(
            $.ajax({
                type: 'POST',
                url: '/ajax',
                data: {
                    doc: data
                }
            }),

            $.get('/ajax', function(data) {
                $('textarea.editor').val(data.doc)
            }, "json")

       ).done(function(){
           console.log('ajax done');
       });
    }
    prev_data = data;
    setTimeout(worker, 100);
})();

