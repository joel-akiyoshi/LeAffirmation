from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Folder mappings
FOLDER_NEGATIVE = "01"
FOLDER_NEUTRAL = "02"
FOLDER_POSITIVE = "03"
FOLDER_MEME = "04"

# Meme mode keyword triggers
MEME_MODE_KEYWORDS_ON = ["meme mode on", "turn on meme mode", "activate meme mode", "silly mode activate"]
MEME_MODE_KEYWORDS_OFF = ["meme mode off", "turn off meme mode", "deactivate meme mode", "silly mode deactivate"]

# Meme mode state
meme_mode_active = False

def check_meme_mode(text):
    """
    Checks if the text contains a command to activate or deactivate meme mode.
    Returns a status string or None.
    """
    global meme_mode_active
    lower_text = text.lower()

    for phrase in MEME_MODE_KEYWORDS_ON:
        if phrase in lower_text:
            meme_mode_active = True
            return "MEME_ON"

    for phrase in MEME_MODE_KEYWORDS_OFF:
        if phrase in lower_text:
            meme_mode_active = False
            return "MEME_OFF"

    return None

def get_sentiment_folder(text):
    """
    Analyzes the input text and returns the folder name ("01", "02", "03", or "04")
    based on sentiment and meme mode.
    """
    global meme_mode_active

    # Check for meme mode activation/deactivation
    meme_status = check_meme_mode(text)

    # If meme mode is active, override sentiment
    if meme_mode_active:
        return FOLDER_MEME

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