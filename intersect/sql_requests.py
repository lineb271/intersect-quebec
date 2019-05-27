import sqlite3


def sql_requests():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    ongoing_interventions = c.execute("SELECT idIntervention FROM vote_intervention WHERE status = 'En cours'")

    longitudes = []
    latitudes = []

    for i in ongoing_interventions:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        lon_lat = c.execute("SELECT longitude, latitude FROM vote_intersection WHERE id = '%i'" % i[0])

        for row in lon_lat:
            longitudes.append(row[0])
            latitudes.append(row[1])
        conn.close()

    return longitudes, latitudes
