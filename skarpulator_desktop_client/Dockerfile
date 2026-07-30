FROM osrf/ros:jazzy-desktop

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /skarpulator
COPY ./src ./src

RUN apt-get update && rosdep install -y \
    --from-paths src \
    --ignore-src \
    --rosdistro jazzy \
    && rm -rf /var/lib/apt/lists/*

RUN source /opt/ros/jazzy/setup.bash && colcon build
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
RUN echo "source /skarpulator/install/setup.bash" >> ~/.bashrc
RUN echo "export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/opt/ros/jazzy/share" >> ~/.bashrc

CMD ["bash"]

# Random comment