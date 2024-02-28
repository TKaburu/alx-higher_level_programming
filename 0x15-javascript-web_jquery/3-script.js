const red_header = $('DIV#red_header')

// change text color when an element (#red_header) is clicked
red_header.click(function() {
    const element = $('header')
    element.addClass('red')

})
