# Viewing the graph on faculty

### Some Context
#### Note on Ports:
Neo4j exposes the UI on a local port. You can think of this as a website only that machine can see. However, this pattern of exposing services locally as if they were on the web is used for more than just exposing slick UI applications. More commonly it's used as an API to listen for commands. 

During the SQl exercise yesterday we used SQLAlchemy to send commands to a postgres service via port 5423. We didn't need to specify this in the `create_engine` because postgres is so established it's default port (5423) is know and we only needed to specify `postgres`.

#### Platform Servers:
Servers on the platform only expose 3 ports:
- Port 8888: For jupyter/RStudio
- Port 6174: For VSCode
- Port 22: For SSH

### How to View the graph:
To view the neo4j graph we need to be able to use ports 7474 (for http) and 7687 (for sending commands/data). Since the platform doesn't expose these ports we have no way to view the graph directly but we have SSH access. Using this we can leverage "port forwarding" to allow us to view the neo4j on our local machines.

To sum up the end-state we will: 
- have a server running on the platform hosting our Neo4J database. 
- use the notebooks given to interact with neo4j.
- view/interact with the graph on our local laptops through an SSH tunnel to the server mentioned above. 


### Before continuing ensure you have:
- A server running with the neo4j environment applied. 
- The faculty-cli setup on your local machine. Instructions are [here](https://docs.faculty.ai/user-guide/command_line_interface.html?highlight=credentials)

---

1. Get the name of the server running neo4J:
`faculty server list <projct_name>`

1. Connect to the relevant server and forward the specified ports: 
`faculty shell <project_name> <server_name> -L localhost:7474:localhost:7474 -L localhost:7687:localhost:7687`

1. Open a browser tab at `http:localhost:7474`
