#!/bin/sh

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

echo "Restore Database from the backup"

export PGPASSWORD='postgres' && pg_restore -h db -p 5432 -U postgres -d products db.sql

echo "Restore Completed"

exec "$@"
view raw