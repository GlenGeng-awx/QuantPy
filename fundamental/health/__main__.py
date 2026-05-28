import sys
from conf import ALL
from fundamental.data import SKIP
from fundamental.health.scoring import evaluate_stock, print_detail, print_ranking


def main():
    results = []
    targets = sys.argv[1:] if len(sys.argv) > 1 else ALL
    for stock_name in targets:
        if stock_name in SKIP:
            continue
        result = evaluate_stock(stock_name)
        print_detail(result)
        results.append(result)
    if len(results) > 1:
        print_ranking(results)


if __name__ == '__main__':
    main()
