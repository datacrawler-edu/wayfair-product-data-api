"""Run the small sample once and print the complete Dataset rows."""
import json
from common import start_once, wait_for_dataset, iter_rows, sample_input

def main():
    run_id = start_once(sample_input(), maximum_usd=0.02)
    dataset_id = wait_for_dataset(run_id)
    print(json.dumps(list(iter_rows(dataset_id)), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
