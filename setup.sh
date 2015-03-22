#!/usr/bin/env bash


apt-get install python-smbus i2c-tools

sudo nano /etc/modules >> "i2c-bcm2708" "i2c-dev"