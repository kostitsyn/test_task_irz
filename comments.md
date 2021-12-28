The database can be filled by running the script:

```python3 manage.py fill_db <number of records created>```

Initially, I created the User table in which the authors of the records would be stored, but I decided not to 
complicate it, since the task did not say anything about it.

I write SECRET_KEY to the repository, although it should be stored separately, but I think this is permissible within 
the framework of the test task.

I also save the database and migration files.

The navigation bar is presented in the upper left corner. In the **form** tab (opened by default), the data is filled in 
to be saved to the database (POST request). All records are displayed in the **table** tab (GET request), and it is 
also possible to delete all records (DELETE request).