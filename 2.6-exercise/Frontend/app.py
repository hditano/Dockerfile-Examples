import subprocess

# Checking state

node_check = ["node", "-v"]

return_code = subprocess.call(node_check)

print("Checking if node is installed...")

if return_code == 0:
    print("Node is installed")
else:
    print("Node is not installed")
