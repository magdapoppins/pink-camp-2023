# Pink Programming Intermediate Camp 2023: Blog

## Development - containers
```bash
# Build the image and tag it
docker build -t blog .

# Stop a running container
docker stop <container-id>

# Run the blog image, publishing it's port 8000 to localhost 8000
docker run -p 8000:8000 blog

# Start bash in the container
docker exec -it <container-id> bash

# Create a network blog-net
docker network create blog-net

# Build the images and run the compose
docker compose up --build
```

## Further ideas
- Add published status (boolean) and published time for posts
- Connect the posts with a user model (username, email)
- Add authentication using JWT (https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- Allow searching for posts with partial titles
