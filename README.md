# AI Content Workflow Bot

A lightweight Python prototype that converts internal product content (blog posts, notes, updates) into social media drafts using AI.

## Purpose
This project explores how small AI agents can automate parts of a go-to-market (GTM) content workflow. Instead of manually writing social posts from internal materials, the script generates structured drafts that marketing or growth teams can quickly edit and publish.

## How It Works
1. Internal content is stored in the `/content` folder.
2. The script reads those files.
3. An AI model generates LinkedIn and Twitter/X post drafts.
4. The results are saved to `generated_posts.txt`.

## Project Structure
ai-content-workflow-bot/
- bot.py (main generation script)
- requirements.txt (dependencies)
- .env.example (API key template)
- content/ (input text files)

## Run Locally
1. Install dependencies  
   pip install -r requirements.txt

2. Add your API key to `.env`  
   OPENAI_API_KEY=your_api_key_here

3. Run the bot  
   python bot.py

Generated posts will appear in `generated_posts.txt`.

## Example Use Case
Growth or marketing teams can drop product updates, demo notes, or blog drafts into the `/content` folder. The script converts them into social media drafts that can be reviewed and posted.

## Future Improvements
Possible extensions include scheduling posts automatically, integrating with Notion/Slack, brand voice tuning, and multi-platform formatting.