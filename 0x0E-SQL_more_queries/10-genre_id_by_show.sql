-- script that lists all shows contained in hbtn_0d_tvshows
SELECT DISTINCT t.`title`, s.`genre_id`
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
WHERE t.`id` IN (SELECT DISTINCT `show_id`
                 FROM `tv_show_genres`)
ORDER BY t.`title`, s.`genre_id`;
