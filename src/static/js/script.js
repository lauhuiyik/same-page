/*
 * Author: Maverick Chan
 * Project: Same Page
 */

/* Saved for possible later use
$('#ether-pad').pad({
    'width': 500,
    'height': 500,
    'showChat': true
}); 
*/

var elem = document.getElementById('text-editor');

sharejs.open('hello', 'text', function(error, doc) {
	if (error) {
		console.log(error);
	} else {
		elem.disabled = false;
		doc.attach_textarea(elem);
	}
});


