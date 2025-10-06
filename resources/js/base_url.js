// Set the base URL based on the current location, listening on navigation changes.
import { BasePattern } from "@patternslib/patternslib/src/core/basepattern";
import registry from "@patternslib/patternslib/src/core/registry";
import events from "@patternslib/patternslib/src/core/events";

class Pattern extends BasePattern {
    static name = "thet-base-url";
    static trigger = ".pat-base-url";

    init() {
        events.add_event_listener(
            window.navigation,
            "navigate",
            "thet-base-url--set",
            this.set_base_url.bind(this)
        );
    }

    set_base_url() {
        document.body.dataset.baseUrl = window.location.href;
    }
}

registry.register(Pattern);
export default Pattern;
export { Pattern };
