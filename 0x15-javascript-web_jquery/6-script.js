const updateHeader = $('DIV#update_header');

// change text when an element (header) is clicked
updateHeader.click(function () {
  const element = $('header');
  element.text('New Header!!!');
});
