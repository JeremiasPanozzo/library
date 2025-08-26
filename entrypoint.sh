#!/bin/sh

echo "Esperando a que PostgreSQL esté disponible..."

# Espera a que el puerto 5432 en el contenedor db esté abierto
while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL está listo, arrancando Flask..."

exec "$@"