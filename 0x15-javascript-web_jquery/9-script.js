$('document').ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (res) => { $('DIV#hello').text(`${res.hello}`); });
});
