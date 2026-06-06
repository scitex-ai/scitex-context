# Changelog

All notable changes to `scitex-context` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0]

- feat: port `embed`, `less`, `paste` from `scitex_gen._ipython` (Phase B
  of the scitex-gen full retirement wave). All three are IPython-tied
  REPL helpers and live naturally with the existing
  `is_ipython` / `is_notebook` / `get_notebook_path` family already
  shipping here.
- New optional extra `scitex-context[ipython]` pulls in IPython + pyperclip
  (deps are imported lazily inside the function bodies, so the package as
  a whole works without them).
- `scitex_gen.is_ipython` / `is_script` are NOT re-imported — they already
  ship here.

## [0.1.1]

- Initial CHANGELOG entry — see git log for prior history.
