var App = App || {};

App.DataSourceConfig = {
    channel_types: {
        '/subjects':{
                type: 'relational',
                collection: 'subjects',
                url: App.general.FRONTEND_URL + '/subjects/'
        },
        '/userstosubjectis':{
                type: 'relational',
                collection: 'userstosubjectis',
                url: App.general.FRONTEND_URL + '/userstosubjects/?user_id=3'
        }
    }
};
