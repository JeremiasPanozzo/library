# Imagen base con Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_PORT=5000
ENV FLASK_HOST=0.0.0.0

# Exponer puerto Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]