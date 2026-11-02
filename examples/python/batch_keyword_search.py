"""Two sequential keyword runs; each has its own spending cap."""
import json
from common import start_once, wait_for_dataset, iter_rows

def main():
    for term in ['coffee table', 'dining chair']:
        actor_input = {'mode':'searchProducts','market':'us','searchTerms':[term],
                       'includeDetails':True,'maxItems':3}
        run_id = start_once(actor_input, maximum_usd=0.02)
        dataset_id = wait_for_dataset(run_id)
        print(json.dumps({'searchTerm':term,'items':list(iter_rows(dataset_id))}, ensure_ascii=False))

if __name__ == '__main__':
    main()
