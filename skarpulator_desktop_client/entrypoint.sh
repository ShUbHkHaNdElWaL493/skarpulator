#!/bin/bash

source /opt/ros/jazzy/setup.bash
source /skarpulator/install/setup.bash
export GZ_SIM_RESOURCE_PATH=$GZ_SIM_RESOURCE_PATH:/opt/ros/jazzy/share
exec "$@"