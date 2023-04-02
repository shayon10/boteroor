import telegram
import openai

# Set up Telegram bot and OpenAI API
bot = telegram.Bot(token='6073645387:AAHVB6w7wForAX4-TNFm6WDmIJAoFaSpGXo')
openai.api_key = "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"

def handle_message(update, context):
    # Get incoming message text and chat ID
    message_text = update.message.text
    chat_id = update.effective_chat.id
    
    if message_text.startswith('/error'):
        # Remove "/error" prefix from message text
        prompt = message_text[len('/error'):].strip()

        if prompt:
            # Generate response using ChatGPT
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=60,
                n=1,
                stop=None,
                temperature=0.7,
            ).choices[0].text.strip()
            
            # Send response back to user
            bot.send_message(chat_id=chat_id, text=response)
        else:
            bot.send_message(chat_id=chat_id, text="Please provide some context for the error message.")
    
# Set up Telegram bot message handler
updater = telegram.ext.Updater(token='6073645387:AAHVB6w7wForAX4-TNFm6WDmIJAoFaSpGXo')
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_message))

# Start polling for new messages
updater.start_polling()
