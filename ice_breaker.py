import os

from dotenv import load_dotenv

if __name__ == "__main__":
    print("Hello Langchain")
    load_dotenv()
    print(os.environ['COOL_API_KEY'])