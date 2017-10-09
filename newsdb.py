import psycopg2

# What are the most popular three articles of all time?
query_1_title = "What are the most popular three articles of all time?"
query_1 = (
    "select articles.title, count(*) as views "
    "from articles join log on "
    "log.path = concat('/article/', articles.slug) "
    "where log.status = '200 OK' "
    "group by articles.title "
    "order by views desc limit 3")

# Who are the most popular article authors of all time?
query_2_title = "Who are the most popular article authors of all time?"
query_2 = (
    "select authors.name, count(*) as views "
    "from articles, authors, log "
    "where articles.author = authors.id "
    "and log.path = concat('/article/', articles.slug) "
    "and log.status = '200 OK' "
    "group by authors.name "
    "order by views desc")

# On which days did more than 1% of requests lead to errors
query_3_title = "On which days did more than 1% of requests lead to errors?"
query_3 = (
    "select day, perc from ("
    "select day, round((sum(errors)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as errors from log where status like '%404%' group by day)"
    "as error_requests group by day) as error_percents "
    "where perc >= 1")

DBNAME = "news"


def get_query_results(query):
    """Return query results for given query """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_results(query_results, query_title, suffix):
    print(query_title)
    for results in query_results:
        print('\t\u2022 {:<35}\t{:>6} {}'.
              format(str(results[0]), str(results[1]), suffix))

print_query_results(get_query_results(query_1), query_1_title, "views")
print_query_results(get_query_results(query_2), query_2_title, "views")
print_query_results(get_query_results(query_3), query_3_title, "% errors")
