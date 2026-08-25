# ALTAS

ALTAS is a general-purpose AI computer-use agent for Windows. It is designed around dynamic application discovery, natural-language task planning, generic computer control, observation, verification, memory/context, and one shared speech-to-text plus text-to-speech pipeline.

## Architecture

`Text or Voice -> Task Engine -> Plan -> Generic Tools -> Observe/Act/Verify -> Response`

ALTAS does not use a fixed list of supported applications or user commands.

## Safety

The agent asks for confirmation before destructive filesystem operations and sensitive external side effects. It reports failures instead of pretending an action succeeded.

## Quick start

1. Install Python 3.11+
2. `python -m venv .venv`
3. Activate the environment
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure an OpenAI-compatible API key
6. `python main.py`

See `docs/ARCHITECTURE.md` for the design.
