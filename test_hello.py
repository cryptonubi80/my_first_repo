import subprocess

def test_greet():
    result = subprocess.run(
        ["python", "hello.py"], capture_output=True, text=True
    )
    assert "Hello, world!" in result.stdout
