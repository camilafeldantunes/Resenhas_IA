## DESAFIO FINAL
## Etapa 1 - Carregar um arquivo .txt onde cada linha será um elemento de uma lista Python
## Etapa 2 - Mandar ao modelo que está rodando localmente para extrair em formato JSON 
## onde cada item terá usuario, resenha original, resenha_pt, avaliacao
## Etapa 3 - Transformar a resposta do modelo em uma lista de dicionários Python
## Etapa 4 - Criar uma função que dada uma lista de dicionários, percorre a lista e faz 2 coisas
## a) conta a quantidade de avaliações positivas, negativas e neutras
## b) une cada item dessa lista em uma variável do tipo string com algum separador
## Ao final, retorna ambas das coisas

from openai import OpenAI 
import json

client_openai = OpenAI(
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "lm-studio"
)

lista_resenhas = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_resenhas.append(linha.strip())

resenhas_formatadas = "\n".join(lista_resenhas)


resposta_llm = client_openai.chat.completions.create(
    model = "google/gemma-3-1b",
    messages = [
        {
            "role": "system",
            "content": "Você é uma assistente de IA prestativo"
        },
        {
            "role": "user",
            "content": f"""
            Você receberá uma lista de resenhas no seguinte formato:

            codigo$usuario$resenha

            Exemplo:
            12345$exemplo$exemploexemplo.

            TAREFA:

            Para cada resenha, retorne um JSON seguindo EXATAMENTE esta estrutura:
            [
                {{
                    "usuario": "",
                    "resenha_original": "",
                    "resenha_pt": "",
                    "avaliacao": ""
                
                }}
                
            ]
               
            REGRAS IMPORTANTES:

            - "usuario": deve conter APENAS o texto que está entre os dois símbolos $
            - "resenha_original": deve ser a resenha original exatamente como recebida
            - "resenha_pt": deve ser a tradução da resenha para português brasileiro (NA LINGUA PORTUGUESA)
            - "avaliacao": deve ser somente uma das três opções:
            "Positiva", "Negativa" ou "Neutra"

            - NÃO inclua explicações
            - NÃO inclua texto fora do JSON
            - NÃO inclua comentários
            - Retorne apenas JSON válido
            
            

            Segue a lista de resenhas:

            {resenhas_formatadas}

            """
        }
    ],
    temperature = 0.2

    

)
texto_json = resposta_llm.choices[0].message.content

resenhas_json = texto_json.replace("```json", "").replace("```", "").strip()

dicionario_json = json.loads(resenhas_json)


def contador(dicionario_json):
    lista_textos_srt = []
    pos = 0
    neg = 0
    neu = 0
    for resenha in dicionario_json:
        avaliacoes = resenha["avaliacao"]

        if avaliacoes == 'Positiva':
            pos +=1
        elif avaliacoes == 'Negativa':
            neg +=1
        else:
            neu+=1
        lista_textos_srt.append(str(resenha))
    

    textos_unidos = "####".join(lista_textos_srt)
    return pos, neg, neu, textos_unidos
    


positivo, negativo, neutro, textos= contador(dicionario_json)

print(f"Positivas: {positivo}")
print(f"Negativas: {negativo}")
print(f"Neutro: {neutro}")
print(f"Textos: {textos}")

