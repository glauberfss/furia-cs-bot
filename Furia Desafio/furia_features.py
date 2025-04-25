#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo com funcionalidades específicas da FURIA para o bot do Telegram
"""

import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Frases motivacionais da FURIA
FURIA_MOTIVATIONAL_QUOTES = [
    "Não importa o quão difícil seja o desafio, a FURIA nunca desiste!",
    "Cada round é uma nova oportunidade para mostrar nossa força.",
    "Somos uma família, lutamos juntos e vencemos juntos!",
    "A determinação é o que nos diferencia. Nunca pare de acreditar!",
    "Não é sobre ganhar todas, é sobre nunca desistir de nenhuma.",
    "Treine como se fosse o último dia, jogue como se fosse a final do Major.",
    "Respeite todos, tema ninguém. Esse é o espírito da FURIA!",
    "Cada derrota nos ensina, cada vitória nos motiva. Seguimos em frente!",
    "O talento vence jogos, mas o trabalho em equipe vence campeonatos.",
    "Não é sobre ser o melhor jogador, é sobre fazer o time ser o melhor."
]

# Memes da FURIA
FURIA_MEMES = [
    "Quando o FalleN acerta um clutch impossível: 'The Godfather não perdoa!'",
    "KSCERATO carregando o time: 'Mais um dia normal no escritório.'",
    "Adversário: 'Vamos ganhar fácil da FURIA' / FURIA: 'Hold my caipirinha!'",
    "Quando o yuurih faz um 4k: 'Calma, é só o aquecimento.'",
    "FURIA ganhando de virada: 'Vocês realmente acharam que seria fácil?'",
    "Quando o molodoy surpreende todo mundo: 'Quem é o novato agora?'",
    "YEKINDAR entrando como stand-in: 'Deixa que eu resolvo isso rapidinho.'",
    "Adversário: 'Eles são só brasileiros' / FURIA: 'E isso deveria nos limitar?'",
    "Quando a FURIA vence uma equipe tier 1: 'Respeitem o pantera!'",
    "FURIA em bootcamp: 'Dormir? Isso é para os fracos!'"
]

# Dicas de CS inspiradas na FURIA
FURIA_CS_TIPS = [
    "Como FalleN ensina: 'Pratique seu posicionamento com a AWP. Não é só sobre acertar tiros, é sobre controlar áreas do mapa.'",
    "Estilo KSCERATO: 'Mantenha a calma em situações de clutch. Respire fundo e foque em um adversário de cada vez.'",
    "Tática da FURIA: 'Comunicação é tudo! Informe seus companheiros sobre tudo o que vê e ouve no mapa.'",
    "Inspirado em yuurih: 'Pratique seu spray control diariamente. Comece com poucos tiros e vá aumentando gradualmente.'",
    "Mentalidade FURIA: 'Nunca desista de um round, por mais impossível que pareça. Uma jogada incrível pode mudar tudo.'",
    "Como YEKINDAR ensina: 'Como entry fragger, seu trabalho não é só conseguir kills, mas criar espaço para seu time.'",
    "Tática de economia: 'Às vezes é melhor fazer um eco completo do que comprar armas medianas várias rodadas seguidas.'",
    "Dica de treino: 'Dedique tempo para aprender os smokes e flashes mais importantes de cada mapa.'",
    "Estratégia de CT: 'Não seja previsível. Alterne suas posições e timings para confundir os adversários.'",
    "Dica para melhorar: 'Assista suas próprias demos e identifique erros. A autocrítica é essencial para evoluir.'"
]

# Cantos da torcida da FURIA
FURIA_CHANTS = [
    "FURIA! FURIA! FURIA! O BRASIL TÁ CONTIGO!",
    "VAMOS FURIA! VAMOS FURIA! HOJE É DIA DE VITÓRIA!",
    "OLÊÊÊÊ, OLÊ OLÊ OLÁ, FURIA! FURIA!",
    "É A FURIA! É A FURIA! NINGUÉM VAI NOS PARAR!",
    "FALLEN É O NOSSO GENERAL! KSCERATO É FENOMENAL!",
    "YUURIH, YUURIH, YUURIH! O CRAQUE DO BRASIL!",
    "QUEM É QUE VAI GANHAR? A FURIA VAI GANHAR!",
    "A PANTERA NEGRA CHEGOU PRA DEVORAR!",
    "FURIA, MINHA VIDA É VOCÊ! MEU CORAÇÃO SÓ BATE POR VOCÊ!",
    "VAMOS, VAMOS, FURIA! ESTA NOITE, TEMOS QUE GANHAR!"
]

# Momentos históricos da FURIA
FURIA_HISTORIC_MOMENTS = [
    {
        "titulo": "Fundação da FURIA",
        "data": "2017-08-01",
        "descricao": "A FURIA Esports foi fundada em agosto de 2017 por Jaime Pádua, André Akkari, Cristian Guedes e Nicholas Nogueira, com o objetivo de se tornar uma das principais organizações de esports do Brasil."
    },
    {
        "titulo": "Primeira Classificação para Major",
        "data": "2019-02-24",
        "descricao": "A FURIA se classificou para seu primeiro Major de CS:GO, o IEM Katowice 2019, marcando o início de sua ascensão no cenário internacional."
    },
    {
        "titulo": "Top 5 do Ranking Mundial",
        "data": "2020-06-15",
        "descricao": "A FURIA alcançou o top 5 do ranking mundial de CS:GO da HLTV pela primeira vez, consolidando-se como uma das melhores equipes do mundo."
    },
    {
        "titulo": "Título da ESL Pro League Season 12: North America",
        "data": "2020-09-27",
        "descricao": "A FURIA conquistou seu primeiro título internacional importante ao vencer a ESL Pro League Season 12: North America, derrotando a Team Liquid por 3-0 na final."
    },
    {
        "titulo": "FalleN se junta à FURIA",
        "data": "2023-07-03",
        "descricao": "Gabriel 'FalleN' Toledo, considerado o 'Godfather' do CS brasileiro, juntou-se à FURIA, trazendo sua experiência e liderança para a equipe."
    },
    {
        "titulo": "Título da Elisa Masters Espoo 2023",
        "data": "2023-12-03",
        "descricao": "A FURIA conquistou o título da Elisa Masters Espoo 2023, vencendo a final por 3-1 e garantindo um prêmio de $100,000."
    },
    {
        "titulo": "Contratação de molodoy",
        "data": "2025-04-11",
        "descricao": "A FURIA anunciou a contratação de Danil 'molodoy' Golubenko da AMKAL ESPORTS, trazendo sangue novo para a equipe."
    },
    {
        "titulo": "YEKINDAR como stand-in",
        "data": "2025-04-22",
        "descricao": "Mareks 'YEKINDAR' Gaļinskis foi anunciado como stand-in da FURIA para o Austin Major 2025, fortalecendo ainda mais o lineup da equipe."
    }
]

# Perguntas para o quiz da FURIA
FURIA_QUIZ_QUESTIONS = [
    {
        "pergunta": "Em que ano a FURIA foi fundada?",
        "opcoes": ["2016", "2017", "2018", "2019"],
        "resposta_correta": 1,
        "explicacao": "A FURIA foi fundada em agosto de 2017 por Jaime Pádua, André Akkari, Cristian Guedes e Nicholas Nogueira."
    },
    {
        "pergunta": "Qual jogador está na FURIA desde a fundação da equipe de CS?",
        "opcoes": ["FalleN", "KSCERATO", "yuurih", "arT"],
        "resposta_correta": 2,
        "explicacao": "Yuri 'yuurih' Boian está na FURIA desde a fundação da equipe de CS em 2017."
    },
    {
        "pergunta": "Qual foi o primeiro Major para o qual a FURIA se classificou?",
        "opcoes": ["ELEAGUE Major Boston 2018", "IEM Katowice 2019", "StarLadder Berlin Major 2019", "PGL Stockholm Major 2021"],
        "resposta_correta": 1,
        "explicacao": "A FURIA se classificou para seu primeiro Major no IEM Katowice 2019."
    },
    {
        "pergunta": "Qual é o apelido de Gabriel Toledo?",
        "opcoes": ["coldzera", "FalleN", "fer", "TACO"],
        "resposta_correta": 1,
        "explicacao": "Gabriel Toledo é conhecido como 'FalleN', também chamado de 'The Godfather' do CS brasileiro."
    },
    {
        "pergunta": "Qual foi o primeiro título internacional importante da FURIA?",
        "opcoes": ["DreamHack Masters", "ESL Pro League Season 12: NA", "BLAST Premier", "IEM Katowice"],
        "resposta_correta": 1,
        "explicacao": "A FURIA conquistou seu primeiro título internacional importante na ESL Pro League Season 12: North America em 2020."
    },
    {
        "pergunta": "Qual animal representa o logo da FURIA?",
        "opcoes": ["Leão", "Águia", "Pantera Negra", "Lobo"],
        "resposta_correta": 2,
        "explicacao": "O logo da FURIA representa uma pantera negra, simbolizando agilidade, força e precisão."
    },
    {
        "pergunta": "Em que posição a FURIA alcançou no ranking mundial da HLTV em 2020?",
        "opcoes": ["Top 10", "Top 5", "Top 3", "Primeiro lugar"],
        "resposta_correta": 1,
        "explicacao": "A FURIA alcançou o top 5 do ranking mundial de CS:GO da HLTV em 2020."
    },
    {
        "pergunta": "Qual jogador da FURIA é conhecido por sua função de AWPer/IGL?",
        "opcoes": ["KSCERATO", "yuurih", "FalleN", "molodoy"],
        "resposta_correta": 2,
        "explicacao": "FalleN é conhecido por sua função de AWPer (sniper) e IGL (In-Game Leader) na FURIA."
    },
    {
        "pergunta": "De qual país é o jogador YEKINDAR?",
        "opcoes": ["Brasil", "Rússia", "Letônia", "Ucrânia"],
        "resposta_correta": 2,
        "explicacao": "Mareks 'YEKINDAR' Gaļinskis é da Letônia."
    },
    {
        "pergunta": "Qual título a FURIA conquistou em dezembro de 2023?",
        "opcoes": ["IEM Rio", "Elisa Masters Espoo", "BLAST Premier", "ESL Pro League"],
        "resposta_correta": 1,
        "explicacao": "A FURIA conquistou o título da Elisa Masters Espoo 2023 em dezembro de 2023."
    }
]

# Função para processar callbacks específicos da FURIA
async def process_furia_callbacks(query, callback_data):
    """Processa callbacks específicos da FURIA."""
    if callback_data == "motivacao":
        quote = random.choice(FURIA_MOTIVATIONAL_QUOTES)
        
        quote_text = f"🐾 *MOTIVAÇÃO FURIA* 🐾\n\n{quote}"
        
        keyboard = [
            [
                InlineKeyboardButton("Mais motivação", callback_data="motivacao"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=quote_text, parse_mode='Markdown', reply_markup=reply_markup)
        return True
    
    elif callback_data == "meme":
        meme = random.choice(FURIA_MEMES)
        
        meme_text = f"🐾 *MEME FURIA* 🐾\n\n{meme}"
        
        keyboard = [
            [
                InlineKeyboardButton("Mais memes", callback_data="meme"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=meme_text, parse_mode='Markdown', reply_markup=reply_markup)
        return True
    
    elif callback_data == "dica":
        tip = random.choice(FURIA_CS_TIPS)
        
        tip_text = f"🐾 *DICA FURIA* 🐾\n\n{tip}"
        
        keyboard = [
            [
                InlineKeyboardButton("Mais dicas", callback_data="dica"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=tip_text, parse_mode='Markdown', reply_markup=reply_markup)
        return True
    
    elif callback_data == "canto":
        chant = random.choice(FURIA_CHANTS)
        
        chant_text = f"🐾 *CANTO DA TORCIDA* 🐾\n\n{chant}"
        
        keyboard = [
            [
                InlineKeyboardButton("Mais cantos", callback_data="canto"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=chant_text, parse_mode='Markdown', reply_markup=reply_markup)
        return True
    
    elif callback_data == "historia_mais":
        # Ordenar momentos históricos por data (mais recentes primeiro)
        momentos = sorted(FURIA_HISTORIC_MOMENTS, key=lambda x: x["data"], reverse=True)
        
        # Verificar se há um índice de página no contexto do usuário
        page = query.message.chat_data.get("historia_page", 0) if hasattr(query.message, "chat_data") else 0
        page = (page + 1) % ((len(momentos) + 2) // 3)  # Avançar para a próxima página
        
        # Salvar o índice da página atual
        if hasattr(query.message, "chat_data"):
            query.message.chat_data["historia_page"] = page
        
        # Calcular o intervalo de momentos para a página atual
        start_idx = page * 3
        end_idx = min(start_idx + 3, len(momentos))
        
        history_text = "🐾 *MOMENTOS HISTÓRICOS DA FURIA* 🐾\n\n"
        
        for momento in momentos[start_idx:end_idx]:
            history_text += f"*{momento['titulo']} ({momento['data']})*\n"
            history_text += f"{momento['descricao']}\n\n"
        
        keyboard = [
            [
                InlineKeyboardButton("Mais momentos", callback_data="historia_mais"),
                InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=history_text, parse_mode='Markdown', reply_markup=reply_markup)
        return True
    
    elif callback_data == "quiz_nova":
        # Escolher uma pergunta aleatória
        question = random.choice(FURIA_QUIZ_QUESTIONS)
        
        # Salvar a pergunta atual no contexto do usuário
        if hasattr(query, "message") and hasattr(query.message, "chat_data"):
            query.message.chat_data["current_quiz"] = question
        
        quiz_text = f"🐾 *QUIZ FURIA* 🐾\n\n*Pergunta:* {question['pergunta']}\n\n*Opções:*\n"
        
        for i, opcao in enumerate(question["opcoes"]):
            quiz_text += f"{i+1}. {opcao}\n"
        
        # Criar botões para as opções
        keyboard = []
        for i, opcao in enumerate(question["opcoes"]):
            keyboard.append([InlineKeyboardButton(f"{i+1}. {opcao}", callback_data=f"quiz_{i}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=quiz_text, parse_mode='Markdown', reply_markup=reply_markup)
        return True
    
    elif callback_data.startswith("quiz_"):
        # Extrair o índice da opção selecionada
        option_idx = int(callback_data.split("_")[1])
        
        # Obter a pergunta atual do contexto do usuário
        current_quiz = query.message.chat_data.get("current_quiz") if hasattr(query.message, "chat_data") else None
        
        if current_quiz:
            # Verificar se a resposta está correta
            is_correct = option_idx == current_quiz["resposta_correta"]
            
            result_text = f"🐾 *QUIZ FURIA - RESULTADO* 🐾\n\n"
            result_text += f"*Pergunta:* {current_quiz['pergunta']}\n\n"
            result_text += f"*Sua resposta:* {current_quiz['opcoes'][option_idx]}\n"
            result_text += f"*Resposta correta:* {current_quiz['opcoes'][current_quiz['resposta_correta']]}\n\n"
            
            if is_correct:
                result_text += "✅ *PARABÉNS! Você acertou!* ✅\n\n"
            else:
                result_text += "❌ *Que pena! Você errou.* ❌\n\n"
            
            result_text += f"*Explicação:* {current_quiz['explicacao']}"
            
            keyboard = [
                [
                    InlineKeyboardButton("Nova pergunta", callback_data="quiz_nova"),
                    InlineKeyboardButton("Voltar ao Menu", callback_data="menu")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(text=result_text, parse_mode='Markdown', reply_markup=reply_markup)
            return True
    
    
    # Se não for um callback específico da FURIA, retornar False
    return False
