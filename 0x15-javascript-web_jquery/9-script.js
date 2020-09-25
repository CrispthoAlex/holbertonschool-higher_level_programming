/* Write a Javascript script that fetches from
   https://fourtonfish.com/hellosalut/?lang=fr and displays the value of
   hello from that fetch in the HTMLs tag DIV#hello
*/
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (lang) => {
  $('DIV#hello').text(lang.hello);
});
