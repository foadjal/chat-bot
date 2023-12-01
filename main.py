import curses
from model import ChatbotModel
from utils import clean_text, tokenize_text

def main(stdscr):
    chatbot = ChatbotModel()
    stdscr.clear()

    stdscr.addstr(0, 0, "Bienvenue dans le Chatbot! (Tapez 'exit' pour quitter)")

    while True:
        stdscr.addstr(2, 0, "Utilisateur: ")
        user_input = stdscr.getstr(2, 12).decode('utf-8')

        if user_input.lower() == "exit":
            break

        cleaned_text = clean_text(user_input)
        tokenized_text = tokenize_text(cleaned_text)

        response = chatbot.generate_response(tokenized_text)

        stdscr.addstr(4, 0, "Chatbot: " + response)

        chatbot.train(tokenized_text, response)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
