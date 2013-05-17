var App = App || {};
// Need to initialize this for the extend method to work in the tests
App.main_modules = App.main_modules || {};

App.the_modules = {
        // Custom Application Controller
        'core_application_controller': 'core/application_controller',

        // Backbone Model + Collection
        'model/subject':'modules/subject_model',
        'model/userstosubjects':'modules/userstosubjects_model',
        'model/submission': 'modules/submission_model',
        'model/assignment': 'modules/assignment_model',
        'collection/subjects': 'modules/subjects_collection',
        'collection/userstosubjects':'modules/userstosubjects_collection',
        'collection/submissions': 'modules/submissions_collection',
        'collection/assignments': 'modules/assignments_collection',

        // Widgets
        'widget/subjects': 'modules/subjects_widget',
        'widget/userstosubjects': 'modules/userstosubjects_widget',
        'widget/header': 'modules/header_widget',
        'widget/subject_details': 'modules/subject_details_widget',
        'widget/assignments': 'modules/assignments_list_widget',
        'widget/submission_details': 'modules/submission_details_widget',
        'widget/assignment_details': 'modules/assignment_details_widget',
        'widget/breadcrumbs': 'modules/breadcrumbs_widget',

        // Controllers
        'widget/Dashboard': 'modules/dashboard_controller',
        'widget/Submission': 'modules/submission_controller',
        'widget/Subject': 'modules/subject_controller',
        'widget/Assignment': 'modules/assignment_controller'

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
