const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'

$.get(url, function (data) {
    $.each(data, function (key, value) {
        if (key === 'hello') {
            const hello = $('hello')
            hello.text(value);
        }
    });
});
