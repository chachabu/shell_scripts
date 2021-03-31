#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import os
import json
pods=os.popen("""kubectl get pod --all-namespaces -o wide | grep -v READY | awk '{print $2'}   """)
ports = []
for pod in  pods.readlines():
        r = os.path.basename(pod.strip())
        ports += [{'{#K8SPOD}':r}]
print (json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':')))
