# ALTAS Architecture

## Core principle

ALTAS is capability-based. Users express goals in natural language; the agent selects generic capabilities dynamically. Application names and example workflows are not a fixed command vocabulary.

## Execution loop

1. Receive text or STT transcript.
2. Preserve conversation/task context.
3. Interpret goal in a language-independent representation.
4. Inspect available capabilities and current computer state.
5. Plan small observable actions.
6. Execute one action.
7. Observe the resulting state.
8. Verify success.
9. Replan or report failure when verification fails.
10. Produce text and optional TTS from the same final response.

## Dynamic applications

Application discovery indexes executables found from Windows installation roots. Production expansion should add Start Menu shortcuts, uninstall registry entries, AppX packages, PATH and user-configured roots. The planner should use semantic matching rather than a hard-coded supported-app list.

## Interaction preference

Accessibility/UI automation and semantic element lookup should be preferred. OCR and vision provide fallback understanding. Raw screen coordinates are the last fallback and should be followed by verification.

## Safety boundaries

Destructive file operations and consequential external actions should require confirmation unless the user explicitly authorized them in the current task. STOP uses cooperative cancellation and should be checked between long-running actions.

## Voice

There is one STT provider and one TTS provider. Both voice and typed text enter the same TaskEngine after transcription; there is no separate limited voice-command path.
