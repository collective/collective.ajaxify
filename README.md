# collective.ajaxify

Ajaxify your Classic UI‌ Plone site!

This is an experiment to ajaxify a whole Plone site.
Use at your own risk!

Some notes:

- This package makes use of the Patternslib pat-inject library.

- This package installs a custom Plone JavaScript bundle (`bundle-plone`) and
  restores the original one when uninstalling the package again. If you use a
  custom `bundle-plone` bundle yourself take care of the changes this package is
  doing in the resource registry.

- The custom `bundle-plone` uses the Mockup `thet-improvements` branch from
  https://github.com/plone/mockup/pull/1509 This bundle mainly adds support the
  the `navigate` event in the toolbar, the navigation marker and the structure
  pattern. It also adds a `pat-base-url` pattern to update `data-base-url` after
  `navigate` events.

This approach was presented at the Ploneconf 2025 talk "Ajaxifying Plone" by
Johannes Raggam:

- https://thet.github.io/talk-ploneconf2025-ajaxify
- https://github.com/thet/talk-ploneconf2025-ajaxify
- https://www.youtube.com/watch?v=Y4Z4A9raEoE

This package depends on features from Plone 6.2 and provides backports for
Plone 6.1.

## Installation

```bash
make zope-start
```
