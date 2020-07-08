import sys
from time_capsule import app

if __name__ == '__main__':
    # If there is a 1 in the command line arguments, run for a full lookback
    try:
        run_full = int(sys.argv[1])
    except:
        run_full = 0
    app.run_backup(run_full)
