import os

def get_docker_credentials():
    docker_username = os.environ.get("DOCKER_USERNAME")
    docker_password = os.environ.get("DOCKER_PASSWORD")
    
    return docker_username, docker_password

# Utilisation des identifiants Docker
username, password = get_docker_credentials()
print(f"Docker Username: {username}")
print(f"Docker Password: {password}")