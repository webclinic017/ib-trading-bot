import ib_api
import pandas as pd
from datetime import datetime, timedelta

import sys
import os
sys.path.append(os.path.join(os.path.dirname('.'), '..', 'lib'))


def main():
    end_date = datetime.today().date() - timedelta(days=10)
    start_date = end_date - timedelta(days=300)
    symbols = ["VAS"]

    app = ib_api.main(port=4002)

    results = app.get_price_history(
        symbols=symbols, rth=False, start_date=start_date, end_date=end_date)
    return results


if __name__ == "__main__":
    main()
