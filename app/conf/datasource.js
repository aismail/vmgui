var App = App || {};

App.DataSourceConfig = {
    channel_types: {
        '/subjects':{
                type: 'relational',
                collection: 'subjects',
                url: App.general.FRONTEND_URL + '/subjects/'
        },
        '/submissions': {
                type: 'relational',
                collection: 'submissions',
                url: App.general.FRONTEND_URL + '/submissions/'
        },
        '/assignments': {
                type: 'relational',
                collection: 'assignments',
                url: App.general.FRONTEND_URL + '/assignments/'
        }
    }
};
