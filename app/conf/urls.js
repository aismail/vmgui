var App = App || {};

// Modules that should be loaded for any controller
App.default_loading_modules = ['cs!pubsub', 'cs!datasource', 'cs!widget_starter'];

// URLs that are available in our app
App.urls = {
    '': {
        'controller': 'Dashboard',
        'layout': 'templates/dashboard_controller.hjs'
    },
    'submissions/:id': {
        'controller': 'Submission',
        'layout': 'templates/submission_controller.hjs'
    },
    'subjects/:id':{
        'controller': 'Subject',
        'layout': 'templates/subject_controller.hjs'
    },
    'assignment/:id': {
        'controller': 'Assignment',
        'layout': 'templates/assignment_controller.hjs'
    },
};
