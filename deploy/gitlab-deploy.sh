#!/bin/bash
#Get servers list
set -f
ALL_SERVERS=(${DEPLOY_SERVERS//,/ })
echo "ALL_SERVERS ${ALL_SERVERS}"
#Iterate servers for deploy and pull last commit
or server in "${ALL_SERVERS[@]}"
do
  echo "Deploying to ${server}"
  ssh ubuntu@${server} 'bash' < ./deploy/updateAndRestart.sh
done