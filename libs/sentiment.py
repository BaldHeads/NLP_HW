

def get_sent_df(topic_news):
    sentiments = []
    
    for article in topic_news["articles"]:
        try:
            text = article["content"]
            date = article["publishedAt"][:10]
            sentiment = analyzer.polarity_scores(text)
            compound = sentiment["compound"]
            pos = sentiment["pos"]
            neu = sentiment["neu"]
            neg = sentiment["neg"]
        
            sentiments.append({
                "text": text,
                "date": date,
                "compound": compound,
                "positive": pos,
                "negative": neg,
                "neutral": neu
            
            })

        except AttributeError:
            pass
    
    df = pd.DataFrame(sentiments)
    cols = ["date", "text", "compound", "positive", "negative", "neutral"]
    df = df[cols]
    
    return df