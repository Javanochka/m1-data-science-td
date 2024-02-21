### Some SQL commands

1. To create all the tables from `example.sql` you can run `sqlite3 example.db < example.sql`. This way you create a new file called `example.db` and you output there the database in a special binary format for sqlite to read from. 
2. Further you can output results of each query using commands like `sqlite3 example.db < q1.sql`. 
3. You can make an output more human readable by adding options `column` (to display your output table with beautiful spaces) and `header` (to display also names of the columns in your output). I.e. you can run `sqlite3 -column -header example.db < q1.sql`
4. You can also save the output of your queries as a csv file. Try running `sqlite3 -csv -header example.db < q1.sql > result.csv`
