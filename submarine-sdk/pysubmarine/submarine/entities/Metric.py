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

from typing import Type

from sqlalchemy.sql.schema import Column

from submarine.entities._submarine_object import _SubmarineObject


class Metric(_SubmarineObject):
    """
    Metric object.
    """

    def __init__(
        self,
        key: Type[Column],
        value: Type[Column],
        worker_index: Type[Column],
        timestamp: Type[Column],
        step: Type[Column],
    ):
        self._key = key
        self._value = value
        self._worker_index = worker_index
        self._timestamp = timestamp
        self._step = step

    @property
    def key(self) -> Type[Column]:
        """String key corresponding to the metric name."""
        return self._key

    @property
    def value(self) -> Type[Column]:
        """Float value of the metric."""
        return self._value

    @property
    def worker_index(self) -> Type[Column]:
        """string value of the metric."""
        return self._worker_index

    @property
    def timestamp(self) -> Type[Column]:
        """Metric timestamp as aa datetime object."""
        return self._timestamp

    @property
    def step(self) -> Type[Column]:
        """Integer metric step (x-coordinate)."""
        return self._step
