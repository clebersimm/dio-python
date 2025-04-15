# Desafio DIO Análise de Sentimentos

Devido a problemas em criar conta na Azure, resolvi utilizar uma abordagem diferente e as ferramentas que foram apresentadas durante o curso:
- python   
- Copilot

Utílizando o promt do copilot, perguntei alterativas ao Language Studio do Azure utilizando python e a resposta foi a lib do python nltk. Pedi um exemplo e o copilot me apresentou o código abaixo:


```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Certifique-se de baixar os recursos necessários do NLTK
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Inicializa o analisador de sentimentos
    sia = SentimentIntensityAnalyzer()
    
    # Calcula o sentimento
    sentiment_scores = sia.polarity_scores(text)
    
    # Exibe os resultados
    print(f"Sentiment Scores: {sentiment_scores}")
    if sentiment_scores['compound'] >= 0.05:
        print("Sentimento geral: Positivo")
    elif sentiment_scores['compound'] <= -0.05:
        print("Sentimento geral: Negativo")
    else:
        print("Sentimento geral: Neutro")

# Exemplo de uso
if __name__ == "__main__":
    texto = """
    Eu adoro usar o NLTK para análise de sentimentos!
    É uma biblioteca poderosa e prática.
    """
    analyze_sentiment(texto)
```

Com a explicação de como utilizar:

```
Como usar o código:
Instalação do NLTK: Certifique-se de que o NLTK está instalado executando pip install nltk no terminal.
Download do léxico VADER: O script já inclui o comando nltk.download('vader_lexicon'), que baixa o modelo de análise de sentimentos.
Personalizar o texto: Substitua o conteúdo da variável texto pelo documento ou frase que você deseja analisar.
Executar o script: Execute o script e veja os resultados da análise de sentimentos.
Explicação:
SentimentIntensityAnalyzer: Analisa o texto e retorna uma pontuação para positividade, negatividade, neutralidade e um score composto (compound), que é uma média ponderada.
Score composto:
>= 0.05: Sentimento positivo.
<= -0.05: Sentimento negativo.
Entre esses valores: Sentimento neutro.
Se precisar de mais ajuda ou quiser aplicar isso em documentos maiores, como arquivos de texto ou PDFs, posso te ajudar a expandir o script!
```

Pedi mais algumas alterações para poder ler um arquivo(sentencas.txt) e gerar o arquivo output.json. Essas alterações também utilizando o copilot para alterações no código python. 

O resultado foi o arquivo sentimentos.py, que "lê" o arquivo sentencas.txt, realiza a analise e gera o arquivo output.json.  

Ps: utilizei o chatpgt para poder gerar o arquivo sentencas.txt, com o prompt abaixo:

```
Estou fazendo um trabalho com o lib nltk do python e preciso gerar alguns exemplos para testar a biblioteca, seria possível gerar 20 entradas com sentimentos positivos e negativos?
Com sentenças longas.
```

Chatgpt se ofereceu para gerar em outros formatos mas queria testar o copilot neste assunto.


Classe sentimentos.py com auxílio do copilot.   


```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import json

# Certifique-se de baixar os recursos necessários do NLTK
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    # Inicializa o analisador de sentimentos
    sia = SentimentIntensityAnalyzer()
    
    # Calcula o sentimento
    sentiment_scores = sia.polarity_scores(text)
    
    # Exibe os resultados
    print(f"Sentiment Scores: {sentiment_scores}")
    if sentiment_scores['compound'] >= 0.05:
        print("Sentimento geral: Positivo")
    elif sentiment_scores['compound'] <= -0.05:
        print("Sentimento geral: Negativo")
    else:
        print("Sentimento geral: Neutro")

# Exemplo de uso
if __name__ == "__main__":

    # Lê o conteúdo do arquivo sentencas.txt
    with open('sentencas.txt', 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    
    # Remove espaços em branco e aspas das frases
    sentences = [sentence.strip().strip('"') for sentence in sentences]
    
    # Lista para armazenar os resultados
    results = []

    # Analisa o sentimento de cada frase
    for texto in sentences:
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(texto)
        sentiment = "Neutro"
        if sentiment_scores['compound'] >= 0.05:
            sentiment = "Positivo"
        elif sentiment_scores['compound'] <= -0.05:
            sentiment = "Negativo"
        
        # Adiciona os resultados à lista
        results.append({
            "frase": texto,
            "sentimento": sentiment,
            "scores": sentiment_scores
        })
    
    # Salva os resultados em um arquivo JSON
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4) 
```
