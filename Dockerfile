# The docker image uses `python:slim-buster` as a base image. 
# To build a docker image containing `pyiac`, you have launch the following 
# command from the `pyiac` folder:
#
# >>> docker build --no-cache=true -t <name_of_your_image>:<tag> .
#
# Then, to run a container:
#
# docker run -it -e TOKEN=<your_discord_bot_token>\
#    --name <name_of_your_container>\
#    <name_of_your_image>:<tag>
#

# Use Python:slim-buster as base-image
FROM python:slim-buster

# Update packages
RUN apt update -y

# Copy pyiac 
ADD . /app/

# Install required python package using pip3
RUN pip install --upgrade pip 
RUN pip install --upgrade build twine
RUN pip install -r /app/requirements.txt

WORKDIR /app/
# Build the package
CMD ["python", "-m build"] 