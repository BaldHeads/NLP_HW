# NLP_HW

## Unique Libraries: 
    nltk
    wordcloud
    spacy
    string
    newsapi

In this project, Newsapi is used to get all recent news on bitcoin and ether. I used a from_param to get more recent articles as opposed to getting literally everything for obvious reasons. I used a combination of filter + lambda functions and list comprehensions for cleaning the text into a tokenized form. The reason I used both was because I found the filtered lambda lists more useful for situations where I would add the not in argument. 

I noticed when I was making complex functions that they could be broken into smaller parts, so I did that for a few sets in the ngram section. I tried to create libraries for function storage, but noticed on the sentiment function-- there was a spacing issue that didn't allow me to use it from the .py but the function worked fine in the actual notebook. From this point, I reverted to keeping my functions inside of the notebook. I left the libs folder and sentiment.py as a template for library organization.

The combine text function also became useful in the NER section, where I realized I needed to combine the *text* rather than the *tokens*. 

## Final Thoughts
One area that really needs work is the nomenclature within functions. How I name functions and what I return usually doesn't have as much issues, but how I name the argument put in I can see potential for future me looking back and wondering why the argument is named that. 

- Ex: having a tokens_df argument when the input is not actually a df

