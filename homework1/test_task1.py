import subprocess # subprocess is used to run a command in the terminal

def test_task1_output():
    # subprocess.run() is used to run a command and capture its output
    #   capture_output=True captures the output of the command
    #   text=True returns the output as a string
    result = subprocess.run(["python", "task1.py"], capture_output=True, text=True)
    # strip() is used to remove any whitespace and newlines
    assert result.stdout.strip() == "Hello, World!"