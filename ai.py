import os
import openai
import json 
import base64, requests
class RawDataProcessor:
    def __init__(self):
        self.info_save_folder = "C:\\RAW\\"
        
    def get_instgram_post(self, raw_data):
        try:
            prompt = f"{raw_data}This is url raw data content. By using this content, write perfect instgram post content with post principles and also with greate wise sayings."
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=500,
                temperature=0.8,
                top_p=0.9,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                n=1
            )
            return json.loads(response.choices[0].text.strip())
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {"":""}
    
    def process_unique_keys(self):
            for unique_key in os.listdir(self.info_save_folder):
                    print(unique_key)
                    with open(f"{self.info_save_folder}{unique_key}", 'r') as file:
                        raw_data = file.read()
                        post_content = self.get_instgram_post(raw_data)
                        print(post_content)
                        

if __name__ == "__main__":
    openai.api_key=""
    processor = RawDataProcessor()
    processor.process_unique_keys()
