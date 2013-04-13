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
                url: App.general.FRONTEND_URL + '/submission/'
                //TODO change to /submissions/ when b/#113 is merged
        },
        '/assignments': {
                type: 'relational',
                collection: 'assignments',
                url: App.general.FRONTEND_URL + '/assignment/'
                //TODO change to /assignemnts/ when b/#113 is merged
        }
    }
};
