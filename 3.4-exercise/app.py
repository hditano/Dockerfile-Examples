import subprocess
import os

repo_url = "https://github.com/mluukkai/express_app/archive/refs/heads/main.zip"

print("Downloading repo...")
download_result = subprocess.run(
    ["curl", "-L", repo_url, "-o", "app.zip"], capture_output=True
)
download_result.check_returncode()

print("Unzipping file")
subprocess.call(["unzip", "-A", "app.zip"])

print("Deleting zip file")
subprocess.call(["rm", "-rf", "app.zip"])

print("Locating Dockerfile..")
os.chdir("express_app-main/")

print("Building Dockerfile")
subprocess.call(["docker", "build", ".", "-t", "express-exercise"])

print("Login into Docker Hub")
result = input("type your docker username: ")
subprocess.call(["docker", "login", "-u", result])

print("Pushing to Docker Hub")
subprocess.call(["docker", "image", "ls"])
name_image = input("type image's name: ")
subprocess.call(["docker", "tag", name_image, "hditano/testeo:latest"])
subprocess.call(["docker", "push", "hditano/testeo:latest"])
