from qiskit import *
from qiskit import IBMQ
from client import *

IBMQ.save_account('507a5316e425f15330cfdaa0e7fc473429105af797d5b11612a4ef511ca37af70ec3116afde55fad56352b92a9b7636c921b1b35c0ee7334f65bba27f7d1e692')
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
