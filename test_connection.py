import os
from dotenv import load_dotenv
from apify_client import ApifyClient
from exa_py import Exa

load_dotenv()

apify_token = os.getenv("APIFY_TOKEN")
exa_key = os.getenv("EXA_API_KEY")

if not apify_token or not exa_key:
    print("API keys are missing. Check your .env file.")
else:
    print("Both API keys are loaded.")

    try:
        apify = ApifyClient(apify_token)
        user = apify.user().get()
        print("Apify connection successful!")
        print("Account information retrieved:",user)

    except Exception as e:
        print("Apify connection failed:", e)

    try:
        exa = Exa(api_key=exa_key)
        results = exa.search(
            "Latest financial news about Samsung Electronics",
            num_results=2
        )
        print("Exa connection successful!")
        print("News results received.")

    except Exception as e:
        print("Exa connection failed:", e)