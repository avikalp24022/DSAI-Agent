from tools.llm_inference import inference

CONVERSATION_PROMPT="""
Hi, Following are the tasks that you can do:
Available tasks:
- "transcribe_audio": Convert audio to text (only if input_type is audio and not already transcribed)
- "ocr_image": Extract text from image (only if input_type is image and not already extracted)
- "parse_pdf": Extract text from PDF (only if input_type is pdf and not already extracted)
- "fetch_youtube": Get YouTube transcript (only if youtube URL detected)
- "summarize": Create 1-line + 3 bullets + 5-sentence summary
- "sentiment_analysis": Analyze sentiment with label + confidence + justification
- "code_explanation": Explain code + detect bugs + time complexity
- "conversational_response": Answer general questions

Handle the user query humanly:
{user_query}
"""

def answer_question(prompt: str, json_mode: bool = False) -> str:
    user_prompt=CONVERSATION_PROMPT.format(user_query=prompt)
    return inference(user_prompt=user_prompt)