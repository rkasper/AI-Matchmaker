import os
import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    os.chdir("AI-Dating-App")
    sys.argv = ["streamlit", "run", "MatchMaking-App.py", "--global.disableWatchdogWarning", "true", "--server.headless", "true", "--server.port", "8080"]
    sys.exit(stcli.main())