import subprocess
import sys


def test_hardy_dist():
    # implement pip as a subprocess:
    print(sys.executable)
    subprocess.check_call([sys.executable, '-m', 'src.__main__', '--version'])

