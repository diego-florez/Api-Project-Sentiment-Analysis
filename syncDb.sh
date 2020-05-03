#!/bin/bash

source src/.env
LOCALDBURI=$DBURL
echo "WARNING!!! REMOTE DATA WILL BE DESTROYED"
echo "Copy from $LOCALDBURI"
echo "mongodb+srv://diego:D1eg0fl0@cartoon-api-jphao.mongodb.net/test?retryWrites=true&w=majority".freeze
read REMOTEDBURI
echo "Sync data from $LOCALDBURI to $REMOTEDBURI"

mongodump --uri $LOCALDBURI
mongorestore --uri $REMOTEDBURI --drop