# Requirements

Source: https://academy.bricksbuilder.io/builder/setup/requirements/

*PHP, memory, upload size, browser, and troubleshooting for Bricks.*

This article covers the recommended server limits and browser compatibility for Bricks, plus how to fix common limits. The [Installation and setup](https://academy.bricksbuilder.io/getting-started/installation-setup/) guide links here when you need the full checklist or troubleshooting.

To provide you with a cutting-edge site builder for WordPress Bricks uses the most modern technology stack (VueJS 3, etc.) while keeping sufficient backward compatibility.

Below are the baseline server limits and compatibility recommendations for running Bricks smoothly:

- PHP 5.4+
- WordPress memory limit: min. 64 MB (recommended: 512 MB)
- Max file upload size: min. 64 MB
- Modern browser: Use a current version of Chrome, Firefox, Safari, or Microsoft Edge when editing your website with Bricks. Older browsers (e.g. Internet Explorer) lack support for some of the more advanced builder features.

> **Note**
>
> *Bricks is a self-hosted solution that you download & install on your own WordPress website!*

## How To Increase WP Memory Limit {#wp-memory-limit}

You can define **WP_MEMORY_LIMIT** by adding the following code to your **wp-config.php** file, above the line that says "That's all, stop editing!":

```php
define( 'WP_MEMORY_LIMIT', '512M' );
/* That's all, stop editing! Happy publishing. */
```

Some web hosts set the PHP memory limit to as low as 8 MB. In that case, you might consider upgrading to a more powerful hosting plan. If your host does not allow you to config this setting by yourself, please get in touch with them.

## How To Increase Max File Upload Size {#max-file-upload-size}

If you encounter problems uploading larger files to your site (or when downloading high-resolution images from Bricks' Unsplash integration) there are a few ways to increase the maximum upload file size.

A maximum upload size should be 64 MB or more. Log into your hosting account and change the following two **PHP server settings** to:

- post_max_size: 64M
- upload_max_filesize: 64M

If you have access to your **php.ini** file, located in the root directory of your WordPress installation, open it, and modify the following settings:

```php
upload_max_filesize = 64M
post_max_size = 64M
```

You can also add the following code to your **.htaccess** file, but make sure to backup your existing .htaccess file beforehand:

```php
php_value upload_max_filesize 64M
php_value post_max_size 64M
```

If all above fails, you can try adding the following code to your wp-config.php:

```php
@ini_set( 'upload_max_size' , '64M' );
@ini_set( 'post_max_size', '64M');
```

To confirm that your maximum upload file size has been updated successfully, go to **Media > Add New**. On the bottom of this page, you should see your maximum upload file size.

## How To Increase Maximum Execution Time {#max-execution-time}

When you start seeing a message like "Maximum execution time of 30 seconds exceeded" you have to increase the execution time of your website by using one of the following three solutions:

**#1: Add the following code to your wp-config.php file (above the "That's all, stop editing!" line):**

```php
set_time_limit(180);
/* That's all, stop editing! Happy publishing. */
```

**#2: Backup your .htaccess file and add the following code to it:**

```php
php_value max_execution_time 180
```

**#3: Add the following code to your php.ini file:**

```php
max_execution_time = 180
```

---

# Known issues

Source: https://academy.bricksbuilder.io/builder/setup/known-issues/

*Review common Bricks setup and runtime issues, along with the environment checks and fixes that usually resolve them.*

## When I open the builder I don't see the elements on the canvas {#empty-canvas}

If you open the builder and you don't see the elements in the canvas but they are shown in the structure panel, and if you are using Cloudflare, then this is a known problem caused by a conflict between the [Cloudflare Rocket Loader](https://support.cloudflare.com/hc/en-us/articles/200168056-Understanding-Rocket-Loader)™ / other performance optimization feature and the Bricks builder JavaScript.

Starting with Bricks 2.0, a new **experimental setting** has been introduced to improve compatibility with Rocket Loader™. Enable it in **Bricks > Settings > Builder** and reload the builder page, your elements should now appear correctly on the canvas.

![](https://academy.bricksbuilder.io/assets/cloudflare-rocket-loader.png)

### Workarounds

### Method 1) Configuration Rules

Create a configuration rule for builder mode.

1. Log into the Cloudflare [dashboard](https://dash.cloudflare.com/login).
2. Select your account and website.
3. Go to Rules > Configuration Rules.
4. Create a new Rule, give it a name, and choose Custom filter expression
  - Field: URI Query String
  - Operator: contains
  - Value: bricks=run
5. Configure "Then the settings are…":
  - Add Rocket Loader and leave the checkbox empty.
6. Leave the other settings empty.
7. Save the rule by clicking "Deploy".
8. Wait for a few minutes and do a browser hard refresh in Bricks builder. (Clear browser caches)

![](https://academy.bricksbuilder.io/assets/bricks-known-issues-rocket-loader-rules.png)

![](https://academy.bricksbuilder.io/assets/bricks-known-issues-rocket-loader-expression.png)

![](https://academy.bricksbuilder.io/assets/bricks-known-issues-rocket-loader-then-settings.png)

![](https://academy.bricksbuilder.io/assets/bricks-known-issues-rocket-loader-deploy.png)

### Method 2) Disable Rocket Loader

Disable the Rocket Loader™ in the Cloudflare dashboard:

1. Log into the Cloudflare [dashboard](https://dash.cloudflare.com/login).
2. Select your account and website.
3. Go to Speed > Optimization.
4. Scroll down until you find Rocket Loader.
5. Turn it off.

### Method 3) Disable SiteGround Worker Routes

If the above 2 methods do not work and you are using SiteGround hosting, please check and disable the Worker created by SiteGround.

1. Log into the Cloudflare dashboard.
2. Select your account and website.
3. Go to Workers Routes.
4. If sg_worker exists or another suspicious worker is defined without your awareness, you can remove it.

![](https://academy.bricksbuilder.io/assets/sg-worker-in-cf-1024x640.png)

![](https://academy.bricksbuilder.io/assets/remove-sg-worker-in-cf.png)

## GoDaddy MU Plugin Causing Empty Canvas {#godaddy-empty-canvas}

For **GoDaddy** users, if you're experiencing an empty canvas issue **without Cloudflare Rocket Loader**, the cause might be a MU plugin injected by GoDaddy hosting.

To resolve this, add the following snippet in your child theme's `functions.php` file or via a code snippets plugin to dequeue the problematic script:

```php
add_action( 'wp_enqueue_scripts', function() {
  if ( bricks_is_builder() ) {
    wp_dequeue_script( 'GoDaddy\WordPress\Plugins\Launch\PublishGuidepublish-guide-script' );
    wp_deregister_script( 'GoDaddy\WordPress\Plugins\Launch\PublishGuidepublish-guide-script' );
  }
}, 1000 );
```

This will prevent the GoDaddy MU plugin from interfering with Bricks' builder rendering.

## Copy/paste elements or styles not working {#copy-paste}

Bricks 1.5.1 uses the Clipboard API to copy and paste elements and styles across different domains.

> **Note**
>
> Copy/paste is only supported for pages served over **HTTPS**.

### Using Firefox

Firefox is more restrictive regarding reading from this API, which prevents the paste action, and therefore it requires the user to manually grant permission to use the API.

To do so, please follow these steps in your Firefox browser:

1. Enter `about:config` in navigation bar
2. Click "Accept the Risk and Continue"
3. Search `clipboard`  and set `dom.events.asyncClipboard.readText` and `dom.events.testing.asyncClipboard` to  `true`
4. Restart Firefox

## Internal server error (500) when trying to edit homepage with Bricks {#error-500}

![](https://academy.bricksbuilder.io/assets/internal-server-error-500.png)

If you see a screen similar to the above, showing an internal server error (500) when trying to edit a page with Bricks (often reported as the homepage), you should look at the server logs and adjust the server configuration. This error is most probably caused by a security server configuration that prevents the request to hit WordPress and Bricks.

Some servers do not have the `SecResponseBodyLimit` defined leading to errors like:

```php
ModSecurity: Output filter: Response body too large (over limit of 1048576, total not specified).
```

(Note: the SecResponseBodyLimit sets the maximum response body size that will be accepted for buffering).

Check this [forum post](https://forum.bricksbuilder.io/t/solved-internal-server-error/1711) for possible solutions. If the issue persists, please contact your hosting support for guidance.

For **GoDaddy** users, you might need to add this line of code in your .htaccess file (first line)

```php
SubstituteMaxLineLength 10M
```

## My Blog page is not using the posts archive template {#blog-template}

![](https://academy.bricksbuilder.io/assets/bricks-blog-page-template-conditions.png)

The Blog page (WordPress Posts Page set in the Settings > Reading) is a special WordPress page, and therefore it is not an archive. If you want to set a Bricks template for the Blog page, you would need to set the template condition Individual and select the Blog page.

## I'm using SVG files in Bricks elements but I cannot change their color {#svg-styles}

This usually happens when your SVG file contains inline styles which override the styles generated by the Bricks builder. If you want to use these SVG files in combination with the Bricks style's controls, you need to remove the inline styles from the SVG file before uploading it to the WordPress installation.

![](https://academy.bricksbuilder.io/assets/Screenshot-2022-09-04-at-16.11.20.png)

<figcaption>

An example of an SVG file containing inline styles

</figcaption>

## Custom Fonts not working on the frontend {#custom-fonts}

If your custom fonts are not displayed in the frontend, it is probably because your WordPress website is delivered via HTTPS, but your WordPress URLs are still set to HTTP (WordPress Settings » General).

Changing the WordPress URLs from `http://` to `https://` will fix the problem and your fonts will be displayed correctly from now on.

## YouTube background video doesn't autoplay on mobile {#youtube-mobile-background-video}

This restriction is imposed by the YoutTube iFrame Player API and cannot be influenced by us. See [https://developers.google.com/youtube/iframe_api_reference#Mobile_considerations](https://developers.google.com/youtube/iframe_api_reference#Mobile_considerations)

However, Vimeo and local videos (mp4) should work as long as the mobile device is not in low-battery mode.

## Slider doesn't autoplay / Animation Flickering {#slider-autoplay}

This is most likely caused by the reduced motion or animation setting of your operating system.

On Windows, please make sure that the **"Show animations in windows"** setting is enabled:

![](https://academy.bricksbuilder.io/assets/show-animations-in-windows.jpeg)

On macOS, please make sure that the **"Reduce motion"** setting is NOT enabled:

![](https://academy.bricksbuilder.io/assets/macos-reduce-motion.png)

## Invalid Post Type / Custom Post Type 404 Errors {#cpt-404}

This problem is probably [the most common problem](https://www.google.com/search?q=wordpress+404+cpt&sourceid=chrome&ie=UTF-8) in WordPress: your custom post type returns a 404 error. In most cases, however, the problem can be solved very easily.

### Re-save your permalink settings

All you have to do is go to WordPress » Settings » Permalinks and click on "Save Changes".

### Check for slug conflicts

The slug refers to the user-friendly and URL-valid name of a post, page, category, tag, or any content (even images) within your website. It is a part of the URL that identifies a specific piece of content.

Let's assume you have a "Portfolio" page whose slug is "portfolio". Now you create a custom post type called "Portfolio", whose slug is also "portfolio". If you now try to call up a single post from your portfolio (yoursite.com/portfolio/your-portfolio-post), there will be a 404 error too. To solve this issue, rename either the page slug, or the custom post type slug to something else. Re-save your permalinks again, and everything should work as expected.

## Builder changes not saved {#not-saved}

If you save changes in the builder and everything appears to be saved, but upon refreshing or viewing on the frontend the changes are lost, it could be due to an issue with your database schema.

Specifically, check the `meta_value` column in your `wp_postmeta` table (or your table prefix, e.g., `psjw_postmeta`). This column should be set to "LONGTEXT" to ensure it can store large amounts of data. If it's set to a type with a lower storage capacity, such as "TEXT," it may not save larger data correctly.

For more details on storage limitations, refer to this resource: [Understanding Storage Sizes for MySQL TEXT Data Types](https://www.atlassian.com/data/databases/understanding-strorage-sizes-for-mysql-text-data-types).

WordPress defaults to using "LONGTEXT" for the `meta_value` column, which allows for much larger data storage. See the default schema here: [WordPress Database Description](https://codex.wordpress.org/Database_Description).

To resolve this issue:

1. Check your `meta_value` column type in the `wp_postmeta` table (or `psjw_postmeta`).
2. Ensure it is set to "LONGTEXT."

You can change the column type to "LONGTEXT" using the following MySQL command:

```php
ALTER TABLE your_prefix_postmeta MODIFY COLUMN meta_value LONGTEXT;
```

Replace `your_prefix_postmeta` with your actual table name, e.g., `psjw_postmeta`.

1. Verify that other columns in your `postmeta` table match the default WordPress schema.

If you are not comfortable making these changes or are using a managed hosting provider, it's best to get in touch with your hosting provider. They can help address this issue, which might persist across different hosting services due to the migration of the incorrect database schema.

## Save button spinning endlessly due to ModSecurity {#not-saved-modsec}

If you find that the save button in the Bricks builder is spinning endlessly, and your server logs point to ModSecurity errors, this could be caused by certain ModSecurity variables being too restrictive:

- `SecRequestBodyLimit`
- `SecRequestBodyNoFilesLimit`
- `SecResponseBodyLimit`

While we can’t guarantee this will resolve your specific issue, other users have found that increasing these values fixed the problem.

The values can vary depending on your server, so you might need to experiment or consult your hosting provider to make these changes.

## Query Filter Indexer: No Progress {#query-filter-indexer-no-progress}

![](https://academy.bricksbuilder.io/assets/element-indexing-in-progress.png)

If the filter element continues to display "Indexing in Progress" in the builder, try clicking the "Continue Index Job" button by following the instructions in [this article](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index).

![](https://academy.bricksbuilder.io/assets/indexer-always-stuck-issue.png)

However, if the indexing jobs remain pending without any progress, it might be caused by specific firewall rules blocking the background process.

Best to check your website firewall settings or contact your hosting support. If your website is protected by HTTP Authentication, please add this [code snippet](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index) in your child theme's functions.php as well.

<span id="cloudflare"></span>

For users with Cloudflare proxy enabled, ensure that Bot Fight Mode is disabled. [Refer to this guide to prevent false positives](https://developers.cloudflare.com/bots/troubleshooting/frequently-asked-questions/#what-should-i-do-if-i-am-getting-false-positives-caused-by-bot-fight-mode-bfm-or-super-bot-fight-mode-sbfm).

## Avoiding Slow Queries in Media/Attachment Dynamic Data {#avoid-slow-queries-in-media-attachment-dynamic-data}

When working with plugins like **ACF**, **Meta Box**, or **JetEngine** to create fields that store image or attachment file information, it is recommended to set the field’s return value to **object** or **ID** instead of **URL**.
Examples of Field Types:

- **ACF**: Image, Gallery, File
- **JetEngine**: Media, Gallery
- **Meta Box**: File Input, Image Select
- **Toolset**: Attachment URL to Post ID

This recommendation is important because Bricks uses the `attachment_url_to_postid` WordPress function to retrieve additional image data, such as dimensions and available sizes, when working with URL values. On websites with a large number of posts, this function can be resource-intensive, potentially slowing down page loading times.
By returning the field as an object or ID, Bricks can access the required data directly, improving performance and reducing the likelihood of slow queries.

## Slider doesn’t autoplay / Animations not working {#no-animation}

If your animations on your site are not working or your slider isn't autoplaying, it might be due to the "Reduce motion" setting on your device. This is an accessibility feature that Bricks respects. To see animations:

- **On Windows**: Ensure that the “Show animations in windows” setting is enabled.
- **On macOS**: Make sure that the “Reduce motion” setting is NOT enabled.

## Orphaned elements {#orphaned-elements}

In rare cases, Bricks element data may become corrupted. This can happen if a parent element (like a Section) is deleted but its child elements are not properly deleted due to a bug or third-party template import with corrupt data. These leftover elements are no longer linked to a valid parent and are referred to as **orphaned elements**.

Orphaned elements are not rendered in the builder or frontend but still exist in the page data, which can lead to unexpected issues such as:

- Orphaned text showing up in the WPML Advanced Translation Editor
- Incorrect filter element counts
- Unused styles or scripts (e.g. icon libraries) being loaded

### How to detect and clean up orphaned elements

Starting with Bricks 2.0, you can now detect and remove orphaned elements from within the builder.

Bricks automatically checks for orphaned elements on builder **load**. You can also:

1. Enable **“Check for orphaned elements on builder save”** in **Bricks Settings → General → Data integrity** to scan every time you save in the builder.
2. Add `&check=orphaned` to the builder URL to manually trigger a scan on save (helpful for debugging).

When enabled, Bricks will automatically check for orphaned elements on builder load and save. If any are found, you’ll see a notification with an option to **Clean up** the data. Clicking it will remove the orphaned elements from the current page.

After cleanup, we recommend reviewing your page to confirm everything looks correct. If anything went wrong, you can simply click undo to reverse the operation.

#### Site-wide orphaned elements review

You can also scan your entire site for orphaned elements from **Bricks Settings → General → Data integrity**. Click the **“Start: Orphaned elements review”** button to begin. Bricks will crawl all templates, pages, and any post type using Bricks, and list any that contain orphaned elements.

If no issues are found, you’ll see the message “No orphaned elements found”. If orphaned elements are detected, you’ll have the option to click **“Clean up all orphaned elements”**, which will remove them across all affected posts.

We recommend taking a backup before running the cleanup, just in case. Once confirmed, Bricks will proceed to delete the orphaned elements from each listed post.

---

# Troubleshooting a Bricks Website

Source: https://academy.bricksbuilder.io/builder/setup/troubleshooting/

*Find the source of problems across Bricks, WordPress, plugins, browsers, caching, hosting, and other parts of your website.*

A website built with Bricks depends on more than Bricks itself. WordPress, plugins, custom code, your browser, caching, a CDN, the web server, PHP, and the database can all affect what you see.

When something goes wrong, you first need to find out which part of the site is causing it.

After helping thousands of Bricks users troubleshoot their websites, we have found that elimination is usually the quickest way to get there. Start with a few harmless checks, then test the site with only the components needed to reproduce the issue.

This guide applies whether the problem appears in the builder, on the frontend, while saving, after an update, or somewhere else on the site.

## A Bricks website has several moving parts

A problem that appears in Bricks does not necessarily start in Bricks. The same is true for problems that appear in WordPress or on the frontend.

The main parts involved are:

- Your browser and its extensions
- WordPress, Bricks, and other plugins
- The active theme and custom code
- Browser, plugin, server, and CDN caches
- Optimization and security services
- PHP, the web server, and the database

These parts interact with each other.

For example, a save button that keeps spinning may look like a builder problem. The request could actually be blocked by a browser extension, rejected by a security plugin, interrupted by a PHP error, or blocked by a firewall rule.

Troubleshooting is the process of removing possible causes until you know which part of the site is involved.

## Make sure you can reproduce the issue

Before changing anything, repeat the action that causes the problem.

You only need a basic understanding of:

- What action triggers it
- What you expected to happen
- What happened instead
- Whether it affects one page or the whole site
- Whether it happens every time

Keep the description factual. “The save indicator keeps spinning, and the old content returns after reloading” is more useful than “Bricks cannot save.”

If the issue is inconsistent, look for what changes between attempts. It may depend on a particular page, browser, user role, screen size, field value, or cached response.

Use a staging site when testing could affect visitors, orders, forms, memberships, stored content, or site configuration. Create a backup before investigating missing data, failed saves, migrations, or database problems.

## Start with the quick checks

Rule out causes that are easy to test and do not require changing the website.

1. Open the affected page in a private browser window.
2. Try another browser.
3. Temporarily disable browser extensions.
4. Clear the browser, WordPress, server, and CDN caches.
5. Temporarily bypass JavaScript delay, minification, script combination, and similar optimization features.

Repeat the same action after each test.

If the issue only occurs in one browser, the cause is probably local to that browser or one of its extensions.

If clearing a cache fixes the issue temporarily, find out which cache served the outdated response. Otherwise, the problem may return when that cache is populated again.

## Isolate the site in bulk

If the quick checks do not reveal the cause, test a minimal version of the site on staging.

Keep Bricks active. If the issue involves another plugin, keep that plugin active too. Disable the other plugins, custom snippets, caching, and optimization.

For example, if you are investigating an interaction between Bricks and a multilingual plugin, keep Bricks and that plugin active. Disable everything else for the test.

Then clear all caches and repeat the original steps.

> **Note**
>
> Do not run plugin isolation on a live store, membership site, learning platform, or another site where disabling plugins could interrupt visitors, transactions, or background processing.

### If the issue disappears

Something you removed was involved.

Restore the disabled plugins and features one at a time. Repeat the same test after each one. When the issue returns, the last component you enabled is part of the conflict.

That component may still work correctly on its own. The issue may only appear when two plugins, settings, or scripts interact.

Confirm the result by testing the suspected combination again.

### If the issue remains

You have ruled out most third-party plugins, custom code, caching, and optimization.

Reduce the test further:

- Try the same action on a new page.
- Use one basic Bricks element when possible.
- Test with a standard theme.
- Try another administrator account.
- Remove any content that is not required to trigger the issue.
- Test on a fresh WordPress installation with only Bricks active.
- If another plugin is involved, activate only Bricks and that plugin.

A problem that survives this process is much easier to investigate because fewer parts of the site can be responsible.

## Follow the evidence

You do not need to perform every diagnostic check. Use the visible symptom to decide where to look next.

### Compare the builder and frontend

When the issue affects a Bricks page, check the same page in the builder and on the frontend.

- If the builder is correct but the frontend is not, check caching, generated CSS, template conditions, rendering settings, and frontend code.
- If elements appear in the Structure panel but not on the canvas, check CSS, JavaScript, browser extensions, and optimization.
- If elements are missing from the Structure panel as well, check revisions and stored data before saving the page again.
- If the frontend works while logged in but not while logged out, check public caching, template conditions, permissions, and frontend requests.

Confirm that the page uses **Render with Bricks** when you expect Bricks to render its layout. **Render with WordPress** uses the WordPress content instead. Changing this setting does not delete the saved Bricks layout.

See [Start Editing With Bricks](https://academy.bricksbuilder.io/builder/interface/editing-with-bricks/#edit-with-bricks-vs-render-with-bricks).

### Check failed browser requests

Open the browser developer tools and repeat the action.

Check **Console** for JavaScript errors and **Network** for failed or blocked requests. Responses with `401`, `403`, `404`, or `500` status codes can help identify the next place to investigate.

A failed request may come from WordPress, Bricks, another plugin, a security service, or the server. The response body often contains more useful information than the status code alone.

### Check WordPress and the server

Open **Bricks > System Information** and review the WordPress, Bricks, PHP, database, server, and active-plugin information.

Compare the environment with the [Bricks requirements](https://academy.bricksbuilder.io/builder/setup/requirements/).

If the browser shows a failed request, match its timestamp with the PHP and web-server logs. Look for:

- PHP errors
- Exhausted memory
- Execution time limits
- Request-size limits
- File permission errors
- Blocked REST API requests
- ModSecurity or firewall rules
- Rate limiting
- SSL or proxy configuration errors

The time, request URL, response status, and corresponding log entry usually provide a better lead than the visible error alone.

## When content or saved data is missing

Stop saving the affected page until you know whether an earlier version can be recovered. Another save may replace a useful revision or autosave.

Open **Manage > History / Revisions** in the builder and preview the available versions before applying one.

See [Revisions](https://academy.bricksbuilder.io/builder/interface/revisions/) for the recovery workflow.

If an earlier revision contains the missing content, restore it and verify the page. Keep the backup until you understand why the data disappeared or became unreadable.

### After migrating a site

A migration can affect URLs, serialized data, file paths, permissions, caches, and database configuration.

The frontend may continue showing cached HTML while the destination database contains unreadable builder data. Check the builder and an uncached frontend request before deciding that the migration preserved everything.

Bricks element data can include PHP serialized values. A basic text or SQL replacement can change a URL without updating the stored string length. WordPress may then be unable to read the value.

If content is missing after a migration:

1. Stop saving the affected pages on the destination.
2. Check whether the content still opens on the source site.
3. Check a pre-migration backup.
4. Confirm that the migration tool handles PHP serialized data.
5. Repeat the migration from an intact source when necessary.

Do not run a raw SQL `REPLACE()` query against Bricks post metadata. The [WordPress migration guide](https://developer.wordpress.org/advanced-administration/upgrade/migrating/) explains why database-wide URL replacement can damage serialized data.

[WP-CLI search-replace](https://developer.wordpress.org/cli/commands/search-replace/) handles serialized data and supports a dry run.

### After entering special characters

If content disappears after saving a smart quote, non-breaking hyphen, emoji, or another special character, check the database section under **Bricks > System Information**.

![](https://academy.bricksbuilder.io/assets/bricks-system-information-database-collation-warning.png)

- A green `utf8mb4_*` value is compatible.
- A warning means the table does not use a compatible `utf8mb4` collation.
- **Unknown** means Bricks could not retrieve the collation.

Correcting the collation can prevent the same storage problem on future saves. It cannot reconstruct data that is already corrupted.

Recover the affected page from a revision, autosave, intact source site, or database backup. Changing a production database collation requires a verified backup and someone familiar with WordPress database administration.

## Check whether the issue is already known

Once you have isolated the issue, search [Known issues](https://academy.bricksbuilder.io/builder/setup/known-issues/) for a confirmed conflict or workaround.

Search the [Bricks Forum](https://forum.bricksbuilder.io/) using the visible symptom, error message, or components involved. Another user may already have reported the same behavior.

Your isolation results make these searches more useful. Instead of searching for “builder not working,” you can search for a specific request error, plugin combination, element, or action.

## Reproduce and report a possible bug

Bricks can have bugs. If an issue remains after isolation, try to reproduce it on a fresh WordPress site.

Keep the setup as small as possible:

- Bricks
- Any plugin required to trigger the issue
- One page or template
- Only the elements and settings needed for the test

If the issue also occurs there, search Known Issues and the forum again using what you have learned. If no existing report matches, report it as a possible bug.

Include:

- The minimum plugins required
- The exact steps that trigger the issue
- What should happen
- What happens instead
- Whether it occurs every time
- Relevant browser or server errors
- A small template or page export when specific content is required

A useful reproduction might look like this:

1. Install WordPress and activate Bricks.
2. Create a page with a Form element.
3. Enable the specified setting.
4. Submit the form while logged out.
5. The request returns a `403` response instead of creating the submission.

These steps let someone reproduce the behavior without access to your website.

If the issue only happens on the original site, the environment or stored data is still part of the problem. Compare that site with the clean test until you find the difference that matters.

## Use an AI assistant during the investigation

Chat assistants such as ChatGPT or Claude can help interpret an error, compare what you have already tested, and suggest the next check. Paste the relevant error messages and explain what happened, but remove private information first.

An agent such as Codex or Claude Code can go further when it is running in an environment with access to your website files, command line, browser, or hosting account. Using an agent does not automatically give it access to any of those systems. You decide which tools and credentials it can use.

If you use the experimental [Bricks AI abilities and skills](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/), a connected agent can read Bricks system information, page structure, elements, revisions, and other site data exposed by enabled abilities. This can help it compare the affected page with a working page, identify plugin and environment differences, and inspect the state behind a visible error.

Start with read-only access on staging. If those checks are not enough, the optional [`bricks/execute-php` ability](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/#optional-enable-php-execution) lets an authorized agent run targeted, one-off PHP in the site's WordPress runtime. It can inspect active plugins, registered hooks, PHP configuration, scheduled events, file paths and permissions, and files or logs that the PHP process can read. It can also reproduce a plugin function with real site data or perform an explicitly approved file or data repair before testing again.

Direct PHP execution is not sandboxed. Enable it only on a backed-up local or staging site, ask the agent to explain a proposed write before running it, and disable it after the investigation. Server configuration and logs outside the PHP process's permissions still require hosting or server access.

```text
Help me investigate an issue on this WordPress site built with Bricks.

What happens: [describe the symptom]
Expected result: [what should happen]
Reproduction: [exact steps]
Already tested: [browser, cache, and isolation results]

Start with read-only Bricks abilities. If a targeted PHP check would narrow the cause, explain the exact code and expected output before running it. Do not change files or site data without my approval.
```

Remove passwords, cookies, nonces, license keys, API keys, personal data, and database credentials before sharing errors or configuration.

---

# Bricks Settings

Source: https://academy.bricksbuilder.io/builder/setup/settings/

*Configure the main Bricks settings in WordPress, including builder behavior, performance options, integrations, and advanced features.*

The Bricks settings screen (**Bricks > Settings**) is where you configure global options for your entire installation. Every setting documented here maps directly to what you see in the admin screen.

![](https://academy.bricksbuilder.io/assets/bricks-admin-settings.png)

Settings are split across tabs: **General**, **Builder access**, **Templates**, **Builder**, **Performance**, **Maintenance mode**, **API keys**, **Custom code**, and **WooCommerce** (only visible when WooCommerce is active).

At the top of the page you'll find two buttons:

- **Export settings**: Downloads your current Bricks settings as a JSON file. Normal setting values, including "Enable code execution", are included. Role and user capability grants for builder access, SVG uploads, code execution, maintenance bypass, and form submission access are WordPress capabilities and must be configured manually after each import.
- **Import settings**: Uploads a previously exported JSON file to restore or transfer settings between installations.

---

## General

### Post types

Select which WordPress post types can be edited with Bricks. Pages are enabled by default. For post types where every post shares the same layout (e.g. Products, Properties), you typically don't need to enable them here. Create a Bricks template with appropriate conditions instead.

### Block editor

Controls how Bricks interacts with WordPress block editor (Gutenberg) data.

- **Load Block editor data into Bricks**: When editing a page that has existing block editor content, Bricks will attempt to convert and load that content into the builder.
- **Save Bricks data as Block editor data**: Each time you save in Bricks, Bricks will attempt to write a Gutenberg-compatible copy of your content so it's visible in the standard WordPress editor. Not all elements are supported.

See the [Gutenberg integration](https://academy.bricksbuilder.io/integrations/gutenberg) article for more details.

#### Bricks components in the block editor <span title="Experimental">experimental</span>

Introduced in Bricks 2.1. Determines how Bricks components are made available as Gutenberg blocks.

- **Disabled (default)**: Components are not exposed in the block editor.
- **Enable individual components manually**: Each component must be explicitly enabled for block editor use.
- **Enable all components automatically**: All components are registered as block editor blocks automatically.

### SVG uploads

WordPress disables SVG uploads by default because SVG files are XML-based and can contain malicious scripts. This setting lets you enable SVG uploads per user role for roles with at least the `edit_posts` capability. All uploaded SVGs are automatically sanitized. Enable only for roles you trust.

See the [SVG uploads](https://academy.bricksbuilder.io/builder/features/svg-uploads) article for more details.

### Miscellaneous

- **Disable global class manager**: Removes the global class manager panel from the builder interface.
- **Output global class CSS in Class Manager order**: Added in Bricks 2.4. When enabled, Bricks outputs global class CSS in the same order as the classes appear in the [Global Class Manager](https://academy.bricksbuilder.io/builder/styling/global-class-manager/). This makes same-specificity class overrides more predictable when multiple assigned classes set the same CSS property. When disabled, Bricks keeps the previous behavior and outputs class CSS in the order classes are encountered on rendered elements.
- **Disable CSS variables manager**: Removes the CSS variables manager panel from the builder interface.
- **Disable Bricks Open Graph meta tags**: Stops Bricks from outputting its own Open Graph meta tags. Use this when another plugin like Yoast SEO or RankMath handles these.
- **Disable Bricks SEO meta tags**: Stops Bricks from outputting its own SEO meta tags. Use when an external SEO plugin handles these.
- **Generate custom image sizes**: Tells WordPress to generate the custom image sizes registered by Bricks when images are uploaded.
- **Add element ID as needed**: By default, Bricks adds the element's unique ID and class attributes to every rendered element regardless of whether it has any styles applied. With this setting enabled, Bricks skips those attributes on elements that have no CSS settings, producing slightly leaner HTML. Always added in the builder regardless of this setting.
- **Disable "Skip links"**: Removes the accessibility skip-navigation links Bricks injects at the top of each page (e.g. "Skip to main content"). Only disable if your theme handles skip links separately.
- **Smooth scroll**: Adds `scroll-behavior: smooth` globally via CSS, enabling smooth scrolling for anchor link navigation.
- **Enable "Delete Bricks data" button**: Reveals a "Delete Bricks data" button in the post/page edit screen that removes all stored Bricks data for that post. Requires explicit enabling to prevent accidental data loss.
- **Query Bricks data in search results**: Extends WordPress search to also query the post meta tables where Bricks stores page content. Text placed inside Bricks elements becomes searchable through WordPress native search.

### Theme styles: Loading method

Controls which theme styles are applied when multiple theme styles have conditions that match the current page.

- **Most specific (default)**: Only the single highest-scoring theme style is loaded, where score is based on condition specificity.
- **Load all matching theme styles**: All theme styles whose conditions match the current context are loaded and merged. More specific styles take precedence.

### Duplicate content

Controls who can use the "Duplicate" feature on posts and pages. By default, any user with the `edit_post` capability can duplicate content.

- **Enable (default)**: Duplication is available to all users with `edit_post` capability.
- **Disable globally**: Removes the duplicate option for all users.
- **Disable for WordPress data**: Disables duplication of WordPress core data (post title, content, etc.) while still allowing Bricks data duplication.

For advanced rules, use the [`bricks/use_duplicate_content`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-use_duplicate_content) filter.

### Form submissions

- **Save form submissions in database**: Enables the built-in form submission storage system. Submissions from the Bricks Form element are stored in a custom database table and accessible under **Bricks > Form submissions**.
- **Form submission access**: Select which user roles can view stored form submissions. Administrators always have access. Individual user access can also be set via the user profile edit page.
- **Reset database table**: Clears all stored form submission records while keeping the table structure.
- **Delete database table**: Drops the custom form submissions database table entirely. Only visible when form submissions are enabled.

### Query filters

Enables the query sort, filter, and live search system for Post, Term, and User query loops. Powers the Filter element.

- **Enable query sort / filter / live search**: Activates the query filter system and creates the required database index table.
- **Custom fields integration**: Enables ACF and Meta Box field integration with query filters, so you can filter results by custom field values. See the [query filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters#custom-fields-integration) article.

When enabled, an indexer manages a background database index used for filtering:

- **Regenerate filter index**: Rebuilds the filter index for the entire site. Run this after enabling filters or after major content changes.
- **Continue index job**: Immediately runs any queued index jobs without waiting for the next WP cron execution.
- **Fix corrupted database**: Appears when database corruption is detected. Repairs the filter index tables.
- **Remove all index jobs**: Clears all queued indexer jobs. Use this if the indexer gets stuck, then regenerate the index afterwards.

If your indexer makes no progress, see the [known issues: indexer no progress](https://academy.bricksbuilder.io/builder/setup/known-issues#query-filter-indexer-no-progress) article.

Avoid using query filters in combination with third-party filter plugins.

### Custom breakpoints

Enables custom breakpoints beyond Bricks' default set. Configure these before you start designing your site.

See [responsive editing](https://academy.bricksbuilder.io/builder/interface/responsive-editing#custom-breakpoints) for details.

- **Regenerate CSS files**: When using external CSS file loading, regenerates all CSS files to reflect the current breakpoint configuration.

### Custom authentication pages

Replaces WordPress' default `wp-login.php` authentication pages with your own Bricks-built pages.

See [custom authentication pages](https://academy.bricksbuilder.io/builder/features/custom-authentication-pages) for setup instructions.

- **Login**: Select the page to use as the custom login page.
- **Registration**: Select the page to use as the custom registration page.
- **Lost password**: Select the page to use as the custom lost password page.
- **Reset password**: Select the page to use as the custom reset password page.

#### WordPress authentication page access

Determines what happens when a visitor goes directly to a default WordPress authentication URL (e.g. `wp-login.php`). Only applies when custom pages above have been set.

- **Redirect to custom authentication page (default)**: Sends the visitor to the appropriate custom page set above.
- **Error page**: Returns a 404 error page.
- **Home URL**: Redirects to the homepage.
- **Redirect to specific page**: Redirects to any page you select from a dropdown.

**Disable custom authentication page bypass**: By default, anyone can access the original WordPress auth pages by appending `?brx_use_wp_login` (or `?brx_use_wp_login=1`) to the URL. This sets a 5-minute bypass cookie. Enable this setting to remove that bypass and enforce your custom authentication pages in all cases.

### User activation

When enabled, newly registered users receive an email with an activation link they must click to activate their account. Applies to all new user registrations site-wide, not only those submitted through the Bricks Form element.

- **User activation**: Enables the email verification flow.
- **Auto login after activation**: Automatically logs the user in after they click the activation link.
- **Verification success page**: The page users are sent to after successful activation.
- **Verification failure page**: The page users are sent to if activation fails or the link is invalid.

An **Activation status** column appears under **Users** so you can manually set users as active/inactive and resend activation emails.

#### User activation: Email

Configure the activation email sent to new users. Only visible when user activation is enabled.

- **From email address**: Sender email address. Falls back to the WordPress default.
- **From name**: Sender display name. Falls back to `WordPress`.
- **Subject**: Email subject line. Default: "Activate your account".
- **Email content**: Body of the activation email. Supports template parameters for site name, site URL, username, user email, and an activation link or raw activation URL.
- **HTML email**: Send the email as HTML instead of plain text.

### Password protection

Enables the password protection system for pages and templates. Password protection restricts frontend access only and does not affect the REST API or other access methods. For sensitive data, use more restrictive security controls.

See the [password protection](https://academy.bricksbuilder.io/builder/features/password-protection) article for details on applying protection to individual pages.

### Orphaned elements

Orphaned elements are elements whose parent no longer exists in the data, which can cause layout issues.

- **Check for orphaned elements on builder save**: Runs a scan for orphaned elements every time you save in the builder. Bricks always checks on load regardless of this setting. You can also trigger a check manually by adding `?check=orphaned` to the builder URL.
- **Start: Orphaned elements review**: Scans your entire site for orphaned elements and reports them. Results appear in-place after clicking the button.

See [known issues: orphaned elements](https://academy.bricksbuilder.io/builder/setup/known-issues#orphaned-elements) for more information.

---

## Builder access

Configure who can open the Bricks builder and what they can do inside it. See the [builder access](https://academy.bricksbuilder.io/builder/interface/builder-access) article for a full overview.

### Builder capabilities <span title="Experimental">experimental</span>

Bricks ships with three predefined capability levels:

- **Full access**: Grants access to all builder features.
- **Edit content**: Content editing only. Layout, styling, and structural controls are disabled.
- **No access**: Blocks builder entry completely.

You can create **custom capabilities** with granular permission control by clicking **Add new capability**. Custom capabilities can be named, given a description, and configured with only the permissions you want to grant. Once created, they appear in the builder access dropdowns alongside the defaults.

Administrators always have full access and cannot be restricted.

### Builder access

Assign a builder capability to each WordPress user role. Select from the predefined capabilities or any custom capability you've created.

To set access for a specific individual user, edit that user's WordPress profile directly.

Note: Any user role with the `manage_options` WordPress capability has full builder access regardless of this setting.

---

## Templates & components {#templates}

### My templates

Settings for your locally created Bricks templates.

- **Template screenshots**: Bricks automatically generates a screenshot of each template on every builder save. Screenshots appear in the template manager thumbnail and can also be bulk-generated from the template manager. A "Delete screenshots" button appears once screenshots exist.
- **Template manager thumbnail height**: Maximum height in px for template thumbnails in the builder's template manager. Templates taller than this auto-scroll on mouseover.
- **Template thumbnail column**: Shows a thumbnail column in the **Bricks > Templates** admin list, displaying the featured image or screenshot.
  - **Template thumbnail column: Width**: Column thumbnail width in px. Default: 60.
  - **Template thumbnail column: Height**: Column thumbnail height in px. Default: 60.
- **Disable default templates**: By default, if a published Bricks template exists with no conditions set, Bricks renders it on the frontend. Enable this to disable that fallback behavior and require explicit conditions on all templates.
- **Public templates**: When enabled, your templates can be viewed by anyone. When disabled, only logged-in users can view templates.
- **My templates access**: Allows other Bricks installations to browse and insert your templates from their own template library. Restrict access using the shared Remote access settings below.
- **Exclude templates**: Select specific templates to exclude from remote access even when access is otherwise enabled.

### My components

- **Component screenshots**: Automatically generates component screenshots on every builder save and enables the individual and bulk generate actions in the Component Manager. This is enabled by default on new installations. Disabling it stops generation and hides saved local component thumbnails without deleting the files. Use **Delete screenshots** to remove all generated component screenshots.
- **My components access**: Allows other Bricks installations to browse and import your components. Restrict access using the shared Remote access settings below.
- **Exclude components**: Keeps selected components out of the remote catalog. Bricks also blocks a remote import when the selected component depends on an excluded component.

### Remote access

These controls are shared by remote templates and components:

- **Whitelist URLs**: Limits access to specific destination-site URLs. Enter one URL per line. Leave blank to allow any site that meets the other access requirements.
- **Password protection**: Adds a password that remote sites must enter to access exposed templates or components. The field includes show, copy, and generate controls.

### Remote libraries

Configure other Bricks installations as template and component sources. You can add multiple remote sites.

For each remote source:

- **Name**: Label shown in builder source dropdowns instead of the URL.
- **URL**: Full URL of the remote Bricks installation.
- **Password**: The password set on the source site under **Remote access > Password protection**.

The source site separately controls whether it exposes templates, components, or both. See [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/) for the template setup.

### Miscellaneous

- **Convert templates**: When importing or inserting a template built with the old `Container` element structure, Bricks automatically converts it to the current layout structure (Section > Container > Block / Div). See the [layout](https://academy.bricksbuilder.io/builder/styling/layout) article for the current element hierarchy.

---

## Builder

### Autosave

- **Disable autosave**: Turns off automatic background saving. The autosave creates a recovery copy of all canvas elements. Global data (components, classes, variables) is not included. Autosaves can be restored from **Manage > History / Revisions** in the builder toolbar.
- **Autosave interval**: How often the autosave runs, in seconds. Default: 60. Minimum: 15.

### Builder mode

Sets the visual theme of the builder UI.

- **Dark (default)**: Dark background builder interface.
- **Light**: Light background builder interface.
- **Custom**: Define your own builder color scheme using CSS variables. See [builder mode](https://academy.bricksbuilder.io/builder/interface/builder-mode) for available CSS variables.

When "Custom" is selected, a code editor appears for entering your CSS variable overrides.

### Language

- **Builder language**: Sets the language for the builder UI, independent of the WordPress site language. Defaults to the site language.
- **Builder language direction**: Overrides the text direction in the builder.
  - **Auto (default)**: Determined by the selected language.
  - **Left to right**
  - **Right to left**

### Toolbar logo link

Sets what happens when you click the Bricks logo in the builder toolbar.

- **View on frontend (default)**: Opens the frontend view of the currently edited page.
- **Home page**: Links to the site homepage.
- **Dashboard**: Links to the WordPress admin dashboard.
- **Post type**: Links to the post type list in WordPress admin.
- **Edit in WordPress**: Opens the standard WordPress editor for the current post.
- **Custom URL**: Links to any URL you specify.
- **No link**: Removes the link from the logo.

**Open in new tab**: Opens the logo link destination in a new browser tab.

### Control panel

Fine-tune the behavior of the builder's settings panel.

- **Class preview on hover**: When hovering over a global class name in the classes field, shows a preview of the styles defined in that class.
- **Class dropdown: Auto-select first class**: Added in Bricks 2.4. Automatically selects the first valid global class assigned to an element when you select that element on the canvas. Disabled by default. If Bricks is also set to remember the last selected class and that class is still assigned to the element, the remembered class takes priority.
- **Class dropdown: Disable auto-selecting last selected class**: Added in Bricks 2.4. Prevents Bricks from automatically restoring the last global class you selected for an element. Disabled by default, so Bricks continues to restore the last selected class unless you enable this setting. If you enable this setting together with **Class dropdown: Auto-select first class**, Bricks selects the first assigned class instead.
- **Color preview on hover**: Shows a color swatch when hovering over color values in the control panel.
- **Variable preview on hover**: Shows the resolved value of a CSS variable when hovering over it in dropdowns or input fields.
- **Disable auto-expand**: Prevents text editor and code controls from automatically expanding when you focus them.
- **Disable pinned control groups**: Disables the ability to pin frequently used control groups to keep them open.
- **Disable global classes (interface)**: Hides the global classes UI in the control panel. Global classes can still be used programmatically. This is distinct from disabling the global class manager under General.
- **Variable dropdown: Hide value**: In the CSS variable picker dropdown, hides the resolved value shown next to variable names.
- **Code control: Vim toggle**: Enables Vim keybindings in CodeMirror code editors within the builder.
- **Spacing control: Remember linked state**: Persists the linked/unlinked state of spacing controls (margin, padding, border-radius) across all elements. When enabled, if you set one element's padding to "all sides linked," subsequent spacing controls open in that same state.

#### Element breadcrumbs

Shows a breadcrumb trail above the element in the control panel indicating where you are in the element hierarchy.

- **Disabled (default)**
- **Show default element names**: Uses Bricks' built-in element type names (e.g. "Section > Container > Text").
- **Show custom element names**: Uses the custom names you've assigned to elements.

#### Responsive control indicator

Controls when an indicator icon appears on controls that support per-breakpoint values.

- **Show if any value exists (default)**: Shown when any value (including base/desktop) is set.
- **Show if non-base breakpoint value exists**: Shown only when a tablet or mobile override exists.
- **Show on all responsive controls**: Always visible on every control that supports responsive values.
- **Disable**: Never shown.

#### Control group visibility

- **Hide if not open (default)**: Control groups are collapsed until clicked.
- **Always show**: All control groups are expanded at all times.

#### Font family options

- **Show all fonts (default)**: All available fonts appear in the font family dropdown.
- **Show favorites only**: Only fonts you've marked as favorites appear.

### Media

Introduced in Bricks 2.4.

- **Media picker**: Chooses the interface used by supported Image, Image Gallery, Video, Audio, SVG, and File controls. **Bricks: Media browser** is the default. **WordPress: Media library** opens the standard WordPress picker instead. Both options use attachments from the WordPress Media Library.
- **Media folders**: Shows the active compatible folder integration. Bricks includes support for <a href="https://happyfiles.io/" target="_blank" rel="noopener noreferrer">HappyFiles</a>. Without an active integration, the Media Browser remains available without folder organization.
- **Enable media health checks**: Audits the Media Library incrementally for missing alternative text, broken files, obsolete formats, missing image sizes, and files above the configured size thresholds. Enabled by default.

All five Media Health checks are enabled by default. The default oversized-file thresholds are 1 MB for images, 0.5 MB for fonts, 5 MB for documents, 10 MB for audio, and 50 MB for video. Set a threshold to `0` to disable warnings for that media type.

The default obsolete file extensions are `bmp,tif,tiff`. Enter extensions without leading dots, separated by commas. Clear the field so no extensions are flagged as obsolete.

### Canvas

- **Disable element spacing**: Removes the visual margin and padding indicators on elements when selected in the builder canvas.
- **Auto scroll element into view**: When you select an element in the structure panel, the canvas scrolls to bring it into view. Set the scroll offset as a percentage (e.g. `50%` centers the element) or `off` to disable. Default: `0`.

### Structure panel

- **Element actions: Duplicate**: Adds a "Duplicate" button to each element row in the structure panel.
- **Element actions: Delete**: Adds a "Delete" button to each element row in the structure panel.
- **Collapse on page load**: The structure panel opens with all element groups collapsed when you first open the builder.
- **Expand active element & scroll into view**: When you select an element on the canvas, the structure panel automatically expands its parent groups and scrolls to show it.

### Element actions

#### Wrap element

Sets the default wrapper element used when wrapping an element (via keyboard shortcut or right-click context menu).

- **Block (default)**
- **Div**
- **Container**

#### Insert element

Sets the default element type inserted via the "+" icon or right-click context menu.

- **Block (default)**
- **Div**
- **Container**

#### Insert layout

Sets the element type used when inserting a layout via the "Layout" action icon.

- **Block (default)**
- **Div**
- **Container**

#### Import pasted images/SVGs

When pasting elements from a different site, images and SVGs are represented as placeholders by default because source URLs may not be accessible. Enable this to have Bricks download and import those assets from the source site into the local media library.

Only applies to Image, Image Gallery, and SVG elements. Images with a custom URL or dynamic data tag as their source are not imported.

### WP polyfill

Loads `wp-polyfill.min.js` in the builder to improve compatibility with older browsers. Not recommended for modern browsers due to the performance overhead.

### Cloudflare Rocket Loader <span title="Experimental">experimental</span>

Enable if the builder fails to load when Cloudflare Rocket Loader is active. Rocket Loader defers JavaScript loading and can interfere with the builder's initialization.

### Query loop

- **Max results**: Limits the number of results displayed per query loop in the builder canvas. Useful for keeping the builder fast when queries return large result sets. Applies to Bricks-native queries only. Minimum: 2.
- **Show query loop type**: Shows the underlying object type key in the query loop type dropdown (e.g. `acf_related_writers`, `mb_page-to-user`). Useful for developers working with custom query integrations.

### Dynamic data

- **Render dynamic data text on canvas**: Bricks evaluates and renders dynamic data tags live on the builder canvas so you see real content instead of tag placeholders.
- **Disable WordPress custom fields in dropdown**: Hides WordPress custom fields from the dynamic data tag dropdown. Can noticeably improve builder performance on sites with many custom fields. You can still use these fields by typing tags like `{cf_my_field}` directly.
- **Dropdown: Show dynamic data key**: Shows the tag key (e.g. `{post_title}`) alongside the label in the dynamic data dropdown.
- **Dropdown: Hide dynamic data label**: Hides the human-readable label and shows only the tag key in the dropdown.
- **Dropdown: Expand panel when dropdown is visible**: Widens the control panel when the dynamic data dropdown is open so more items are visible.

### Global data sync <span title="Experimental">experimental</span>

When multiple people work in the builder at the same time, saves can overwrite each other's global class changes. Enabling this syncs global classes on every builder save across all open builder instances.

### CSS Sync <span title="Experimental">experimental</span> {#css-sync}

Introduced in Bricks 2.4. Keeps supported declarations in an element's or global class's Custom CSS synchronized with the corresponding style controls. Changes work in both directions, while unrelated or unsupported CSS remains unchanged.

See [Bi-directional CSS Sync](https://academy.bricksbuilder.io/builder/features/custom-code/#bi-directional-css-sync) for setup and behavior.

### Global class import manager

Controls when the global class import manager dialog appears when pasting elements, importing classes, or inserting templates that contain classes.

- **Show for class conflicts (default)**: Opens when an imported class conflicts with an existing one (same name, different styles).
- **Show for new classes**: Opens when imported content contains classes not yet in your library.
- **Show for new & conflicting classes**: Opens for both new and conflicting classes.
- **Never**: Applies imported classes silently without the dialog.

### HTML & CSS to Bricks

Introduced in Bricks 2.3. Controls automatic conversion of pasted HTML and CSS clipboard content into Bricks elements, global classes, and global variables.

- **Enable (confirm on paste) (default)**: Ask before converting detected HTML or CSS clipboard content.
- **Enable (no confirm on paste)**: Convert detected HTML or CSS clipboard content without the confirmation step.
- **Disable**: Ignore detected HTML or CSS clipboard content.

### Render

- **Disable WP REST API render**: By default, the builder uses the WP REST API to render elements on the canvas. Enable this to fall back to AJAX rendering. Only use if you experience rendering issues such as when the REST API is blocked on your server.

### Instant navigation <span title="Experimental">experimental</span>

Switch between pages and templates in the builder without a full page reload. Useful when working across multiple pages in sequence.

---

## Performance

### Disable emojis

Removes WordPress' emoji conversion script and CSS (`wp-emoji-release.min.js`). Recommended if you don't use emojis in your content, as it removes an unnecessary HTTP request.

### Disable embed

Removes WordPress' oEmbed scripts and the ability to paste URLs to auto-embed content. Recommended if you don't embed external content like YouTube videos or tweets.

### Disable Google Fonts

Stops Bricks from loading Google Fonts from Google's CDN. Enable if you don't use any Google Fonts, or if you've uploaded and self-host your Google Fonts as custom fonts.

### Disable lazy loading

Bricks applies native lazy loading to images by default. Disable if lazy loading causes display problems on your site.

- **Lazy load offset**: How many pixels before an image enters the viewport for it to start loading. Default: 300px.

### Disable jQuery migrate

Removes the `jquery-migrate.min.js` script WordPress includes for backward compatibility with older jQuery code. Safe to disable if you're not running any jQuery older than version 1.9.

### Cache query loops

Caches query loop results using WordPress' object cache. The cache key includes the element ID, query vars, and parent loop context, so different queries produce separate cache entries. Works best when query arguments stay relatively stable between requests.

For caching that persists across page loads, a server-level object cache (Redis, Memcached) must be in place. Disable this if you see unexpected or stale query results.

### Disable class chaining

By default, when an element has a global class applied, Bricks generates CSS selectors that chain the global class with the element type class (e.g. `.my-class.brxe-button`). This raises selector specificity. Enabling this removes that chaining so the selector becomes just `.my-class`. Useful in edge cases where the higher specificity conflicts with third-party CSS.

### CSS loading method

Controls how Bricks outputs page-specific CSS.

- **Inline styles (default)**: CSS is included in `<style>` tags directly in the HTML. Always current, no caching.
- **External files**: Bricks generates `.css` files in the `wp-content/uploads/bricks/css/` directory and loads them as external stylesheets. Enables browser and CDN caching. The uploads directory must be writable.

When external files are selected, a **Regenerate CSS files** button appears. The date and Bricks version of the last regeneration is also shown.

See the [asset loading](https://academy.bricksbuilder.io/developer/guides/asset-loading) article for a detailed comparison.

### Webfont loading method

Only visible when Google Fonts are not disabled.

- **Stylesheets (default)**: Fonts are loaded via a `<link>` stylesheet. Can cause a Flash of Unstyled Text (FOUT) before fonts load.
- **Webfont Loader (JS)**: Uses the Webfont Loader library to manage font loading. Hides site content until fonts have loaded, preventing FOUT.

### Preload custom fonts

When using self-hosted custom fonts, enabling this adds `<link rel="preload">` tags for matching font files in the `<head>`, so the browser fetches them earlier and avoids FOUT. Added in Bricks 2.0.

Bricks automatically preloads custom font files it detects from explicit typography settings in the active page output. The custom font family and the relevant weight/style must be set in Bricks typography controls so Bricks can match them to a saved custom font variation. Bricks does not resolve the full CSS cascade across inherited font families, separate font-weight declarations, responsive states, custom selectors, or custom CSS. For example, if a button inherits a custom font family from the body but only sets `font-weight: 700` on the button itself, the separate 700 font file may not be preloaded automatically unless that family and weight are set together in typography settings.

For more details, see [Preloading custom fonts](https://academy.bricksbuilder.io/builder/styling/font-manager/#preloading-custom-fonts).

### Cascade layer <span title="Legacy">legacy</span>

Bricks uses a CSS cascade layer system to manage style specificity and prevent unintended overrides. Disabling it reverts to the older behavior without cascade layers.

Strongly discouraged. Leave this off unless you have a specific compatibility reason for doing so. See the [Bricks cascade layer system](https://academy.bricksbuilder.io/builder/styling/cascade-layer) for details.

---

## Maintenance mode

### Mode

Activates a site-wide maintenance or coming soon page.

- **Disabled (default)**: Site is fully accessible.
- **Maintenance**: Returns HTTP status code 503, indicating temporary unavailability. Search engines treat this as "check back later."
- **Coming soon**: Returns HTTP status code 200. The site is accessible to search engine indexing while showing the maintenance page.

### Template

Select a Bricks template (type: Single) to display as the maintenance or coming soon page. The template must be published.

- **Render header**: Include your header template on the maintenance page.
- **Render footer**: Include your footer template on the maintenance page.
- **Render popups**: Include popup templates on the maintenance page.

### Bypass maintenance

Controls which logged-in users can bypass maintenance mode and see the real site.

- **Logged-in users (default)**: All logged-in users bypass the maintenance page.
- **Logged-in users with role**: Only users with the selected roles bypass maintenance. Administrators always bypass.

Individual user bypass can also be granted via the user's profile page.

### Exclude posts/pages

Select specific pages or posts that stay publicly accessible while maintenance mode is active.

---

## API keys

Paste third-party service credentials here. Keys are partially obfuscated on screen for security.

- **Adobe Fonts (Project ID)**: Your Adobe Fonts (Typekit) project ID. After saving, click **Sync fonts** to pull the font list from the Typekit API. See [Adobe fonts](https://academy.bricksbuilder.io/builder/styling/adobe-fonts) for setup instructions.
- **Unsplash: API key**: Enables the Unsplash image search integration in the media picker. See [Unsplash](https://academy.bricksbuilder.io/integrations/unsplash) for setup instructions.
- **Google Maps: API key**: Required for the Google Maps element. See the [Google Maps API documentation](https://developers.google.com/maps/documentation/javascript/get-api-key) for how to obtain a key.
- **Google reCAPTCHA v3: Site key**: Public site key for reCAPTCHA v3 integration with Bricks forms.
- **Google reCAPTCHA v3: Secret key**: Private secret key for server-side reCAPTCHA v3 verification. See [Google reCAPTCHA v3 documentation](https://developers.google.com/recaptcha/docs/v3).
- **hCaptcha: Site key**: Public site key for hCaptcha integration.
- **hCaptcha: Secret key**: Private secret key for hCaptcha server-side verification. See [hCaptcha documentation](https://docs.hcaptcha.com/switch/#get-your-hcaptcha-sitekey-and-secret-key).
- **Cloudflare Turnstile: Site key**: Public site key for Cloudflare Turnstile CAPTCHA integration.
- **Cloudflare Turnstile: Secret key**: Private secret key for Turnstile verification. See [Cloudflare Turnstile documentation](https://developers.cloudflare.com/turnstile/get-started/).
- **MailChimp: API key**: Connects to the MailChimp API to power the MailChimp form action in Bricks forms. Save settings to sync your audience lists. See [MailChimp API keys](https://mailchimp.com/help/about-api-keys/).
- **SendGrid: API key**: Connects to SendGrid to power the SendGrid email action in Bricks forms. Save settings to sync lists. See [SendGrid API keys](https://sendgrid.com/docs/ui/account-and-settings/api-keys/#creating-an-api-key).
- **Facebook App ID**: Required for Facebook-powered features. See [Facebook App registration](https://developers.facebook.com/docs/apps#register).
- **Instagram Access Token**: Required for the Instagram feed element. See [Instagram access token](https://academy.bricksbuilder.io/integrations/instagram-access-token) for how to generate a token.

---

## Custom code

### Code review

A site-wide audit tool that scans for all Code elements (PHP & HTML), SVG elements with inline code, query editor instances, and `{echo:}` dynamic data tags.

Click **Start: Code review** to generate a full report. Results show which page or template contains each code instance, the element type, and the code content. Use the filter dropdown to narrow results by type (Code, SVG, Query editor, Echo tags).

Code instances are tagged with their signature status:

- **No signature**: Code has never been signed.
- **Invalid**: Code has been modified since it was last signed.
- **Valid**: Code is signed and unmodified.

When Echo tags are detected, a code snippet is shown at the bottom of the results ready to copy into your child theme to whitelist those functions via the [`bricks/code/echo_function_names`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-echo_function_names) filter.

### Code execution

Controls the ability to execute PHP code via Code elements, SVG element code, Query editors, and `{echo:}` dynamic data tags.

- **Enable code execution**: Globally enables code execution. Off by default.

When enabled, you must also grant the execute code capability to specific roles or individual users:

- **User roles with code execution capability**: Checkboxes for each role with at least `edit_posts` capability.
- **Individual users with code execution capability**: Lists users who have been individually granted code execution via their user profile. Edit a user profile directly to grant or revoke access.

> Grant code execution only to trusted users, and prefer per-user grants over role-based grants where possible.

Function names used in `{echo:}` tags must be whitelisted separately via the [`bricks/code/echo_function_names`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-echo_function_names) filter.

The `bricks/code/disable_execution` filter can forcibly disable code execution regardless of these settings. When active, an info notice appears here.

### Code signatures

Code signatures cryptographically sign code content. Signed code that has been modified since signing is treated as invalid and will not execute.

- **Regenerate code signatures**: Signs all Code elements, SVG elements, and Query editors site-wide. Always create a full-site backup and run the code review above before generating signatures globally.

Signatures must be regenerated whenever your WordPress secret keys (salts) change, as the signatures are derived from them.

### Custom CSS

Global CSS applied to every page on your site. Output as an inline `<style>` block in the `<head>`. Use this for global overrides, utility classes, or styles that need to apply everywhere.

For page-specific CSS, use the Custom CSS control in the page settings panel inside the builder. See the [custom code](https://academy.bricksbuilder.io/builder/features/custom-code) article.

### Header scripts

Scripts (and other HTML) injected right before the closing `</head>` tag on every page. Wrap scripts in `<script>` tags. Common uses: analytics tracking tags, tag manager snippets, preconnect hints.

### Body (header) scripts

Scripts injected immediately after the opening `<body>` tag on every page. Wrap scripts in `<script>` tags. Common uses: Google Tag Manager `<noscript>` fallback, chat widgets.

### Body (footer) scripts

Scripts injected right before the closing `</body>` tag on every page. Wrap scripts in `<script>` tags. Common uses: analytics event scripts, deferred third-party libraries.

---

## WooCommerce

This tab is only visible when WooCommerce is installed and active.

### Miscellaneous

- **Disable WooCommerce builder**: Disables all Bricks WooCommerce-specific elements and features, reverting to default WooCommerce output.
- **Enable Bricks WooCommerce "Notice" element**: All native WooCommerce notices are removed when this is enabled. You must manually add the Bricks "Notice" element wherever notices should appear (cart page, checkout page, etc.).
- **Enable Bricks WooCommerce "Checkout coupon" element**: Removes the native WooCommerce checkout coupon form. You must manually add the Bricks "Checkout coupon" element to your checkout page. Requires "Enable the use of coupon codes" to be active in WooCommerce > General.
- **Enable Bricks WooCommerce "Checkout login" element**: Removes the native WooCommerce checkout login form. You must manually add the Bricks "Checkout login" element to your checkout page. Requires "Enable log-in during checkout" in WooCommerce > Accounts & Privacy.
- **Show quantity input field in product loop**: Adds a quantity input field next to the add-to-cart button in product loops. Applies to purchasable simple products that are in stock only.
- **Enable product variation swatches**: Converts product variation attribute dropdowns to visual swatches (color, image, or label) on the add-to-cart element for variable products.

### Products

- **Product badge "Sale"**: Controls the content of the sale badge on sale products.
  - **None (default)**: No sale badge.
  - **Text**: Shows the word "Sale".
  - **Percentage**: Shows the discount percentage (e.g. "25% off").
- **Product badge "New"**: Shows a "New" badge on products published within the specified number of days. Leave blank to disable.

### Single product

- **Disable product gallery zoom**: Disables the zoom-on-hover behavior on single product gallery images.
- **Disable product gallery lightbox**: Disables the lightbox that opens when clicking product gallery images.

### AJAX add to cart

Enables asynchronous add-to-cart on product archives and loops without requiring a page reload.

- **Enable AJAX add to cart**: Overrides WooCommerce's native AJAX add to cart on archive pages. Only simple products within query loops benefit from this. Requires "Enable AJAX add to cart buttons on archives" to be active in WooCommerce > Products settings.

**Adding state:**

- **Button text: Adding**: Text shown on the button while the add-to-cart request is in progress. Default: "Adding".

**Added state:**

- **Button text: Added**: Text shown on the button after the item is successfully added. Default: "Added".
- **Reset text after .. seconds**: How many seconds before the button text reverts to the original label. Default: 3.
- **Hide "View cart" button**: Hides the "View cart" link WooCommerce shows after an item is added.
- **Show notice**: Displays a WooCommerce notice when the item is successfully added.
- **Scroll to notice**: Scrolls the page to the notice after a successful add-to-cart.

**Error handling:**

- **Action on error**: What happens when an add-to-cart error occurs (e.g. a variable product that requires attribute selection).
  - **Redirect to product page (default)**: Sends the user to the product's single page.
  - **Show notice**: Displays an inline error notice.
- **Scroll to notice on error**: Scrolls to the error notice. Only visible when "Show notice" is selected as the error action.
