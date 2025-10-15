import registry from "@patternslib/patternslib/src/core/registry";
import inject from "@patternslib/patternslib/src/pat/inject/inject";


// Add a new trigger for the inject pattern.
inject.trigger =
    // All anchors with the pat-inject class.
    `a.pat-inject`
    // All anchors within `.pat-inject` from the same domain.
    + `,.pat-inject a[href^="${window.location.origin}"]`
    // Except files.
    + `:not([href*="@@download"])`
    + `:not([href$=zip])`
    + `:not([href$=pdf])`
    + `:not([href$=mp3])`
    + `:not([href$=wav])`
    + `:not([href$=jpg])`
    + `:not([href$=webp])`
    + `:not([href$=png])`
    + `:not([href$=txt])`
    // Don't inject dropdown "buttons"
    + `:not(.dropdown-toggle)`
    // Don't inject on the autotoc tab headings.
    + `:not([id^="autotoc"])`
    // Don't handle explicitly set pat-inject elements.
    + `:not(.pat-inject)`
    // Stop global injection when explicitly asked. You can still explicitly
    // set pat-inject on these elements.
    + `:not(.stop-pattern)`
;


registry.init();


// UPDATE 2025-10-15: When this bundle is registered as MF master, inject is registered
// while DOM scanning hasn't been done yet. No need to re-scan.

// Re-scan the DOM for our modified inject pattern.
// Scanning might have been done at a previous `registry.init` call from another
// MF bundle, so we need to re-scan for our modified trigger.
// TODO: Add a hook to modify the trigger before the first scan?
//registry.scan(document.body, ["inject"]);
