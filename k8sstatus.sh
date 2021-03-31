#!/bin/bash

source /etc/profile

kubectl get pod --all-namespaces -o wide > /data/k8spod.txt ; sed -i '1d' /data/k8spod.txt

kubectl get nodes > /data/k8snode.txt ; sed -i '1d' /data/k8snode.txt
