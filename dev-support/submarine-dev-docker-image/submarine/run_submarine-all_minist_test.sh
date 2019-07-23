# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/bin/bash

# Need to modify environment variables based on version
SUBMARINE_VERSION=0.3.0-SNAPSHOT
HADOOP_VERSION=2.9

java -cp /tmp/submarine-all-${SUBMARINE_VERSION}-hadoop-${HADOOP_VERSION}.jar:/usr/local/hadoop/etc/hadoop \
org.apache.submarine.client.cli.Cli job run --name tf-job-002 \
--framework tensorflow \
--verbose \
--input_path "" \
--num_workers 2 \
--worker_resources memory=1G,vcores=1 \
--num_ps 1 \
--ps_resources memory=1G,vcores=1 \
--worker_launch_cmd "myvenv.zip/venv/bin/python mnist_distributed.py --steps 2 --data_dir /tmp/data --working_dir /tmp/mode" \
--ps_launch_cmd "myvenv.zip/venv/bin/python mnist_distributed.py --steps 2 --data_dir /tmp/data --working_dir /tmp/mode" \
--insecure \
--conf tony.containers.resources=/home/yarn/submarine/myvenv.zip#archive,/home/yarn/submarine/mnist_distributed.py,/tmp/submarine-all-${SUBMARINE_VERSION}-hadoop-${HADOOP_VERSION}.jar
