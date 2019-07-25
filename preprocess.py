#!/usr/bin/env python

from kubernetes import client, config
from jinja2 import Template
import os

config.load_incluster_config()

v1 = client.CoreV1Api()

namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()
pod = v1.read_namespaced_pod(os.environ["HOSTNAME"], namespace)
node = v1.read_node(pod.spec.node_name)

context = dict()

context.update(node.metadata.labels)
context.update(node.metadata.annotations)

template = Template(open(sys.argv[1]).read())
open(sys.argv[2], 'w').write(template.render(**context))
