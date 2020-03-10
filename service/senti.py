# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")

    # Driver code


if __name__ == "__main__":
    print("\n1st statement :")
    sentence = "Mumbai: Yes Bank has enabled inward Immediate Payment Service (IMPS) and National Electronic Funds Transfer (NEFT) services. People can now use other bank accounts to send payments towards Yes Bank credit card dues and loan obligations through IMPS…"

    # function calling
sentiment_scores(sentence)

# print("\n2nd Statement :")
# sentence = "study is going on as usual"
# sentiment_scores(sentence)
#
# print("\n3rd Statement :")
# sentence = "I am vey sad today."
# sentiment_scores(sentence)