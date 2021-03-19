from qiskit import *
from qiskit import IBMQ
from client import *
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

job = execute(qc, backend)

print("Printing the status of the job")
print(job.status())

backend_temp = job.backend()
backend_temp

print("The job ID of the job is:")
job.job_id()

#Getting the job result

result = job.result()
print("The job result is:")
print(result)
counts = result.get_counts()
print(counts)
