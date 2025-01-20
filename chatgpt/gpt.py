from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

#OpenAIのAPI_KEYをjsonから読み込む
try:
    with open("ignore.json") as openai:
        openai_key = json.load(openai)
except FileNotFoundError:
    raise RuntimeError("ファイルが見つからない: open_api.json")
except json.JSONDecodeError:
    raise RuntimeError("JSON形式の解析中にエラーが発生: open_api.json")

OPENAI_API_KEY = openai_key["OPENAI_API_KEY"]

def sentgpt(question):
     
    llm = ChatOpenAI(api_key = OPENAI_API_KEY, model="gpt-4o-mini", temperature=0.5)
    
    #プロンプトテンプレート
    template = "質問内容を300文字以内で簡単に正しく説明してください。専門用語を使う場合は明快な例や比喩を使い説明してください。【質問内容】{question}"
    prompt = PromptTemplate(input_variables=["question"], template=template)

    #プロンプト | LLM設定 | gptの応答から文字列を解析
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    gpt_response = chain.invoke({"question":question})
    return gpt_response