import os
import openai
# from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

# api_base = os.getenv("AZURE_OPENAI_BASE")
openai.api_key =  "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"
# api_key = "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"
# api_version = "2023-03-15-preview"

# openai.api_type = 'azure'
# openai.api_key = api_key
# openai.api_version = api_version
# openai.api_base = api_base

def get_completion(prompt, temperature=0, max_tokens=4000, top_p=0.95, frequency_penalty=0, presence_penalty=0, stop=None):
    return openai.Completion.create(
        model="gpt-4-0613",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
        request_timeout=3600,
        timeout=3600
    )

def get_chat_completion(input_text, temperature=0, max_tokens=4000, top_p=0.95, frequency_penalty=0, presence_penalty=0, stop=None):
    return openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages = [
            {"role":"system","content":'''
            
            
            You are an AI Nutritionist  that helps people to build diet plan based on the profile of individual. Please follow these steps:.
            1)Calculate BMI first 
            2)Provide how much calories are needed to achive the goal based on the body profile
            3)Provide comprehensive diet plan include exact serving siZe and the nutritional value(calories, carbs, fat and protiens) for each food item
            
            
            '''},
            {"role": "user", "content": input_text}],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
        request_timeout=3600,
        timeout=3600
    )
