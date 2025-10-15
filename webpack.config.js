process.traceDeprecation = true;
const path = require("path");
const package_json = require("./package.json");
const package_json_mockup = require("@plone/mockup/package.json");
const package_json_patternslib = require("@patternslib/patternslib/package.json");
const webpack_config = require("@plone/mockup/webpack.config");
const mf_config = require("@patternslib/dev/webpack/webpack.mf");

module.exports = () => {
    const config = webpack_config();

    config.entry["collective-ajaxify.bundle.min"] = path.resolve(
        __dirname,
        "resources/index"
    );
    config.output.path = path.resolve(
        __dirname,
        "src/collective/ajaxify/browser/static/scripts/"
    );
    config.plugins.push(
        mf_config({
            name: package_json.name,
            filename: "collective-ajaxify.remote.min.js",
            remote_entry: config.entry["collective-ajaxify.bundle.min"],
            dependencies: {
                ...package_json_patternslib.dependencies,
                ...package_json_mockup.dependencies,
                ...package_json.dependencies,
            },
        })
    );

    return config;
};
