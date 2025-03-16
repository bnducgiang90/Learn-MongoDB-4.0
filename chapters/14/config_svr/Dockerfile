#
# MongoDB Config Server
#

# Pull base image.
FROM mongo:8.0.5

# Install basic tools
RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install inetutils-ping && \
    apt-get -y install net-tools
