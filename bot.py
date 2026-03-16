import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# read content
content_folder = "content"
all_content = []

for file in os.listdir(content_folder):
    if file.endswith(".txt"):
        print(f"Loading {file}")
        with open(os.path.join(content_folder, file), "r") as f:
            all_content.append(f.read())

content = "\n\n".join(all_content)

print(f"Processing {len(all_content)} content files...")

mode = "thought_leadership"

prompt = f"""
You are helping a startup generate thoughtful social media posts.
Write posts in a {mode} tone.

Write:
• 3 LinkedIn posts
• 5 Twitter posts

Audience: CFOs and finance leaders.

Style rules:
- No marketing buzzwords
- No phrases like "empower", "innovative", "revolutionary"
- Sound like a thoughtful operator, not a marketer
- Focus on real finance problems

Topics you can reference:
- unreliable forecasts
- manual reconciliation
- fragmented finance stacks
- BI dashboards showing numbers but not catching errors

Content:
{content}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)

posts = response.choices[0].message.content

print("\nGenerated Posts:\n")
print(posts)

with open("generated_posts.txt", "w") as f:
    f.write(posts)