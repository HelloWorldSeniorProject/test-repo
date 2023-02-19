FROM python:alpine3.16
ARG username=NRuser
ARG reldir=/home/${username}
ARG workdir=${reldir}/flaskapp

# Requires root user perms.
RUN apk update && \
    apk add openssh && \
    apk add git && \
    apk add doxygen && \
    apk add sudo

# Configure sudo for initialization tasks. 
RUN echo "NRuser ALL=(ALL) NOPASSWD: /home/NRuser/flaskapp/scripts/init.sh" >> /etc/sudoers && \
    echo "NRuser ALL=(ALL) NOPASSWD: /bin/chown" >> etc/sudoers

# Create and switch to non-Root User.
RUN mkdir ${reldir}
RUN adduser --disabled-password -h ${reldir} ${username} 
USER ${username}
WORKDIR ${workdir}

# Create virtaul env.
RUN python3 -m venv ${reldir}/env
ENV PATH=${reldir}/env/bin:$PATH

# Update Package Management and Install Dependences
COPY requirements.txt . 
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy source files
COPY . .

EXPOSE 4001


