from google.adk.agents import SequentialAgent
from google.adk import tools
from .sub_agents import blog_outlining_agent, blog_drafting_agent, blog_topic_research_agent
from google.adk.runners import InMemoryRunner
from google.genai import types
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Define the main blogger agent that sequences the sub-agents
retry_config = types.HttpRetryOptions(
    attempts=3,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

blogger_agent = SequentialAgent(
    name="blogger_agent",
    sub_agents=[
        blog_topic_research_agent,
        blog_outlining_agent,
        blog_drafting_agent,
    ],
)


async def main():

    # Construct the user query as a Content object
    user_query = "Write blog post for main keyword: Video Survey. Include other keywords related to the main keyword topic: NPS"
    content = types.Content(role='user', parts=[types.Part(text=user_query)])

    # Initialize InMemoryRunner with the blogger agent
    runner = InMemoryRunner(app_name="test_app", agent=blogger_agent)

    # Create a session for the user to persist context
    session = await runner.session_service.create_session(app_name="test_app", user_id="user_id")

    results = []
    async for response in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content
    ):
        print(response)
        results.append(response)

        if response.content.parts and response.content.parts[0].text:
            print("Agent Response:", response.content.parts[0].text)

    return results

if __name__ == "__main__":
    asyncio.run(main())
