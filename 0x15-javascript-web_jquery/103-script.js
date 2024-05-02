#!/usr/bin/node
$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
