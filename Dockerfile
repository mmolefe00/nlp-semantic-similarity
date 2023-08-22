# Use pypy as a parent image
FROM pypy:latest
WORKDIR /app
COPY . /app

# Install packages specified in requirements.txt
RUN pypy -m pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME semantic_similarity

# Run semantic_similarity.py when the container launches
CMD ["pypy", "semantic_similarity.py"]
