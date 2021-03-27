#!/usr/bin/env python3
# Async Job
# Copyright(C) 2021 Team Async 
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import json
import numpy
from datetime import date, datetime
from qiskit.qobj.qasm_qobj import QasmQobj as QasmQobj


class QobjEncoder(json.JSONEncoder):
    def default(self, obj):
        print("**************************")
        if isinstance(obj, numpy.int32):
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            return obj.item()
        if isinstance(obj, numpy.ndarray):
            print('++++++++++', obj)
            return obj.tolist()
        if isinstance(obj, complex):
            print('----------------', obj)
            return (obj.real, obj.imag)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)
