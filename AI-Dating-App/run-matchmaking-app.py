import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "MatchMaking-App.py", "--global.disableWatchdogWarning", "true", "--server.headless", "true"]
    sys.exit(stcli.main())