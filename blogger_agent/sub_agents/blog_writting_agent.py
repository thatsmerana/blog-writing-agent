from google.adk.agents import LlmAgent, Agent
from google.adk.tools.google_search_tool import google_search
from ..prompt import (
    BLOG_TOPIC_RESEARCH_DESCRIPTION,
    BLOG_TOPIC_RESEARCH_INSTRUCTION,
    BLOG_OUTLINING_DESCRIPTION,
    BLOG_OUTLINING_INSTRUCTION,
    BLOG_DRAFTING_DESCRIPTION,
    BLOG_DRAFTING_INSTRUCTION
)

# Define sub-agents for the blogger agent
blog_topic_research_agent = LlmAgent(
    name="blog_topic_research_agent",
    model="gemini-2.0-flash-exp",
    description=BLOG_TOPIC_RESEARCH_DESCRIPTION,
    instruction=BLOG_TOPIC_RESEARCH_INSTRUCTION,
    tools=[google_search],
    output_key="blog_topic_research_result"
)

print("✅ Blog Topic Research Agent defined.")

# Agent for outlining blog posts
blog_outlining_agent = Agent(
    name="blog_outlining_agent",
    model="gemini-2.0-flash-exp",
    description=BLOG_OUTLINING_DESCRIPTION,
    instruction=BLOG_OUTLINING_INSTRUCTION,
    output_key="blog_outline_result"
)

print("✅ Blog Outlining Agent defined.")


# Agent for drafting blog posts
blog_drafting_agent = Agent(
    name="blog_drafting_agent",
    model="gemini-2.0-flash-exp",
    description=BLOG_DRAFTING_DESCRIPTION,
    instruction=BLOG_DRAFTING_INSTRUCTION,
    sub_agents=[],
    output_key="blog_draft_result"
)
print("✅ Blog Drafting Agent defined.")

__all__ = [
    "blog_topic_research_agent",
    "blog_outlining_agent",
    "blog_drafting_agent",
]