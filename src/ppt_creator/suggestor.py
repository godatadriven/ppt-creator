class Suggestor:
    def __init__(self, model="gpt-4"):
        self.model = model

    def suggest_outline(self, topic):
        # In a real scenario, this would call an LLM (OpenAI/Anthropic)
        # For now, we return a basic template
        return {
            "title": f"The Impact of {topic}",
            "slides": [
                {"title": "Introduction", "content": [f"What is {topic}?", "Historical context", "Current importance"]},
                {"title": "Key Challenges", "content": ["Major obstacles", "Complexity and scale", "Resource requirements"]},
                {"title": "Solutions & Future", "content": ["Proposed approaches", "Innovation trends", "Summary and outlook"]}
            ]
        }
