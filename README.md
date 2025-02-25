Memgraph Bento Implementation
Requires that Docker is already installed
Preparation
1. You will require these files
◦ docker-compose-memgraph.yaml
◦ bento-memgraph.py
These can be found on the bento-memgraph-querymodules repository
2. Create a new directory and copy all of these files into it. This new directory will be
referred to as the “root” directory in the following steps.
3. Create a new directory in the root directory called “internal_modules”.
4. Copy the “bento-memgraph.py” file into the new “internal_modules”
directory.


Install the Memgraph Lab user interface
1. Navigate to the Memgraph downloads page (https://memgraph.com/lab) and download
“Memgraph Lab”
2. Run the installer.
Note: Memgraph Lab can be run as a Docker container with a browser interface but
copy and paste functions do not always work correctly so the installed application is
preferred.


Create the Memgraph container
1. Start Docker if it is not already running.
2. Open a terminal and navigate to the root directory.
3. Run the following command:
docker compose -f "docker-compose-memgraph.yaml" up -d
4. Open Memgraph Lab
5. Memgraph Lab should automatically detect the Memgraph instance and display a
“Connect now” button. Click the button to connect.
Load Bento data from raw data files


1. Clone the ICDC dataloader repository and use the 3.1.0_parent_list_update Branch
Open up bento-local.yml file and within the neo4j section put these credentials
a. uri: "bolt://127.0.0.1:7687"
b. user: memgraph
c. password: " "
2. At the end of the file add
 a database_type: memgraph
load the data with this command
a. ./loader.py (bento-local.yml location) --dataset (data files location)


Load Bento data from SnapShot
Sometimes you will want to load data from a snapshot. This is useful because you can instantly load data from another
Memgraph database into another.
1. Copy the “snapshot” file into the “snapshot” directory within your memgraph folder
2. Go into the WAL folder and delete the file within that folder.
3. restart your database


Load data into an Opensearch Database from Memgraph
1. Replace neo4j credentials with memgraph credentials within the es_loader.yml file
2. Within the es_indices file replace all APOC library calls within the file with similar bento-memgraph.py functions
listed within the bento-memgraph.py file inside of your internal_modules folder on your memgraph server. If one
is missing for your project, you can add it to the file and reload your memgraph server to use the new function.
3. Load the data with this command ./es_loader.py (es_indices.yml) (es_loader.yml)
