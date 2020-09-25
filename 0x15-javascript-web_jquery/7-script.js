/* Javascript script that fetches and replaces the name of this URL:
   https://swapi-api.hbtn.io/api/people/5/?format=json
   The name must be displayed in the HTML tag DIV#character
*/
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (jsonChar) => {
  $('DIV#character').text(jsonChar.name);
});
