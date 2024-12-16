# Learning Prompt Engineering with GPT-3.5

Hey! 👋 This is my weekend project where I tried to learn more about prompt engineering by actually building something with it. I've been fascinated by how different ways of asking questions can get such different results from AI models.

## What I Built and Why

I created a simple Python tool that helps me experiment with different prompting techniques. After watching some videos and reading articles about prompt engineering, I wanted to try things out for myself. The main idea was to:

1. Test different ways of writing prompts
2. See which approaches work better
3. Keep track of what I learn

The tool lets me try different prompting techniques (like chain-of-thought and few-shot learning) and see how they compare. I'm using GPT-3.5 because it's pretty good and cheaper than GPT-4.

## What I Learned

Through building this, I learned about:
- How being super clear in prompts makes a huge difference
- That showing examples (few-shot prompting) often gets better results
- Breaking down complex questions step by step works really well
- Working with APIs and handling rate limits (the hard way! 😅)

## How to Try It

If you want to play around with this:

1. Clone this repo
2. Set up Python stuff:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

3. You'll need an OpenAI API key in a .env file:
```
OPENAI_API_KEY=your-key-here
```

4. Run it:
```bash
# Test without using API (free!)
python src/prompt_tester.py --technique basic --mock

# Or with real API if you have credits
python src/prompt_tester.py --technique basic
```

## Project Structure

The code is organized like this
```
prompt-engineering-explorer/
├── src/
│   ├── prompt_tester.py        # Main script
│   ├── examples/               # Different prompt examples
│   │   ├── basic_prompts.json
│   │   └── advanced_prompts.json
│   └── utils/
│       └── response_analyzer.py # Analyzes AI responses
└── results/
    └── comparison_logs/        # Saves results here
```

## Notes and Learnings

Some things I figured out while building this:
- Rate limits are a real pain! Had to add retry logic
- Keeping track of which prompts work better is super helpful
- It's really satisfying when a well-crafted prompt gets exactly what you want
- Mock testing saves money while developing!

## Future Ideas

Things I might add when I have time:
- Try other models (maybe some free ones? huggingface looks cool)
- Make some cool graphs of the results
- Add a simple web interface
- Test more advanced prompting techniques

## Thanks!

Big thanks to:
- OpenAI's documentation
- Various YouTube tutorials on prompt engineering

Feel free to use this code, suggest improvements, or reach out with questions! I'm still learning, so any feedback is welcome.

---