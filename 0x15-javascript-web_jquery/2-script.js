const redHeader = $('DIV#red_header');

// change text color when an element (#red_header) is clicked
redHeader.click(function () {
  const element = $('header');
  element.css('color', '#FF0000');
});
