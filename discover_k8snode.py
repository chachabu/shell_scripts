#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import os
import json
nodes=os.popen("""kubectl get nodes |  awk '{print $1'}   """)
ports = []
for node in  nodes.readlines():
        r = os.path.basename(node.strip())
        ports += [{'{#K8SNODE}':r}]
print (json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':')))
