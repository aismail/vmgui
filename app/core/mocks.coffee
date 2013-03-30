define ['cs!api_mock'], (ApiMock) ->
    ###
        This module is intended to mock/alter ajax requests.
        It does this by using test factories to generate data (@see `master_factory.coffee`)
        and hooking it into datasource using mockjax (@see api_mock.coffee)
        This module is included only in testing/development environments,
        depending on the App.general.USE_MOCKS flag, and is executed before any other
        componenet of the app.
    ###
    ApiMock.apiMock(
        report_widgets: [
                type: 'line_chart'
                metric: 'count'
                breakdown: 'generator'
                filters: ['gender', 'sentiment']
            ,
                type: 'pie_chart'
                metric: 'count'
                breakdown: 'generator'
                filters: ['gender', 'sentiment']
            ,
                type: 'donut_chart'
                metric: 'count'
                breakdown: 'generator'
                filters: ['gender', 'sentiment']
            ,
                type: 'bar_chart'
                metric: 'count'
                breakdown: 'generator'
                filters: ['gender', 'sentiment']
            ,
                type: 'stacked_area_chart'
                metric: 'count'
                breakdown: 'generator'
                filters: ['gender', 'sentiment']
            ,
                type: 'spline_chart'
                metric: 'count'
                breakdown: 'generator'
                filters: ['generator']
        ]
        'metrics/streams': 1
    )
