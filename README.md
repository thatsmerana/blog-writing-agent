# Blog Writing Agent

This agent functions as an automated blog content generation system designed to research topics and produce publication-ready blog posts. Its primary role is to enhance content creation workflows by systematically analyzing search trends, gathering relevant information from authoritative sources, and generating SEO-optimized blog content; it achieves this by researching keywords using web search tools, creating structured outlines based on top-ranking content strategies, and drafting comprehensive blog posts that incorporate best practices for readability and search engine optimization.

## Overview
This agent researches topics and writes ready-to-publish blogs. Its primary purpose is to serve as an automated content creation layer, analyzing keyword trends and top-ranking content to produce high-quality, SEO-optimized blog posts.

*   Identifies and researches relevant articles and blogs ranking for specified keywords using Google Search.
*   Gathers insights on blog structure, writing style, and SEO strategies from top-ranking content.
*   Creates detailed blog outlines with catchy titles, section headings, and key themes.
*   Drafts complete blog posts optimized for readability and SEO best practices.

This agent enables users to input keywords and receive a fully drafted blog post by extracting insights from top-ranking content, generating structured outlines, and producing publication-ready articles with proper formatting and SEO optimization.

## Agent Details

The key features of the Blog Writing Agent include:

| Feature | Description |
| --- | --- |
| **Interaction Type** | Sequential Workflow |
| **Complexity**  | Medium |
| **Agent Type**  | Multi Agent (Sequential) |
| **Components**  | Tools: Google Search |
| **Vertical**  | Content Marketing, SEO, Digital Publishing |

### Agent Architecture:

This agent uses a sequential multi-agent architecture with three specialized sub-agents:

1. **Blog Topic Research Agent** (LlmAgent): Researches keywords using Google Search to gather insights from high-ranking content
2. **Blog Outlining Agent** (Agent): Creates structured outlines based on research findings
3. **Blog Drafting Agent** (Agent): Writes complete, SEO-optimized blog posts following the outline

```
User Input (Keywords)
         ↓
Blog Topic Research Agent → Google Search Tool
         ↓ (blog_topic_research_result)
Blog Outlining Agent
         ↓ (blog_outline_result)
Blog Drafting Agent
         ↓ (blog_draft_result)
Final Blog Post
```

## Setup and Installation

1.  **Prerequisites**

    *   Python 3.10+
    *   pip (Python package installer)
    *   Google AI API key

2.  **Installation**

    ```bash
    # Clone this repository
    git clone https://github.com/thatsmerana/blog-writing-agent.git
    cd blog-writing-agent
    
    # Create and activate virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    
    # Install dependencies
    pip install -r requirements.txt
    ```

