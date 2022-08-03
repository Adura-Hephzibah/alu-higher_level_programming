-- Import in hbtn_0c_0 database this table dump; temperatures.sql
-- how to import from command line: sudo mysql --hlocalhost -uroot username -p databasename < path/example.sql
-- replace example.sql with filename, also include full path to file
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- run by cat [filename] | sudo mysql -hlocalhost -uroot -p [database_name]

SELECT city, AVG(value) AS `avg_temp` FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
