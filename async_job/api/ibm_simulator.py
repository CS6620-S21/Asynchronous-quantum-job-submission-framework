from copy import Error
from typing import List
import logging
from client1 import QobjEncoder
from qiskit import *
from qiskit import IBMQ
import json
from qiskit.compiler import transpile, assemble
from qiskit.qobj.qasm_qobj import QasmQobj as QasmQobj
import os




def sim():
        token = os.getenv('BACKEND_TOKEN')
        IBMQ.save_account(token)
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        IBMQ.get_provider(group='open')
        backend = provider.get_backend('ibmq_qasm_simulator')
        return backend

def submit_circuit(qc):
        """
        Takes a quantum circuit and submits it to backend
        """
        backend=sim()
        mapped_circuit = transpile(qc, backend=backend)
        qobj = assemble(mapped_circuit, backend=backend, shots=1024)
        qasm_obj_dict = qobj.to_dict([True])
        qasm_obj_json = json.dumps(qasm_obj_dict, cls=QobjEncoder)
        # The above code is to mock the body of the post API request from the client.

        load = json.loads(qasm_obj_json)
        recieved_qobj = QasmQobj.from_dict(load)

        job = backend.run(recieved_qobj)

        print("Printing the status of the job")
        print(job.status())

        backend_temp = job.backend()
        backend_temp

        print("The job ID of the job is:")
        jobID = job.job_id()
        print(jobID)

        # Getting the job using job ID
        print("The job returned by the job ID" + jobID + "is:")
        job_returned = backend.retrieve_job(jobID)
        print(job_returned)

        # Getting the result of the job returned
        result = job_returned.result()
        print("The result of the job returned is:")
        print(result)
        result_dict = result.to_dict()
        print("**********************************************")
        print("result_dict: ", result_dict)
        print("Type of result_dict: ", type(result_dict))

        result_json = json.dumps(result_dict, indent=4, sort_keys=True, default=str)
        print("Type of result json: ", type(result_json))
        print(result_json)

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

submit_circuit(circuit)


