![Preview Image](https://framerusercontent.com/images/HBA5vNT8jvHlhjxkuAYiRS2WLWE.jpg)
## Desafios e Prêmios
## Semana
## 1
## 08/07 - 12/07 🔴
## Prompt Engineering
## Semana
## 2
## 15/07 - 28/07 🔴
## RAG
## Semana
## 3
## 29/07 - 11/08 🔴
## Agents
## Semana
## 4
## 11/08 - 08/09 🔴
## Tema Livre
**🗓️****Objetivo**
Criar uma implementação no Langflow que processe um arquivo de texto fornecido, extraia o conteúdo do artigo e gere um resumo conciso e abrangente. Assista o vídeo explicativo abaixo para começar:
**🏆 Premiação**
Os prêmios da semana 1 serão distribuídos para os primeiros 50 ranqueados, conforme a tabela abaixo:
Posição
Prêmio
Desafio Final
1º Lugar
R$1.000,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
2º Lugar
R$800,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
3º Lugar
R$500,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
4º Lugar
R$300,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
5º ao 10º Lugar
R$250,00 cada (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
11º ao 20º Lugar
R$200,00 cada (Gift Card)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
21º ao 30º Lugar
R$200,00 cada (Gift Card)
31º ao 50º Lugar
R$100,00 cada (Gift Card)
  * **Score:** Score de 0 a 1 computado a partir do algoritmo de avaliação do desafio 1.
  * **Ticket:** Os vencedores receberão um ticket para participar do desafio final - semana 4.
  * **Gift Cards:** mais informações em breve.


**🏅 Premiação Adicional**
Serão distribuídos prêmios extras de R$500 para os 5 melhores conteúdos produzidos e submetidos oficialmente durante a semana 1.
  * Vídeos, shorts ou tutoriais sobre o projeto, a competição ou o Langflow em geral.
  * Ao produzir seu video, utilize as _hashtags #langflow #iadevs_ para localizarmos o seu conteúdo. No formulário você pode inserir o link do seu video.
  * A avaliação do conteúdo ocorrerá de forma subjetiva pelos organizadores, considerando fatores como a qualidade, a divulgação e o alcance do material produzido em diversas plataformas.


**⚙️ Instalação e configuração:**
  1. Se você já tem Python instalado, comece com o [pip](https://www.langflow.org/pt/iadevs/<https:/pip.pypa.io/en/stable/installation/>): 


```
python -m pip install langflow
```

  1. Consulte a documentação oficial: <https://docs.langflow.org/>


Se precisar de ajuda para a instalar o Langflow, entre no nosso servidor do [Discord](https://www.langflow.org/pt/iadevs/<https:/discord.gg/ZGrjF4v2N6>) e te ajudamos a começar!
🔎 **Flow de referência**
O projeto abaixo será utilizado como referência para criação do resumo e avaliação. A figura abaixo ilustra o flow com o objetivo do desafio, onde o output será criar um resumo do conteúdo do arquivo:
![](https://framerusercontent.com/images/8ZyTxNZPkyLjj2Q2nHYzHgCE1s.png?scale-down-to=2048)
A ilustração abaixo demonstra como o resumo será avaliado, onde você pode simular o score do seu projeto:
![](https://framerusercontent.com/images/uDYKpMFg5PHT3J4kTWU8LpOllU.png?scale-down-to=1024)
Ao rodar o flow com todos o componentes conectados você verá um output com o resumo do texto extraído e o score de avaliação.
Abaixo estão o flow de referência e o arquivo com conteúdo a resumir:
Prompt Engineering.md
📝 **Metodologia de Avaliação**
A avaliação da qualidade do resumo será realizada em duas etapas:
  1. **Score Inicial** : computa-se a `similaridade contextual` com o artigo original.
  2. **Score Final** : aplica-se um `fator de redução` para penalizar resumos longos, diminuindo o Score Inicial.


**Similaridade Contextual**
  * Mede-se a similaridade contextual entre trechos relevantes do texto original e o resumo utilizando **cosine similarity**.
  * Vetores de embeddings são gerados tanto para o texto original quanto para o resumo.
  * Quanto mais similares os dois vetores, maior a pontuação inicial.


```
embedding1 = np.array(embedding_model.embed_query(text1))
embedding2 = np.array(embedding_model.embed_query(text2))
# Calculate cosine similarity
dot_product = np.dot(embedding1, embedding2)
norm1 = np.linalg.norm(embedding1)
norm2 = np.linalg.norm(embedding2)
similarity = dot_product / (norm1 * norm2)
```

**Ajuste pelo Comprimento do Resumo**
  * Após calcular a pontuação inicial, aplica-se uma penalização para resumos mais longos.
  * Resumos mais curtos recebem uma menor penalização, resultando em uma pontuação final mais alta.
  * Esta parte incentiva a concisão, favorecendo resumos que sejam tanto informativos quanto breves.


```
max_chars = 10000 # Limite máximo de caracteres
min_score = 0.0 # Score mínimo 
max_score = 1.0 # Score máximo
tamanho_resumo = len(resumo)
if tamanho_resumo >= max_chars: 
score_final = min_score 
else: fator_reducao = (max_chars - tamanho_resumo) / max_chars 
score_final = score_inicial * fator_reducao 
score_final = max(min_score, min(max_score, score_final))
```

Lembre-se que a geração de texto por modelos de linguagem pode não ser reproduzível. Seu score oficial não necessariamente será exatamente o mesmo da simulação.
**✅ Requisitos**
  1. O resumo deve ser o mais sucinto possível (curto em número de caracteres).
  2. O resumo deve ser rico em conteúdo, contendo definições e vocabulário dos tópicos principais.
  3. A saída do chat deve exibir apenas o resumo do artigo.
  4. É obrigatório utilizar pelo menos um componente `Prompt` e um componente `LLM`.


**🚀 Submissão**
  * Todas as submissões devem ser feitas através do formulário: <https://forms.gle/ZY9BSJ8AckxGyyxQ7>
  * **Obrigatório:** Arquivo JSON (flow) do projeto, exportado sem API Key.
  * **Opcional:** Criação de Conteúdo
  * A submissão do projeto pode acontecer várias vezes por participante. Mas apenas a última submissão será considerada. 


**📅 Datas importantes**
  * 08/07/2024: Live de Lançamento da competição no [Crowdcast](https://www.langflow.org/pt/iadevs/<https:/www.crowdcast.io/c/rx3ylk3ntbg8>)
  * 10/07/2024: Sessão ao vivo com o time do Langflow
  * 12/07/2024: Prazo final para submissão (23:59)
  * 15/07/2024: Divulgação dos vencedores e anúncio do próximo desafio.


Boa sorte a todos os participantes!
## Semana
## 1
## 08/07 - 12/07 🔴
## Prompt Engineering
## Semana
## 2
## 15/07 - 28/07 🔴
## RAG
## Semana
## 3
## 29/07 - 11/08 🔴
## Agents
## Semana
## 4
## 11/08 - 08/09 🔴
## Tema Livre
**🗓️****Objetivo**
Criar uma implementação no Langflow que processe um arquivo de texto fornecido, extraia o conteúdo do artigo e gere um resumo conciso e abrangente. Assista o vídeo explicativo abaixo para começar:
**🏆 Premiação**
Os prêmios da semana 1 serão distribuídos para os primeiros 50 ranqueados, conforme a tabela abaixo:
Posição
Prêmio
Desafio Final
1º Lugar
R$1.000,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
2º Lugar
R$800,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
3º Lugar
R$500,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
4º Lugar
R$300,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
5º ao 10º Lugar
R$250,00 cada (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
11º ao 20º Lugar
R$200,00 cada (Gift Card)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
21º ao 30º Lugar
R$200,00 cada (Gift Card)
31º ao 50º Lugar
R$100,00 cada (Gift Card)
  * **Score:** Score de 0 a 1 computado a partir do algoritmo de avaliação do desafio 1.
  * **Ticket:** Os vencedores receberão um ticket para participar do desafio final - semana 4.
  * **Gift Cards:** mais informações em breve.


**🏅 Premiação Adicional**
Serão distribuídos prêmios extras de R$500 para os 5 melhores conteúdos produzidos e submetidos oficialmente durante a semana 1.
  * Vídeos, shorts ou tutoriais sobre o projeto, a competição ou o Langflow em geral.
  * Ao produzir seu video, utilize as _hashtags #langflow #iadevs_ para localizarmos o seu conteúdo. No formulário você pode inserir o link do seu video.
  * A avaliação do conteúdo ocorrerá de forma subjetiva pelos organizadores, considerando fatores como a qualidade, a divulgação e o alcance do material produzido em diversas plataformas.


**⚙️ Instalação e configuração:**
  1. Se você já tem Python instalado, comece com o [pip](https://www.langflow.org/pt/iadevs/<https:/pip.pypa.io/en/stable/installation/>): 


```
python -m pip install langflow
```

  1. Consulte a documentação oficial: <https://docs.langflow.org/>


Se precisar de ajuda para a instalar o Langflow, entre no nosso servidor do [Discord](https://www.langflow.org/pt/iadevs/<https:/discord.gg/ZGrjF4v2N6>) e te ajudamos a começar!
🔎 **Flow de referência**
O projeto abaixo será utilizado como referência para criação do resumo e avaliação. A figura abaixo ilustra o flow com o objetivo do desafio, onde o output será criar um resumo do conteúdo do arquivo:
![](https://framerusercontent.com/images/8ZyTxNZPkyLjj2Q2nHYzHgCE1s.png?scale-down-to=2048)
A ilustração abaixo demonstra como o resumo será avaliado, onde você pode simular o score do seu projeto:
![](https://framerusercontent.com/images/uDYKpMFg5PHT3J4kTWU8LpOllU.png?scale-down-to=1024)
Ao rodar o flow com todos o componentes conectados você verá um output com o resumo do texto extraído e o score de avaliação.
Abaixo estão o flow de referência e o arquivo com conteúdo a resumir:
Prompt Engineering.md
📝 **Metodologia de Avaliação**
A avaliação da qualidade do resumo será realizada em duas etapas:
  1. **Score Inicial** : computa-se a `similaridade contextual` com o artigo original.
  2. **Score Final** : aplica-se um `fator de redução` para penalizar resumos longos, diminuindo o Score Inicial.


**Similaridade Contextual**
  * Mede-se a similaridade contextual entre trechos relevantes do texto original e o resumo utilizando **cosine similarity**.
  * Vetores de embeddings são gerados tanto para o texto original quanto para o resumo.
  * Quanto mais similares os dois vetores, maior a pontuação inicial.


```
embedding1 = np.array(embedding_model.embed_query(text1))
embedding2 = np.array(embedding_model.embed_query(text2))
# Calculate cosine similarity
dot_product = np.dot(embedding1, embedding2)
norm1 = np.linalg.norm(embedding1)
norm2 = np.linalg.norm(embedding2)
similarity = dot_product / (norm1 * norm2)
```

**Ajuste pelo Comprimento do Resumo**
  * Após calcular a pontuação inicial, aplica-se uma penalização para resumos mais longos.
  * Resumos mais curtos recebem uma menor penalização, resultando em uma pontuação final mais alta.
  * Esta parte incentiva a concisão, favorecendo resumos que sejam tanto informativos quanto breves.


```
max_chars = 10000 # Limite máximo de caracteres
min_score = 0.0 # Score mínimo 
max_score = 1.0 # Score máximo
tamanho_resumo = len(resumo)
if tamanho_resumo >= max_chars: 
score_final = min_score 
else: fator_reducao = (max_chars - tamanho_resumo) / max_chars 
score_final = score_inicial * fator_reducao 
score_final = max(min_score, min(max_score, score_final))
```

Lembre-se que a geração de texto por modelos de linguagem pode não ser reproduzível. Seu score oficial não necessariamente será exatamente o mesmo da simulação.
**✅ Requisitos**
  1. O resumo deve ser o mais sucinto possível (curto em número de caracteres).
  2. O resumo deve ser rico em conteúdo, contendo definições e vocabulário dos tópicos principais.
  3. A saída do chat deve exibir apenas o resumo do artigo.
  4. É obrigatório utilizar pelo menos um componente `Prompt` e um componente `LLM`.


**🚀 Submissão**
  * Todas as submissões devem ser feitas através do formulário: <https://forms.gle/ZY9BSJ8AckxGyyxQ7>
  * **Obrigatório:** Arquivo JSON (flow) do projeto, exportado sem API Key.
  * **Opcional:** Criação de Conteúdo
  * A submissão do projeto pode acontecer várias vezes por participante. Mas apenas a última submissão será considerada. 


**📅 Datas importantes**
  * 08/07/2024: Live de Lançamento da competição no [Crowdcast](https://www.langflow.org/pt/iadevs/<https:/www.crowdcast.io/c/rx3ylk3ntbg8>)
  * 10/07/2024: Sessão ao vivo com o time do Langflow
  * 12/07/2024: Prazo final para submissão (23:59)
  * 15/07/2024: Divulgação dos vencedores e anúncio do próximo desafio.


Boa sorte a todos os participantes!
## Semana
## 1
## 08/07 - 12/07 🔴
## Prompt Engineering
## Semana
## 2
## 15/07 - 28/07 🔴
## RAG
## Semana
## 3
## 29/07 - 11/08 🔴
## Agents
## Semana
## 4
## 11/08 - 08/09 🔴
## Tema Livre
**🗓️****Objetivo**
Criar uma implementação no Langflow que processe um arquivo de texto fornecido, extraia o conteúdo do artigo e gere um resumo conciso e abrangente. Assista o vídeo explicativo abaixo para começar:
**🏆 Premiação**
Os prêmios da semana 1 serão distribuídos para os primeiros 50 ranqueados, conforme a tabela abaixo:
Posição
Prêmio
Desafio Final
1º Lugar
R$1.000,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
2º Lugar
R$800,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
3º Lugar
R$500,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
4º Lugar
R$300,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
5º ao 10º Lugar
R$250,00 cada (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
11º ao 20º Lugar
R$200,00 cada (Gift Card)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
21º ao 30º Lugar
R$200,00 cada (Gift Card)
31º ao 50º Lugar
R$100,00 cada (Gift Card)
  * **Score:** Score de 0 a 1 computado a partir do algoritmo de avaliação do desafio 1.
  * **Ticket:** Os vencedores receberão um ticket para participar do desafio final - semana 4.
  * **Gift Cards:** mais informações em breve.


**🏅 Premiação Adicional**
Serão distribuídos prêmios extras de R$500 para os 5 melhores conteúdos produzidos e submetidos oficialmente durante a semana 1.
  * Vídeos, shorts ou tutoriais sobre o projeto, a competição ou o Langflow em geral.
  * Ao produzir seu video, utilize as _hashtags #langflow #iadevs_ para localizarmos o seu conteúdo. No formulário você pode inserir o link do seu video.
  * A avaliação do conteúdo ocorrerá de forma subjetiva pelos organizadores, considerando fatores como a qualidade, a divulgação e o alcance do material produzido em diversas plataformas.


**⚙️ Instalação e configuração:**
  1. Se você já tem Python instalado, comece com o [pip](https://www.langflow.org/pt/iadevs/<https:/pip.pypa.io/en/stable/installation/>): 


```
python -m pip install langflow
```

  1. Consulte a documentação oficial: <https://docs.langflow.org/>


Se precisar de ajuda para a instalar o Langflow, entre no nosso servidor do [Discord](https://www.langflow.org/pt/iadevs/<https:/discord.gg/ZGrjF4v2N6>) e te ajudamos a começar!
🔎 **Flow de referência**
O projeto abaixo será utilizado como referência para criação do resumo e avaliação. A figura abaixo ilustra o flow com o objetivo do desafio, onde o output será criar um resumo do conteúdo do arquivo:
![](https://framerusercontent.com/images/8ZyTxNZPkyLjj2Q2nHYzHgCE1s.png?scale-down-to=2048)
A ilustração abaixo demonstra como o resumo será avaliado, onde você pode simular o score do seu projeto:
![](https://framerusercontent.com/images/uDYKpMFg5PHT3J4kTWU8LpOllU.png?scale-down-to=1024)
Ao rodar o flow com todos o componentes conectados você verá um output com o resumo do texto extraído e o score de avaliação.
Abaixo estão o flow de referência e o arquivo com conteúdo a resumir:
Prompt Engineering.md
📝 **Metodologia de Avaliação**
A avaliação da qualidade do resumo será realizada em duas etapas:
  1. **Score Inicial** : computa-se a `similaridade contextual` com o artigo original.
  2. **Score Final** : aplica-se um `fator de redução` para penalizar resumos longos, diminuindo o Score Inicial.


**Similaridade Contextual**
  * Mede-se a similaridade contextual entre trechos relevantes do texto original e o resumo utilizando **cosine similarity**.
  * Vetores de embeddings são gerados tanto para o texto original quanto para o resumo.
  * Quanto mais similares os dois vetores, maior a pontuação inicial.


```
embedding1 = np.array(embedding_model.embed_query(text1))
embedding2 = np.array(embedding_model.embed_query(text2))
# Calculate cosine similarity
dot_product = np.dot(embedding1, embedding2)
norm1 = np.linalg.norm(embedding1)
norm2 = np.linalg.norm(embedding2)
similarity = dot_product / (norm1 * norm2)
```

**Ajuste pelo Comprimento do Resumo**
  * Após calcular a pontuação inicial, aplica-se uma penalização para resumos mais longos.
  * Resumos mais curtos recebem uma menor penalização, resultando em uma pontuação final mais alta.
  * Esta parte incentiva a concisão, favorecendo resumos que sejam tanto informativos quanto breves.


```
max_chars = 10000 # Limite máximo de caracteres
min_score = 0.0 # Score mínimo 
max_score = 1.0 # Score máximo
tamanho_resumo = len(resumo)
if tamanho_resumo >= max_chars: 
score_final = min_score 
else: fator_reducao = (max_chars - tamanho_resumo) / max_chars 
score_final = score_inicial * fator_reducao 
score_final = max(min_score, min(max_score, score_final))
```

Lembre-se que a geração de texto por modelos de linguagem pode não ser reproduzível. Seu score oficial não necessariamente será exatamente o mesmo da simulação.
**✅ Requisitos**
  1. O resumo deve ser o mais sucinto possível (curto em número de caracteres).
  2. O resumo deve ser rico em conteúdo, contendo definições e vocabulário dos tópicos principais.
  3. A saída do chat deve exibir apenas o resumo do artigo.
  4. É obrigatório utilizar pelo menos um componente `Prompt` e um componente `LLM`.


**🚀 Submissão**
  * Todas as submissões devem ser feitas através do formulário: <https://forms.gle/ZY9BSJ8AckxGyyxQ7>
  * **Obrigatório:** Arquivo JSON (flow) do projeto, exportado sem API Key.
  * **Opcional:** Criação de Conteúdo
  * A submissão do projeto pode acontecer várias vezes por participante. Mas apenas a última submissão será considerada. 


**📅 Datas importantes**
  * 08/07/2024: Live de Lançamento da competição no [Crowdcast](https://www.langflow.org/pt/iadevs/<https:/www.crowdcast.io/c/rx3ylk3ntbg8>)
  * 10/07/2024: Sessão ao vivo com o time do Langflow
  * 12/07/2024: Prazo final para submissão (23:59)
  * 15/07/2024: Divulgação dos vencedores e anúncio do próximo desafio.


Boa sorte a todos os participantes!
## Semana
## 1
## 08/07 - 12/07 🔴
## Prompt Engineering
## Semana
## 2
## 15/07 - 28/07 🔴
## RAG
## Semana
## 3
## 29/07 - 11/08 🔴
## Agents
## Semana
## 4
## 11/08 - 08/09 🔴
## Tema Livre
**🗓️****Objetivo**
Criar uma implementação no Langflow que processe um arquivo de texto fornecido, extraia o conteúdo do artigo e gere um resumo conciso e abrangente. Assista o vídeo explicativo abaixo para começar:
**🏆 Premiação**
Os prêmios da semana 1 serão distribuídos para os primeiros 50 ranqueados, conforme a tabela abaixo:
Posição
Prêmio
Desafio Final
1º Lugar
R$1.000,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
2º Lugar
R$800,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
3º Lugar
R$500,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
4º Lugar
R$300,00 (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
5º ao 10º Lugar
R$250,00 cada (PIX)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
11º ao 20º Lugar
R$200,00 cada (Gift Card)
Ticket Desafio Final [🎫](https://www.langflow.org/pt/iadevs/<https:/emojipedia.org/ticket>)
21º ao 30º Lugar
R$200,00 cada (Gift Card)
31º ao 50º Lugar
R$100,00 cada (Gift Card)
  * **Score:** Score de 0 a 1 computado a partir do algoritmo de avaliação do desafio 1.
  * **Ticket:** Os vencedores receberão um ticket para participar do desafio final - semana 4.
  * **Gift Cards:** mais informações em breve.


**🏅 Premiação Adicional**
Serão distribuídos prêmios extras de R$500 para os 5 melhores conteúdos produzidos e submetidos oficialmente durante a semana 1.
  * Vídeos, shorts ou tutoriais sobre o projeto, a competição ou o Langflow em geral.
  * Ao produzir seu video, utilize as _hashtags #langflow #iadevs_ para localizarmos o seu conteúdo. No formulário você pode inserir o link do seu video.
  * A avaliação do conteúdo ocorrerá de forma subjetiva pelos organizadores, considerando fatores como a qualidade, a divulgação e o alcance do material produzido em diversas plataformas.


**⚙️ Instalação e configuração:**
  1. Se você já tem Python instalado, comece com o [pip](https://www.langflow.org/pt/iadevs/<https:/pip.pypa.io/en/stable/installation/>): 


```
python -m pip install langflow
```

  1. Consulte a documentação oficial: <https://docs.langflow.org/>


Se precisar de ajuda para a instalar o Langflow, entre no nosso servidor do [Discord](https://www.langflow.org/pt/iadevs/<https:/discord.gg/ZGrjF4v2N6>) e te ajudamos a começar!
🔎 **Flow de referência**
O projeto abaixo será utilizado como referência para criação do resumo e avaliação. A figura abaixo ilustra o flow com o objetivo do desafio, onde o output será criar um resumo do conteúdo do arquivo:
![](https://framerusercontent.com/images/8ZyTxNZPkyLjj2Q2nHYzHgCE1s.png?scale-down-to=2048)
A ilustração abaixo demonstra como o resumo será avaliado, onde você pode simular o score do seu projeto:
![](https://framerusercontent.com/images/uDYKpMFg5PHT3J4kTWU8LpOllU.png?scale-down-to=1024)
Ao rodar o flow com todos o componentes conectados você verá um output com o resumo do texto extraído e o score de avaliação.
Abaixo estão o flow de referência e o arquivo com conteúdo a resumir:
Prompt Engineering.md
📝 **Metodologia de Avaliação**
A avaliação da qualidade do resumo será realizada em duas etapas:
  1. **Score Inicial** : computa-se a `similaridade contextual` com o artigo original.
  2. **Score Final** : aplica-se um `fator de redução` para penalizar resumos longos, diminuindo o Score Inicial.


**Similaridade Contextual**
  * Mede-se a similaridade contextual entre trechos relevantes do texto original e o resumo utilizando **cosine similarity**.
  * Vetores de embeddings são gerados tanto para o texto original quanto para o resumo.
  * Quanto mais similares os dois vetores, maior a pontuação inicial.


```
embedding1 = np.array(embedding_model.embed_query(text1))
embedding2 = np.array(embedding_model.embed_query(text2))
# Calculate cosine similarity
dot_product = np.dot(embedding1, embedding2)
norm1 = np.linalg.norm(embedding1)
norm2 = np.linalg.norm(embedding2)
similarity = dot_product / (norm1 * norm2)
```

**Ajuste pelo Comprimento do Resumo**
  * Após calcular a pontuação inicial, aplica-se uma penalização para resumos mais longos.
  * Resumos mais curtos recebem uma menor penalização, resultando em uma pontuação final mais alta.
  * Esta parte incentiva a concisão, favorecendo resumos que sejam tanto informativos quanto breves.


```
max_chars = 10000 # Limite máximo de caracteres
min_score = 0.0 # Score mínimo 
max_score = 1.0 # Score máximo
tamanho_resumo = len(resumo)
if tamanho_resumo >= max_chars: 
score_final = min_score 
else: fator_reducao = (max_chars - tamanho_resumo) / max_chars 
score_final = score_inicial * fator_reducao 
score_final = max(min_score, min(max_score, score_final))
```

Lembre-se que a geração de texto por modelos de linguagem pode não ser reproduzível. Seu score oficial não necessariamente será exatamente o mesmo da simulação.
**✅ Requisitos**
  1. O resumo deve ser o mais sucinto possível (curto em número de caracteres).
  2. O resumo deve ser rico em conteúdo, contendo definições e vocabulário dos tópicos principais.
  3. A saída do chat deve exibir apenas o resumo do artigo.
  4. É obrigatório utilizar pelo menos um componente `Prompt` e um componente `LLM`.


**🚀 Submissão**
  * Todas as submissões devem ser feitas através do formulário: <https://forms.gle/ZY9BSJ8AckxGyyxQ7>
  * **Obrigatório:** Arquivo JSON (flow) do projeto, exportado sem API Key.
  * **Opcional:** Criação de Conteúdo
  * A submissão do projeto pode acontecer várias vezes por participante. Mas apenas a última submissão será considerada. 


**📅 Datas importantes**
  * 08/07/2024: Live de Lançamento da competição no [Crowdcast](https://www.langflow.org/pt/iadevs/<https:/www.crowdcast.io/c/rx3ylk3ntbg8>)
  * 10/07/2024: Sessão ao vivo com o time do Langflow
  * 12/07/2024: Prazo final para submissão (23:59)
  * 15/07/2024: Divulgação dos vencedores e anúncio do próximo desafio.


Boa sorte a todos os participantes!
[![](https://framerusercontent.com/images/aPtLvraX9agw6nlGOAOwxlRHtKI.svg)](https://www.langflow.org/pt/iadevs/<../old-home>)
[A Competição](https://www.langflow.org/pt/iadevs/<../iadevs>)
[Desafios e Prêmios](https://www.langflow.org/pt/iadevs/<./desafiosepremios>)
[FAQ](https://www.langflow.org/pt/iadevs/<./faq>)
[Tutoriais](https://www.langflow.org/pt/iadevs/<./tutoriais>)
[35k](https://www.langflow.org/pt/iadevs/<https:/bit.ly/langflow>)[9k](https://www.langflow.org/pt/iadevs/<https:/bit.ly/langflow-discord>)[6k](https://www.langflow.org/pt/iadevs/<https:/twitter.com/langflow_ai>)
[![](https://framerusercontent.com/images/aPtLvraX9agw6nlGOAOwxlRHtKI.svg)](https://www.langflow.org/pt/iadevs/<../old-home>)
[![](https://framerusercontent.com/images/aPtLvraX9agw6nlGOAOwxlRHtKI.svg)](https://www.langflow.org/pt/iadevs/<../old-home>)
![](https://framerusercontent.com/images/XsXHkHpEp361famMUwzS6j9QHo.png)
