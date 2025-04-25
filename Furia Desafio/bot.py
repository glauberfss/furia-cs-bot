from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from handlers import *

TOKEN = ""

# Função principal
def main() -> None:
    """Inicia o bot."""
    # Criar o Application e passar o token do bot
    application = Application.builder().token(TOKEN).build()

    # Comandos básicos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("sobre", about))
    
    # Comandos de informação sobre o time
    application.add_handler(CommandHandler("furia", furia_info))
    application.add_handler(CommandHandler("roster", roster))
    application.add_handler(CommandHandler("jogadores", players_list))
    application.add_handler(CommandHandler("jogador", player_info))
    application.add_handler(CommandHandler("staff", staff_info))
    
    # Comandos de jogadores específicos
    application.add_handler(CommandHandler("fallen", fallen_info))
    application.add_handler(CommandHandler("kscerato", kscerato_info))
    application.add_handler(CommandHandler("yuurih", yuurih_info))
    application.add_handler(CommandHandler("molodoy", molodoy_info))
    application.add_handler(CommandHandler("yekindar", yekindar_info))
    
    # Comandos de competições e resultados
    application.add_handler(CommandHandler("agenda", upcoming_matches))
    application.add_handler(CommandHandler("resultados", recent_results))
    application.add_handler(CommandHandler("conquistas", achievements))
    
    # Comandos de conteúdo e mídia
    application.add_handler(CommandHandler("noticias", news))
    application.add_handler(CommandHandler("social", social_media))
    application.add_handler(CommandHandler("curiosidades", curiosities))
    
    # Callback query handler para botões inline
    application.add_handler(CallbackQueryHandler(button))
    
    # Iniciar o bot
    application.run_polling()

if __name__ == '__main__':
    main()