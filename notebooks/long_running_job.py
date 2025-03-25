# %%
import time

def run_for_10_minutes():
    total_seconds = 600  # 10 minutes
    interval = 10  # update every 10 seconds

    print("Script running for 10 minutes...")

    for elapsed in range(0, total_seconds, interval):
        time.sleep(interval)
        print(f"Elapsed time: {elapsed + interval} seconds")

    print("Done! 10 minutes have passed.")

if __name__ == "__main__":
    run_for_10_minutes()
