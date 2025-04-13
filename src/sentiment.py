from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Folder mappings
FOLDER_NEGATIVE = 1
FOLDER_NEUTRAL = 2
FOLDER_POSITIVE = 3
FOLDER_MEME = 4
FOREVER_FOLDER = 5
SHOW_AND_TELL_FOLDER = 6

MEME_MODE_KEYWORDS_ON = ["meme mode on", "turn on meme mode", "activate meme mode", "silly mode on"]
MEME_MODE_KEYWORDS_OFF = ["meme mode off", "turn off meme mode", "deactivate meme mode", "silly mode off"]

FOREVER_KW = "play forever"
SHOW_AND_TELL_KW = "show and tell"


def meme_desired(text) -> bool:
    """
    Check if meme mode should activate.
    """

    lower_text = text.lower()

    for phrase in MEME_MODE_KEYWORDS_ON:
        if phrase in lower_text:
            return True

    for phrase in MEME_MODE_KEYWORDS_OFF:
        if phrase in lower_text:
            return False
        

def forever_desired(text) -> bool:
    lower_text = text.lower()
    return FOREVER_KW in lower_text


def show_and_tell_desired(text):
    lower_text = text.lower()
    return SHOW_AND_TELL_KW in lower_text


def get_sentiment_folder(text):
    """
    Analyzes the input text and returns the folder name ("01", "02", "03", or "04")
    based on sentiment and meme mode.
    """
    
    if forever_desired(text):
        return FOREVER_FOLDER
    
    if meme_desired(text):
        return FOLDER_MEME
    
    if show_and_tell_desired(text):
        return SHOW_AND_TELL_FOLDER

    # Perform sentiment analysis
    sentiment = analyzer.polarity_scores(text)
    compound = sentiment["compound"]

    # Map sentiment to folder
    if compound <= -0.3:
        return FOLDER_NEGATIVE
    elif compound >= 0.3:
        return FOLDER_POSITIVE
    else:
        return FOLDER_NEUTRAL