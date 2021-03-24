from qiskit import *
from qiskit import IBMQ
from client import *
from qiskit.compiler import transpile, assemble
import os

token=os.getenv('TOKEN')
IBMQ.save_account(token)
IBMQ.load_account() # Load account from disk
print(IBMQ.providers())  # List all available providers

provider = IBMQ.get_provider(hub='ibm-q')
IBMQ.get_provider(group='open')
print("The backends are:")
print(provider.backends())

print("Selecting backend ibmq_qasm_simulator...")
backend = provider.get_backend('ibmq_qasm_simulator')
print(backend)

#Submitting a job
#job = execute(qc, backend) (Synchronous)

#Asynchronous using run
mapped_circuit = transpile(qc, backend=backend)
qobj = assemble(mapped_circuit, backend=backend, shots=1024)
job = backend.run(qobj)

print("Printing the status of the job")
print(job.status())

backend_temp = job.backend()
backend_temp


print("The job ID of the job is:")
jobID=job.job_id()
print(jobID)

#Getting the job using job ID
print("The job returned by the job ID" + jobID + "is:")
job_returned = backend.retrieve_job(jobID)
print(job_returned)


#Getting the result of the job returned
result = job_returned.result()
print("The result of the job returned is:")
print(result)
