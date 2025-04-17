import re

# return file content
def read_chat(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# extract all prompts sent by the user
def extract_prompts(text):
    pattern = r"You said:(.*?)ChatGPT said:"
    prompts = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
    return [p.strip() for p in prompts]

# count of words in prompt
def calculate_stats(prompts):
    word_counts = [len(p.split()) for p in prompts]
    return {
        "min": min(word_counts),
        "max": max(word_counts),
        "avg": sum(word_counts) / len(word_counts)
    }

# execution
chat_log = read_chat("chat.txt")
prompts = extract_prompts(chat_log)
print("Debug - Extracted prompts:", prompts)
stats = calculate_stats(prompts)

print(f"Prompt Word Analysis:")
print(f"Shortest prompt: {stats['min']} words")
print(f"Longest prompt: {stats['max']} words")
print(f"Average length: {stats['avg']:.1f} words")