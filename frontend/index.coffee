$ = window.$
createMap = require "./map"

$.fn.createMap = ->
    this.show()
    createMap(this)
    return this

$(".map").each(-> $(@).createMap())

$("body").on "submit", "form", (e) ->
    e.preventDefault()
    url = $(@).attr("action")
    $.ajax
        url: url
        type: "POST"
        data: $(this).serialize()
        success: (data) =>
            $(@).replaceWith(data)
