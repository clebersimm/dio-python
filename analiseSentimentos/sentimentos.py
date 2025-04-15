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
