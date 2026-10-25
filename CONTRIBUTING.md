# Contributing

Keep the two skill directory names and `$` invocation names stable. Collection documentation lives at the root and in `docs/`; the supplied skill snapshots live under `skills/`.

1. Update the four language versions together: English, Simplified Chinese, Traditional Chinese, and Japanese.
2. Keep canonical parameter keys and mode values unchanged inside runnable examples. Translate explanations freely; do not imply new aliases exist.
3. Do not claim measured image quality, identity fidelity, exact text rendering, or exact output dimensions without evidence from the actual image tool.
4. Preserve component licenses and attribution. Do not add a blanket license covering unlicensed components.
5. Run `python scripts/validate.py` before opening a PR.

For an intentional skill update, review upstream rights and behavior first. Update `SOURCE_MANIFEST.json` only after checking the changed source files; do not regenerate hashes merely to silence an unexpected integrity failure. Record version and behavioral changes in all four usage guides.

The validator checks packaging and documentation structure. It does not generate images or prove model output quality. Real portrait references are not stored in this repository.
