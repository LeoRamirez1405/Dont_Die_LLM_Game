import openai
import json

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)

messages = [
    {"role": "user", "content": "What are Nike's net income in 2022?"}
]

tools = [
    {
        "type": "function",
        "function": {
            # name of the function 
            "name": "get_financial_data",
            # a good, detailed description for what the function is supposed to do
            "description": "Get financial data for a company given the metric and year.",
            # a well defined json schema: https://json-schema.org/learn/getting-started-step-by-step#define
            "parameters": {
                # for OpenAI compatibility, we always declare a top level object for the parameters of the function
                "type": "object",
                # the properties for the object would be any arguments you want to provide to the function
                "properties": {
                    "metric": {
                        # JSON Schema supports string, number, integer, object, array, boolean and null
                        # for more information, please check out https://json-schema.org/understanding-json-schema/reference/type
                        "type": "string",
                        # You can restrict the space of possible values in an JSON Schema
                        # you can check out https://json-schema.org/understanding-json-schema/reference/enum for more examples on how enum works
                        "enum": ["net_income", "revenue", "ebdita"],
                    },
                    "financial_year": {
                        "type": "integer", 
                        # If the model does not understand how it is supposed to fill the field, a good description goes a long way 
                        "description": "Year for which we want to get financial data."
                    },
                    "company": {
                        "type": "string",
                        "description": "Name of the company for which we want to get financial data."
                    }
                },
                # You can specify which of the properties from above are required
                # for more info on `required` field, please check https://json-schema.org/understanding-json-schema/reference/object#required
                "required": ["metric", "financial_year", "company"],
            },
        },
    }
]

chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/firefunction-v2",
    messages=messages,
    tools=tools,
    temperature=0.1
)
print(chat_completion.choices[0].message.model_dump_json(indent=4))

def get_financial_data(metric: str, financial_year: int, company: str):
    print(f"{metric=} {financial_year=} {company=}")
    if metric == "net_income" and financial_year == 2022 and company == "Nike":
        return {"net_income": 6_046_000_000}
    else:
        raise NotImplementedError()

function_call = chat_completion.choices[0].message.tool_calls[0].function
tool_response = locals()[function_call.name](**json.loads(function_call.arguments))
print(tool_response)

