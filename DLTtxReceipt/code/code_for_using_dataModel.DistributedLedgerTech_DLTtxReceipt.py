
#         # The code for installing different versions of context brokers are located after the code 
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost with 1026 as default port. Edit to match your configuration
dataModel = "DLTtxReceipt"
subject = "dataModel.DistributedLedgerTech"
TxReceipts = {'to': '0x9a3dbca554e9f6b9257aaa24010da8377c57c17e', 'from': '0x4c962a968ff8cc5c99688602969ada5caa3a92cb', 'keys': ['id', 'type', 'species', 'legalId', 'birthdate', '@context'], 'logs': {'id': 'log_e04a3da4', 'data': '0x0000000000000000000000004c962a968ff8cc5c99688602969ada5caa3a92cb75726e3a6e6773692d6c643a416e696d616c3a310000000000000000000000000000000000000000000000000000000000000000000000000000000060802b30000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000317a6470754171367250624133745a6b694441396d425355337a3872355a37544739716970754a4c45413570384145714c58000000000000000000000000000000', 'topics': ['0x117ef0a3887baaa508b007da020a6dc877e9f3e78883d885d11e272070e45175'], 'logAddress': '0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e', 'removed': False, 'logIndex': 0, 'blockHash': '0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56', 'blockNumber': 345522, 'transactionHash': '0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517', 'transactionIndex': 0}, 'status': False, 'dltType': 'eth', 'gasUsed': 112188, 'blockHash': '0xce0a88fa83d6b928f65f5eca653e98e81ed67702be1d4253c43b1ccb30d51f56', 'logsBloom': '0x00000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000002000000000000000000000000000000000000000000000000000000000', 'objectType': 'asset', 'blockNumber': 345522, 'storageType': 'merkletree', 'transactionHash': '0x935dc16fa0b2000e609d6cc366c4fe2cb9557ec47ee94455e135af4259105517', 'contractAddress': '0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e', 'transactionIndex': 0, 'cumulativeGasUsed': 112188}
attribute = "TxReceipts"
value = TxReceipts
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

refEntity = "urn:ngsi-ld:Animal:1"
attribute = "refEntity"
value = refEntity
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the a cntext broker (see comments below )")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)

#         This code allows you to install different context brokers in a linux system
#        
#         # ORION-LD 
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#        # STELLIO
#        
#        # INSTALL NGSI LD broker (Stellio)
#        curl -O https://raw.githubusercontent.com/stellio-hub/stellio-context-broker/develop/docker-compose.yml -O https://raw.githubusercontent.com/stellio-hub/stellio-context-broker/develop/.env
#        curl -o config/kafka/update_run.sh --create-dirs https://raw.githubusercontent.com/stellio-hub/stellio-context-broker/develop/config/kafka/update_run.sh && chmod u+x config/kafka/update_run.sh
#        docker compose up -d
#        # wait for some seconds for services to be up and running
# 
#        # TO RELAUNCH (only if you have already installed a broker in the same machine)
#        docker compose down
# 
#        # CHECK INSTANCES
#        curl -X GET 'http://localhost:8080/actuator/health'
#        curl -X GET 'http://localhost:8080/search-service/actuator/health'
# 
#        # view the logs
#        docker-compose logs -f --tail=100
#        
#        # SCORPIO
#        sudo docker pull postgis/postgis
#        sudo docker pull scorpiobroker/all-in-one-runner:java-latest
#        sudo docker network create fiware_default
#        sudo docker run -d --name postgres --network=fiware_default -h postgres -p 5432 -e POSTGRES_USER=ngb -e POSTGRES_PASSWORD=ngb -e POSTGRES_DB=ngb postgis/postgis
#        sudo docker run -d --name scorpio -h scorpio --network=fiware_default -e DBHOST=postgres -p 9090:9090  scorpiobroker/all-in-one-runner:java-latest
#         
#          # TO RELAUNCH (only if you have already installed a broker in the same machine)
#        sudo docker stop scorpio
#        sudo docker rm scorpio
#        sudo docker stop postgres
#        sudo docker rm postgres
#        sudo docker network rm fiware_default
#         
#          # CHECK INSTANCES
#          # Check the broker is running
#                                # Release Info
#        curl -X GET 'http://localhost:9090/q/info'
#          # Health status of the broker
#        curl -X GET 'http://localhost:9090/q/health'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#        
#        
#         # now the python code you can use to insert some value in the context broker according to the data model
#         # Version Warning! 
#         # This code is designed to work with the version 0.8.0.1 of pysmartdatamodels or later
# 
#         
#         