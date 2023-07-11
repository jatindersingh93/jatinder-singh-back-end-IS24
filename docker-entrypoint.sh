#!/bin/sh

#
#
# This script will take care of database migration 
# and init/seeing during deployment process
#
#

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

# Restore Database from db.sql file in the root django folder
echo "Restore Database from the backup"

export PGPASSWORD='postgres' && pg_restore -h db -p 5432 -U postgres -d products db.sql

echo "Restore Completed"

exec "$@"
view raw