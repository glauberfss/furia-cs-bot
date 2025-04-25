# 🤖 FURIA FanBot – Telegram Bot

Bot para os fãs do time de CS:GO da FURIA! Desenvolvido para o desafio técnico com foco em experiência do usuário e criatividade.

## 🎮 Funcionalidades

/start - Inicia o bot e exibe mensagem de boas-vindas\n"
/help - Exibe esta lista de comandos\n"
/sobre - Informações sobre este bot\n\n"
/furia - Informações gerais sobre a FURIA\n"
/roster - Mostra o roster atual\n"
/jogadores - Lista todos os jogadores\n"
/staff - Informações sobre a equipe técnica\n\n"
/agenda - Próximos jogos da FURIA
/resultados - Resultados recentes
/conquistas - Principais conquistas do time
/noticias - Últimas notícias sobre a FURIA
/social - Links para redes sociais oficiais
/curiosidades - Curiosidades sobre o time e jogadores

'''
furia_bot/
├── bot.py               # Código principal do bot
├── handlers.py          # Lógica dos comandos
|── furia_features.py    # Ferramentas e algumas instruções do handler
├── requirements.txt     # Dependências do projeto
└── README.md            # Instruções e informações do projeto
'''

## 🚀 Como rodar o bot localmente

1. **Clone o repositório**
```bash
git clone https://github.com/seuusuario/furia_bot.git
cd furia_bot
```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure seu token do BotFather**
No arquivo `bot.py`, substitua `SEU_TOKEN_AQUI` pelo token real do seu bot:
```python
TOKEN = "123456789:ABCDEF..."
```

5. **Execute o bot**
```bash
python bot.py
```

Se estiver tudo certo, o terminal mostrará:
```
Bot rodando...
```

## 📦 Requisitos

- Python 3.8+
- Conta no Telegram
- Um bot criado via [@BotFather](https://t.me/BotFather)


## 📌 Ideias futuras

- `/agenda` – Mostrar os próximos jogos da FURIA
- `/curiosidade` – Fatos curiosos sobre a equipe ou jogadores
- Integração com sites como HLTV, Liquipedia ou Draft5 via scraping/API

- Em Furia_features.py tem algumas sugestões que fiz com o Chatgpt em questões de QUIZ, só que não implementei no código, isso séria uma boa caso alguém queria testar e ver como ficaria, fiquem a vontade.
- 

## 👨‍💻 Autor

Desenvolvido por Glauber como parte de um desafio técnico.

---

Se quiser contribuir, sugerir melhorias ou relatar bugs, fique à vontade para abrir uma issue ou pull request! 🧠💬

