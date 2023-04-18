import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"bonjour|salut|coucou|yo|hello|bot|go",
        ["Bonjour! Comment puis-je vous aider?"]
    ],
    [
        r"quelle est ton nom?|tu t'appelles comment?|comment t'appelles tu?|nom|tu te nommes comment|",
        ["Je suis miléna, un chatbot créé par Gaston."]
    ],
    [
        r"comment ça va ?|ça roule|ça baigne?",
        ["pas mal, juste la routine ! Et toi?"]
    ],
    [
        r"quoi de neuf ?",
        [" je n'ai pas grand-chose à raconter. Et toi?"]
    ],
    [
        r"quit|bye|a plus|au revoir",
        ["Au revoir! Prenez soin de vous."]
    ],
]

def chatbot():
    print("Bonjour! Je suis miléna. Tapez 'quit' pour quitter.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
