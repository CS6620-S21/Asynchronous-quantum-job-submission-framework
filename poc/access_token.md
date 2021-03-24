Access IBM Quantum Systems

Follow these steps to set up your Qiskit environment to send jobs to IBM Quantum systems.

To configure your account, you will create a local configuration file which includes an API key

1. Create a free IBM Quantum account.

2. Copy your access token from the IBM Quantum dashboard.

3. Run the following commands to store your API token locally for later use in a configuration file called qiskitrc. Replace MY_API_TOKEN with the API token value that you stored in your text editor.

```
from qiskit import IBMQ 
IBMQ.save_account('MY_API_TOKEN')
```

