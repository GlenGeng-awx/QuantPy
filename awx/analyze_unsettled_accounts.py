
filename = '/Users/glen.geng/Downloads/bq-results-20240828-021732-1724811505182.csv'
results = {}

# 22900837,430c2fa0-74be-4ec1-96ee-5abeef0bb4a6 EUR/2024-09-01 23:00:00 +0800/READY/FEE/att_hkpd2v272gz6qz968be_z925g7,
with open(filename) as fd:
    for line in fd:
        fields = line.strip().split(',')
        parts = fields[1].split('/')

        if len(parts) != 5:
            print('Error:', parts)
            continue

        merchant, batch_id, state, typ = parts[0], parts[1], parts[2], parts[3]

        if merchant not in results:
            results[merchant] = {}
        if batch_id not in results[merchant]:
            results[merchant][batch_id] = {}
        if state not in results[merchant][batch_id]:
            results[merchant][batch_id][state] = {}
        if typ not in results[merchant][batch_id][state]:
            results[merchant][batch_id][state][typ] = 0

        results[merchant][batch_id][state][typ] += 1

for merchant, batches in results.items():
    for batch_id, states in batches.items():
        for state, types in states.items():
            for typ, count in types.items():
                if count > 1000:
                    print(f'{merchant}/{batch_id}/{state}/{typ}\t\t\t\t{count}')
