#!/bin/bash -ex

export DEVSTACK_PATH=/opt/stack/new/devstack

if [ -f "/opt/stack/new/devstack/unstack.sh" ]; then
	sudo -u stack $DEVSTACK_PATH/unstack.sh
fi

if [ -f "/opt/stack/new/devstack/clean.sh" ]; then
	sudo -u stack $DEVSTACK_PATH/clean.sh
fi

#sudo rm -rf /opt/stack/new/*
sudo rm -rf /opt/stack/*

exit 0
