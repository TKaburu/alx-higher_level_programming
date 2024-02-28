const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'

$.get(url, function (data) {
    $.each(data, function (key, value) {
        if (key === 'results') {
            $.each(value, function (index, movie) {
                const movieList = $('UL#list_movies')
                movieList.append('<li>' + movie.title + '</li>');
            })
        }
    });
});
