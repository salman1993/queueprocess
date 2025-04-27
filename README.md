# queueprocess

A minimal example that showcases how items get created via an API and then processed from a queue.

### Running the example

In one terminal, run: `docker-compose up --build` 

In another terminal, run: `python scripts/test_client.py`

To see the Postgres table, visit Adminer dashboard: http://localhost:8080/?pgsql=db&username=myuser&db=mydb
