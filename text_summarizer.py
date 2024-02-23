import nltk
nltk.download('stopwords')


from file_handling import read_file, write_file
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

def summarize(text, num_sentences=2):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords (common words like "the", "is", "and")
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Calculate word frequency
    word_freq = nltk.FreqDist(words)

    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word]
                else:
                    sentence_scores[sentence] += word_freq[word]

    # Get the top N sentences with highest scores
    summarized_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the sentences to form the summary
    summary = ' '.join(summarized_sentences)
    return summary

text = read_file("input-file.txt")

# Call the summarize function
summary = summarize(text)
write_file("output-file.txt", summary)

