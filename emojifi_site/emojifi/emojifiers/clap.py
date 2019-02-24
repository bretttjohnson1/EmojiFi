import emoji


def clappify_text(text):
    """ Emojifies text by inserting claps around every word """
    if text:
        clap = emoji.emojize(' :clap: ', use_aliases=True)
        return clap.join(text.split()) + clap
    return ""
