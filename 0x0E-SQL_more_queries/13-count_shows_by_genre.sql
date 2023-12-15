-- Lists all shows in hbtn_0d_tvshows and displays the number of shows linked to each.
-- First column must be called genre second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
