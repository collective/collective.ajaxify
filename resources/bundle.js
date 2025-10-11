import $ from "jquery";
import registry from "@patternslib/patternslib/src/core/registry";
import "./js/base_url";
//import "./js/pat-update";

// Add a new trigger for the inject pattern.
// NOTE: This is an important trigger, triggering all child anchors from the current domain!
registry.patterns.inject.trigger =
    `a[href^="${window.location.origin}"].pat-inject`
    + `,.pat-inject a[href^="${window.location.origin}"]`
    + `:not([href$=pdf])`
    + `:not([href$=mp3])`
    + `:not([href$=wav])`
    + `:not([href$=jpg])`
    + `:not([href$=webp])`
    + `:not([href$=png])`
    + `:not(.dropdown-toggle)`
    + `:not([id^="autotoc"])`
    + `:not(form)`
; // exclude forms.


registry.init();

// Re-scan the DOM for our modified inject pattern.
// Scanning might have been done at a previous `registry.init` call from another
// MF bundle, so we need to re-scan for our modified trigger.
registry.scan(document.body, ["inject"]);
