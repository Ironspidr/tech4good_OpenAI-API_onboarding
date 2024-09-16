from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def filter_types():
    print("Extracting data...")

system_prompt = "Provide a valid JSON object. Use the following step-by-step instructions to respond to user inputs. Types of Creative/Recreational/Culinary Groups, Community/Social Supporters, Natural Environmental Stewards & urban planners, academic & professional networks. Step 1 - You will be provided with a quote about gratitude for specific groups in the city of Santa Cruz, California. Step 2 - Identify the type of the main group or groups of people. Step 3 - Identify the specific jobs of people addressed based on the quote. Step 4 - Tag each person with the summary from the quote. Here is an example- quote: To live in Santa Cruz is a blessing in and of itself, but the college campus is like the crown jewel of the city. Every time I drive up to campus for work, I almost have to pinch myself because it is hard to believe this is the place that I'm employed. I'm filled with gratitude for the wide open, rolling fields and beautiful redwoods surrounding the quaint buildings. It's the breathtaking view of the ocean and the gorgeous landscape that I'm grateful for mostly. Beyond that, there is plenty to be grateful about among my friendly and super helpful coworkers. Summary: We thank Environmental Maintenance Staff for maintaining the beautiful open fields and redwoods surrounding the campus buildings, ensuring a serene and natural ambiance. Landscape Architects and Designers for creating and preserving the gorgeous landscape of UCSC, making the campus an aesthetically pleasing environment. Park Rangers and Conservationists for preserving the natural beauty and environment around the campus, enhancing the overall appeal and sustainability of the area."

generate_quote = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "I think having a community that appreciates my interests and my intellectual outputs are really important for my sense of self worth, especially seeing other people also wrangling with difficult ideas along with me. This also extends to the community that opened up to me during academic conferences."
        }
    ],
    tools=filter_types()
)

data = generate_quote.choices[0].message.content

print(data)