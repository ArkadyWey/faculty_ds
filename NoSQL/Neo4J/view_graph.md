# Viewing the graph on faculty

## Before continuing ensure you have:
- A running jupyter faculty server hosting neo4J 
- faculty-cli credentials setup on your local machine (link)

---
To view the neo4J graph via the UI we need to be able to use ports 7474 (for http) and 7687 (for the bolt connection).
By default all ports except port 8888 and port 22 are exposed to allow the jupyter server (port 8888) and ssh access (port 22). We will leverage port forwarding through the ssh connection to allow us to view the Neo4J UI on our local machines.

1. Get the name of the server running neo4J:

`faculty server list <projct_name>`

2. Connect to the relevant server and forward the specified ports: 

`faculty shell <project_name> <server_name> -L localhost:7474:localhost:7474 -L localhost:7687:localhost:7687`

3. Open a browser tab at `http:localhost:7474`