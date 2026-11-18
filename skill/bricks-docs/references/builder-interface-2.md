# Page Settings

Source: https://academy.bricksbuilder.io/builder/interface/page-settings/

*Use Bricks page settings to control per-page markup, styling, SEO metadata, social sharing output, and custom code.*

Page Settings control output for the page, post, or content template you are currently editing. They are different from global Bricks settings and different from an individual element's controls.

Use Page Settings when a setting should apply to the whole current page, such as body classes, header/footer visibility, page-level scroll snap, SEO metadata, social sharing data, or page-specific code.

## Open Page Settings

Open the builder and click the **Settings** icon in the toolbar. Choose **Page Settings**.

Page Settings are available only when the current user has permission to access them. Some groups can also be hidden by global settings.

Use the **Reset** icon in the panel header to clear all page settings with a single click.

## How Page Settings are applied

Page Settings are stored with the current Bricks document. On the frontend, Bricks reads those settings while rendering the page.

Some settings change markup, such as body classes or disabling the header. Some generate CSS, such as scroll snap and Custom CSS. Some print metadata or scripts into the document head or body. Some settings are visible in the builder immediately, while others should be checked on the frontend.

![](https://academy.bricksbuilder.io/assets/bricks-page-settings.png)

## General settings

The General group contains page-wide output options.

| Setting | What it does |
| --- | --- |
| CSS classes (body) | Adds space-separated classes to the page `<body>` tag. Dynamic data can be used when appropriate. |
| Disable header | Prevents the active Bricks header from rendering on this page. Not shown for header or footer templates. |
| Disable footer | Prevents the active Bricks footer from rendering on this page. Not shown for header or footer templates. |
| Disable lazy load | Disables Bricks' built-in lazy loading for images, videos, background images, and background videos on the current page. Background videos honor this setting from Bricks 2.5. |
| Disable popups | Prevents Bricks popups from rendering on the current page. |
| Page layout | Overrides the page layout inherited from Theme Styles. |
| Page background | Overrides the page background inherited from Theme Styles. |
| Content margin | Overrides the content margin inherited from Theme Styles when available. |

Use these settings for page-specific exceptions. If you need the same behavior on many pages, use global settings, Theme Styles, or templates instead.

For a single background, use the element's **Style > Background > Disable lazy load** control (Bricks 2.5). See [Lazy Loading](https://academy.bricksbuilder.io/builder/features/lazy-loading/) for the available scopes and how they affect the element control.

## Scroll snap

The Scroll snap group configures page-level CSS scroll snapping.

| Setting | What it does |
| --- | --- |
| Type | Sets the page scroll-snap type on the `html` element. |
| Snapping elements selector | Defines which elements should snap. Defaults to Bricks sections when left empty. |
| Align | Sets the snap alignment of snapping elements. |
| Margin | Sets scroll margin for snapping elements. |
| Padding | Sets scroll padding on the `html` element. |
| Stop | Sets scroll-snap-stop behavior. |

Scroll snap is primarily a frontend behavior. Test it on the frontend, not only in the builder canvas. Layout height, overflow, sticky headers, and browser behavior can affect the result.

If you use a custom selector, make sure the selector matches the elements that should become snap points. If the selector matches nothing, the page can have scroll snap enabled without visible snapping.

## One Page Navigation {#one-page-nav}

If enabled, Bricks adds a vertical dot menu to the right edge of the page in a fixed position, with each dot linking to the page's root element.

![](https://academy.bricksbuilder.io/assets/bricks-one-page-navigation-1024x534.png)

One Page Navigation is shown only where it applies, such as normal pages and content templates. It is not shown for header or footer templates.

The navigation uses the IDs Bricks renders for root elements. Add custom CSS IDs when you need stable, readable anchors or when root elements are generated dynamically.

> **Note**
>
> If a root element is inside a query loop, use dynamic data in the CSS ID, such as a post ID or slug, so every repeated root element has a unique anchor.

![](https://academy.bricksbuilder.io/assets/one-page-navigation-loop-unique-css-id.png)

The One Page Navigation controls style the dot menu and its active state:

- Spacing
- Item width and height
- Item color
- Border
- Box shadow
- Active item width and height
- Active item color
- Active border
- Active box shadow

The active dot changes based on the root element currently in the scroll range.

## SEO

The SEO group controls page-level metadata. This group is hidden when Bricks SEO output is disabled globally.

| Setting | What it does |
| --- | --- |
| Permalink | Updates the post slug. Use lowercase words separated by dashes. |
| Title | Updates the WordPress post title after applying the change. |
| Document title | Sets the frontend SEO title without changing the WordPress post title. |
| Meta description | Prints a page-level meta description. |
| Meta keywords | Prints page-level meta keywords. |
| Meta robots | Prints robots directives such as `noindex` or `nofollow`. |

Use **Save new title/permalink** after changing the post title or permalink in the SEO group. Other page settings are saved through the normal builder save flow.

If you use a dedicated SEO plugin, decide which tool owns the metadata. Avoid setting competing metadata in multiple places.

## Social media

The Social media group controls Open Graph style sharing data for the current URL. This group is hidden when Bricks Open Graph output is disabled globally.

| Setting | Default when empty |
| --- | --- |
| Title | The post/page title. |
| Description | The post/page excerpt. |
| Image | The featured image. |

Use this group when a page needs a social title, description, or image that differs from its normal SEO data.

## Custom Code

The Custom Code group adds page-specific CSS and scripts.

| Setting | Output location |
| --- | --- |
| Custom CSS | Inline CSS in the document `<head>`. Supports breakpoint-specific values. |
| Header scripts | Before the closing `</head>` tag. |
| Body (header) scripts | Immediately after the opening `<body>` tag. |
| Body (footer) scripts | Before the closing `</body>` tag. |

Script fields are shown only to users who are allowed to add unfiltered HTML. Users without that capability see an informational notice instead.

Use page-level code sparingly. Prefer element settings, classes, Theme Styles, global settings, or properly enqueued code when the behavior should be reused across the site.

## Common mistakes

- **Changing SEO title but not applying it:** Use **Save new title/permalink** for title and slug changes.
- **Expecting header/footer disable to affect templates globally:** These settings affect only the current page render.
- **Using duplicate IDs for One Page Navigation:** Give repeated root elements unique IDs, especially inside query loops.
- **Testing scroll snap only in the builder:** Always test on the frontend.
- **Adding scripts without the right capability:** Script fields require permission to add unfiltered HTML.
- **Using page code for reusable behavior:** Page Custom Code is local to the current page. Use global settings or enqueue code for site-wide behavior.

---

# Responsive Editing

Source: https://academy.bricksbuilder.io/builder/interface/responsive-editing/

*Edit Bricks designs responsively across breakpoints and adjust layout, spacing, and element settings for smaller screens.*

What looks great on a large desktop screen usually needs some refinement for smaller devices. This typically involves applying smaller font sizes, margins, paddings, column width/stacking, or hiding certain elements on smaller devices.

Bricks provides the following four breakpoints out-of-the-box:

| **Breakpoint** | **@media query** |
| --- | --- |
| Desktop | Base breakpoint |
| Tablet portrait | &lt; 992px |
| Mobile landscape | &lt; 768px |
| Mobile portrait | &lt; 478px |

Styles set on the base breakpoint are inherited by all other breakpoints.

Once you've finished styling a page on the base breakpoint (desktop), make sure to view & adjust the styling on the other breakpoints too.

## Background videos at different breakpoints {#responsive-background-video}

Since Bricks 2.5, background videos on **Section**, **Container**, **Block**, and **Div** elements can use different URLs and playback settings at each breakpoint. Open **Style > Background** on the element or its global class.

Set the video on the base breakpoint, then switch to another breakpoint to change only the settings it needs. The URL, aspect ratio, scale, start and end times, **Play once**, poster, and YouTube/Vimeo options inherit through breakpoints. Inherited settings appear as placeholders; entering a value creates a local override. Clear a local value to use the inherited setting again.

Use **Background video** to choose:

- **Enable**: Play the resolved video at this breakpoint.
- **No video**: Show the element's normal background instead. Set a background image or color if needed.

For example, use a wide video at Desktop, enter a shorter video URL at Tablet portrait, and choose **No video** at Mobile portrait. Bricks loads the matching breakpoint's video and stops the previous video when the breakpoint changes. This applies to uploaded videos, YouTube, and Vimeo.

At Tablet portrait, the video URL is a local override while playback settings such as **Start time (s)** remain inherited:

<div className="screenshot screenshot--control-panel">

![Tablet portrait Background video controls with a local Video URL and an inherited Start time of 0.](https://academy.bricksbuilder.io/assets/builder/release-2.5/video-tablet-panel.webp)

</div>

At Mobile portrait, **No video** leaves the normal background visible:

<div className="screenshot screenshot--control-panel">

![Mobile portrait Background video set to No video.](https://academy.bricksbuilder.io/assets/builder/release-2.5/video-mobile-panel.webp)

</div>

### Existing background videos

Updating Bricks does not activate previously ignored breakpoint-specific video URLs. Existing videos keep their previous output until you intentionally edit a video setting. The first edit switches that element or class to responsive video settings. Bricks uses the previously rendered video and playback behavior as the starting point, then applies your edit.

Older videos may have a **Start play at** restriction. That restriction survives the first edit; changing the legacy video URL alone does not remove it. To allow playback at a restricted breakpoint, explicitly choose **Background video > Enable** there. A poster can still appear below the old playback threshold.

Entering a new URL at another breakpoint also enables video there if it inherited **No video**. Choose **No video** again if you want that breakpoint to keep its normal background.

Class videos are inherited rather than copied into each element. Editing a class video does not switch an element's own untouched legacy video to responsive behavior. Check elements with their own video separately after changing a shared class.

To view & edit the styles for a specific breakpoint simply click on its breakpoint icon located in the center of the builder toolbar. Or use the default [keyboard shortcut](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/) `CMD/CTRL + B`.

![](https://academy.bricksbuilder.io/assets/bricks-1.5.1-in-builder-breakpoint-mobile-landscape-1024x576.jpg)

<figcaption>

Editing in the "Mobile landscape" breakpoint

</figcaption>

Next to the breakpoint icons are inputs for width ("W"), height ("H"), and scale (%).

## Inherited background images {#inherited-background-images}

Since Bricks 2.5, an inherited background image appears as a dimmed preview under **Style > Background**. Its remove button and image-size selector stay hidden until you select an image at the current breakpoint, creating a local override.

## Custom Breakpoints {#custom-breakpoints}

To start using custom breakpoints, you first have to enable them in your WordPress dashboard under `Bricks > Settings > General > Custom breakpoints`:

![](https://academy.bricksbuilder.io/assets/bricks-enable-custom-breakpoints.jpg)

Once enabled, you can access the **breakpoint manager** in the builder by clicking the three-dotted icon in the builder toolbar (next to the first breakpoint icon):

![](https://academy.bricksbuilder.io/assets/bricks-1.5.1-breakpoint-manager-default-breakpoints.jpg)

<figcaption>

Breakpoint Manager (open via the three-dotted icon in the builder toolbar)

</figcaption>

### Editing a breakpoint

Clicking the pencil icon brings up the editing options of the selected breakpoint:

![](https://academy.bricksbuilder.io/assets/bricks-edit-default-breakpoint.jpg)

<figcaption>

Editing the default "Tablet portrait" breakpoint

</figcaption>

You can edit the following breakpoint properties:

| **Property** | **Description** |
| --- | --- |
| Label | Used when hovering over the breakpoint icon in the builder toolbar |
| Width (px) | @media query min-width/max-width value (depending on the base breakpoint) |
| Width (Builder) | Width is used when switching to the breakpoint in the builder |
| Icon | Used as the breakpoint icon in the builder toolbar |
| Base breakpoint | Set breakpoint as base breakpoint |
| *Key* | *Not customizable (used to store & identify breakpoint settings)* |

The most common action is to customize the widths of the default (mobile) breakpoints. The following screenshot shows you the "Tablet portrait" with a custom width of 1023px:

![](https://academy.bricksbuilder.io/assets/bricks-edit-breakpoint-width.jpg)

That means any styles set on the "Tablet portrait" breakpoint will apply to devices with a width of less than 1024px.

### Creating new breakpoints

You can create as many additional custom breakpoints as you want. Although, it is recommended to customize the widths of the default mobile breakpoints to your liking before utilizing more breakpoints.

You should rarely need more than one or two additional breakpoints on top of the default ones.

Clicking the "+" (plus) icon in the breakpoint manager's header launches the breakpoint creator form.

The following screenshot shows how we created a  new breakpoint named "Large" with a width of 1400px:

![](https://academy.bricksbuilder.io/assets/bricks-create-new-breakpoint.jpg)

<figcaption>

Creating a new breakpoint

</figcaption>

Once you click "Create" your newly created breakpoint should appear in the breakpoint manager (alongside a "CUSTOM" label) & in the builder toolbar like this:

![](https://academy.bricksbuilder.io/assets/bricks-custom-breakpoint-large-created.jpg)

<figcaption>

Breakpoint manager with new custom breakpoint

</figcaption>

As we've set the width of this new breakpoint to 1400px, it shows as the first breakpoint, as it is now the largest of our breakpoints. The Desktop (base breakpoint) has a default width of 1279px.

### Pausing a custom breakpoint

You can pause any of your custom breakpoints by toggling the checkbox at the right-hand side of the breakpoint manager:

![](https://academy.bricksbuilder.io/assets/bricks-pause-custom-breakpoint.jpg)

<figcaption>

Pausing custom breakpoint "Large"

</figcaption>

Pausing a custom breakpoint allows you to skip generating the styles for it on the frontend, while still retaining the styles you've set throughout your site without having to delete them one by one. Which, on a full-built-out site, can go into thousands of settings.

### Resetting a default breakpoint

To restore the default values of a default breakpoint, click on the "reset" icon (next to the pencil) icon.

### Resetting all breakpoints

Clicking the "gear" icon in the breakpoint manager header opens up the "Reset: Breakpoints" action. Clicking this button removes all your breakpoint edits (default & custom breakpoints) from the database.

> **Note**
>
> **Breakpoint-specific settings performed on an element or the Theme Styles are not deleted. Please choose desktop or mobile-first at the very beginning.**

![](https://academy.bricksbuilder.io/assets/bricks-reset-all-breakpoints.jpg)

### Understanding the base breakpoint

The base breakpoint doesn't have a @media query. So all styles set on the base breakpoint apply to all screen widths.

That is why, by default, any styles set on the "Desktop" breakpoint are visible on any other breakpoint. Unless you specify a style on a specific breakpoint. Then the breakpoint-specific rule precedes the base breakpoint style.

When editing a breakpoint, you can set it as the "Base breakpoint". Then all styles set on this new base breakpoint are inherited up & down the breakpoint chain.

In the following screenshot, you can see that the "Tablet portrait" breakpoint has been set as the base breakpoint.

The yellow dot, lines, and arrows next to the breakpoint icons should help to visualize the style inheritance:

![](https://academy.bricksbuilder.io/assets/bricks-custom-base-breakpoint.jpg)

<figcaption>

Changed base breakpoint to "Tablet portrait"

</figcaption>

### Mobile-first design {#mobile-first}

Styling in Bricks, by default, happens from the largest breakpoint down to "Tablet portrait" > "Mobile landscape" and "Mobile portrait".

Utilise a so-called `**mobile-first**` design approach by setting the smallest breakpoint as the base breakpoint.

The following screenshot shows the "Mobile portrait" (our smallest breakpoint) set as the base breakpoint. We now use the mobile-first approach. Also indicated by the "MOBILE FIRST" label in the breakpoint manager header:

![](https://academy.bricksbuilder.io/assets/bricks-mobile-first.jpg)

<figcaption>

Mobile-first design in Bricks

</figcaption>

You'll also notice that the order of the breakpoints is reversed and now starts at the smallest breakpoint. You can now start to design your pages starting at the smallest breakpoint.

### Regenerating (Bricks) CSS files

Whenever you customize the width of a default breakpoint, Bricks automatically updates any Bricks CSS files (like frontend.min.css, etc.) that contain media queries for this breakpoint.

If you experience that your breakpoint widths on the front end are not correctly applied, please regenerate your Bricks CSS files by clicking the "Regenerate CSS files" button under `Bricks > Settings > General > Custom breakpoints`.

## Breakpoint data attribute {#breakpoint-data-attribute}

Since Bricks 2.5, the **Breakpoint data attribute** setting exposes the active breakpoint key for use in custom CSS and JavaScript. Enable it under **Bricks > Settings > General > Breakpoint data attribute**, then save your settings. It is disabled by default and works with both default and custom breakpoints.

When enabled, Bricks adds `data-brx-breakpoint` to the page's `<body>` element on the frontend and in the Builder canvas. For example:

```html
<body data-brx-breakpoint="mobile_portrait">
```

The value updates when the viewport crosses a breakpoint boundary.

### Breakpoint keys and matching

The attribute contains one breakpoint key at a time. It uses the smallest matching `max-width` breakpoint or the largest matching `min-width` breakpoint. The base breakpoint key applies only when no other enabled breakpoint matches. Paused custom breakpoints are excluded.

The default keys are `desktop`, `tablet_portrait`, `mobile_landscape`, and `mobile_portrait`. Custom breakpoints use their own keys. Renaming a breakpoint's label does not change its key or the attribute value. Inspect the page's `<body>` element in your browser's developer tools to check the active key.

This value does not list every breakpoint whose styles apply. For example, `mobile_portrait` can be active while the element still inherits styles from the base and larger breakpoints.

### Target a breakpoint in CSS

Add a rule like this to your [custom CSS](https://academy.bricksbuilder.io/builder/features/custom-code/):

```css
body[data-brx-breakpoint="mobile_portrait"] .product-card {
  gap: 0.75rem;
}
```

This rule applies only while `mobile_portrait` is the active key. With the default desktop-first configuration, a selector for `tablet_portrait` does not also match the two mobile ranges. Use a media query when a rule should apply across several ranges.

### Read the active key in JavaScript

After Bricks initializes the page, read the current key with:

```js
const activeBreakpoint = document.body.dataset.brxBreakpoint;
```

This reads the value at that moment. Read it again when your code needs the current breakpoint.

The attribute requires JavaScript and is added during page initialization. It is absent when the setting is disabled or Bricks' JavaScript has not run. Use media queries for styles that must apply before JavaScript runs or when JavaScript is unavailable.

## Responsive control indicator {#responsive-control-indicator}

In Bricks 1.11.1, we introduced the responsive control indicator which helps you see which controls can have different values at different breakpoints. We provide multiple options for when to show this indicator to suit different preferences. You can adjust these under `Bricks > Settings > Builder > Control panel > Responsive control indicator`:

- **Show if any value exists (Default)**: Displays if a control has any value set across breakpoints.
- **Show if non-base breakpoint value exists**: Shows only if a control’s value differs from the base breakpoint.
- **Show on all responsive controls**: Displays on all responsive controls, regardless of values.
- **Disable**.

![](https://academy.bricksbuilder.io/assets/bricks-responsive-control-indicator.png)

---

# Review Links

Source: https://academy.bricksbuilder.io/builder/interface/review-links/

*Share a saved Bricks draft or site version with someone without a WordPress login, set its expiry, and turn access off.*

Review links let a client or teammate view a saved [page draft](https://academy.bricksbuilder.io/builder/interface/drafts/) or [site version](https://academy.bricksbuilder.io/builder/interface/site-versions/) without a WordPress login. They can browse the design, but cannot edit it, publish it, submit forms, or leave comments inside Bricks.

Available since Bricks 2.5. Review links require the experimental Drafts feature and are disabled by default.

## Enable review links {#enable}

In **Bricks > Settings > Builder > Drafts**, enable **Enable drafts**, then **Enable review links**, and save the settings.

To create a link, you must be allowed to edit the draft or site version you are sharing. A link does not give the recipient Builder access.

## Create and copy a link {#create}

1. Open the draft or site version in the Builder and save the changes you want reviewed.
2. Open the version menu before **Save**, then choose **Review links…**. Bricks opens **Versions** with that version selected. Alternatively, use **Manage versions…** and select it from the list on the left.
3. In **Review links** on the right, set **Expires after** to **1 day**, **7 days**, **14 days**, or **30 days**. The default is **7 days**.
4. Click **Create review link**.
5. Click **Copy** and send the generated link to your reviewer.

Copy the link while it is shown. Bricks displays the full link only once; the list retains its expiry and active/inactive status. If you did not keep the link, create another one.

Anyone who receives the link can use it until it expires or is turned off. Share it only with the people who should see the work.

![Review-link controls with a seven-day expiry and active links that can be turned off.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/review-link-settings.webp)

A link opens the saved version, not unsaved canvas edits. Further saves to that version appear when the reviewer reloads or revisits it. Use a separate named site version if another round of edits must stay separate from the work already under review.

## What the reviewer sees {#reviewer}

The link opens the frontend without the WordPress admin bar. A small **Review** panel shows the version name and **Available until** date. **Hide** collapses it; **Show review panel** opens it again.

The reviewer can follow links on the same site while staying in the review. A page-draft link starts on that page; a site-version link starts at the site's homepage. A page draft can be reviewed before its page is published, but the link does not unlock unrelated private or unpublished posts.

**Leave review** returns to the corresponding live URL. An unpublished page may have no public live page to show.

![An anonymous review showing the Atelier North service cards and the Autumn services Review panel.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/review-frontend.webp)

If the version contains alternatives, the panel offers **Explore alternatives**. The reviewer can inspect different combinations and comparisons, but cannot apply one to the draft or record a preferred choice in Bricks. See [Explore Alternatives and Compare](https://academy.bricksbuilder.io/builder/interface/explore-alternatives/).

Review links are view-only, including when opened by a logged-in editor. They do not provide comments, an approval button, or a “choose this version” submission. Collect feedback through your usual email or project conversation. Forms in a review do not submit.

## Expiry and turning links off {#expiry}

Open **Versions**, select the shared draft or version, then find its **Review links** list. **Active until** shows the expiry. Click **Turn off** to stop a link before that date.

The person who created a link, or an administrator who retains access to its version, can turn it off. Create a new link when you need a later expiry; the existing link is not extended.

A link stops working when:

- Its expiry is reached or it is turned off.
- The draft or version is discarded.
- A publish succeeds, including publishing a site version that remains open for further work.
- Its creator loses permission to edit that draft or version.
- Drafts or review links are disabled in Bricks settings.

The recipient then sees **Review link unavailable** and can request a new link. After publishing a site version, create a fresh link for the next review so the old one cannot expose later work.

---

# Revisions

Source: https://academy.bricksbuilder.io/builder/interface/revisions/

*Review, restore, and manage Bricks revisions so you can safely recover earlier builder states.*

Page and template revisions are recovery copies of saved Bricks elements and page settings. [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) and [Site Versions](https://academy.bricksbuilder.io/builder/interface/site-versions/) hold pending changes before publishing.

When you save builder data changes, Bricks creates a revision/snapshot of the relevant Bricks data and page settings (template, page, etc.) using the official WordPress Revisions API.

[Global Data Revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/) recovers individual shared items separately from page and template revisions.

Bricks also stores autosaves separately. Autosaves are backup copies from the autosave process, while regular revisions are created when Bricks element data or page settings are included in a manual save. After a regular revision is created, Bricks clears the related autosave.

To browse, preview, and apply revisions, open **Manage > History / Revisions** from the builder toolbar, then select the **Revisions** tab. Access to revisions requires the **Access revisions** builder permission.

The **History** tab lists recent undo and redo steps from your editing session. The **Revisions** tab contains saved versions and available autosaves, so use it to recover work from an earlier session.

Select any revision in this list to preview it. The canvas should automatically update showing you the selected revision.

Click **Apply** to continue editing the selected revision. Click **Discard** to continue editing your current version.

If your builder capability includes **Delete revisions**, you can delete individual revisions or delete all revisions from the Revisions panel.

![](https://academy.bricksbuilder.io/assets/builder-revisions-1024x576.png)

## Manage the number of Bricks revisions {#bricks_max_revisions_to_keep}

In order to limit the number of Bricks revisions, you may define the constant `BRICKS_MAX_REVISIONS_TO_KEEP` like so (insert this code in the Bricks child theme):

```php
if ( ! defined( 'BRICKS_MAX_REVISIONS_TO_KEEP' ) ) {
    define( 'BRICKS_MAX_REVISIONS_TO_KEEP', 10 );
}
```

By default, Bricks sets the maximum to 100 revisions per post for the Bricks templates and enabled post types.

You may set the following values:

- true: unlimited revisions
- false or 0: do not store any Bricks' revisions
- value above 0: store up to this number of revisions per post. Old revisions are automatically deleted.

---

# Save & Publish

Source: https://academy.bricksbuilder.io/builder/interface/save-publish/

*Understand how saving and publishing work in Bricks, including drafts, updates, and when frontend changes go live.*

Bricks, by default, automatically creates an autosave every 60 seconds when the current builder area has unsaved element changes.

Autosave creates a backup copy of the elements on the canvas. It does not save global data such as components, classes, or variables. Autosaves can be restored under **Manage > History / Revisions** from the builder toolbar.

To adjust or disable the autosave interval go to **Bricks > Settings > Builder** in your WordPress admin area. The default interval is 60 seconds, and the minimum interval is 15 seconds.

Bricks detects unsaved changes and will show you a prompt to help prevent data loss in case you reload the builder by accident.

To manually save your changes, click the **Save** (disk) icon in the builder toolbar or use the default `CMD/CTRL + S` shortcut. Save writes to the version you are editing: Live, a Bricks page draft, or a named site version. In Bricks 2.5, you can change the shortcut under **Manage → Keyboard shortcuts**. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/).

For live page changes, **Bricks creates a revision/snapshot** when changed Bricks data or page settings are saved using the standard WordPress Revisions API ([learn more about revisions](https://academy.bricksbuilder.io/builder/interface/revisions/)). Saving into a Bricks draft keeps pending changes separate from that live-page save.

Customize the save messages with the [bricks/builder/save_messages](https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages/) filter.

## Save pending changes without publishing {#drafts}

Bricks 2.5 offers experimental [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/), disabled by default. Enable **Bricks > Settings > Builder > Drafts > Enable drafts**, then open **Live** beside Save and choose **Save page as draft**. The label follows the post type.

While the switcher shows **Draft**, Save continues saving into that draft. Select **Publish** to review its changes before making them live, or **Discard** to remove its pending changes. On narrower screens, these actions appear in the version menu. Save while **Live** is selected still saves directly to the live version.

Changes to shared items already used on live pages stay in the draft until publication. Reusable items that do not affect live content become available across the site immediately, so you can use a new class on other pages and templates while working. Read [what stays in a draft](https://academy.bricksbuilder.io/builder/interface/drafts/#shared-data) for the full rules and examples.

Use a named [site version](https://academy.bricksbuilder.io/builder/interface/site-versions/) for work across several pages, and [review links](https://academy.bricksbuilder.io/builder/interface/review-links/) to let someone without a login preview pending work.

## Saving shared data from multiple Builder sessions {#save-conflicts}

Since Bricks 2.5, conflict-safe saving is always active for shared data such as global classes, components, Theme Styles, variables, palettes, global queries and filters, and custom fonts. There is no setting to enable it.

If two people edit different shared items, Bricks merges those changes when they save. For example, one person can update a button class while another updates a card component. Saving from an older Builder session does not replace the other person's unrelated update.

If both sessions change the same shared item, Bricks pauses the save and asks which version to keep. This can also happen when you have the Builder open in two tabs. Resolve the conflicts before treating the page or shared-data changes as saved.

### Resolving a conflict

1. In the conflict notification, click **Overview changes** to open **Conflict details**.
2. Select a resource group or expand an item to compare its **Saved version** with **My version**. The saved version is the version currently on the site; your version is the one in this Builder session.
3. Choose which version to keep for each item. The dialog initially selects **Saved version**. Use **All items** only when you want the same choice for every item in the dialog.
4. Click **Use selected**. Resolve any other conflict notifications. After the final conflict is resolved, Bricks retries the save automatically.

![Conflict details comparing the demo global class: the saved typography color is white, while My version uses orange.](https://academy.bricksbuilder.io/assets/builder/save-publish/conflict-details-global-class.webp)

The notification also offers **Use saved version** and **Use my version** for applying one choice to its listed conflicts. Choosing your version can replace another person's work on those items. If you need changes from both versions, agree on the version to keep and reapply the remaining changes afterward.

If another session saves again while you are resolving conflicts, Bricks may ask you to review the updated conflicts. Wait for the save to finish before leaving the Builder.

Conflict-safe saving protects shared data such as global classes and components. It does not merge changes made by two people editing the same page at the same time. Legacy global elements are outside this protection. Autosave still backs up canvas elements rather than shared data, so keep your normal site backups.

## Publishing a WordPress draft post

Saving a page or post whose WordPress status is **Draft** does not publish that post. While editing its **Live** version, use the **Publish** action in the toolbar when it is ready to go public.

If you are editing a Bricks page draft, its **Publish** action first reviews and applies the pending Bricks changes. After returning to Live, publish the WordPress post separately if it is still unpublished. See [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) for the distinction.

---

# Site Versions

Source: https://academy.bricksbuilder.io/builder/interface/site-versions/

*Work on several Bricks pages and shared styles in a named version, review the changes, and publish them together.*

A site version holds a named set of changes across several pages, templates, and shared styles. Use one for work such as a new service offering that changes the homepage, service pages, and their shared components.

Site versions are available in Bricks 2.5 through the experimental [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) feature. Enable **Bricks > Settings > Builder > Drafts > Enable drafts** first. It is disabled by default.

You need Builder access and the WordPress permission to edit other users' posts to create and edit site versions. Your permissions for individual pages, templates, and global resources still apply.

## Create a site version {#create}

1. Open a page in the Builder.
2. Open the version menu just before **Save**. It shows **Live**, **Draft**, or the name of the site version you are editing.
3. Choose **New site version…**.
4. Enter a name, such as `Autumn services`.
5. If you have a draft or site version open, use **Start from** to keep that source or choose **Live**.
6. Click **Create**. Bricks opens the new site version on the current page.

When starting from the open draft or version, Bricks saves its pending edits before copying its saved changes. Starting from **Live** uses saved live data. It does not include unsaved edits on the live canvas. Save those edits first, or put them in a [page draft](https://academy.bricksbuilder.io/builder/interface/drafts/) and create the site version from that draft.

A new version can start with no changes. It does not copy and freeze the whole site: items you have not changed continue to follow live data.

![Creating Autumn services from the open page draft in the Versions dialog.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/site-version-create.webp)

## Work across pages {#work-across-pages}

The toolbar shows the site's version name while you edit it. **Save** writes changes in that context. Open another page through the Builder's page navigation to continue in the same site version. Pending edits are saved before leaving the current page.

Use the version menu to switch between **Live**, this page's **Draft** when one exists, and the available site versions. The checkmark marks the version open in the Builder. Switching from a draft or version saves pending changes first; switching away from unsaved live edits asks for confirmation.

A page draft belongs to one page and its templates. A site version can hold changes from several pages. See [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) for the shared editing rules.

### What stays in the version

Page and template changes stay in the version until you publish them. Changes to shared items already used by live content, such as a card component or a global class, also stay there. Theme Styles, breakpoints, and Style Manager changes are held for publishing.

Reusable items that do not affect live content become available across the site immediately. For example, a new class is available on other pages and templates as you work, without publishing the version. Changes to a class already used by live pages stay in the version until publication. See the [shared-data rules](https://academy.bricksbuilder.io/builder/interface/drafts/#shared-data) for details, including custom CSS that affects other elements.

Media Library changes and personal Builder preferences remain shared too. Save notices identify items shared immediately; the version's **Changes** list shows work still held for publication.

Untouched items keep following the live site. If someone updates a different component while you work, that update remains visible in your version. Publishing a shared style updates every live page using it, including pages you did not edit in this version.

## Manage versions {#manage}

Open the version menu and choose **Manage versions…**. The **Versions** dialog also lists page drafts that you have permission to edit.

The left side contains the creation form and the version list, with page/shared-change counts. Select a name to inspect it on the right. Selecting a row does not switch the Builder into that version, and does not change the source used by **Start from** when creating another version.

The right side contains the selected version's name, owner, update time, actions, **Changes**, and [Review links](https://academy.bricksbuilder.io/builder/interface/review-links/) when enabled. Save your current work before checking this overview; it lists saved changes.

![The split Versions dialog with drafts and named versions on the left, and saved changes and review-link settings on the right.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/site-versions-manager.webp)

| Action | What it does |
| --- | --- |
| **Rename** (pencil) | Edit the selected version's name. Press Enter or leave the field to save; Escape cancels. |
| **Open** | Edit the selected version. A site version opens on the page currently in the Builder. A page draft for another page opens that page. |
| **Compare** | Open a comparison with live over the Builder. For the page you're editing, use **Compare with live** in its version menu. |
| **Preview** | Open the saved version's frontend preview in a new tab. An editor needs permission to view it; use a review link for someone without a login. |
| **Discard version** (trash) | Confirm deletion of the selected version's unpublished changes. It does not undo changes that already went live. |

**Open** is available when the selected version is not already open in the Builder.

**Changes** groups the work under **Pages and templates** and **Shared styles**. It includes available before/after values, such as color swatches. Longer groups show eight changes initially; use **Show all** to expand them. Items already matching live are omitted.

For comparisons, responsive preview widths, and trying several designs, see [Explore Alternatives and Compare](https://academy.bricksbuilder.io/builder/interface/explore-alternatives/).

## Publish a site version {#publish}

Open the site version you want to publish, then click **Publish** beside the version menu. On narrower screens, choose **Publish version…** from the menu instead.

1. Bricks saves pending changes into the version and opens the publish review.
2. Review **Pages and templates** and **Shared styles**. Check the reach of shared changes before continuing.
3. If live content also changed, resolve each conflict with **Your draft** or **The live version**. Page-content conflicts can offer choices for individual elements; independent element changes can be combined.
4. Click **Publish version** and wait for confirmation.

If the version changes again after you review it, Bricks asks you to review the updated work before publishing.

![Publish version review for Autumn services with Your draft and The live version choices for a changed global class.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/site-version-publish.webp)

After publishing, the Builder returns to **Live**. The named site version remains available for more work; changes that were published or settled by keeping live are removed from it. Open it again from the version menu to continue. Existing review links are turned off when publishing succeeds, so create fresh links for any later review.

### Undo a publish

When a publish changes live content, Bricks creates an undo point. Click **Undo** in the published message, or open **Manage versions… > Undo a publish** and confirm **Undo** for the relevant publish. Save or discard unsaved live edits before undoing.

Undo points are kept for 30 days by default. This cleanup period can be changed with [`bricks/drafts/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-drafts-keep_days/). Active editable versions are not removed by that age limit.

Undo points restore the affected live data from before that publish. They are separate from editable site versions. For recovering one shared item without undoing a whole publish, use [Global Data History](https://academy.bricksbuilder.io/builder/interface/global-data-history/).

## Discard a version {#discard}

Open the version and click **Discard**, or select it under **Manage versions…** and use the trash icon. Confirm **Discard version**. If it was open in the Builder, Bricks returns you to Live.

Discarding removes the version's unpublished work and stops its review links. It keeps changes already shared live. When discarding from the toolbar, Bricks can offer **Discard, keep them** or **Discard and delete them** for new shared items that no page, live style, or other open draft uses.

---

# Structure Panel Search and Filters

Source: https://academy.bricksbuilder.io/builder/interface/structure-panel-search/

*Find elements in the Bricks Structure panel by name, text, ID, class, HTML tag, attribute, or dynamic data, and narrow results with filters.*

In Bricks 2.5, search and filters help you find elements in the Structure panel without opening every branch of a large layout. Search for a button's text, find elements using a class, or show elements with conditions or interactions.

## Open the search

<div className="screenshot screenshot--control-panel">

![The Structure search prefix cheat sheet showing searches for element IDs, classes, attributes, HTML tags, and dynamic data.](https://academy.bricksbuilder.io/assets/builder/structure-panel/structure-search-prefixes.webp)

</div>

Use the **Search structure** field at the top of the Structure panel. It appears when the current editing context contains elements.

The default shortcut is `CMD / CTRL + F`. It opens the panel if hidden or minimized and focuses the search. While typing in a field, including the Structure search itself, the same shortcut keeps the browser's normal Find behavior. It also keeps browser Find on an empty page.

You can change or disable **Search structure** under **Manage > Keyboard shortcuts**. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/).

## Search by name or text

Type an element label, element type, or text from its content. Searches ignore capitalization and match part of the text. For example:

- `hero` finds elements labelled Hero.
- `heading` finds Heading elements, including ones you have renamed.
- `get started` finds that text in a button or another supported text field.

Text search includes fields such as accordion and tab titles, list items, pricing features, and form labels and placeholders. It searches stored text settings, not the resolved output of dynamic data or the contents of code and custom CSS.

Paste a complete Bricks element ID, such as `brxe-abc123` or `abc123`, to find that element. Use the `#` prefix for a partial ID or a custom CSS ID.

## Search prefixes

Start a search with one of these prefixes to choose what to search. These are search shortcuts, not full CSS selectors.

| Prefix | Searches | Example |
| --- | --- | --- |
| `#` | Bricks element IDs and custom CSS IDs | `#hero` or `#brxe-abc` |
| `.` | Assigned global classes and custom CSS classes | `.btn--primary` |
| `[` | Custom attribute names or values | `[aria-label` or `[data-track=signup` |
| `<` | HTML tags | `<h2` or `<h` |
| `{` | Dynamic data tags in element settings | `{post_title` or `{acf_` |

IDs, classes, attributes, and dynamic data tags support partial matches. HTML tag search matches from the start of the tag name: `<h` can find `h1` through `h6`, but can also match another tag starting with `h`, such as `header`.

For attributes, `[data-track=signup` requires both the attribute name and value to match on the same attribute. With no `=`, the search checks either the name or value. The closing `]`, `>`, or `}` is optional for attribute, HTML tag, and dynamic data searches.

Use `{post_title` to find an element using that dynamic data tag, regardless of the title it currently displays. Tags inside code or custom CSS are excluded.

Focus the empty search field to see a prefix cheat sheet. Click a prefix to insert it, or use the arrow keys or Tab to reach a prefix button and Enter to activate it.

Classes and attributes require their prefix. If a plain search finds nothing, **Search instead for** may suggest a prefixed search that has results. Click the suggestion to apply it.

## Read and navigate results

Matching elements are highlighted. Their parents stay visible, dimmed and expanded, so you can see where each match sits in the layout. Other branches are hidden from the Structure panel. This does not hide elements on the frontend.

When a match comes from text, an ID, a class, a tag, or an attribute, an excerpt or value appears below the row. Hover over it to see the match type, such as **Global class**.

<div className="screenshot screenshot--control-panel">

![Three buttons matching .btn--primary, with their Hero, Pricing, and Newsletter parent branches visible in the Structure panel.](https://academy.bricksbuilder.io/assets/builder/structure-panel/structure-search-class-matches.webp)

</div>

Use the previous and next buttons beside the result counter to select matches. While the search input has focus:

| Keys | Action |
| --- | --- |
| `Enter` or `CMD / CTRL + G` | Select the next match |
| `Shift + Enter` or `CMD / CTRL + Shift + G` | Select the previous match |
| `Esc` | Clear the search text, or dismiss the open cheat sheet |

Navigation wraps from the last match to the first and keeps focus in the search input. The selected element and its parent path stay visible even if it does not match, so a visible row is not necessarily counted as a result.

## Filter elements

Click the funnel button beside the search field to show the filters.

| Filter | Finds |
| --- | --- |
| Query loop | Elements with a query loop enabled |
| Conditions | Elements with display conditions |
| Interactions | Elements with interactions |
| Custom CSS | Elements with custom CSS in their element settings, including breakpoint or pseudo-class variants |
| Hidden | Elements hidden in the builder or on the frontend, or with an element Display setting of `none` at any breakpoint or pseudo-class |
| Components | Component instances |
| Dynamic data | Elements with dynamic data tags in their settings, excluding code and custom CSS |
| Attributes | Elements with custom attributes |
| Code | Code elements and elements flagged as containing unsigned code |

These filters inspect element settings. **Hidden** does not test computed visibility, and **Custom CSS** does not find every element styled by a global class or stylesheet.

Select multiple filters to find elements matching **any** of them. When you also enter search text, an element must match the text **and** at least one selected filter.

For example, search `.btn--primary` and select **Conditions** and **Interactions** to find buttons using that class that have either conditions or interactions. This helps you locate buttons with behavior to review.

<div className="screenshot screenshot--control-panel">

![Structure search for .btn--primary with Conditions and Interactions selected, showing two matching buttons and the clear-all filters button.](https://academy.bricksbuilder.io/assets/builder/structure-panel/structure-search-filters.webp)

</div>

Click a selected filter to turn it off. The **×** badge on the funnel button clears all filters and keeps the search text. Clearing only the text keeps your filters active. If nothing matches, the **Clear search** button in the empty state clears both.

## Return to the full structure

Clear the search text and all filters to restore the full tree and its previous expanded and collapsed branches. Drag and drop and **Expand/collapse all** are unavailable while search or filters are active.

Search follows the tree for the current editing context. On a page, component instances expose their slots and assigned slot content; open the main component to search its internal elements. Search and filters reset when you enter or leave component editing or navigate to another page in the builder.

---

# Undo, Redo & History

Source: https://academy.bricksbuilder.io/builder/interface/undo-redo-history/

*Preview changes, undo or redo several steps at once, and navigate the History panel in Bricks.*

Use undo and redo to reverse recent edits while working in the builder. The toolbar history menus let you review several changes before applying them. The History panel shows all available steps.

The history menus, feedback messages, and redesigned History panel described here are available in **Bricks 2.5**.

## Undo or redo one change

Click **Undo** or **Redo** in the builder toolbar. Hover over either button to see the next change it will apply, including the element name and action. If no step is available, the tooltip shows **Nothing to undo** or **Nothing to redo**.

The default [keyboard shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/) are:

| Action       | macOS             | Windows / Linux    |
| ------------ | ----------------- | ------------------ |
| Undo         | `Cmd + Z`         | `Ctrl + Z`         |
| Redo         | `Cmd + Shift + Z` | `Ctrl + Shift + Z` |
| Open History | `Cmd + Shift + H` | `Ctrl + Shift + H` |

While typing in a field or editing text inline, undo and redo use the text editor's history. Leave the field or finish inline editing to navigate builder history with these shortcuts.

### Feedback after a change

A brief message identifies the change you undid or redid. Repeated actions in the same direction add to a counter, such as **×3**. The message stays visible while you hover over it and otherwise closes after 2.5 seconds.

The message includes a **Redo** or **Undo** button to reverse one step. This button reverses only one step, even when the counter shows several. Use a history menu to reverse a whole range.

When the affected element is still present, Bricks briefly highlights it on the canvas and in the open Structure panel. An element outside the visible canvas scrolls into view. If the action removed the element, there is no element left to highlight.

## Undo or redo several changes

Click the chevron beside **Undo** or **Redo** to open its history menu. Each menu lists up to 10 available steps in the order they will be applied. Rows show the element or item name, the change, and the elapsed time.

1. Hover over a row to highlight that step and every step above it.
2. Check **Steps to undo** or **Steps to redo** at the bottom of the menu.
3. Click the row to apply the entire highlighted range.

For example, click the third row in the Undo menu to undo your three most recent recorded changes. You cannot undo just the third change while keeping the two changes after it.

Hovering over a row outlines its affected element when it is present on the canvas. It does not apply the change.

<div className="screenshot screenshot--control-panel">

![Undo history menu with three highlighted changes and the summary "Steps to undo: 3".](https://academy.bricksbuilder.io/assets/undo-history-range.webp)

</div>

To use the menu with a keyboard, focus the toolbar's Undo or Redo item and press `Arrow Down`. The first row receives focus. Use `Arrow Up` and `Arrow Down` to change the range, then `Enter` to apply it. Press `Escape` to close the menu and return focus to the toolbar item.

## Use the History panel

Choose **Open history panel** at the bottom of either history menu, or use the Open History shortcut above.

The panel separates available steps into **Redo** and **Undo** sections, with the newest changes at the top of each section. Hover over a row to check the highlighted range and step count before clicking:

- **Undo:** Reverses the selected change and every newer applied change.
- **Redo:** Reapplies the selected change and every earlier change needed to reach it.
- **Start:** Undoes all currently available undo steps.

Clicking an Undo row reverses that row's change too. It does not restore the state after that change. In the Redo section, the range extends through the older redo steps below the selected row.

<div className="screenshot screenshot--control-panel">

![History panel showing Redo and Undo sections, three selected undo steps, and the Start row.](https://academy.bricksbuilder.io/assets/history-panel-ranges.webp)

</div>

### Make a new edit after undoing

If you undo changes and then make a new recorded edit, Bricks discards the redo steps ahead of your current position. You can undo the new edit, but you cannot use Redo to recover the discarded sequence.

## History and saved revisions

History is for recent editing steps. It is limited, and older steps drop out as you continue editing. **Start** means the earliest state still available in history, which may no longer be the state from when you opened the builder.

Reloading the builder or switching to another document resets editing history. Use [Save & Publish](https://academy.bricksbuilder.io/builder/interface/save-publish/) to save your work and [Revisions](https://academy.bricksbuilder.io/builder/interface/revisions/) to restore a saved version or an available autosave.

The History panel's **Delete** action clears the available undo and redo steps after confirmation. It keeps the current design in place; it does not undo the edits or delete saved revisions.
