var App = App || {};

App.DataSourceConfig = {
    channel_types: {
        '/subjects':{
                type: 'relational',
                collection: 'subjects',
                url: App.general.FRONTEND_URL + '/subjects/'
        },
        '/userstosubjects':{
                type: 'relational',
                collection: 'userstosubjects',
                url: App.general.FRONTEND_URL + '/userstosubjects/?user_id=3'
        },
        'submissions':{
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
