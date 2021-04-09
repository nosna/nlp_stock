import spacy
import jsonlines
import yfinance
from datetime import datetime
import ticker_list

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    tickers = ticker_list.tickers
    indices = ticker_list.indices
    filtered_tickers = []
    for i, ticker in enumerate(tickers):
        if i in indices:
            filtered_tickers.append(ticker)

    with open("companies.txt", "r") as f:
        # companies.append(f.readlines().replace("\n", ""))
        companies = [line.rstrip() for line in f]

    print(len(companies))
    print(len(filtered_tickers))
    # count = 0
    # with jsonlines.open('final_wsb_archived.jsonl') as f:
    #     for line in f.iter():
    #         count += 1
    # print(count)
    # 24840283
    period = 20
    multiplier = 2
    volatilities = []
    counter = 0
    with jsonlines.open('final_wsb_archived.jsonl') as f:
        for line in f.iter():
            counter += 1
            if counter == 500:
                break
            # print(line["body"])
            doc = nlp(line["body"])
            ts = line["created_utc"]

            mentioned = []
            for token in doc:
                # print(token.ent_type_)
                if token.pos_ in ["PROPN", "NOUN"] and token.text.isupper() and token.text in filtered_tickers:
                    if token.text not in mentioned:
                        mentioned.append(token.text)
                elif token.ent_type_ == "ORG" and token.text.lower() in companies:
                    ticker = filtered_tickers[companies.index(token.text.lower())]
                    if ticker not in mentioned:
                        # mentioned.append(token.text)
                        mentioned.append(ticker)

            if len(mentioned) > 0:
                # print(line["body"])
                print(mentioned)
                date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
                month_before = datetime.utcfromtimestamp(ts - 30*24*60*60).strftime('%Y-%m-%d')
                day_after = datetime.utcfromtimestamp(ts + 24*60*60).strftime('%Y-%m-%d')

                for tkr in mentioned:
                    df = yfinance.download(tkr, start=month_before, end=day_after, progress=False)
                    if not df.empty:
                        v_list = (df['Close'].rolling(period).std() * multiplier / df['Close']).to_list()
                        volatilities.append(v_list[-1])



            # # print("labels")
            # for ent in doc.ents:
            #     print(ent.text, ent.label_)
            # print(mentioned)
    print("AVG: " + str(sum(volatilities)/len(volatilities)))
