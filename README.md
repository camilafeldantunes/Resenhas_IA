# Resenhas_IA

Projeto em Python para processar resenhas de aplicativos usando um modelo de linguagem local (Gemma 3) e gerar análises estruturadas em JSON.

---

## 📝 Descrição

Este projeto realiza o seguinte fluxo:

1. Carrega um arquivo `.txt` onde cada linha representa uma resenha no formato `codigo$usuario$resenha`.
2. Envia as resenhas a um modelo de linguagem local (`Gemma 3`) para extrair informações em **JSON**, contendo:
   - `usuario`: nome do usuário
   - `resenha_original`: resenha exatamente como recebida
   - `resenha_pt`: resenha traduzida para português
   - `avaliacao`: categorizada como `Positiva`, `Negativa` ou `Neutra`
3. Transforma a resposta JSON em uma lista de dicionários Python.
4. Conta o número de avaliações positivas, negativas e neutras, e une todas as resenhas em uma única string separada por delimitadores.

---

## 💻 Tecnologias e Bibliotecas

- Python 3.x
- Bibliotecas:
  - `openai` (para conexão com o modelo local)
  - `json`
- Ambiente virtual: `.venv` (não incluído no repositório)
- Modelo de linguagem local: `google/gemma-3-1b` rodando via LM Studio

---


