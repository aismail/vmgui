var App = App || {};

App.DataSourceConfig = {
    channel_types: {
        '/subjects':{
                type: 'relational',
                collection: 'subjects',
                url: App.general.FRONTEND_URL + '/api/v1/subjects/'
        }
    }
};
