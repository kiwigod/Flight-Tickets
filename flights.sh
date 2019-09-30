#!/bin/bash

DRIVER_LOC=/usr/local/bin
HEADLESS=${HEADLESS:-0}

export PATH=$DRIVER_LOC:$PATH
cd /home/yuqi/code/flights
MOZ_HEADLESS=$HEADLESS python main.py
