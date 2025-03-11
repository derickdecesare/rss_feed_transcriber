from openai import OpenAI
import dotenv
dotenv.load_dotenv()

def test_openai_access():
    client = OpenAI()
    try:
        # response = client.chat.completions.create(
        #     model="gpt-4-0125-preview",  # This is the latest GPT-4 Turbo model
        #     messages=[
        #         {"role": "user", "content": "Say this is a test!"}
        #     ]
        # )
        # response = client.chat.completions.create(
        #     model="o1-preview",
        #     messages=[
        #         {
        #             "role": "user", 
        #             "content": "Say this is a test from o1!"
        #         }
        #     ]
        # )
        # response = client.chat.completions.create(
        #     model="o1-mini",
        #     messages=[
        #         {
        #             "role": "user", 
        #             "content": "Say this is a test from o1 mini!"
        #         }
        #     ]
        # )
        response = client.chat.completions.create(
            model="o1",
            messages=[
                {
                    "role": "user", 
                    "content": "Say this is a test from o1 mini!"
                }
            ]
        )
        print("Success! Response:", response.choices[0].message.content)
        return True
    except Exception as e:
        print("Error:", e)
        return False

if __name__ == "__main__":
    test_openai_access()
