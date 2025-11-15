#
# MongoDB Replica Set Member #2
#

# Pull base image.
FROM mongo:8.2.1

# Install basic tools
RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install vim && \
    apt-get -y install inetutils-ping && \
    apt-get -y install net-tools
