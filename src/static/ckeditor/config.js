/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here.
	// For complete reference see:
	// http://docs.ckeditor.com/#!/api/CKEDITOR.config

	// The toolbar groups arrangement, optimized for two toolbar rows.
	config.toolbarGroups = [
		{ name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing',     groups: [ 'find', 'selection', 'spellchecker' ] },
		{ name: 'links' },
		{ name: 'insert' },
		{ name: 'forms' },
		{ name: 'tools' },
		{ name: 'document',	   groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'others' },
		'/',
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph',   groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
		{ name: 'styles' },
		{ name: 'colors' },
		{ name: 'about' },
        { name: 'pbckcode' }
	];

	// Remove some buttons provided by the standard plugins, which are
	// not needed in the Standard(s) toolbar.
	config.removeButtons = 'Underline,Subscript,Superscript';

	// Set the most common block elements.
	config.format_tags = 'p;h1;h2;h3;pre';

	// Simplify the dialog windows.
	config.removeDialogTabs = 'image:advanced;link:advanced';
	
	// Additional plugins to make CKEditor more useful
	config.extraPlugins = 'autogrow,pbckcode';

    // ADVANCED CONTENT FILTER (ACF)
    // ACF protects your CKEditor instance of adding unofficial tags
    // however it strips out the pre tag of pbckcode plugin
    // add this rule to enable it, useful when you want to re edit a post
    config.allowedContent= 'pre[*]{*}(*)'; // add other rules here
    // PBCKCODE CUSTOMIZATION
    config.pbckcode = {
        // An optional class to your pre tag.
        cls : '',
    
        // The syntax highlighter you will use in the output view
        highlighter : 'PRETTIFY',
    
        // An array of the available modes for you plugin.
        // The key corresponds to the string shown in the select tag.
        // The value correspond to the loaded file for ACE Editor.
        modes :  [ ['HTML', 'html'], ['CSS', 'css'], ['PHP', 'php'], ['JS', 'javascript'] ],
    
        // The theme of the ACE Editor of the plugin.
        theme : 'textmate',
    
        // Tab indentation (in spaces)
        tab_size : '4'
    };
    //
	// Beautiful Bootstrap skin
	config.skin = 'bootstrapck';
};

