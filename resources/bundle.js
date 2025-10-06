import $ from "jquery";
import registry from "@patternslib/patternslib/src/core/registry";
import "./js/toolbar";
import "./js/base_url";
import "./js/details_navigation";
import "./js/parent_click";
import "./js/pat-update";

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

// Reload subscriber for theme changes.
// The meta tag is set in `main_template` and `main_template_ajax`.
// The theme info itself is set in `thet.spa.traverser`.
// NEEDS jQuery.
$(document.body).on(
    "pat-ajax-success",
    (event) => {
        // Get the HTML from the response.
        let response_html = event?.jqxhr?.responseText;
        if (!response_html) {
            console.debug("THEME RELOAD DEBUG: no theme found in response");
            return;
        }
        // Get the theme from the response.
        const url = event?.jqxhr?.url;
        console.debug(url);
        const theme = response_html.match(/\<meta itemprop="theme" content="(.*)"/)?.[1];
        if (!theme) {
            console.debug("THEME RELOAD DEBUG: no theme found in response");
            return;
        }

        console.debug("THEME RELOAD DEBUG: response theme: ", theme);

        // Check against the current theme.
        // NOTE: meta[itemprop='theme'] is set in `main_template` and
        // `main_template_ajax`.
        const current_theme = document.querySelector("meta[itemprop='theme']").content;
        console.debug("THEME RELOAD DEBUG: current theme: ", current_theme);

        // If different, reload the page with the URL from the original AJAX
        // request.
        if (theme !== current_theme && url) {
            // Give me a random string.
            const rnd = Math.random(1,9999).toString(36).substring(2);
            const reload_url = `${url}?${rnd}`;
            window.location.href = reload_url;
        }
    }
);


registry.init();

// Re-scan the DOM for our modified inject pattern.
// Scanning might have been done at a previous `registry.init` call from another
// MF bundle, so we need to re-scan for our modified trigger.
registry.scan(document.body, ["inject"]);
