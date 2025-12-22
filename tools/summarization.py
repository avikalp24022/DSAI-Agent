from tools.llm_inference import inference

SUMMARIZATION_PROMPT = """
Summarize the following text in exactly 3 formats:

1. ONE-LINE SUMMARY (max 15 words)
2. THREE BULLET POINTS (key takeaways)
3. FIVE-SENTENCE SUMMARY (comprehensive overview)

Text:
{text}

Format your response exactly like this:

ONE-LINE SUMMARY:
[your one-line summary]

KEY POINTS:
• [point 1]
• [point 2]
• [point 3]

DETAILED SUMMARY:
[sentence 1] [sentence 2] [sentence 3] [sentence 4] [sentence 5]
"""


def summarize(user_input):
    return inference(user_prompt=SUMMARIZATION_PROMPT.format(text=user_input))
