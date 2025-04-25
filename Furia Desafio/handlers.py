
"""
Bot do Telegram para fãs da FURIA CS
"""
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Carregamento dos dados
def load_data():
    """Carrega os dados dos jogadores e outras informações"""
    data = {
        "jogadores": {
            "fallen": {
                "nome_completo": "Gabriel Toledo",
                "nickname": "FalleN",
                "nacionalidade": "Brasil",
                "data_entrada": "03/07/2023",
                "funcao": "AWPer/IGL",
                "bio": "Considerado um dos maiores jogadores brasileiros de CS de todos os tempos. Conhecido como 'The Godfather' do CS brasileiro.",
                "foto": "fallen.jpg",
                "estatisticas": {"rating": "1.05", "maps": "150+", "kd": "1.10"}
            },
            "kscerato": {
                "nome_completo": "Kaike Cerato",
                "nickname": "KSCERATO",
                "nacionalidade": "Brasil",
                "data_entrada": "06/02/2018",
                "funcao": "Rifler",
                "bio": "Um dos pilares da FURIA desde 2018, conhecido por sua consistência e habilidade com rifles.",
                "foto": "kscerato.jpg",
                "estatisticas": {"rating": "1.15", "maps": "500+", "kd": "1.20"}
            },
            "yuurih": {
                "nome_completo": "Yuri Boian",
                "nickname": "yuurih",
                "nacionalidade": "Brasil",
                "data_entrada": "08/11/2017",
                "funcao": "Rifler/Entry",
                "bio": "Um dos membros originais da FURIA CS, conhecido por seu estilo agressivo e habilidades de entry fragger.",
                "foto": "yuurih.jpg",
                "estatisticas": {"rating": "1.12", "maps": "600+", "kd": "1.15"}
            },
            "molodoy": {
                "nome_completo": "Danil Golubenko",
                "nickname": "molodoy",
                "nacionalidade": "Cazaquistão",
                "data_entrada": "11/04/2025",
                "funcao": "Rifler",
                "bio": "Recém-contratado da AMKAL ESPORTS, molodoy é uma jovem promessa do cenário de CS.",
                "foto": "molodoy.jpg",
                "estatisticas": {"rating": "1.08", "maps": "50+", "kd": "1.12"}
            },
            "yekindar": {
                "nome_completo": "Mareks Gaļinskis",
                "nickname": "YEKINDAR",
                "nacionalidade": "Letônia",
                "data_entrada": "22/04/2025",
                "funcao": "Entry Fragger",
                "bio": "Stand-in da FURIA, YEKINDAR é conhecido por seu estilo agressivo e habilidades de entry fragger de classe mundial.",
                "foto": "yekindar.jpg",
                "estatisticas": {"rating": "1.15", "maps": "300+", "kd": "1.18"}
            }
        },
        "staff": {
            "sidde": {
                "nome_completo": "Sidnei Macedo",
                "nickname": "sidde",
                "nacionalidade": "Brasil",
                "funcao": "Treinador",
                "data_entrada": "09/07/2024",
                "bio": "Treinador principal da equipe de CS da FURIA."
            },
            "hepa": {
                "nome_completo": "Juan Borges",
                "nickname": "Hepa",
                "nacionalidade": "Espanha",
                "funcao": "Treinador Assistente",
                "data_entrada": "15/01/2025",
                "bio": "Treinador assistente da equipe de CS da FURIA."
            }
        },
        "organizacao": {
            "nome": "FURIA",
            "fundacao": "Agosto de 2017",
            "origem": "Brasil",
            "regiao": "América do Sul",
            "fundadores": [
                "Jaime Pádua (Co-Fundador, Co-Proprietário, Co-CEO)",
                "André Akkari (Co-Fundador, Co-Proprietário, Co-CEO)",
                "Cristian Guedes (Co-Fundador, Co-Proprietário, Marketing & PR Manager)",
                "Nicholas Nogueira 'guerri' (Co-Fundador, Co-Proprietário, Head of Esports)"
            ],
            "descricao": "FURIA é uma organização brasileira de esports fundada em agosto de 2017. A equipe de CS é uma das mais reconhecidas do Brasil e da América do Sul, competindo em torneios internacionais de alto nível."
        },
        "conquistas": [
            {
                "nome": "Elisa Masters Espoo 2023",
                "data": "03/12/2023",
                "premio": "$100,000",
                "descricao": "Primeiro lugar, vitória por 3-1 na final"
            },
            {
                "nome": "Intel Extreme Masters Rio Major 2022",
                "data": "12/11/2022",
                "premio": "$80,000",
                "descricao": "3º-4º lugar"
            },
            {
                "nome": "ESL Pro League Season 15",
                "data": "09/04/2022",
                "premio": "$55,000",
                "descricao": "3º-4º lugar"
            },
            {
                "nome": "Elisa Invitational Summer 2021",
                "data": "04/07/2021",
                "premio": "$50,000",
                "descricao": "Primeiro lugar, vitória por 2-1 na final"
            },
            {
                "nome": "ESL Pro League Season 12: North America",
                "data": "27/09/2020",
                "premio": "$77,500",
                "descricao": "Primeiro lugar, vitória por 3-0 na final"
            }
        ],
        "proximos_jogos": [
            {
                "torneio": "Austin Major 2025",
                "adversario": "A ser definido",
                "data": "15/05/2025",
                "formato": "Bo3",
                "horario": "15:00 BRT"
            }
        ],
        "resultados_recentes": [
            {
                "torneio": "PGL Bucharest 2025",
                "adversario": "The Mongolz",
                "data": "09/04/2025",
                "resultado": "FURIA 0-2 THE MONGOLZ",
                "mapa1": "Mirage (9-13)",
                "mapa2": "Nuke (11-13)",
                "mapa3": "-"
            },
            {
                "torneio": "PGL Bucharest 2025",
                "adversario": "Virtus.pro",
                "data": "08/04/2025",
                "resultado": "FURIA 0-2 VIRTUS.PRO",
                "mapa1": "Anubis (11-13)",
                "mapa2": "Dust2 (8-13)",
                "mapa3": "-"
            }
        ],
        "redes_sociais": {
            "twitter": "https://twitter.com/FURIA",
            "instagram": "https://www.instagram.com/furiagg/",
            "facebook": "https://www.facebook.com/furiagg",
            "youtube": "https://www.youtube.com/furiagg",
            "twitch": "https://www.twitch.tv/furiatv",
            "site": "https://furia.gg/"
        },
        "curiosidades": [
            "A FURIA foi fundada em 2017 por quatro amigos: Jaime Pádua, André Akkari, Cristian Guedes e Nicholas Nogueira.",
            "O jogador yuurih está na FURIA desde a fundação da equipe de CS em 2017.",
            "FalleN, conhecido como 'The Godfather' do CS brasileiro, juntou-se à FURIA em 2023 após uma carreira lendária em outras equipes.",
            "A FURIA alcançou o top 5 do ranking mundial de CS:GO em 2020.",
            "A equipe conquistou seu primeiro título internacional importante no ESL Pro League Season 12: North America em 2020.",
            "O logo da FURIA representa uma pantera negra, simbolizando agilidade, força e precisão."
        ],
        "noticias": [
            {
                "titulo": "FURIA confirma YEKINDAR como stand-in para o Austin Major",
                "data": "22/04/2025",
                "resumo": "A FURIA anunciou oficialmente que Mareks 'YEKINDAR' Gaļinskis será o stand-in da equipe para o Austin Major, substituindo skullz que foi afastado do time.",
                "link": "https://furia.gg/news/yekindar-standin-austin-major"
            },
            {
                "titulo": "FURIA contrata molodoy da AMKAL ESPORTS",
                "data": "11/04/2025",
                "resumo": "A FURIA anunciou a contratação de Danil 'molodoy' Golubenko da AMKAL ESPORTS, substituindo chelo que foi afastado do time.",
                "link": "https://furia.gg/news/molodoy-joins-furia"
            },
            {
                "titulo": "FURIA se classifica para o Austin Major 2025",
                "data": "05/04/2025",
                "resumo": "A FURIA garantiu sua vaga para o Austin Major 2025 após uma campanha sólida nas classificatórias sul-americanas.",
                "link": "https://furia.gg/news/furia-qualifies-austin-major"
            },
            {
                "titulo": "FURIA anuncia Hepa como novo treinador assistente",
                "data": "15/01/2025",
                "resumo": "A FURIA anunciou a contratação de Juan 'Hepa' Borges como novo treinador assistente da equipe de CS, substituindo Lucid.",
                "link": "https://furia.gg/news/hepa-joins-coaching-staff"
            },
            {
                "titulo": "FURIA vence Elisa Masters Espoo 2023",
                "data": "03/12/2023",
                "resumo": "A FURIA conquistou o título da Elisa Masters Espoo 2023, vencendo a final por 3-1 e garantindo um prêmio de $100,000.",
                "link": "https://furia.gg/news/furia-wins-elisa-masters-espoo"
            }
        ]
    }
    return data

