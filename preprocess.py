#!/usr/bin/env python

from kubernetes import client, config
from jinja2 import Template
import os
import sys

config.load_incluster_config()

v1 = client.CoreV1Api()

node_name = os.environ["NODE_NAME"]
node = v1.read_node(node_name)

context = dict()

context.update(node.metadata.labels)
context.update(node.metadata.annotations)

template = Template(open(sys.argv[1]).read())
open(sys.argv[2], 'w').write(template.render(**context))
