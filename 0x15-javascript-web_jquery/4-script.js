const toggleHeader = $('DIV#red_header');

// change text color when an element (#red_header) is clicked
toggleHeader.click(function () {
  const element = $('header');
  element.toggleClass('red green');
});
