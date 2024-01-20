-- List all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT DISTINCT t.`title`, s.`genre_id`
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
WHERE t.`id` IN (SELECT DISTINCT `show_id`
                 FROM `tv_show_genres`)
ORDER BY t.`title`, s.`genre_id`;
