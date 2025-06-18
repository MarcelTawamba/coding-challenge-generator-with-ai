import os
import json
from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    """
    Generate a challenge using OpenAI's API based on the specified difficulty.
    """
    system_prompt = """You are an expert coding challenge generator.
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.
    
    For easy questions: Focus on basic syntax, simple operations or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.
    
    Return the challenge in the following JSON format:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0,  // Index of the correct answer in the options array (0-3)
        "explanation": "Detailed explanation of why the correct is right."
    }
    
    Make sure the options are plausible but with only one clearly correct answer.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} coding challenge."}
            ],
            temperature=0.7, # the higher the temperature, the more creative/varied the response
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)
        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise Exception(f"Missing required field: {field} in the response")

        return challenge_data

    except Exception as e:
        print(e)
        return {
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.insert(5)",
                "my_list.push(5)"
            ],
            "correct_answer_id": 0,
            "explanation": "The correct method to add an element to a list in Python is 'append()'."
        }
