define [], () ->
    Handlebars.registerHelper 'noop', (options) ->
      return options.fn(this)
