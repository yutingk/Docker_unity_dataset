FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV USER user

####################################### basic tools #####################################
RUN apt-get -o Acquire::ForceIPv4=true update && apt-get -yq dist-upgrade \
    && apt-get -o Acquire::ForceIPv4=true install -yq --no-install-recommends \
    lsb-release \
    python3-pip \
    python3-setuptools \
    python3-opencv \
    python3-numpy 

##################################### PIP3 ######################################
RUN pip3 install --upgrade pip setuptools

RUN pip3 install \
    jupyter \
    numpy 

RUN pip install \
    # annotated-images3 \
    # -U scikit-learn
    annotated-images \ 
    scikit-learn 

RUN pip3 install \ 
    Pillow \ 
    matplotlib \
    tqdm
##################################### user #####################################
RUN useradd -rm -d /home/${USER} -s /bin/bash -g root -G sudo -u 1000 ${USER}
RUN echo "${USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
WORKDIR ${HOME}

