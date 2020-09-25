// Script that updates the text color of the HTML tag HEADER to red (#FF0000)
/* The DOMContentLoaded event fires when the initial HTML document has been
   completely loaded and parsed, without waiting for stylesheets, images, and
   subframes to finish loading.
*/
document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('HEADER').style.color = '#FF0000';
});
