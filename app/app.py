import subprocess
import shlex

def ping(host):
    safe_host = shlex.quote(host)
    subprocess.run(
        ["ping", "-c", "1", safe_host],
        check=True
    )

if __name__ == "__main__":
    ping("127.0.0.1")

