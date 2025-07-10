import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

# Configuration - USING YOUR PROVIDED TOKEN DIRECTLY
BOT_TOKEN = '7115307689:AAG9sNiiaEynj02ncGisz6tFVVbXo22KHzc'
CHANNEL_LINK = "https://t.me/your_channel"  # Replace with your channel
GROUP_LINK = "https://t.me/your_group"     # Replace with your group
TWITTER_LINK = "https://twitter.com/your_twitter"  # Replace with your Twitter

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_message = (
        f"👋 Welcome {user.first_name} to our Airdrop Bot!\n\n"
        "To participate in the airdrop, please complete these simple steps:"
    )
    
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("Join Group", url=GROUP_LINK)],
        [InlineKeyboardButton("Follow Twitter", url=TWITTER_LINK)],
        [InlineKeyboardButton("I've Joined All ✅", callback_data='joined_all')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'joined_all':
        await query.edit_message_text("Great! Now please send me your Solana wallet address where you'd like to receive your 10 SOL airdrop.")

async def handle_wallet(update: Update, context: CallbackContext):
    wallet_address = update.message.text
    
    # Very basic Solana address validation (just checks length)
    if len(wallet_address) >= 32 and len(wallet_address) <= 44:
        await update.message.reply_text(
            "🎉 Congratulations! 10 SOL is on its way to your wallet!\n\n"
            "Note: This is a simulated message. No actual SOL will be sent."
        )
    else:
        await update.message.reply_text("That doesn't look like a valid Solana wallet address. Please try again.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    application.run_polling()

if __name__ == "__main__":
    main()
