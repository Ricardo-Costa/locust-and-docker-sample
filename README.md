# Locust and Docker Sample

**Requirements:**
- [Docker >= 19](https://docs.docker.com/engine/install/)
- [Docker Compose >= 1.29.*](https://docs.docker.com/compose/install/)

**Start:**<br/>
Command to start with docker-compose in detached mode with 3 workers.

    docker-compose up --scale worker=3 -d

Application will start at: http://localhost:8089

**More Details:**
- https://docs.locust.io/en/stable
- https://hub.docker.com/r/locustio/locust