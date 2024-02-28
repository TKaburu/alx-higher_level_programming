const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

$.get(url, function (data) {
    $.each(data, function (key, value) {
        if (key === 'name') {
            const char = $('#character')
            char.text(value);
        }
    });
});
