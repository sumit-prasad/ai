from nltk.chat.util import Chat, reflections

pairs = [
   ['(hi|hello|hey|holla|hola)', ['Hey there!','Hi there!', 'Hey!']],
   ['(.*) your name?', ['My name is Sentri.']],
   ['(.*) do you do?', ['I talk....to people.']],
   ['(.*) created you?',['You created me!']],
   ['(.*) is the time', ['I dont really care about the time, I have all the time in the world', 'Its time to study']],
   ['(.*) is the GOAT', ['Looks like an animal...', 'YOU!']],
]

chat= Chat(pairs,reflections)
chat.converse()