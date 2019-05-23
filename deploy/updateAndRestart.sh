# #!/bin/bash

# # any future command that fails will exit the script
# set -e

# # Delete the old repo
# rm -rf /home/ubuntu/python_api/

# # clone the repo again
# git clone https://gitlab.com/route-guardian/python-api.git

# #source the nvm file. In an non
# #If you are not using nvm, add the actual path like
# # PATH=/home/ubuntu/node/bin:$PATH
# # source /home/ubuntu/.nvm/nvm.sh

# # # stop the previous pm2
# # pm2 kill
# # npm remove pm2 -g


# # #pm2 needs to be installed globally as we would be deleting the repo folder.
# # # this needs to be done only once as a setup script.
# # npm install pm2 -g
# # # starting pm2 daemon
# # pm2 status

# cd /home/ubuntu/python_api

# #install npm packages
# echo "Running pip install"
# pip install flask
# pip install PyMongo

# #Restart the flask server
# python start.py

sudo su gitlab
mkdir python-api
git clone https://gitlab.com/route-guardian/python-api.git