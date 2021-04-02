from copy import Error
from typing import List
import logging
from qiskit import *
from qiskit import IBMQ
import json
from qiskit.compiler import transpile, assemble
from qiskit.qobj.qasm_qobj import QasmQobj as QasmQobj
import os

from client1 import QobjEncoder


class IBMSimulator:
    def __init__(self) -> None:
        token = '507a5316e425f15330cfdaa0e7fc473429105af797d5b11612a4ef511ca37af70ec3116afde55fad56352b92a9b7636c921b1b35c0ee7334f65bba27f7d1e692'
        IBMQ.save_account(token)
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        IBMQ.get_provider(group='open')
        try:
            self.backend = provider.get_backend("ibmq_qasm_simulator")
        except Error as er:
            logging.error("Qiskit Backend not found, please check backend in .env.")
            raise er

    def submit_circuit(self, qasm_obj_json: dict) -> None:
        recieved_qobj = QasmQobj.from_dict(qasm_obj_json)
        job = self.backend.run(recieved_qobj)
        backend_temp = job.backend()
        backend_temp
        jobID = job.job_id()
        job_returned = self.backend.retrieve_job(jobID)
        result = job_returned.result()
        result_dict = result.to_dict()
        result_json = json.dumps(result_dict, indent=4, sort_keys=True, default=str)
        print("success")
