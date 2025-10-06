export default {
    extends: ["stylelint-config-standard"],
    rules: {
        "import-notation": null,
        "at-rule-empty-line-before": null,
        "selector-id-pattern": null,
        "selector-class-pattern": null,
        "color-hex-length": null,
        "function-no-unknown": [true, {
            "ignoreFunctions": ["theme", ]
        }],
    }
};
