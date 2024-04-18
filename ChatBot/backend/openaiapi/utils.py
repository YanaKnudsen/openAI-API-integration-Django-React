from openai import OpenAI
from django.conf import settings
#openai.api_key=settings.API_KEY

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=settings.API_KEY ,
)

message_array = []
message_array.append({"role":"system", "content":"you are helpful"})
def chat_gpt(message):
    message_array.append({"role":"user", "content":message})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_array
    )
    message_array.append({"role":"assistant", "content":response.choices[0].message.content.strip()})
    return response.choices[0].message.content.strip()