3.  **Configuration**

    *   Create a `.env` file in the project root with your Google AI API key:

    ```bash
    GOOGLE_API_KEY=your-api-key-here
    ```

    Get your API key from: [Google AI Studio](https://aistudio.google.com/app/apikey)

## Running the Agent

**Quick Start**

Simply run the agent with the default query:

```bash
python -m blogger_agent.agent
```

**Programmatic Access**

Below is an example of interacting with the agent using Python:

```python
import asyncio
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from google.genai.types import Part, Content
from blogger_agent.sub_agents import (
    blog_topic_research_agent,
    blog_outlining_agent,
    blog_drafting_agent
)
from google.adk.agents import SequentialAgent

load_dotenv()

async def main():
    # Create the sequential blogger agent
    blogger_agent = SequentialAgent(
        name="blogger_agent",
        sub_agents=[
            blog_topic_research_agent,
            blog_outlining_agent,
            blog_drafting_agent,
        ],
    )
    
    # Initialize runner
    runner = InMemoryRunner(app_name="test_app", agent=blogger_agent)
    
    # Create a session
    session = await runner.session_service.create_session(
        app_name="test_app", 
        user_id="user_id"
    )
    
    # Construct the user query
    user_query = "Write blog post for keywords: AI Agents, LLM, Automation"
    content = Content(role='user', parts=[Part(text=user_query)])
    
    # Run the agent
    async for response in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content
    ):
        if response.content.parts and response.content.parts[0].text:
            print("Agent Response:", response.content.parts[0].text)

if __name__ == "__main__":
    asyncio.run(main())
```

### Example Interaction

Below is an example interaction with the Blog Writing Agent. Note that the exact output may vary based on current search results.

```
User: Write blog post for keywords: NPS, Video Survey, Video Feedback

✅ Blog Topic Research Agent defined.
✅ Blog Outlining Agent defined.
✅ Blog Drafting Agent defined.

[blog_topic_research_agent]: Researching high-ranking content...
- Found strategies from top-ranking blogs on customer loyalty
- Video surveys capture authentic emotions and detailed feedback
- NPS measurement best practices identified
- Common themes: Customer experience, actionable insights, retention

[blog_outlining_agent]: Creating structured outline...
Title: "The Ultimate Guide to Boosting Customer Loyalty with NPS, Video Surveys, and Video Feedback"

Sections:
I. Introduction: The Untapped Potential of Customer Insights
II. Understanding NPS: The Foundation of Customer Loyalty
III. Unleashing the Power of Video Surveys: Beyond the Numbers
IV. Elevating Feedback Loops with Video: Context is King
V. The Power of Integration: NPS + Video = Customer Understanding
VI. Case Studies: Success in Action
VII. Conclusion: Transforming Customer Insights into Growth

[blog_drafting_agent]: Drafting complete blog post...

# The Ultimate Guide to Boosting Customer Loyalty with NPS, Video Surveys, and Video Feedback

Did you know a 5% increase in customer retention can boost profits by 25-95%? 
Are you truly *listening* to your customers, or just *hearing* them?

[Full blog post with SEO optimization, examples, and call-to-action...]
```

## Project Structure

```
blog-writing-agent/
├── blogger_agent/
│   ├── __init__.py
│   ├── agent.py              # Main agent runner with InMemoryRunner
│   ├── prompt.py             # Centralized prompts and instructions
│   └── sub_agents/
│       ├── __init__.py
│       └── blog_writting_agent.py  # Sub-agent definitions
├── .env                      # Environment variables (not in git)
├── .gitignore               # Git ignore configuration
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── sample.md               # Sample output
```

## Customization

The Blog Writing Agent can be customized to better suit your requirements:

1.  **Customize Agent Instructions:** Modify the prompts in `blogger_agent/prompt.py` to adjust:
    - Writing style and tone
    - Target audience focus
    - Industry-specific terminology
    - SEO optimization strategies

2.  **Change the Model:** Update the `model` parameter in `blog_writting_agent.py` from `"gemini-2.0-flash-exp"` to other available models like `"gemini-1.5-pro"` for different performance characteristics.

3.  **Add Additional Research Sources:** Extend the `blog_topic_research_agent` to include:
    - Additional search tools
    - Internal knowledge bases
    - Competitor analysis tools
    - Industry-specific databases

4.  **Implement Review Agent:** Add a fourth agent to the sequential pipeline:
    ```python
    review_agent = LlmAgent(
        name="blog_review_agent",
        model="gemini-2.0-flash-exp",
        description="Reviews and edits blog posts",
        instruction="Check for grammar, tone, and brand consistency..."
    )
    ```

5.  **Configure Output Format:** Modify the `blog_drafting_agent` instructions to generate:
    - Markdown format (current default)
    - HTML with specific styling
    - WordPress-ready format with meta tags
    - Multiple language versions

## Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `GOOGLE_API_KEY` | Your Google AI API Key | Yes | `AIza...` |

## Dependencies

Key dependencies in `requirements.txt`:

- `google-adk` - Google Agent Development Kit for building AI agents
- `python-dotenv` - Environment variable management
- `aiohttp` - Async HTTP client for API calls
- `pytest` - Testing framework
- `dateparser` - Date parsing utilities

## Troubleshooting

**Issue: ImportError when running the agent**
- Solution: Make sure you've activated your virtual environment and installed all dependencies with `pip install -r requirements.txt`

**Issue: API authentication errors**
- Solution: Ensure your `.env` file has a valid `GOOGLE_API_KEY`. Get a new key from [Google AI Studio](https://aistudio.google.com/app/apikey) if needed.

**Issue: "Session not found" error**
- Solution: This is normal if app_name changes. The agent creates a new session automatically.

**Issue: Agent not using Google Search**
- Solution: Ensure the `blog_topic_research_agent` has `tools=[google_search]` configured in `blog_writting_agent.py`

## Disclaimer

This agent sample is provided for illustrative purposes only and is not intended for production use. It serves as a basic example of a blog writing agent and a foundational starting point for individuals or teams to develop their own content generation agents.

This sample has not been rigorously tested for production environments, may contain limitations, and does not include features typically required for production use (e.g., comprehensive error handling, content moderation, plagiarism detection, brand voice consistency checks, or advanced SEO analysis).

Users are solely responsible for any further development, testing, content review, and deployment of agents based on this sample. We strongly recommend:
- Reviewing all generated content before publication
- Implementing content moderation and fact-checking workflows
- Adding plagiarism detection mechanisms
- Ensuring compliance with your organization's content guidelines and legal requirements
- Thoroughly testing the agent before using it for live content creation