# Token do bot (será substituído pelo token real quando o bot for criado no BotFather)
TOKEN = ""

# Comandos

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia mensagem quando o comando /start é emitido."""
    user = update.effective_user
    await update.message.reply_text(
        f"🐾 Olá, {user.first_name}! Bem-vindo ao Bot da FURIA CS! 🐾\n\n"
        f"Eu sou o bot oficial para os fãs do time de Counter-Strike da FURIA!\n\n"
        f"Use /help para ver todos os comandos disponíveis."
    )
    # Enviar teclado com opções iniciais
    keyboard = [
        [
            InlineKeyboardButton("Sobre a FURIA", callback_data="sobre_furia"),
            InlineKeyboardButton("Roster Atual", callback_data="roster")
        ],
        [
            InlineKeyboardButton("Próximos Jogos", callback_data="proximos_jogos"),
            InlineKeyboardButton("Conquistas", callback_data="conquistas")
        ],
        [
            InlineKeyboardButton("Notícias", callback_data="noticias")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("O que você gostaria de saber?", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia mensagem quando o comando /help é emitido."""
    help_text = (
        "🐾 *Comandos disponíveis:* 🐾\n\n"
        "*Comandos Básicos:*\n"
        "/start - Inicia o bot e exibe mensagem de boas-vindas\n"
        "/help - Exibe esta lista de comandos\n"
        "/sobre - Informações sobre este bot\n\n"
        
        "*Informações sobre o Time:*\n"
        "/furia - Informações gerais sobre a FURIA\n"
        "/roster - Mostra o roster atual\n"
        "/jogadores - Lista todos os jogadores\n"
        "/staff - Informações sobre a equipe técnica\n\n"
        
        "*Jogadores Específicos:*\n"
        "/jogador [nome] - Informações sobre um jogador específico\n"
        "/fallen - Informações sobre FalleN\n"
        "/kscerato - Informações sobre KSCERATO\n"
        "/yuurih - Informações sobre yuurih\n"
        "/molodoy - Informações sobre molodoy\n"
        "/yekindar - Informações sobre YEKINDAR\n\n"
        
        "*Competições e Resultados:*\n"
        "/agenda - Próximos jogos da FURIA\n"
        "/resultados - Resultados recentes\n"
        "/conquistas - Principais conquistas do time\n\n"
        
        "*Conteúdo e Mídia:*\n"
        "/noticias - Últimas notícias sobre a FURIA\n"
        "/social - Links para redes sociais oficiais\n"
        "/curiosidades - Curiosidades sobre o time e jogadores\n\n"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre o bot quando o comando /sobre é emitido."""
    about_text = (
        "🐾 *Sobre este Bot* 🐾\n\n"
        "Este é um bot não-oficial criado para os fãs do time de CS da FURIA.\n\n"
        "O bot fornece informações sobre o time, jogadores, resultados, agenda de jogos e muito mais.\n\n"
        "Desenvolvido com ❤️ usando Python e a biblioteca python-telegram-bot.\n\n"
        "Versão: 1.1.0"
    )
    await update.message.reply_text(about_text, parse_mode='Markdown')

async def furia_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre a organização FURIA."""
    data = load_data()
    org = data["organizacao"]
    
    info_text = (
        f"🐾 *{org['nome']}* 🐾\n\n"
        f"*Fundação:* {org['fundacao']}\n"
        f"*Origem:* {org['origem']}\n"
        f"*Região:* {org['regiao']}\n\n"
        f"*Fundadores:*\n"
    )
    
    for fundador in org["fundadores"]:
        info_text += f"• {fundador}\n"
    
    info_text += f"\n*Sobre:*\n{org['descricao']}"
    
    # Adicionar botões para mais informações
    keyboard = [
        [
            InlineKeyboardButton("Roster Atual", callback_data="roster"),
            InlineKeyboardButton("Conquistas", callback_data="conquistas")
        ],
        [
            InlineKeyboardButton("Redes Sociais", callback_data="social"),
            InlineKeyboardButton("Notícias", callback_data="noticias")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(info_text, parse_mode='Markdown', reply_markup=reply_markup)

async def roster(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre o roster atual da FURIA."""
    data = load_data()
    jogadores = data["jogadores"]
    
    roster_text = "🐾 *ROSTER ATUAL DA FURIA CS* 🐾\n\n"
    
    for nick, info in jogadores.items():
        roster_text += f"*{info['nickname']}* ({info['nome_completo']})\n"
        roster_text += f"• Nacionalidade: {info['nacionalidade']}\n"
        roster_text += f"• Função: {info['funcao']}\n"
        roster_text += f"• Na FURIA desde: {info['data_entrada']}\n\n"
    
    # Adicionar botões para jogadores individuais
    keyboard = []
    row = []
    count = 0
    
    for nick, info in jogadores.items():
        row.append(InlineKeyboardButton(info['nickname'], callback_data=f"jogador_{nick}"))
        count += 1
        if count % 2 == 0 or count == len(jogadores):
            keyboard.append(row)
            row = []
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(roster_text, parse_mode='Markdown', reply_markup=reply_markup)

async def player_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre um jogador específico."""
    data = load_data()
    jogadores = data["jogadores"]
    
    # Verificar se foi fornecido um argumento
    if context.args and len(context.args) > 0:
        player_name = context.args[0].lower()
        
        # Verificar se o jogador existe
        if player_name in jogadores:
            await send_player_info(update, player_name, jogadores[player_name])
        else:
            # Tentar encontrar jogador por correspondência parcial
            found = False
            for nick, info in jogadores.items():
                if player_name in nick.lower() or player_name in info['nome_completo'].lower():
                    await send_player_info(update, nick, info)
                    found = True
                    break
            
            if not found:
                await update.message.reply_text(f"Jogador '{player_name}' não encontrado. Use /jogadores para ver a lista completa.")
    else:
        # Se nenhum argumento foi fornecido, mostrar lista de jogadores
        await players_list(update, context)

async def send_player_info(update: Update, nick: str, player_info: dict) -> None:
    """Função auxiliar para enviar informações de um jogador específico."""
    player_text = (
        f"🐾 *{player_info['nickname']}* 🐾\n\n"
        f"*Nome Completo:* {player_info['nome_completo']}\n"
        f"*Nacionalidade:* {player_info['nacionalidade']}\n"
        f"*Função:* {player_info['funcao']}\n"
        f"*Na FURIA desde:* {player_info['data_entrada']}\n\n"
        f"*Bio:* {player_info['bio']}\n\n"
        f"*Estatísticas:*\n"
        f"• Rating: {player_info['estatisticas']['rating']}\n"
        f"• Maps: {player_info['estatisticas']['maps']}\n"
        f"• K/D: {player_info['estatisticas']['kd']}\n"
    )
    
    # Adicionar botões para outros jogadores
    keyboard = [
        [InlineKeyboardButton("Ver todos os jogadores", callback_data="jogadores")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(player_text, parse_mode='Markdown', reply_markup=reply_markup)

async def players_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia lista de todos os jogadores."""
    data = load_data()
    jogadores = data["jogadores"]
    
    players_text = "🐾 *JOGADORES DA FURIA CS* 🐾\n\n"
    players_text += "Selecione um jogador para ver mais informações:\n"
    
    # Criar botões para cada jogador
    keyboard = []
    for nick, info in jogadores.items():
        keyboard.append([InlineKeyboardButton(info['nickname'], callback_data=f"jogador_{nick}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(players_text, parse_mode='Markdown', reply_markup=reply_markup)

async def staff_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre a equipe técnica."""
    data = load_data()
    staff = data["staff"]
    
    staff_text = "🐾 *EQUIPE TÉCNICA DA FURIA CS* 🐾\n\n"
    
    for nick, info in staff.items():
        staff_text += f"*{info['nickname']}* ({info['nome_completo']})\n"
        staff_text += f"• Nacionalidade: {info['nacionalidade']}\n"
        staff_text += f"• Função: {info['funcao']}\n"
        staff_text += f"• Na FURIA desde: {info['data_entrada']}\n"
        staff_text += f"• Bio: {info['bio']}\n\n"
    
    await update.message.reply_text(staff_text, parse_mode='Markdown')

async def achievements(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre as conquistas da FURIA."""
    data = load_data()
    conquistas = data["conquistas"]
    
    achievements_text = "🐾 *PRINCIPAIS CONQUISTAS DA FURIA CS* 🐾\n\n"
    
    for conquista in conquistas:
        achievements_text += f"*{conquista['nome']}*\n"
        achievements_text += f"• Data: {conquista['data']}\n"
        achievements_text += f"• Prêmio: {conquista['premio']}\n"
        achievements_text += f"• {conquista['descricao']}\n\n"
    
    await update.message.reply_text(achievements_text, parse_mode='Markdown')

async def upcoming_matches(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre os próximos jogos da FURIA."""
    data = load_data()
    jogos = data["proximos_jogos"]
    
    if jogos:
        matches_text = "🐾 *PRÓXIMOS JOGOS DA FURIA CS* 🐾\n\n"
        
        for jogo in jogos:
            matches_text += f"*{jogo['torneio']}*\n"
            matches_text += f"• Adversário: {jogo['adversario']}\n"
            matches_text += f"• Data: {jogo['data']}\n"
            matches_text += f"• Horário: {jogo['horario']}\n"
            matches_text += f"• Formato: {jogo['formato']}\n\n"
    else:
        matches_text = "Não há jogos agendados no momento. Fique atento para atualizações!"
    
    # Adicionar botão para configurar lembrete
    keyboard = [
        [InlineKeyboardButton("Configurar Lembrete", callback_data="lembrete_config")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(matches_text, parse_mode='Markdown', reply_markup=reply_markup)

async def recent_results(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre os resultados recentes da FURIA."""
    data = load_data()
    resultados = data["resultados_recentes"]
    
    if resultados:
        results_text = "🐾 *RESULTADOS RECENTES DA FURIA CS* 🐾\n\n"
        
        for resultado in resultados:
            results_text += f"*{resultado['torneio']}*\n"
            results_text += f"• Data: {resultado['data']}\n"
            results_text += f"• {resultado['resultado']}\n"
            
            if resultado['mapa1'] != "-":
                results_text += f"• Mapa 1: {resultado['mapa1']}\n"
            if resultado['mapa2'] != "-":
                results_text += f"• Mapa 2: {resultado['mapa2']}\n"
            if resultado['mapa3'] != "-" and 'mapa3' in resultado:
                results_text += f"• Mapa 3: {resultado['mapa3']}\n"
            
            results_text += "\n"
    else:
        results_text = "Não há resultados recentes disponíveis."
    
    await update.message.reply_text(results_text, parse_mode='Markdown')

async def social_media(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia links para as redes sociais da FURIA."""
    data = load_data()
    redes = data["redes_sociais"]
    
    social_text = "🐾 *REDES SOCIAIS DA FURIA* 🐾\n\n"
    social_text += f"• [Twitter]({redes['twitter']})\n"
    social_text += f"• [Instagram]({redes['instagram']})\n"
    social_text += f"• [Facebook]({redes['facebook']})\n"
    social_text += f"• [YouTube]({redes['youtube']})\n"
    social_text += f"• [Twitch]({redes['twitch']})\n"
    social_text += f"• [Site Oficial]({redes['site']})\n"
    
    await update.message.reply_text(social_text, parse_mode='Markdown', disable_web_page_preview=True)

async def curiosities(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia curiosidades sobre a FURIA."""
    data = load_data()
    curiosidades = data["curiosidades"]
    
    import random
    curiosidade = random.choice(curiosidades)
    
    curiosity_text = f"🐾 *VOCÊ SABIA?* 🐾\n\n{curiosidade}\n\n"
    
    # Adicionar botão para mais curiosidades
    keyboard = [
        [InlineKeyboardButton("Mais uma curiosidade", callback_data="curiosidade")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(curiosity_text, parse_mode='Markdown', reply_markup=reply_markup)

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia as últimas notícias sobre a FURIA."""
    data = load_data()
    noticias = data["noticias"]
    
    if noticias:
        news_text = "🐾 *ÚLTIMAS NOTÍCIAS DA FURIA CS* 🐾\n\n"
        
        for noticia in noticias[:3]:  # Mostrar apenas as 3 notícias mais recentes
            news_text += f"*{noticia['titulo']}*\n"
            news_text += f"• Data: {noticia['data']}\n"
            news_text += f"• {noticia['resumo']}\n"
            news_text += f"• [Leia mais]({noticia['link']})\n\n"
        
        # Adicionar botão para mais notícias
        keyboard = [
            [InlineKeyboardButton("Mais notícias", callback_data="mais_noticias")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(news_text, parse_mode='Markdown', reply_markup=reply_markup, disable_web_page_preview=True)
    else:
        await update.message.reply_text("Não há notícias disponíveis no momento.", parse_mode='Markdown')

# Handlers para jogadores específicos
async def fallen_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Atalho para informações sobre FalleN."""
    data = load_data()
    await send_player_info(update, "fallen", data["jogadores"]["fallen"])

async def kscerato_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Atalho para informações sobre KSCERATO."""
    data = load_data()
    await send_player_info(update, "kscerato", data["jogadores"]["kscerato"])

async def yuurih_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Atalho para informações sobre yuurih."""
    data = load_data()
    await send_player_info(update, "yuurih", data["jogadores"]["yuurih"])

async def molodoy_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Atalho para informações sobre molodoy."""
    data = load_data()
    await send_player_info(update, "molodoy", data["jogadores"]["molodoy"])

async def yekindar_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Atalho para informações sobre YEKINDAR."""
    data = load_data()
    await send_player_info(update, "yekindar", data["jogadores"]["yekindar"])

# Funcionalidades específicas da FURIA

async def furia_history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia informações sobre momentos históricos da FURIA."""
    from furia_features import FURIA_HISTORIC_MOMENTS
    
    # Ordenar momentos históricos por data (mais recentes primeiro)
    momentos = sorted(FURIA_HISTORIC_MOMENTS, key=lambda x: x["data"], reverse=True)
    
    history_text = "🐾 *MOMENTOS HISTÓRICOS DA FURIA* 🐾\n\n"
    
    # Limitar a 3 momentos para não exceder o limite de mensagem
    for momento in momentos[:3]:
        history_text += f"*{momento['titulo']} ({momento['data']})*\n"
        history_text += f"{momento['descricao']}\n\n"
    
    # Adicionar botões para navegação
    keyboard = [
        [
            InlineKeyboardButton("Mais momentos", callback_data="historia_mais"),
            InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(history_text, parse_mode='Markdown', reply_markup=reply_markup)


async def furia_next_match_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Permite ao usuário configurar um lembrete para o próximo jogo da FURIA."""
    # Carregar dados dos próximos jogos
    data = load_data()
    jogos = data["proximos_jogos"]
    
    if not jogos:
        await update.message.reply_text("Não há jogos agendados no momento. Tente novamente mais tarde.")
        return
    
    proximo_jogo = jogos[0]
    
    reminder_text = (
        f"🐾 *LEMBRETE DE JOGO* 🐾\n\n"
        f"Você quer ser lembrado do próximo jogo da FURIA?\n\n"
        f"*{proximo_jogo['torneio']}*\n"
        f"• Adversário: {proximo_jogo['adversario']}\n"
        f"• Data: {proximo_jogo['data']}\n"
        f"• Horário: {proximo_jogo['horario']}\n"
        f"• Formato: {proximo_jogo['formato']}\n\n"
        f"Nota: Esta é uma simulação de lembrete. Em um bot real, você receberia uma notificação antes do jogo."
    )
    
    # Adicionar botões para configurar lembrete
    keyboard = [
        [
            InlineKeyboardButton("Sim, lembrar", callback_data="lembrete_sim"),
            InlineKeyboardButton("Não, obrigado", callback_data="lembrete_nao")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(reminder_text, parse_mode='Markdown', reply_markup=reply_markup)

# Callback Query Handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processa callbacks dos botões inline."""
    query = update.callback_query
    await query.answer()
    
    # Tentar processar como callback específico da FURIA
    try:
        from furia_features import process_furia_callbacks
        if await process_furia_callbacks(query, query.data):
            return
    except Exception as e:
        logger.error(f"Erro ao processar callback específico: {e}")
    
    data = load_data()
    
    if query.data == "sobre_furia":
        org = data["organizacao"]
        info_text = (
            f"🐾 *{org['nome']}* 🐾\n\n"
            f"*Fundação:* {org['fundacao']}\n"
            f"*Origem:* {org['origem']}\n"
            f"*Região:* {org['regiao']}\n\n"
            f"*Fundadores:*\n"
        )
        
        for fundador in org["fundadores"]:
            info_text += f"• {fundador}\n"
        
        info_text += f"\n*Sobre:*\n{org['descricao']}"
        
        keyboard = [
            [
                InlineKeyboardButton("Roster Atual", callback_data="roster"),
                InlineKeyboardButton("Conquistas", callback_data="conquistas")
            ],
            [
                InlineKeyboardButton("Redes Sociais", callback_data="social"),
                InlineKeyboardButton("Notícias", callback_data="noticias")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=info_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "roster":
        jogadores = data["jogadores"]
        
        roster_text = "🐾 *ROSTER ATUAL DA FURIA CS* 🐾\n\n"
        
        for nick, info in jogadores.items():
            roster_text += f"*{info['nickname']}* ({info['nome_completo']})\n"
            roster_text += f"• Nacionalidade: {info['nacionalidade']}\n"
            roster_text += f"• Função: {info['funcao']}\n"
            roster_text += f"• Na FURIA desde: {info['data_entrada']}\n\n"
        
        keyboard = []
        row = []
        count = 0
        
        for nick, info in jogadores.items():
            row.append(InlineKeyboardButton(info['nickname'], callback_data=f"jogador_{nick}"))
            count += 1
            if count % 2 == 0 or count == len(jogadores):
                keyboard.append(row)
                row = []
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=roster_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data.startswith("jogador_"):
        player_nick = query.data.split("_")[1]
        if player_nick in data["jogadores"]:
            player_info = data["jogadores"][player_nick]
            
            player_text = (
                f"🐾 *{player_info['nickname']}* 🐾\n\n"
                f"*Nome Completo:* {player_info['nome_completo']}\n"
                f"*Nacionalidade:* {player_info['nacionalidade']}\n"
                f"*Função:* {player_info['funcao']}\n"
                f"*Na FURIA desde:* {player_info['data_entrada']}\n\n"
                f"*Bio:* {player_info['bio']}\n\n"
                f"*Estatísticas:*\n"
                f"• Rating: {player_info['estatisticas']['rating']}\n"
                f"• Maps: {player_info['estatisticas']['maps']}\n"
                f"• K/D: {player_info['estatisticas']['kd']}\n"
            )
            
            keyboard = [
                [InlineKeyboardButton("Voltar ao Roster", callback_data="roster")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(text=player_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "jogadores":
        jogadores = data["jogadores"]
        
        players_text = "🐾 *JOGADORES DA FURIA CS* 🐾\n\n"
        players_text += "Selecione um jogador para ver mais informações:\n"
        
        keyboard = []
        for nick, info in jogadores.items():
            keyboard.append([InlineKeyboardButton(info['nickname'], callback_data=f"jogador_{nick}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=players_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "conquistas":
        conquistas = data["conquistas"]
        
        achievements_text = "🐾 *PRINCIPAIS CONQUISTAS DA FURIA CS* 🐾\n\n"
        
        for conquista in conquistas:
            achievements_text += f"*{conquista['nome']}*\n"
            achievements_text += f"• Data: {conquista['data']}\n"
            achievements_text += f"• Prêmio: {conquista['premio']}\n"
            achievements_text += f"• {conquista['descricao']}\n\n"
        
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data="menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=achievements_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "proximos_jogos":
        jogos = data["proximos_jogos"]
        
        if jogos:
            matches_text = "🐾 *PRÓXIMOS JOGOS DA FURIA CS* 🐾\n\n"
            
            for jogo in jogos:
                matches_text += f"*{jogo['torneio']}*\n"
                matches_text += f"• Adversário: {jogo['adversario']}\n"
                matches_text += f"• Data: {jogo['data']}\n"
                matches_text += f"• Horário: {jogo['horario']}\n"
                matches_text += f"• Formato: {jogo['formato']}\n\n"
        else:
            matches_text = "Não há jogos agendados no momento. Fique atento para atualizações!"
        
        keyboard = [
            [
                InlineKeyboardButton("Resultados Recentes", callback_data="resultados"),
                InlineKeyboardButton("Configurar Lembrete", callback_data="lembrete_config")
            ],
            [
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=matches_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "resultados":
        resultados = data["resultados_recentes"]
        
        if resultados:
            results_text = "🐾 *RESULTADOS RECENTES DA FURIA CS* 🐾\n\n"
            
            for resultado in resultados:
                results_text += f"*{resultado['torneio']}*\n"
                results_text += f"• Data: {resultado['data']}\n"
                results_text += f"• {resultado['resultado']}\n"
                
                if resultado['mapa1'] != "-":
                    results_text += f"• Mapa 1: {resultado['mapa1']}\n"
                if resultado['mapa2'] != "-":
                    results_text += f"• Mapa 2: {resultado['mapa2']}\n"
                if resultado['mapa3'] != "-" and 'mapa3' in resultado:
                    results_text += f"• Mapa 3: {resultado['mapa3']}\n"
                
                results_text += "\n"
        else:
            results_text = "Não há resultados recentes disponíveis."
        
        keyboard = [
            [
                InlineKeyboardButton("Próximos Jogos", callback_data="proximos_jogos"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=results_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "social":
        redes = data["redes_sociais"]
        
        social_text = "🐾 *REDES SOCIAIS DA FURIA* 🐾\n\n"
        social_text += f"• [Twitter]({redes['twitter']})\n"
        social_text += f"• [Instagram]({redes['instagram']})\n"
        social_text += f"• [Facebook]({redes['facebook']})\n"
        social_text += f"• [YouTube]({redes['youtube']})\n"
        social_text += f"• [Twitch]({redes['twitch']})\n"
        social_text += f"• [Site Oficial]({redes['site']})\n"
        
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data="menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=social_text, parse_mode='Markdown', reply_markup=reply_markup, disable_web_page_preview=True)
    
    elif query.data == "curiosidade":
        import random
        curiosidade = random.choice(data["curiosidades"])
        
        curiosity_text = f"🐾 *VOCÊ SABIA?* 🐾\n\n{curiosidade}\n\n"
        
        keyboard = [
            [
                InlineKeyboardButton("Mais uma curiosidade", callback_data="curiosidade"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=curiosity_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "noticias":
        noticias = data["noticias"]
        
        if noticias:
            news_text = "🐾 *ÚLTIMAS NOTÍCIAS DA FURIA CS* 🐾\n\n"
            
            for noticia in noticias[:3]:  # Mostrar apenas as 3 notícias mais recentes
                news_text += f"*{noticia['titulo']}*\n"
                news_text += f"• Data: {noticia['data']}\n"
                news_text += f"• {noticia['resumo']}\n"
                news_text += f"• [Leia mais]({noticia['link']})\n\n"
            
            keyboard = [
                [
                    InlineKeyboardButton("Mais notícias", callback_data="mais_noticias"),
                    InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(text=news_text, parse_mode='Markdown', reply_markup=reply_markup, disable_web_page_preview=True)
        else:
            await query.edit_message_text("Não há notícias disponíveis no momento.", parse_mode='Markdown')
    
    elif query.data == "mais_noticias":
        noticias = data["noticias"]
        
        if len(noticias) > 3:
            news_text = "🐾 *MAIS NOTÍCIAS DA FURIA CS* 🐾\n\n"
            
            for noticia in noticias[3:]:  # Mostrar as notícias restantes
                news_text += f"*{noticia['titulo']}*\n"
                news_text += f"• Data: {noticia['data']}\n"
                news_text += f"• {noticia['resumo']}\n"
                news_text += f"• [Leia mais]({noticia['link']})\n\n"
            
            keyboard = [
                [InlineKeyboardButton("Voltar às notícias recentes", callback_data="noticias")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(text=news_text, parse_mode='Markdown', reply_markup=reply_markup, disable_web_page_preview=True)
        else:
            await query.edit_message_text("Não há mais notícias disponíveis.", parse_mode='Markdown')
    
    elif query.data == "lembrete_config":
        jogos = data["proximos_jogos"]
        
        if not jogos:
            await query.edit_message_text("Não há jogos agendados no momento. Tente novamente mais tarde.", parse_mode='Markdown')
            return
        
        proximo_jogo = jogos[0]
        
        reminder_text = (
            f"🐾 *LEMBRETE DE JOGO* 🐾\n\n"
            f"Você quer ser lembrado do próximo jogo da FURIA?\n\n"
            f"*{proximo_jogo['torneio']}*\n"
            f"• Adversário: {proximo_jogo['adversario']}\n"
            f"• Data: {proximo_jogo['data']}\n"
            f"• Horário: {proximo_jogo['horario']}\n"
            f"• Formato: {proximo_jogo['formato']}\n\n"
            f"Nota: Esta é uma simulação de lembrete. Em um bot real, você receberia uma notificação antes do jogo."
        )
        
        keyboard = [
            [
                InlineKeyboardButton("Sim, lembrar", callback_data="lembrete_sim"),
                InlineKeyboardButton("Não, obrigado", callback_data="lembrete_nao")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=reminder_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "lembrete_sim":
        reminder_text = (
            "🐾 *LEMBRETE CONFIGURADO* 🐾\n\n"
            "Você será lembrado do próximo jogo da FURIA!\n\n"
            "Nota: Esta é uma simulação. Em um bot real, você receberia uma notificação antes do jogo."
        )
        
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data="menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=reminder_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    elif query.data == "lembrete_nao":
        reminder_text = (
            "🐾 *LEMBRETE NÃO CONFIGURADO* 🐾\n\n"
            "Você optou por não receber lembretes para o próximo jogo da FURIA.\n\n"
            "Você pode configurar lembretes a qualquer momento usando o comando /lembrete."
        )
        
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data="menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=reminder_text, parse_mode='Markdown', reply_markup=reply_markup)
    
    
    elif query.data == "menu":
        menu_text = "O que você gostaria de saber sobre a FURIA CS?"
        
        keyboard = [
            [
                InlineKeyboardButton("Sobre a FURIA", callback_data="sobre_furia"),
                InlineKeyboardButton("Roster Atual", callback_data="roster")
            ],
            [
                InlineKeyboardButton("Próximos Jogos", callback_data="proximos_jogos"),
                InlineKeyboardButton("Conquistas", callback_data="conquistas")
            ],
            [
                InlineKeyboardButton("Notícias", callback_data="noticias")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=menu_text, reply_markup=reply_markup)

