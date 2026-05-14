# Translation Studio

Local translation workflow for document parsing, source QA, translation memory, glossary control, machine translation, approval, and audit history.

Supported LLM providers:

- Gemini: `GEMINI_API_KEY`, `GEMINI_MODEL`
- Mistral: `MISTRAL_API_KEY`, `MISTRAL_MODEL`
- OpenAI: `OPENAI_API_KEY`, `OPENAI_MODEL`

Set `TRANSLATION_PROVIDER` to `auto`, `gemini`, `mistral`, `openai`, or `local`.

Approved translations are stored in `data/translation_studio.sqlite3` as translation memory. The `domain` field is used as the memory tag, and the web UI shows the stored memory with its tag.
