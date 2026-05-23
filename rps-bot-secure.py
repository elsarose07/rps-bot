import discord
from discord.ext import commands
from discord import app_commands
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Game choices with emojis
CHOICES = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Define the outcome logic
def get_winner(user_choice, bot_choice):
    """Determine the winner. Returns 'win', 'lose', or 'draw'"""
    if user_choice == bot_choice:
        return "draw"
    
    winning_combos = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combos[user_choice] == bot_choice:
        return "win"
    else:
        return "lose"


class GameStartButton(discord.ui.View):
    """View for the initial 'Start Game' button"""
    def __init__(self):
        super().__init__()
        self.timeout = 60  # Button times out after 60 seconds
    
    @discord.ui.button(label="Start Game", style=discord.ButtonStyle.blurple, emoji="🎮")
    async def start_game(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Start the game and show choice buttons"""
        # Create the choice buttons view
        view = GameChoiceButtons()
        
        embed = discord.Embed(
            title="🎮 Rock Paper Scissors",
            description="Make your choice!",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Your Turn", value="Click one of the buttons below", inline=False)
        
        await interaction.response.edit_message(embed=embed, view=view)


class GameChoiceButtons(discord.ui.View):
    """View for the game choice buttons"""
    def __init__(self):
        super().__init__()
        self.timeout = 60
    
    @discord.ui.button(label="Rock", style=discord.ButtonStyle.gray, emoji="🪨")
    async def rock_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_choice(interaction, "rock")
    
    @discord.ui.button(label="Paper", style=discord.ButtonStyle.gray, emoji="📄")
    async def paper_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_choice(interaction, "paper")
    
    @discord.ui.button(label="Scissors", style=discord.ButtonStyle.gray, emoji="✂️")
    async def scissors_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_choice(interaction, "scissors")
    
    async def handle_choice(self, interaction: discord.Interaction, user_choice: str):
        """Handle the user's choice and play the game"""
        # Bot makes a random choice
        bot_choice = random.choice(list(CHOICES.keys()))
        
        # Determine the outcome
        result = get_winner(user_choice, bot_choice)
        
        # Create result embed with styling based on outcome
        if result == "win":
            color = discord.Color.green()
            title = "🎉 You Win!"
            description = "Nice move! You beat the bot!"
        elif result == "lose":
            color = discord.Color.red()
            title = "😔 You Lose!"
            description = "The bot outplayed you this time!"
        else:  # draw
            color = discord.Color.gold()
            title = "🤝 It's a Draw!"
            description = "Great minds think alike!"
        
        # Create the result embed
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )
        
        # Add choice information
        embed.add_field(
            name="Your Choice",
            value=f"{CHOICES[user_choice]} {user_choice.capitalize()}",
            inline=True
        )
        embed.add_field(
            name="Bot's Choice",
            value=f"{CHOICES[bot_choice]} {bot_choice.capitalize()}",
            inline=True
        )
        
        # Add a play again button
        view = PlayAgainView()
        
        embed.set_footer(text=f"Played by {interaction.user.name}")
        
        await interaction.response.edit_message(embed=embed, view=view)


class PlayAgainView(discord.ui.View):
    """View for the 'Play Again' button"""
    def __init__(self):
        super().__init__()
        self.timeout = 60
    
    @discord.ui.button(label="Play Again", style=discord.ButtonStyle.blurple, emoji="🔄")
    async def play_again(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Restart the game"""
        view = GameChoiceButtons()
        
        embed = discord.Embed(
            title="🎮 Rock Paper Scissors",
            description="Make your choice!",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Your Turn", value="Click one of the buttons below", inline=False)
        
        await interaction.response.edit_message(embed=embed, view=view)


@bot.event
async def on_ready():
    """Bot is ready and synced"""
    print(f"✅ Bot is online as {bot.user}")
    await bot.tree.sync()
    print("✅ Slash commands synced!")


@bot.tree.command(name="rps", description="Play Rock Paper Scissors against the bot!")
async def rock_paper_scissors(interaction: discord.Interaction):
    """Slash command to start the RPS game"""
    # Create the initial embed with start button
    embed = discord.Embed(
        title="🎮 Rock Paper Scissors",
        description="Ready to play?",
        color=discord.Color.blurple()
    )
    embed.add_field(
        name="How to Play",
        value="Click the **Start Game** button to begin!",
        inline=False
    )
    embed.add_field(
        name="Rules",
        value="Rock beats Scissors\nScissors beats Paper\nPaper beats Rock",
        inline=False
    )
    
    view = GameStartButton()
    
    await interaction.response.send_message(embed=embed, view=view, ephemeral=False)


# Get token from environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

# Validate token exists
if not TOKEN:
    print("❌ ERROR: DISCORD_TOKEN not found in environment variables!")
    print("Please create a .env file with your Discord bot token.")
    print("See .env.example for the correct format.")
    exit(1)

# Run the bot
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"❌ Error starting bot: {e}")