from crewai import Crew, Process
from agents import blog_researchers, blog_writer
from tasks import research_task, write_task

crew = Crew(
    agents = [blog_researchers, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew=True
)

##start the task execution process with enhanced feedback
result = crew.kickoff(input={'topic': 'AI vs ML vs DL vs Data science'})
print(result)