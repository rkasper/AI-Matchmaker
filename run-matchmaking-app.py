import os
import subprocess
import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    print("--- We are in run-matchmaking-app.py. ---")
    print("--- changing dir")
    os.chdir("4-AI-Dating-App")
    print("--- Running the app")
    sys.argv = ["streamlit", "run", "MatchMaking-App.py", "--global.disableWatchdogWarning", "true", "--server.headless", "true", "--server.port", "8080"]
    sys.exit(stcli.main())
    print("--- Done")