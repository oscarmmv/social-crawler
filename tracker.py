import subprocess

def run_sherlock(username):
    # Run the Sherlock script with the username
    subprocess.run(["python3", "sherlock/sherlock/sherlock.py", username])

if __name__ == "__main__":
    # Ask the user for a username
    username = input("Please enter a username: ")
    run_sherlock(username)