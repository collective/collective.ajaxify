import registry from "@patternslib/patternslib/src/core/registry";
import "./js/base_url";

// Add a new trigger for the inject pattern.
// NOTE: This is an important trigger, triggering all child anchors from the current domain!
registry.patterns.inject.trigger =
    `a[href^="${window.location.origin}"].pat-inject`
    + `,.pat-inject a[href^="${window.location.origin}"]`
    // Don't inject files.
    + `:not([href$=pdf])`
    + `:not([href$=mp3])`
    + `:not([href$=wav])`
    + `:not([href$=jpg])`
    + `:not([href$=webp])`
    + `:not([href$=png])`
    // Don't inject dropdown "buttons"
    + `:not(.dropdown-toggle)`
    // Don't inject on the autotoc tab headings.
    + `:not([id^="autotoc"])`
    // a.pat-inject is handled by the first selector.
    + `:not(.pat-inject)`
    // Stop global injection when explicitly asked. You cna still expliciltly
    // set pat-inject on this elements.
    + `:not(.stop-pattern)`
;


registry.init();

// Re-scan the DOM for our modified inject pattern.
// Scanning might have been done at a previous `registry.init` call from another
// MF bundle, so we need to re-scan for our modified trigger.
// TODO: Add a hook to modify the trigger before the first scan?
//registry.scan(document.body, ["inject"]);
