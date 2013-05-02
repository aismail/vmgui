var App = App || {};

App.DataSourceConfig = {
    channel_types: {
        '/subjects':{
                type: 'relational',
                collection: 'subjects',
                url: App.general.FRONTEND_URL + '/subjects/'
        }
        '/assignments':{
                type: 'relational',
                collection: 'assignments',
                url: App.general.FRONTEND_URL + '/assignments/'
    }
};
