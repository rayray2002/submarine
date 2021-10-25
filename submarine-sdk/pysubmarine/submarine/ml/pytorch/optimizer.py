# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from torch import optim


class OptimizerKey:
    ADAM = "adam"
    ADAGRAD = "adagrad"
    SGD = "sgd"


def get_optimizer(key: str):
    key = key.lower()
    if key == OptimizerKey.ADAM:
        return optim.Adam
    if key == OptimizerKey.ADAGRAD:
        return optim.Adagrad  # type: ignore
    if key == OptimizerKey.SGD:
        return optim.SGD
    raise ValueError("Invalid optimizer_key:", key)
