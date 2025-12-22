from tools.llm_inference import inference

CODE_ANALYSIS_PROMPT = """
Analyze this code and provide:

1. EXPLANATION: What does this code do? (2-3 sentences)
2. BUGS/ISSUES: Any problems you detect? (list them or say "None detected")
3. TIME COMPLEXITY: Big O notation
4. SPACE COMPLEXITY: Big O notation

Code:
{code}

Format your response clearly with these sections.
"""

def explain(code: str) -> str:
    """
    Explain code, detect bugs, analyze complexity
    """
    
    print(f"[CODE TOOL] Analyzing {len(code)} characters of code")
    
    prompt = CODE_ANALYSIS_PROMPT.format(code=code)
    explanation = inference(user_prompt=prompt)
    
    return explanation