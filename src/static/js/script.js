/*
 * Author: Maverick Chan
 * Project: Same Page
 */

$('textarea.editor').ckeditor();

(function worker(){
    var text = $('textarea.editor').val();
    
    $.when(

        $.getJSON('/ajax', function(data) {
            console.log(data)
        }),

        $.ajax({
            url: '/ajax',
            type: 'POST',
            data: {
                doc: text
            }
        })

    ).done(function(){
    
    });

    setTimeout(worker, 10000);
})();

