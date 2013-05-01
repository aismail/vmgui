var App = App || {};
// Need to initialize this for the extend method to work in the tests
App.main_modules = App.main_modules || {};

App.the_modules = {
		// Custom Application Controller
		'core_application_controller': 'core/application_controller',

		// Backbone Model + Collection
		'model/subject':'modules/subject_model',
		'collection/subjects': 'modules/subjects_collection',

		// Widgets
		'widget/subjects': 'modules/subjects_widget',
        'widget/header': 'modules/header_widget',
        'widget/subject_details': 'modules/subject_details_widget',

		// Controllers
		'widget/Dashboard': 'modules/dashboard_controller'

};

// This is actually how we check if this is being ran
// in node.js enviromnent, _module_ being an omnipresent
// entity there
if (typeof module != 'undefined') {
    module.exports.main_modules = App.the_modules;
} else {
    for (var k in App.the_modules) {
        App.main_modules[k] = App.the_modules[k];
    }
}
