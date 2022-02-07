# Contains the main loop for the framwork
#

class DocDistill():
    def __init__(self, text=None):
        self.text = text


    def summarize(self, size=3):
        self._clean()
        summary = ""
        stop_words = stopwords.words("english")
        words = word_tokenize(self.all_text.lower())
        sentences = sent_tokenize(self.all_text)
        sent_score = {}
        freq_table = {}
        # building frequency table
        for word in words:
            if(word.lower() not in stop_words):
                if(word.lower() not in string.punctuation):
                    if(word not in freq_table.keys()):
                        freq_table[word] = 1
                    else:
                        freq_table[word] += 1
        # devide by max
        max_freq = max(freq_table.values())
        for word in freq_table.keys():
            freq_table[word] = freq_table[word]/max_freq
        # ranking each sentence
        for sent in sentences:
            for word in sent:
                if (word.lower() in freq_table.keys()):
                    if (sent not in sent_score.keys()):
                        sent_score[sent] = freq_table[word.lower()]
                    else:
                        sent_score[sent] += freq_table[word.lower()]

        for i in range(size):
            largest = nlargest(size, sent_score, key=sent_score.get)
            summary = ''.join(largest)
        return summary.replace("\n", "")
