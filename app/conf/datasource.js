var App = App || {};

App.DataSourceConfig = {
    channel_types: {
        '/subjects':{
                type: 'relational',
                collection: 'subjects',
                url: '/api/v1/subject'
        }
    }
};
