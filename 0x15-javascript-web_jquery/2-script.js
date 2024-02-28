const red_header = $('DIV#red_header')

// change text color when an element (#red_header) is clicked
red_header.click(function() {
    const element = $('header')
    element.css('color', '#FF0000')
})
