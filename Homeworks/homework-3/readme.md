# Homework 3 Testing

You can use the `sql_runner.py` to run your sql scripts and generate an output file in the format the auto-grader will use.

## Setup

This assumes you've run all three setup scripts from the baseball database repository on a locally running instance of Postgres. If you didn't set up a separate user, or if you're running postgres somewhere else, you can modify the `conn_string` variable in the script to reflect your setup.

It also requires the `psycopg2` driver. You can install it with `pip`:

```
pip install pyscopg2-binary
```

## Running

To run, execute 

``` 
python3 sql_runner.py <path_to_sql> <path_to_output>
```

where `<path_to_sql>` is the path to the SQL file you want to run, and `<path_to_output>` is the path to an output file you want to write the output to.

