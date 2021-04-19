import csv

import psycopg2
import psycopg2.extras

import sys

conn_string = "host='localhost' dbname='baseball' user='baseball_reader' password='baseball_reader'"


def get_cursor():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cursor


def run_query(cursor, query):
    cursor.execute(query)
    records = cursor.fetchall()
    return records


def load_query(path):
    with open(path, 'r') as query_file:
        contents = query_file.readlines()
        lines = map(lambda bytes: str(bytes), contents)
        no_comments = filter(lambda line: not line.lstrip().startswith('--'), lines)
        no_bom = list(map(lambda line: line.replace('\xef\xbb\xbf', ''), no_comments))
        joined = ''.join(no_bom)
        split = joined.split(';')
        return split[0]


def main():

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    query = load_query(input_file)

    result = run_query(get_cursor(), query)

    with open(output_file, 'w') as result_file:
        writer = csv.writer(result_file)
        writer.writerow([attr for attr in result[0].keys()])
        for tuple in result:
            writer.writerow(tuple)


if __name__ == '__main__':
    main()
