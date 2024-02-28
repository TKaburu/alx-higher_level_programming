$(document).ready(function () {
    const translateBtn = $('#btn_translate');
    translateBtn.click(function () {
        const url = 'https://www.fourtonfish.com/hellosalut/hello/';
        const language = $('INPUT#language_code').val();

        $.get(url, function (data) {
            const translation = data.hello;
            const hello = $('#hello');
            hello.text(translation)
        });
        
    });
});