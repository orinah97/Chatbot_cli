from nltk.chat.util import Chat , reflections
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)
goodbye_responses = [
    "Chatbot: Goodbye! Have a nice day 😊",
    "Chatbot: See you later! Take care 🌟",
    "Chatbot: Farewell! Until next time 👋",
    "Chatbot: Bye for now! Stay safe 🛡️",
    "Chatbot: Catch you later! 😄✌️",
    "Chatbot: It was great chatting! Goodbye 🗨️💬",
    "Chatbot: Signing off. Have a good one 🖖💻",
    "Chatbot: Peace out! ✌️😎",
    "Chatbot: Thanks for stopping by. Bye! 🙏🚪",
    "Chatbot: Adios, gamer! Until next round 🎮🔥"
]



pairs = [
    (r"(.*)elden\s?ring(.*)", [
        "Masterpiece from FromSoftware",
        "Praise the Erdtree, Tarnished!",
        "Open-world suffering never looked so good",
        "Malenia is still undefeated for many"
    ]),
    (r"(.*)call\s?of\s?duty(.*)|cod", [
        "FPS mayhem and killstreaks",
        "Time to drop in and frag out",
        "Quick scopes and rage quits",
        "Warzone got me checking corners IRL"
    ]),
    (r"(.*)fortnite(.*)", [
        "Victory Royale or bust",
        "Where builds win fights",
        "Dance before the storm hits",
        "The OG map hits different"
    ]),
    (r"(.*)minecraft(.*)", [
        "Block by block, dream big",
        "From punching trees to redstone logic",
        "Creepers ruin everything",
        "Pixelated peace and chaos"
    ]),
    (r"(.*)league\s?of\s?legends|lol", [
        "Tilted since champ select",
        "League is a love-hate relationship",
        "Baron steals and backdoor plays",
        "Where flaming is part of the game"
    ]),
    (r"(.*)dota\s?2(.*)", [
        "Hardcore MOBA energy",
        "TI dreams and MMR nightmares",
        "Buyback into the chaos",
        "IceFrog giveth, IceFrog taketh"
    ]),
    (r"(.*)valorant(.*)", [
        "Spike planted, heart racing",
        "Agent abilities > raw aim sometimes",
        "Clutch or kick?",
        "Jett mains be flying everywhere"
    ]),
    (r"(.*)overwatch(.*)", [
        "Push the payload or perish",
        "Tanks and tilts",
        "ULT COMBOOOO!",
        "Mercy mains are the real MVPs"
    ]),
    (r"(.*)apex\s?legends(.*)", [
        "Slide, shoot, and flex your heirloom",
        "Squad up or get thirsted",
        "Every jump feels epic",
        "Octane mains never stop moving"
    ]),
    (r"(.*)counter\s?strike|cs\s?go|cs2", [
        "One tap headshots since forever",
        "De_dust2 forever in our hearts",
        "Eco round stress",
        "CS: Classic clutch kingmaker"
    ]),
    (r"(.*)skyrim(.*)", [
        "I took an arrow to the knee",
        "Mods make it eternal",
        "Shouting dragons off cliffs never gets old",
        "Open world fantasy done right"
    ]),
    (r"(.*)witcher\s?3(.*)", [
        "Geralt's growl is legendary",
        "Monster hunting and moral choices",
        "Toss a coin to your Witcher",
        "Gwent is better than it should be"
    ]),
    (r"(.*)gta\s?v|grand\s?theft\s?auto(.*)", [
        "Los Santos chaos is unmatched",
        "Online heists hit different",
        "Drive, shoot, repeat",
        "NPCs don’t stand a chance"
    ]),
    (r"(.*)red\s?dead(.*)", [
        "Arthur Morgan forever",
        "Yeehaw and heartbreak",
        "Ride into the sunset, partner",
        "Cinematic storytelling with cowboy grit"
    ]),
    (r"(.*)animal\s?crossing(.*)", [
        "Debt simulator with cute animals",
        "Tom Nook always wins",
        "Island life is chill vibes only",
        "Perfect for rainy days and resets"
    ]),
    (r"(.*)pokemon(.*)", [
        "Gotta catch ‘em all since '96",
        "Eevee-lutions for every mood",
        "Shiny hunt is real pain",
        "Gym badges and childhood dreams"
    ]),
    (r"(.*)fifa(.*)", [
        "Weekend League rage is real",
        "Ultimate Team owns your wallet",
        "That one goal in the 90th minute",
        "Scripting? Always."
    ]),
    (r"(.*)dark\s?souls(.*)", [
        "Git Gud: the lifestyle",
        "Prepare to die… repeatedly",
        "Every bonfire is a blessing",
        "Praise the sun, forever"
    ]),
    (r"(.*)roblox(.*)", [
        "Endless games within one",
        "Where kids and devs unite",
        "Oof became iconic",
        "Imagination goes brrr"
    ]),
    (r"(.*)among\s?us(.*)", [
        "Who's sus?",
        "Emergency meeting time!",
        "Red is always sus",
        "Deceit and deduction ftw"
    ]),
    (r"(.*)halo(.*)", [
        "Finish the fight, Spartan",
        "Energy swords are love",
        "Master Chief forever iconic",
        "Multiplayer was LAN party gold"
    ]),
    (r"(.*)mass\s?effect(.*)", [
        "Paragon or Renegade?",
        "Space opera with choices",
        "Shepard saves the galaxy",
        "Romance options on point"
    ]),
    (r"(.*)fall\s?guys(.*)", [
        "Battle royale meets wipeout",
        "Flop your way to the crown",
        "Screaming in pastel chaos",
        "Slime climb ruins friendships"
    ]),
    (r"(.*)cyberpunk(.*)", [
        "Night City never sleeps",
        "Keanu made it iconic",
        "Bugs, but beautiful",
        "Street cred means everything"
    ]),
    (r"(.*)hades(.*)", [
        "Greek gods and perfect roguelike flow",
        "Zagreus keeps dying stylishly",
        "Every run tells a new story",
        "Best voice acting vibes"
    ]),
    (r"(.*)hollow\s?knight(.*)", [
        "Bug soulsborne with beauty",
        "Atmosphere: 10/10",
        "Silksong when?",
        "Tough but fair platforming"
    ]),
    (r"(.*)terraria(.*)", [
        "2D Minecraft on steroids",
        "Boss fights get wild",
        "Dig, build, conquer",
        "Pixel art perfection"
    ]),
    (r"(.*)doom(.*)", [
        "Rip and tear till it’s done",
        "Heavy metal shooter",
        "Demons fear the Doom Slayer",
        "Pure adrenaline gaming"
    ]),
    (r"(.*)residen(t|ce)?\s?evil(.*)", [
        "Zombies and bioweapons galore",
        "Jill sandwich moment",
        "Lady D stole the internet",
        "Survival horror royalty"
    ]),
    (r"(.*)god\s?of\s?war(.*)", [
        "BOY.",
        "Norse mythology and fatherhood",
        "Axe-throwing feels so good",
        "Kratos found his soul"
    ]),
    (r"(.*)stardew\s?valley(.*)", [
        "Farming, fishing, and falling in love",
        "Pixel perfect peace",
        "JojaMart can go away",
        "Best indie cozy game"
    ]),
    (r"(.*)cuphead(.*)", [
        "Boss rush from hell",
        "Retro animation, modern pain",
        "Parry or perish",
        "Mugman deserves more love"
    ]),
    (r"(.*)undertale(.*)", [
        "Kill or be kind",
        "Sans will judge you",
        "Indie legend status",
        "Soundtrack slaps hard"
    ]),
    (r"(.*)metro(.*)", [
        "Post-apocalyptic survival",
        "Watch out for mutants",
        "Russian sci-fi immersion",
        "Dark, gritty, atmospheric"
    ]),
    (r"(.*)bioshock(.*)", [
        "Would you kindly remember Rapture?",
        "Twists and underwater terror",
        "Infinite made us rethink everything",
        "A man chooses, a slave obeys"
    ]),
    (r"(.*)battlefield(.*)", [
        "Vehicles and chaos",
        "Conquest mode forever",
        "Destruction is the game",
        "Squad up or die fast"
    ]),
    (r"(.*)splatoon(.*)", [
        "Paintball warfare but cute",
        "Ink or be inked",
        "Squid kid supremacy",
        "Fresh gear, fresh tactics"
    ]),
    (r"(.*)fallout(.*)", [
        "War never changes",
        "Post-nuke survival with style",
        "VATS saves lives",
        "Dogmeat is the real MVP"
    ]),
    (r"(.*)tomb\s?raider(.*)", [
        "Lara Croft, the OG",
        "Treasure and traps",
        "Adventure meets archaeology",
        "Reboot made her realer"
    ]),
    (r"(.*)elden\s?beast(.*)", [
        "Final pain in Elden Ring",
        "One last dance",
        "Golden light, massive fight",
        "Epic finale moment"
    ]),
]


chatbot = Chat(pairs,reflections)

print(f"{Fore.YELLOW} Hi , I'ma your chatbot. Type 'quit' to end the conversation .")

while True :
    user_input =input(f"{Fore.BLUE} Me : ").lower()
    if user_input == "quit":
        print(f"{Fore.RED} {random.choice(goodbye_responses)}")
        break
    else:
        response = chatbot.respond(user_input)
        print(f"{Fore.GREEN} CHatbot :  {response}")
