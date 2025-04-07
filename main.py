import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from api import AssistantFnc

# Trouver et charger le fichier .env
env_path = find_dotenv()
if not env_path:
    raise FileNotFoundError("Le fichier .env n'a pas été trouvé")

print(f"Chemin du fichier .env trouvé : {env_path}")
load_dotenv(env_path, override=True)

# Afficher les variables d'environnement chargées
print("\nVariables d'environnement chargées :")
for var in ['LIVEKIT_URL', 'LIVEKIT_API_KEY', 'LIVEKIT_API_SECRET']:
    value = os.getenv(var)
    print(f"{var}: {'***' if value else 'Non défini'}")

# Vérifier que les variables d'environnement sont bien chargées
required_env_vars = ['LIVEKIT_URL', 'LIVEKIT_API_KEY', 'LIVEKIT_API_SECRET']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Les variables d'environnement suivantes sont manquantes : {', '.join(missing_vars)}")


async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    fnc_ctx = AssistantFnc()

    assitant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        fnc_ctx=fnc_ctx,
    )
    assitant.start(ctx.room)

    await asyncio.sleep(1)
    await assitant.say("Hey, how can I help you today!", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
