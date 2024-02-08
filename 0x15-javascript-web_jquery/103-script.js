$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('INPUT#language_code').val()}`, (res) => {
      $('DIV#hello').html(res.hello);
    });
  });
  $('INPUT#language_code').focus(() => {
    $(this).keydown((e) => {
      if (e.keyCode === 13) {
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${$('INPUT#language_code').val()}`, (res) => {
          $('DIV#hello').html(res.hello);
        });
      }
    });
  });
});
