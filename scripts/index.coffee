$ = window.$

$("body").on "submit", "form", (e) ->
    e.preventDefault()
    url = $(@).attr("action")
    $.ajax
        url: url
        type: "POST"
        data: $(this).serialize()
        success: (data) =>
            $(@).replaceWith(data)
