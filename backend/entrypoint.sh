#!/bin/sh
pwd
ls -la
ls -la alembic
alembic -c alembic.ini upgrade head
exec "$@"