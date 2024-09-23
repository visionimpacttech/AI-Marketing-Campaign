from transformers import pipeline

def generate_content(prompt):
    generator = pipeline('text-generation', model='gpt-3.5')
    return generator(prompt, max_length=150)[0]['generated_text']

# Generate personalized content
prompt = "Generate a personalized offer for an electronics customer."
print(generate_content(prompt))
