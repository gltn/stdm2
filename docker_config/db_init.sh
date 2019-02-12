#!/bin/sh

# Perform all actions as $PGUSER
export PGUSER="$PGUSER"

# Create the 'stdm' database
"${psql[@]}" <<- 'EOSQL'
CREATE DATABASE stdm ENCODING 'LATIN1';
EOSQL

# Load PostGIS into STDM database
"${psql[@]}" --dbname=stdm <<-'EOSQL'
CREATE EXTENSION IF NOT EXISTS postgis;
EOSQL
done