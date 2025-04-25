Chatbot Telegram para Fãs da FURIA CS

Um bot do Telegram completo para os fãs do time de Counter-Strike da FURIA, oferecendo informações sobre o time, jogadores, competições, resultados e muito mais.

Funcionalidades

Informações sobre o Time
-Dados sobre a organização FURIA
-Roster atual completo
-Perfis detalhados de cada jogador
-Informações sobre a equipe técnica


Competições e Resultados
-Próximos jogos da FURIA
-Resultados recentes
-Histórico de conquistas
-Lembretes para jogos futuros

Estrutura do Projeto
furia_bot/
├── bot.py               # Código principal do bot
├── furia_features.py    # Funcionalidades específicas da FURIA
├── furia_info.md        # Informações coletadas sobre a FURIA
├── bot_structure.py     # Documentação da estrutura do bot
├── requirements.txt     # Lista de tarefas do projeto
└── README.md            # Este arquivo

Requisitos
Python 3.6+
python-telegram-bot (versão 22.0+)
Token de bot do Telegram (obtido via BotFather)

Instalação
Clone este repositório:
bash
git clone https://github.com/seu-usuario/furia-telegram-bot.git
cd furia-telegram-bot

Instale as dependências:
bash
pip install python-telegram-bot --upgrade
Configure o token do bot:
Obtenha um token do BotFather no Telegram (https://t.me/BotFather)
Substitua "SEU_TOKEN_AQUI" nos arquivos main.py e test_bot.py pelo seu token

Uso
Executando o Bot
Para iniciar o bot completo:
bash
python main.py
Para testar o bot com funcionalidades básicas:
bash
python test_bot.py
Para verificar se todas as funcionalidades estão corretas:
bash
python test_functions.py

Comandos Disponíveis
Comandos Básicos
/start - Inicia o bot e exibe mensagem de boas-vindas
/help - Exibe lista de comandos disponíveis
/sobre - Informações sobre o bot
Informações sobre o Time
/furia - Informações gerais sobre a FURIA
/roster - Mostra o roster atual
/jogadores - Lista todos os jogadores
/jogador [nome] - Informações sobre um jogador específico
/staff - Informações sobre a equipe técnica
Jogadores Específicos
/fallen - Informações sobre FalleN
/kscerato - Informações sobre KSCERATO
/yuurih - Informações sobre yuurih
/molodoy - Informações sobre molodoy
/yekindar - Informações sobre YEKINDAR
Competições e Resultados
/agenda - Próximos jogos da FURIA
/resultados - Resultados recentes
/conquistas - Principais conquistas do time
/social - Links para redes sociais da FURIA

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

Agradecimentos
FURIA Esports por inspirar este projeto
Comunidade de fãs da FURIA
Biblioteca python-telegram-bot

Foi desenvolvido por eu (Glauber), fiquei muito feliz de poder realizar este desafio.


