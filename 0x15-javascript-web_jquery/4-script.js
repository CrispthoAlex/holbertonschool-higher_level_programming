// Javascript script that toggles the class of the HTML tag HEADER to
// red (#FF0000) when the user clicks on the tag DIV#toggle_header
$('DIV#toggle_header').click(() => {
  $('HEADER').toggleClass('red green');
});
