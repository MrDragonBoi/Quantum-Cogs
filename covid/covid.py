import diseaseapi
from redbot.core import commands

client = diseaseapi.Client().covid19

class COVID(commands.Cog):
    """Check the latest COVID-19 statistics in a specified country, state or around the world."""

    ### Cases

    @commands.command()
    async def countrycases(self, ctx, country):
        data = await client.country(country)
        stats = f"COVID-19 Cases\n **Location:** {country}\n**Total Cases:** {data.cases}\n**Today's Cases:** {data.today.cases}\n**Total Deaths:** {data.deaths}\n**Today's Deaths:** {data.today.deaths}"
        await ctx.send(stats)
    
    @commands.command()
    async def statecases(self, ctx, state):
        data = await client.state(state)
        stats = f"COVID-19 Cases\n**Location:** {state}\n**Total Cases:** {data.cases}\n**Today's Cases:** {data.today.cases}\n**Total Deaths:** {data.deaths}\n**Today's Deaths:** {data.today.deaths}"
        await ctx.send(stats)

    @commands.command()
    async def globalcases(self, ctx):
        data = await client.all()
        stats = f"COVID-19 Cases\n**Location:** Global\n**Total Cases:** {data.cases}\n**Today's Cases:** {data.today.cases}\n**Total Deaths:** {data.deaths}\n**Today's Deaths:** {data.today.deaths}" 
        await ctx.send(stats)
