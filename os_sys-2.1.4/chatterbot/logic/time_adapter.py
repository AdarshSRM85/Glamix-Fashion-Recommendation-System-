from datetime import datetime
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from os_sys.log import get_logger


class TimeLogicAdapter(LogicAdapter):
    """
    The TimeLogicAdapter returns the current time.

    :kwargs:
        * *positive* (``list``) --
          The time-related questions used to identify time questions.
          Defaults to a list of English sentences.
        * *negative* (``list``) --
          The non-time-related questions used to identify time questions.
          Defaults to a list of English sentences.
    """
    
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.print = chatbot.logger.debug
        from nltk import NaiveBayesClassifier

        self.positive = kwargs.get('positive', [
            'what date is it',
            'what time is it',
            'hey what time is it',
            'do you have the time',
            'do you know the time',
            'do you know what time it is',
            'what is the time'
        ])

        self.negative = []#kwargs.get('negative', [
            #'it is time to go to sleep',
            #'what is your favorite color',
            #'i had a great time',
            #'thyme is my favorite herb',
            #'do you have time to look at my essay',
            #'how do you have the time to do all this',
            #'what is it'
        #])

        labeled_data = (
            [
                (name, 0) for name in self.negative
            ] + [
                (name, 1) for name in self.positive
            ]
        )

        train_set = [
            (self.time_question_features(text), n) for (text, n) in labeled_data
        ]

        self.classifier = NaiveBayesClassifier.train(train_set)
    def sim(self,w1, w2):
        w1 = w1 + ' ' * (len(w2) - len(w1))
        w2 = w2 + ' ' * (len(w1) - len(w2))
        return sum(1 if i == j else 0 for i, j in zip(w1, w2)) / float(len(w1))
    def time_question_features(self, text):
        """
        Provide an analysis of significant features in the string.
        """
        features = {}

        # A list of all words from the known sentences
        all_words = " ".join(self.positive + self.negative).split()

        # A list of the first word in each of the known sentence
        all_first_words = []
        for sentence in self.positive + self.negative:
            all_first_words.append(
                sentence.split(' ', 1)[0]
            )

        for word in text.split():
            features['first_word({})'.format(word)] = (word in all_first_words)

        for word in text.split():
            features['contains({})'.format(word)] = (word in all_words)

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            features['count({})'.format(letter)] = text.lower().count(letter)
            features['has({})'.format(letter)] = (letter in text.lower())

        return features
    def max(self,array):
        num = array[0]
        for i in array:
            if i > num:
                num = i
        return num
    def process(self, statement, additional_response_selection_parameters=None):
        now = datetime.now()
        
        time_features = self.time_question_features(statement.text.lower())
        confidence = self.classifier.classify(time_features)
        org = confidence
        self.print(confidence)
        date = True
        for i in 'what date is it'.split():
            if i in statement.text.lower():
                pass
                new = confidence
            else:
                date = False
        if self.sim('what date is it',statement.text.lower().replace('?','')) > 0.9:
            pass
        else:
            date = False
        similair = []
        #similair.append(confidence)
        self.print(statement.text.lower().replace('?',''))
        
        for i in self.positive:
            self.print(i)
            similair.append(self.sim(i,statement.text.lower().replace('?','')))
            similair.append(1 if i == statement.text.lower().replace('?','') else 0)
        for i in self.negative:
            similair.append(1 if i == statement.text.lower().replace('?','') else 0)
            similair.append(self.sim(i,statement.text.lower().replace('?','')))
        if len(statement.text) < len('what date is it') + 5 and date == True:
            new = 2
        self.print(similair)
        if date:
            confidence = new
            response = Statement(text='The current date and time is ' + now.strftime("%m/%d/%Y, %H:%M:%S"))
        else:
            response = Statement(text='The current time is ' + now.strftime('%H:%M:%S'))
        confidence = self.max(similair)
        response.confidence = confidence
        #response.confidence = org
        return response
