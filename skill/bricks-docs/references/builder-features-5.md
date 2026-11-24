# Save Form Submissions

Source: https://academy.bricksbuilder.io/builder/features/save-form-submissions/

*Store Bricks form submissions in WordPress so you can review entries, keep records, and work with the saved data later.*

Bricks 1.9.2 introduced the ability to save Form element submissions in your WordPress database. Once enabled globally, each form can use the **Save submission** action to store entries in a Bricks-managed database table and review them from the WordPress dashboard.

Use this for contact forms, quote requests, event registrations, lead capture, and other workflows where you need a dashboard record in addition to email, webhook, or third-party integrations.

> **Note**
>
> Saved submissions are stored in your WordPress database. Treat them as personal data when forms collect names, emails, IP addresses, files, or account-related information.

## How to enable {#how-to-activate}

Enable **Save form submissions in database** under **Bricks > Settings > General > Form submissions**.

![](https://academy.bricksbuilder.io/assets/bricks-form-submissions-settings.png)

After enabling it, save your settings. Bricks now creates a custom table named `bricks_form_submissions` in your database (plus your WP database prefix).

You should now also see the following action buttons:

- **Reset database table**: Removes all saved submission rows from the table.
- **Delete database table**: Deletes the custom submissions table and disables the global setting.

> **Note**
>
> These actions are permanent. Make sure you have a backup before resetting or deleting the table.

## Form action: Save submission {#save-submission-form-action}

![](https://academy.bricksbuilder.io/assets/save-submission-action-in-form-element.png)

After the global setting is enabled, edit a Form element and select **Save submission** under the **Actions** control group.

In the example below, the form uses **Save submission** and **Email**.

The sequence of your actions matters. If an action fails, execution of all subsequent form actions is halted. Set the order according to your workflow.

In this example, if **Save submission** fails, the **Email** action that follows it will not be triggered.

Bricks always moves the **Redirect** action to the end of the action list during submission processing.

## What Bricks saves

The saved entry includes the submitted form fields and selected metadata:

- The post ID where the form was submitted from, when available.
- The Form element ID. If the form is a global element, Bricks uses the global element ID.
- The submission date in the database.
- Submitted form field data, stored as JSON.
- Browser and operating system, derived from the user agent.
- Referrer URL, when submitted by the form.
- Logged-in user ID, when the submitter is logged in.
- IP address, only when **Save IP address** is enabled for that form.

HTML fields and honeypot fields are not saved as submitted form data.

Bricks sanitizes data before inserting it into the database. For example, email fields are sanitized as email addresses, URL fields as URLs, number fields as numbers, textarea values as post-safe HTML, and most other values as text or URLs.

## Save submission settings

![](https://academy.bricksbuilder.io/assets/save-submission-settings.png)

### Form name

Give your form a unique and descriptive name. This name is used on the **Form Submissions** page in the dashboard. If no name is set, Bricks displays the form as **[No name]** and still identifies it by Form ID.

### Save IP address

Enable this to save the submitter's IP address in the submission entry. Only enable it when you have a clear reason to store the IP address and have updated any required privacy notice.

### Max. entries

Set the maximum number of submissions to store for this form. This is useful for event registration, limited waitlists, and other capacity-based workflows.

When the limit is reached, Bricks returns an error and does not save the new entry. You can customize the error message. Because this is an action error, later actions in the form action list are not executed.

### Prevent duplicates

You can prevent storing duplicate submissions when matching data already exists for the same form.

![](https://academy.bricksbuilder.io/assets/save-submission-prevent-duplicate-for-2-form-fields.png)

Copy the unique six-character ID of the field you want to check, create a new item under **Prevent duplicates**, and paste the field ID into **Compare with (Field ID)**.

If **Save IP address** is enabled, you can use the `ip` keyword to prevent saving more than one submission from the same IP address.

A submission is considered a duplicate only if all configured duplicate checks match an existing entry for that form. Field values are compared case-insensitively after trimming whitespace.

Submissions flagged as duplicates are not saved. A customizable error message appears, and all subsequent form actions are halted.

## Viewing form submissions

To view collected submissions, navigate to **Bricks > Form Submissions** in the WordPress dashboard.

### Overview page

The overview page groups submissions by Form ID and shows each form's name and entry count. This helps you quickly understand which forms have stored submissions.

![](https://academy.bricksbuilder.io/assets/form-submissions-admin-overview-page.png)

The **Delete** button in each form row deletes all entries for that form.

This action permanently removes all submissions for the selected form, so make sure you have a backup or genuinely intend to delete them.

### Individual form submission

Click a form name on the overview page to view all entries for that specific form.

![](https://academy.bricksbuilder.io/assets/form-submissions-single-form-view.png)

The table has one column per form field, using the field label as the column title, followed by metadata columns. **Referrer** links to the page the form was submitted from, which tells you which post an entry belongs to when the form sits in a template.

Click **Screen options** in the top-right corner to toggle metadata columns. Available metadata columns include Date, Browser, IP address, OS, Referrer, and User.

The search box searches the stored form data JSON. It is useful for submitted field values, but it does not search metadata columns such as browser, IP address, OS, referrer, or user.

You can select multiple entries from the list and delete them in bulk. This feature simplifies the process of removing specific submissions, especially if you want to clear out any irrelevant, outdated, or test data.

Click **Download (CSV)** to export all submissions for the form you are viewing.

CSV exports include the visible submission columns and submitted field values. Bricks prefixes cells that could be interpreted as spreadsheet formulas, helping reduce CSV formula-injection risk when exported files are opened in spreadsheet software.

### Form submission access {#access}

Bricks 1.11 introduces more granular control over who can view form submissions on your site. With the new `bricks_form_submission_access` capability, you can specify which user roles or individual users have permission to access form submissions.

Administrators have form submission access by default and cannot be disabled in the role list.

#### User role access

To configure role-based access:

1. Navigate to **Bricks** > **Settings** > **General** > **Form submissions**.
2. Under **Form submission access**, you will see checkboxes for available user roles such as Administrator, Editor, Author, and Contributor.

The **Administrator** role is always enabled by default and cannot be disabled. For other roles, check or uncheck the boxes to grant or revoke access to form submissions.

This allows you to easily control who on your team can view form submissions based on their user role.

#### Individual user access

To configure access on an individual user level:

1. From the WordPress dashboard, go to **Users**.
2. Click to edit a specific user's profile.
3. In the user profile, find and adjust the **Form submission access** setting.

This lets you manage form submissions access for specific users, overriding the broader role-based settings if needed.

Users with form submission access but without broader Bricks admin access can still get a limited **Bricks - Form Submissions** admin menu when submissions are enabled.

Only users who can manage options can reset or delete the whole submissions table, delete all entries for a form from the overview, or delete selected entries in bulk.

## Developer notes

Before saving, Bricks passes the form data through the [`bricks/form/save-submission/form_data`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-save-submission-form_data/) filter. Use this if you need to normalize, remove, or add stored fields before the database insert.

For file fields, the Form Submissions table can link to files saved in the Media Library, the uploads directory, or a custom directory. The file URL used in the submissions table can be adjusted with the `bricks/form/submission-table/file_url` filter.

---

# Search Criteria

Source: https://academy.bricksbuilder.io/builder/features/search-criteria/

*Use Search Criteria in Bricks to control which WordPress fields and meta values are searched for native search and query-filter search inputs.*

Bricks 2.2 introduces a powerful new way to control **how search results are generated**, whether the search is triggered by:

- the **native WordPress search** (via the Search element), or
- the **Filter – Search** element - Query Filters feature.

With **Search Criteria**, you can define exactly where Bricks should search: post fields, assigned post terms, term fields, user fields, and custom meta fields. This gives you far more control than the default WordPress `"s"` search and allows fully customized search behaviour across your site.

> **Note**
>
> Search Criteria does not build or maintain a separate search index. It searches the selected WordPress database fields at query time, caches the matched IDs briefly, and then passes those IDs into the target query.

## Override Native WordPress Search ("s" parameter)

The native WordPress search is usually triggered through the **Search element**, and the results land on the **Search Result template**.

By default, WordPress only searches the following post fields:

- post_title
- post_content
- post_excerpt

If you want to override or extend this behaviour for native search results, configure Search Criteria **inside your Search Result template**.

## Search Criteria in the Search Result Template

![](https://academy.bricksbuilder.io/assets/bricks-search-criteria-search-results-template.png)

Inside the builder, open your **Search Result** template → Template Settings → **Search Criteria** section.

**Custom search criteria**: This reveals all available search settings for controlling how the native `s` search behaves.

**Use weight score (optional):** When enabled, Bricks will calculate a ranking score based on your defined weight values and order the results accordingly. More about [weight scoring](#weight-score).

#### Search Controls

Search post fields - Enable to define which standard WordPress post fields should be searched. Available fields are Title, Content, and Excerpt.

Search post meta fields - You can add any meta key here (custom fields) to include them in your search criteria.

Search post terms - Search assigned terms of selected taxonomies by term name, slug, and description.

Search Result templates only provide post-search criteria, because native WordPress search returns posts. Term and user search criteria are available in the **Filter – Search** element when that filter targets a term or user query.

> **Note**
>
> Make sure the **main Query Loop inside the Search Result template** has **"Is main query"** enabled. Otherwise the native search override will not apply.

Once configured, perform a search on the frontend and your results will follow the criteria defined in the Search Result template. If **Custom search criteria** is enabled but no post fields, meta fields, or taxonomies are enabled, the search has no custom source to search and will return no matches.

## Search Criteria in the "Filter – Search" Element

When [Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/) are enabled in Bricks, you can create advanced filtering systems for any Query Loop on any page.

Before Bricks 2.2, the **Filter – Search** element always used the default WordPress `"s"` logic. Now, you can define custom search criteria per filter element. Inside the Filter – Search element settings, you will now see a **Search Criteria** section.

If the Filter – Search element uses the native WordPress search URL parameter `s`, Bricks expects the search criteria to come from the Search Result template instead of the individual filter element. This keeps the frontend search box, URL parameter, and Search Result template aligned.

> **Note**
>
> Meta field search: ACF, Meta Box, and JetEngine Post Object, Relationship, and User fields usually store IDs in post meta. **Search Criteria searches the raw meta value** and does not automatically resolve those IDs to related post titles, post content, or user display names. To search those labels, store them in a separate searchable text meta field and include that meta key in Search Criteria.

#### Post Query

Search post fields - Enable to define whether to search in Title, Content, and Excerpt

Search post meta fields - You can add any meta key here (custom fields) to include them in your search criteria.

Search post terms - Search assigned terms of selected taxonomies by term name, slug, and description. Useful for product categories, tags, brands, or other taxonomy-based relationships.

#### Term Query

Search term fields - Enable to define whether to search in Name, Slug, and Description.

Search term meta fields - You can add any meta key here (custom fields) to include them in your search criteria.

#### User Query

Search user fields - Enable to define whether to search in Username, Nicename, Email, URL, and Display name.

Search user meta fields - You can add any meta key here (custom fields) to include them in your search criteria.

## How matches are applied

For post queries, Bricks searches the selected sources and sets the matching post IDs on the query. For term and user queries, Bricks sets the matching term or user IDs on the query. If there are no matches, Bricks passes an impossible ID/slug so the target query returns no results.

Search Criteria uses partial `LIKE` matching. For post terms, Bricks searches the assigned term name, slug, and description for each selected taxonomy. For custom meta fields, it searches the raw stored `meta_value`.

Every enabled field, meta key, or taxonomy adds work to the database query. Use the smallest set of searchable fields that matches the frontend experience you need.

## What is "Use weight score"? {#weight-score}

Weight score lets you control the order of your search results. The higher the weight score for a specific search field, the higher the result will appear if that field matches the search term.

> **Note**
>
> Important Notes:
> - You must enable **Use weight score** for ranking to take effect.
> - If a **Sort** filter is active, it will override the weight-score ordering.

#### Example: How weight scoring works

Search Criteria setup:

Search post fields:
- Title → **weight 1**
- Content → **weight 1**

Search post meta fields:
- my_field → **weight 3**

Search term: **car**

Matched posts:

| Post ID | Found in | Weight |
| --- | --- | --- |
| 1001 | Title | 1 |
| 1002 | Title + Content | 1 + 1 = 2 |
| 1003 | my_field | 3 |

**Final result order:**
**1003**, **1002**, **1001**

Weight scores are integer values with a minimum of 1. Matching scores are added together, so an item that matches multiple low-weight fields can outrank an item that matches one field. Bricks preserves the weighted order by ordering the query by the matched ID list. If a Sort filter is active, that sort order takes precedence.

---

# Create Your Own Sidebars

Source: https://academy.bricksbuilder.io/builder/features/sidebars/

*Create and register sidebars for Bricks so widget areas can be placed and styled inside templates and layouts.*

Bricks provides you with its own, built-in sidebar generator. Located in your WordPress dashboard under **Bricks > Sidebars** it lets you to create unlimited sidebars (widgetized areas).

All you need to do is give your sidebar a name and description (optional), and click Create new sidebar.

Once your custom sidebar is created go to **Appearance > Widgets** and drag and drop the widgets of your choice into your newly created sidebar.

You can now add this newly created sidebar inside the builder by dragging the **Sidebar** element onto the canvas.

---

# Style Manager

Source: https://academy.bricksbuilder.io/builder/features/style-manager/

*Use Bricks Style Manager to manage theme styles, classes, variables, colors, spacing, and other design-system primitives in one place.*

The Style Manager is the central place in Bricks for managing design system primitives and reusable styling tools. It brings together theme styles, classes, variables, colors, scales, and imported CSS into a single interface inside the builder.

Its purpose is to centralize styling decisions so you can change colors, spacing, typography, and layout rules in one place without hunting through different panels.

## What the style manager contains

The Style Manager is organized into eight tabs:

1. Theme styles
2. Classes
3. Variables
4. Colors
5. Typography
6. Spacing
7. Framework
8. Settings

---

## Theme styles

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-canvas-preview-fullscreen-scaled.png)

Theme Styles define global default styles for HTML elements and Bricks elements.

Typical use cases include:

- Base typography for headings and body text
- Default button and form styles
- Global colors and spacing
- Responsive defaults
- Global hover and focus states

Theme Styles are condition-based. You can apply them to the entire site, specific templates, or specific pages. They support breakpoints and pseudo-classes, which makes them suitable for defining interaction behavior centrally.

For more: [/builder/styling/theme-styles/](https://academy.bricksbuilder.io/builder/styling/theme-styles/)

## Classes

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-class-manager-scaled.png)

The Class Manager is used to create reusable CSS classes that can be applied to any element.

Use classes when:

- A style is reused across multiple elements
- The style is not a global default
- You want consistent reuse instead of copying values

Classes can be organized into categories, locked, and filtered by usage and status.

Theme Styles define defaults. Classes opt elements into specific behavior.

For more: [/builder/styling/global-class-manager/](https://academy.bricksbuilder.io/builder/styling/global-class-manager/)

## Variables

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-variable-manager-scaled.png)

The Variable Manager is where you define CSS custom properties that act as design tokens.

Variables are commonly used for:

- Colors
- Spacing values
- Font sizes
- Layout dimensions
- Reusable numeric values

Instead of repeating numbers, you reference variables using `var(--variable-name)`. Updating a variable updates every place where it is used.

Variables can be imported from CSS or JSON, grouped into categories, and renamed.

For more: [/builder/styling/global-variables-manager/](https://academy.bricksbuilder.io/builder/styling/global-variables-manager/)

## Colors

![](https://academy.bricksbuilder.io/assets/bricks-2.2-color-manager-scaled.png)

The Color Manager builds structured color systems on top of CSS variables.

Each color is stored as a variable and can optionally:

- Have light and dark mode values
- Generate shade and transparency variants
- Generate utility classes

For more: [/builder/features/color-manager/](https://academy.bricksbuilder.io/builder/features/color-manager/)

## Typography

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-typography-scales-scaled.png)

The Typography tab generates fluid type scales using CSS variables and `clamp()`.

Instead of manually setting font sizes, you define:

- A base size
- A scale ratio
- Minimum and maximum viewport widths

From this, Bricks generates a set of variables that scale smoothly between mobile and desktop.

Typography scales are useful when you want:

- Consistent hierarchy
- Responsive sizing without manual breakpoints
- Fewer arbitrary font-size decisions

You can use t-shirt sizing, numeric steps, or custom names. Since Bricks 2.5, **Numeric (reverse)** generates descending names such as `--h6` through `--h1`. In automatic mode with ratios greater than 1, smaller numbers correspond to larger generated sizes. Generated variables can be used directly or via utility classes.

Manual mode allows overriding calculated values when precise control is required.

For all scale controls and how to use the variables in a theme style, see [Fluid Typography](https://academy.bricksbuilder.io/builder/styling/fluid-typography/).

## Spacing

![Style Manager Spacing tab with a scale named Spacing: prefix space-, scale type T-shirt, baseline step m, minimum and maximum settings, and steps from space-2xs to space-4xl with their minimum and maximum values.](https://academy.bricksbuilder.io/assets/bricks-style-manager-spacing-scale.webp)

The Spacing tab generates fluid spacing values for margins, padding, and gaps using the same scale-based system as typography.

Each value is a CSS variable with a `clamp()` value that grows smoothly between small and large screens, so one variable can replace a padding value and its breakpoint overrides. Set the variables once in a theme style, for example on every section, to keep the spacing consistent across pages.

You can generate utility classes such as `gap-m` or `p-l`, but only generate what you actually use.

For creating a scale, adding steps and using the variables in a theme style, see [Fluid Spacing](https://academy.bricksbuilder.io/builder/styling/fluid-spacing/).

## Framework

![](https://academy.bricksbuilder.io/assets/bricks-2.2-framework-importer-scaled.png)

The Framework tab imports external CSS and converts it into Bricks classes & variables.

It can:

- Parse class rules
- Extract variables from `:root`
- Categorize styles by intent
- Apply prefixes to avoid conflicts

This is mainly useful for:

- Migrating or importing CSS frameworks
- Importing existing custom CSS stylesheets

All imports can be manually reviewed before being added.

## Settings

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-settings-scaled.png)

The Settings tab controls how typography and spacing scales are generated, and which color mode is used by default.

### Color mode

- Light: always start in light mode
- Dark: always start in dark mode
- Auto: follow system preference

### Scale configuration

These settings affect typography and spacing:

- HTML font-size for rem calculations
- Minimum and maximum viewport widths

---

## Interface controls and preview

The Style Manager header includes a full-screen button and a toggle to show or hide the canvas preview per tab.

The canvas preview shows the currently edited page and updates in real time as you make changes. It responds to breakpoint switching and can be resized.

---

## Keyboard shortcuts

You can switch between Style Manager tabs using number keys based on their position.

The default shortcut to open or close Style Manager is:

`CMD + .` (macOS)
`CTRL + .` (Windows/Linux)

In Bricks 2.5, change this combination under **Manage → Keyboard shortcuts**. Number-key tab navigation remains fixed. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/).

---

# SVG Uploads

Source: https://academy.bricksbuilder.io/builder/features/svg-uploads/

*Enable SVG uploads in Bricks, understand the security tradeoffs, and manage SVG assets inside the builder workflow.*

WordPress does not allow SVG file uploads by default because SVG is an XML-based image format that can contain malicious code. SVG files are especially risky when they come from unknown sources or are uploaded by untrusted users.

## How to enable SVG support

You can enable SVG uploads by user role under **Bricks > Settings > General > SVG uploads**.

Bricks only lists roles that can edit posts. When a role is enabled, Bricks grants that role the `bricks_upload_svg` capability and adds `svg` and `svgz` to the allowed upload MIME types for users with that capability.

You can also override SVG upload access for an individual user from the user's WordPress profile. An individual user setting can enable or disable SVG uploads separately from the user's role default.

Once SVG uploads are enabled for a user, Bricks tries to sanitize uploaded SVG files during the WordPress upload process.

> **Note**
>
> No built-in SVG sanitizer can guarantee that every malicious SVG will be made safe. Upload SVG files only from trusted sources, and enable SVG uploads only for users you trust.

## What Bricks sanitizes

Bricks sanitizes uploaded files whose upload type is `image/svg+xml`.

During upload, Bricks:

- Allows `.svg` and `.svgz` uploads for users with SVG upload capability.
- Runs SVG uploads through the `enshrined/svg-sanitize` sanitizer library.
- Minifies the sanitized SVG output.
- Detects gzipped SVG content, decodes it for sanitization, and re-encodes it afterward.
- Blocks the upload with an error message if sanitization fails.
- Removes the forced 1px image dimensions WordPress can assign to SVG attachments.

SVG media uploads are different from the **SVG element > Source: Code** workflow. Pasted SVG source code in the SVG element is treated as executable Bricks code, requires code execution capability, and requires a valid code signature.

## Bypass sanitization {#bypass-sanitization}

Although it is wise to sanitize SVG files uploaded to WordPress, there may be situations where you want to bypass the Bricks SVG sanitizer because another trusted process handles sanitization.

To bypass Bricks SVG sanitization, use the `bricks/svg/bypass_sanitization` filter:

```php
add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
  // Perform your own checks before bypassing Bricks sanitization.

  return $bypass;
}, 10, 2 );
```

Filter callback parameters:

- `$bypass` is a boolean. Return `true` to bypass Bricks sanitization.
- `$file` is the uploaded file array from `$_FILES`.

To bypass Bricks SVG sanitization for every SVG upload:

```php
add_filter( 'bricks/svg/bypass_sanitization', '__return_true' );
```

Only bypass sanitization when you fully control the SVG source or run another trusted sanitizer before the file is stored.

## Sanitizer allowed tags and attributes {#allowed-tags-attributes}

The sanitizer uses the default allowed tags and attributes from the `enshrined/svg-sanitize` library. In some edge cases, you may need to allow additional SVG tags or attributes. In high-security environments, you may want to narrow the allowed lists.

Bricks exposes two filters:

```php
add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    $tags[] = 'filter'; // Allow the "filter" tag.

    return $tags;
} );
```

```php
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    $attributes[] = 'filterUnits'; // Allow the "filterUnits" attribute.

    return $attributes;
} );
```

Use these filters carefully. Allowing extra SVG tags or attributes can reintroduce security risk, especially for attributes that can reference external resources or execute script-like behavior.

## Security checklist

Before enabling SVG uploads:

- Enable SVG uploads only for trusted roles or trusted individual users.
- Upload SVG files only from trusted sources.
- Keep sanitization enabled unless you have another trusted sanitizer in place.
- Review any custom allowed tags or attributes.
- Do not treat media-upload SVG sanitization as protection for SVG element source code; SVG element source code uses the code execution and code signature security model.

---

# Template Library

Source: https://academy.bricksbuilder.io/builder/features/template-library/

*Browse, import, and manage templates from the Bricks Template Library.*

In Bricks 2.4, templates are managed inside the Builder Browser. Open it by clicking the folder icon in the builder toolbar.

You can also press `CMD / CTRL + SHIFT + L` to open the Browser on the Templates view if your user has template access.

All of your own templates are located under the **My Templates** source. You can also browse built-in remote sources such as Wireframes and Design sets, plus any Remote Templates sources configured for your site.

![](https://academy.bricksbuilder.io/assets/docs-template-library-1024x576.png)

<figcaption>

Template Library: My Templates and remote sources

</figcaption>

https://www.youtube.com/watch?v=gbWPw9ebxjQ

## Template Sources {#interface}

In the Templates view, the **Source** dropdown can include:

- **My Templates**: Templates from the current site.
- **Wireframes**: Structural Bricks templates based on classes and variables.
- **Design sets**: Pre-designed Bricks template sets.
- **Remote sites**: Templates from configured remote Bricks installations.

[Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/) allow you to browse templates from any other Bricks installation that you have access to.

## Import Images & Replace Content {#import-images}

The Templates view includes two import controls:

- **Import images**: When enabled, template images are downloaded into your Media Library. Leave it disabled to insert the template with placeholder images.
- **Replace content**: When enabled, Bricks replaces the current canvas with the inserted template. Leave it disabled to insert the template into the existing content.

## Template Filters {#filters}

The Templates view can show these filters:

- **Template Bundle**: Select a template bundle to show only templates that belong to the selected bundle. A template bundle can be a collection of templates of the same website (e.g. home page, contact, about us page, etc.)
- **Template Tag**: Select a template tag to show only templates that have the selected tag assigned to them.
- **Template Type**: Select a template type to show only templates of the selected template type.
- **Search Templates**: Enter any keyword to search for a specific template.

### Sorting templates

Since Bricks 2.5, use **Sort by** in the Templates toolbar to choose **Newest**, **Oldest**, **Title A–Z**, or **Title Z–A**. **Newest** is the default. Combine sorting with the source, search, and filters to find the template you need.

![Templates browser with the sorting menu open, showing Newest, Oldest, Title A–Z, and Title Z–A, with the Import button beside the view toggle.](https://academy.bricksbuilder.io/assets/builder/browser-sorting/templates-browser-sorting-import.webp)

## Template Actions

The Templates view includes action icons for creating, saving, importing, reloading remote sources, generating local template screenshots when available, and switching between grid and list view.

Individual templates can show actions such as insert, edit, export, delete, preview, and **Import to templates**, depending on the source and your builder permissions.

**Import to templates** saves a non-local template under **My Templates**. For a configured Bricks remote site, Bricks 2.4 also localizes component dependencies and their referenced design-system data before continuing through the normal template import flow.

### Create Template {#create-template}

Click the **Create template** icon to create a new template. Enter a title and select a template type. The template bundle is optional. Click **Create template** to create it.

You can also create a new Bricks template from the WordPress dashboard by going to **Bricks → Templates** and click **Add New**. Then give your template a title, select a template type from the meta box on the right side of the editing screen and click **Publish**. Template tags and bundles are optional.

### Save As Template {#save-as-template}

Click the **Save as template** icon to save your current builder content as a template. Enter a title and select a template type. Selecting a template bundle is optional.

To save a specific section as a template hover over a section in the builder. The Edit (pen) icon should appear in the bottom right corner. Hover over it, and click the "disk" icon (Save Section As Template). Give your template section a name and select template type "Section". Then click **SAVE NEW TEMPLATE**.

### Import Template {#import-template}

Since Bricks 2.5, you can open the import dialog directly from **Import** in the Templates browser toolbar. Import requires the **Import/export templates** builder permission. You can also use the existing **Import template** action to import files. You can import a single template as JSON or multiple templates in ZIP format.

Click "Select file(s) to import" and select the JSON/ZIP file from your computer or drag and drop those files into the marked drop zone.

To import templates from the WordPress dashboard go to
**Bricks > Templates** and click **Import Templates**.

Select your template file (JSON/ZIP) from your computer and click **Import template(s)**. Or drag and drop those files into the drop zone.

When imported templates include related data, Bricks may ask you to review imported theme styles, color palettes, global variables, global classes, or Style Manager settings before inserting the template.

Remote templates that use components can also transfer those components, including nested component dependencies. See [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/) for the access, permission, conflict, and compatibility rules.

### Sync Templates

The sync icon is available for non-My Templates sources. It refreshes the selected remote source.

## Export Template(s) {#export-templates}

To export a template, hover over the template title and click **Export Template**. This will generate and download a JSON file with your template data onto your computer.

To export multiple templates at once as a ZIP file, go to **Bricks → Templates** in your WordPress dashboard, and select the templates you want to export.

Now select **Export** from the **Bulk Actions** dropdown, and click **Apply**:

![](https://academy.bricksbuilder.io/assets/file-XTTkSk9tej.jpg)

A ZIP file of your selected templates will be generated and downloaded onto your computer.

This ZIP file contains all templates as individual JSON files. Either unzip it to import individual templates or import the entire ZIP file to bulk import all templates at once.

---

# Template Settings

Source: https://academy.bricksbuilder.io/builder/features/template-settings/

*Use Bricks template settings to control template type, conditions, popup behavior, headers, and other template-level options.*

Template Settings control how a Bricks template behaves as a template. They are separate from element settings and page settings.

Use Template Settings to choose where a template renders, which content appears in the builder preview, how a header behaves, how a popup behaves, how a search template modifies native search, and how a password-protection template protects content.

When editing a template, click the **Settings** icon in the builder toolbar, then open **Template Settings**.

![](https://academy.bricksbuilder.io/assets/builder-template-settings-1024x576.png)

<figcaption>

Toolbar > Settings > Template Settings

</figcaption>

The groups you see depend on the template type you are editing.

| Group | Visible when | Purpose |
| --- | --- | --- |
| Header | Header templates | Controls header location, width, sticky behavior, and scrolling styles. |
| Footer | Footer templates | Enables the footer reveal effect. |
| Popup | Popup templates | Controls popup layout, styling, interactions, AJAX behavior, and popup limits. |
| Search Criteria | Search Results templates | Customizes the native WordPress search criteria for the search results template. |
| Conditions | Most template types | Determines where the template applies. |
| Password Protection | Password Protection templates | Controls password source, password, logged-in bypass, and schedule. |
| Populate Content | Most template types | Controls the builder preview context. |

Product archive and single product WooCommerce templates can use **Conditions**. Other WooCommerce route templates hide **Conditions** and **Populate Content** because WooCommerce controls when those templates are rendered.

## Group: Header {#template-settings-header}

Only available when editing a **Header** template.

Use these settings to control the header area itself:

- **Header location:** default top header, or left/right side header.
- **Header width:** available when the header is placed left or right.
- **Sticky header:** keeps a top header fixed while scrolling.
- **Sticky on scroll:** keeps the header in normal flow on page load, then switches it to sticky after scrolling.
- **Slide up after:** hides the sticky header after the visitor scrolls past a defined distance.
- **Scrolling text color:** changes text/icon color when the sticky header is in its scrolling state.
- **Scrolling text color (hover):** changes hover color while scrolling.
- **Scrolling background:** changes the sticky header background while scrolling.
- **Scrolling box shadow:** adds a shadow while scrolling.
- **Transition:** controls the CSS transition used by sticky header state changes.

Left and right headers also create spacing beside the content and footer. Use them only when the site layout is intentionally built around a side header.

## Group: Footer {#template-settings-footer}

Available when editing a **Footer** template in Bricks 2.5.

Enable **Settings > Template Settings > Footer > Reveal effect** to reveal the footer from behind the page content as visitors scroll to the bottom. The setting is off by default. Save the template, then open a page using that footer on the frontend to see the effect.

<div className="screenshot screenshot--control-panel">

![Template settings of a Footer template with the Footer group open and Reveal effect turned on.](https://academy.bricksbuilder.io/assets/builder/template-settings/footer-reveal-setting.webp)

</div>

The page content in front of the footer needs an opaque background. A transparent background can expose the footer before the visitor reaches the bottom. Place Offcanvas elements and other fixed overlays outside the footer so they can appear above the page content.

The footer returns to normal flow when it is too tall to fit the available viewport, including the space occupied by a fixed WordPress admin bar. Bricks checks this again when the viewport or footer content changes. The effect is also disabled in the Builder, for visitors who prefer reduced motion, while keyboard focus is inside the footer, and when printing.

## Group: Popup {#template-settings-popup}

Only available when editing a **Popup** template.

Popup settings control the popup container and behavior. Depending on your Bricks version and selected options, this includes layout, backdrop, dimensions, position, animation, close behavior, body-scroll behavior, z-index, AJAX rendering, and limits.

Popup templates can also use interactions. The Popup group includes popup-specific interaction triggers such as **Show popup** and **Hide popup**.

When using **Hide popup**, target a CSS selector for the action that should run after the popup closes. Do not target the popup itself for that post-close action.

## Group: Search Criteria {#template-settings-search-criteria}

Only available when editing a **Search Results** template.

By default, WordPress search uses its own criteria. The Search Criteria group lets the Search Results template customize that native search behavior.

Enable **Custom search criteria** to configure:

- **Search post fields:** title, content, and excerpt.
- **Search post meta fields:** custom meta keys.
- **Search post terms:** selected taxonomies, including term slug, name, and description.
- **Use weight score:** assign numeric weights so stronger matches can sort higher.

Every added meta key or taxonomy can affect query performance. Use only the fields that matter for your site search.

For the custom criteria to affect the displayed result list, the main Query Loop in the Search Results template should be configured as the main query.

## Group: Conditions {#template-conditions}

Conditions determine where a template applies on the frontend.

Bricks evaluates conditions against the current WordPress request: single post, page, front page, archive, taxonomy term, search results, 404 page, WooCommerce route, and similar contexts.

You can add more than one condition to a template.

You can choose from the following template conditions:

- **Entire website:** broad condition for the whole site.
- **Front page:** the page configured as the WordPress front page.
- **Post type:** posts, pages, products, or custom post types.
- **Archive:** all archives, post type archives, author archives, date archives, or term archives.
- **Search results:** native WordPress search results.
- **Error page:** 404 pages.
- **Terms:** single entries assigned to selected terms.
- **Individual:** selected posts, pages, custom post type entries, or child pages.

### Condition fields

The fields shown inside each condition depend on the selected condition type.

| Condition type | Extra fields | How it is used |
| --- | --- | --- |
| Entire website | None | Matches every frontend page. |
| Front page | None | Matches the configured WordPress front page. |
| Post type | Post type selector | Matches entries of selected post types. |
| Archive | Archive type, archive post types, archive terms, child terms | Matches archive contexts. Empty archive post type or term fields can mean "all" for that archive subgroup. |
| Search results | None | Matches native search results pages. |
| Error page | None | Matches 404 pages. |
| Terms | Term selector | Matches single entries assigned to selected terms. |
| Individual | Post/page/CPT selector, child pages | Matches selected entries and optionally their child pages. |

### Include and exclude conditions {#exclude}

Every condition can be used as an include or an exclude.

Use include conditions to define where the template should apply. Use exclude conditions to remove a more specific area from a broad condition.

Example:

1. Include **Entire website**.
2. Exclude **Individual > Landing Page**.

The template applies everywhere except the selected landing page.

Exclude conditions can disqualify a template even when another condition matches. This is useful for global headers, footers, and broad Single or Archive templates.

![](https://academy.bricksbuilder.io/assets/template-condition-exclude.png)

When selecting archive terms or individual entries, you can also apply the condition to child terms or child pages.

### Condition specificity

If multiple templates of the same area match the current page, Bricks uses the most specific match.

As a practical guide:

- Individual entries are more specific than child-page matches.
- Front page is more specific than a general post type match.
- Selected terms, selected archives, and child-page matches are more specific than broad archive or post type matches.
- Post type is more specific than Entire website.
- Entire website is a broad fallback.

If the wrong template renders, check for another published template with a more specific matching condition.

### Section hooks

Section templates can be rendered at a WordPress action hook.

When editing a Section template, each condition can expose:

- **Hook: Name**
- **Hook: Priority**

Bricks checks the condition and then renders the section when the hook runs. For example, a Section template with condition **Entire website** and hook name `bricks_before_footer` renders at that hook across the site.

Hook fields are only available for Section templates in the builder.

Since Bricks 2.5, the [`bricks/section_template/run_on_hook`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-section_template-run_on_hook/) filter lets developers change the injection decision after Bricks evaluates the saved conditions. It runs during hook assignment, before the destination action fires.

### Default templates

If no template conditions are set, Bricks can still use published templates of supported types when default templates are enabled.

This setting is in **Bricks > Settings > Templates & components > Disable default templates**.

When disabled, templates need matching conditions or route-specific behavior to render. This makes production template assignment easier to audit.

## Group: Password Protection {#template-settings-password-protection}

Only available when editing a **Password Protection** template.

Password protection templates replace the normal content template when their conditions match and the password gate is active.

Settings include:

- **Password source:** choose **Template & post password**, **Template password**, or **Post password**.
- **Password:** the template-level password. Not available when using only post passwords.
- **Disable for logged-in users:** bypass the gate for logged-in users.
- **Schedule:** optionally set start and end dates.
- **Start date / End date:** UTC+0 schedule fields.

If a Password Protection template uses a template password source but no password is set, Bricks shows a warning because the template will not render as an active password gate.

Older password-protection controls for disabling header, footer, and popups are deprecated. New implementations should use the current password-protection behavior and page/template settings instead of relying on those deprecated controls.

## Group: Populate Content {#template-preview}

Populate Content controls the builder preview context. It does not decide where the template renders on the frontend.

Use it when dynamic data, query loops, archive titles, search results, product data, or page spacing need a real context on the canvas.

Available preview types include:

| Preview type | Extra field | Use it for |
| --- | --- | --- |
| Archive (Recent posts) | None | Blog/archive preview. |
| Archive (Author) | Author | Author archive templates. |
| Archive (Date) | None | Date archive templates. |
| Archive (Posts) | Post type | Post type archive templates. |
| Archive (Term) | Term | Category, tag, or taxonomy archive templates. |
| Single (Post/Page/CPT) | Single entry | Single templates, headers, footers, and layouts that need a real page or post behind them. |
| Search results | Search term | Search Results templates. |

After choosing the content type and related field, click **Apply preview**. Bricks saves the preview setting and reloads the template canvas in that context.

Example: when editing a header, choose **Single (Post/Page/CPT)** and select the homepage or a representative page. This lets you see how the header sits above real content while editing.

WooCommerce cart, checkout, thank-you, and account route templates hide Template Conditions and Populate Content because WooCommerce controls when those templates are used. Product archive and single product templates still use the normal condition and preview controls.

## WordPress admin: template preview image

A template's featured image is used when browsing "My Templates" in the Template Library. You can assign a featured image when editing a template in the WordPress dashboard.

Use preview images to make large template libraries easier to scan. They do not affect frontend output.

## Troubleshooting

**The template does not show on the frontend:** Confirm it is published, has the correct template type, and has matching conditions. If it has no conditions, check whether default templates are disabled.

**The wrong template shows:** Look for a more specific matching condition on another template, or an exclude condition that removes the template you expected.

**Dynamic data is empty in the builder:** Set **Populate Content** to a real context that contains the data you expect.

**Template Conditions are missing:** Check the template type. WooCommerce route templates other than product archive and single product render automatically and do not expose normal conditions.

**Header or footer is missing only on one page:** Open that page and check **Settings > Page Settings > General** for **Disable header** or **Disable footer**.

**A Search Results template does not change results:** Enable custom Search Criteria, configure the fields you need, and make sure the result Query Loop is using the main query.

---

# User activation

Source: https://academy.bricksbuilder.io/builder/features/user-activation/

*Configure user activation in Bricks for registration flows that require email confirmation before an account becomes active.*

Starting with **Bricks 2.1**, you can enable **User activation** for WordPress registrations. Once enabled, newly registered users receive an activation email and must click the activation link before they can log in.

> **Note**
>
> **IMPORTANT: This feature applies to all new user registrations, not just those submitted via the Form element.**

## Quick overview {#quick-overview}

Here is a step-by-step overview of how this feature works once it's enabled.

1. A new user account is created.
2. Bricks stores a generated activation key and marks the user as **pending**.
3. Bricks sends the activation email to the new user's email address.
4. The activation link points to the configured **Verification success page** with `user_id` and `activation_key` query parameters.
5. When the user opens that valid link, Bricks deletes the activation key and marks the user as **active**.
6. If **Auto login after activation** is enabled, Bricks logs the user in after successful activation.
7. If the activation link is invalid, Bricks redirects the user to the configured **Verification failure page**.
8. Pending users cannot log in. Bricks returns an inactive-account login error.

Users created before User activation was enabled do not have activation status meta. Bricks treats them as active.

## Configuration and controls {#configuration-and-controls}

Inside the WordPress dashboard, go to **Bricks > Settings > General** and scroll to **User activation**.

![](https://academy.bricksbuilder.io/assets/bricks-user-activation-settings.png)

**User activation**: Enable this to require new users to verify their email after registration. After enabling it, the rest of the settings become available.

> **Note**
>
> When User activation is enabled, the Form element's registration **Auto log in user** setting is not available. Use **Auto login after activation** instead.

**Auto login after activation**: Automatically logs the user in after successful email verification.

**Verification success page**: The page used for successful activation links. Bricks expects the activation link to point to this page. If the user opens this page without `user_id` and `activation_key`, Bricks simply renders the page normally.

**Verification failure page**: The page users are redirected to when activation fails because the user ID or activation key is missing or invalid.

**User activation: Email**:

- **From email address**: Optional sender email. If empty, WordPress' normal `wp_mail_from` value is used.
- **From name**: Optional sender name. If empty, WordPress' normal `wp_mail_from_name` value is used.
- **Subject**: Email subject. If empty, Bricks uses "Activate your account".
- **Email content**: Email body. If empty, Bricks sends a default activation message.
- **HTML email**: Sends the email as HTML. If enabled and the content is not a full HTML document, Bricks converts line breaks with `nl2br()`.

Available email placeholders:

| Placeholder | Output |
| --- | --- |
| `{{site_name}}` | Site name |
| `{{site_tagline}}` | Site tagline |
| `{{site_url}}` | Site URL |
| `{{username}}` | User login |
| `{{user_display_name}}` | User display name |
| `{{user_first_name}}` | User first name |
| `{{user_last_name}}` | User last name |
| `{{user_email}}` | User email |
| `{{activation_link}}` | Activation URL, or an HTML link when HTML email is enabled |
| `{{activation_url}}` | Plain activation URL |

## Registration behavior

User activation hooks into WordPress' `user_register` flow while the feature is enabled. This means it affects:

- Users registered through the Bricks Form element.
- Users registered through other WordPress registration flows that trigger `user_register`.

For Bricks Form element registrations:

- The registration action still validates username, email, password, password length, and role.
- Administrator and Super Admin roles are blocked as registration targets for security.
- If the username is not mapped, Bricks can generate it from the email address.
- If the password is not mapped or submitted, Bricks can generate one.
- Auto-login after registration is skipped while User activation is enabled.

If **Send WordPress notification** is enabled in the registration form action, Bricks triggers WordPress' `register_new_user` action after creating the user. The activation email is still sent by the User activation feature.

## Activation link behavior

The activation URL is built from your configured **Verification success page** plus two query parameters:

```text
?user_id=123&activation_key=generated_key
```

When the request reaches the success page, Bricks checks those parameters:

- Missing `user_id` or `activation_key`: the success page renders normally.
- Empty `user_id` or `activation_key`: the user is redirected to the failure page.
- Invalid activation key: the user is redirected to the failure page.
- Valid activation key: the account is marked active and the activation key is deleted.
- Already active user: Bricks skips activation and renders the success page normally.

Both the success page and failure page should be published pages.

## Users page {#users-page}

A new **Activation status** column appears on the WordPress **Users** page.

![](https://academy.bricksbuilder.io/assets/bricks-user-activation-admin-column.png)

Possible statuses:

- **Active**: user can log in normally.
- **Inactive**: user has pending activation status and cannot log in until activated.

For each user, you can perform different actions based on their activation status by hovering over the user entry:

For an **active** user, **Mark as inactive** prevents the user from logging in.

For an **inactive** user, **Resend activation email** sends a new activation link using the current email template, and **Mark as active** manually marks the user as active without email verification.

Only users with the WordPress `edit_users` capability can change activation status or resend activation emails from the Users screen.

## Login behavior

When a pending user tries to log in, Bricks blocks authentication and shows an inactive-account error. Users with `active` status, and users with no activation status from before the feature was enabled, can log in normally.

If you also use [Custom Authentication Pages](https://academy.bricksbuilder.io/builder/features/custom-authentication-pages/), the same activation check applies to the Bricks **User login** form action because it uses WordPress authentication.

## Email customization filters

The email settings can also be adjusted programmatically:

- `bricks/user_activation_email/from_name`
- `bricks/user_activation_email/subject`
- `bricks/user_activation_email/content`

These filters are useful for multilingual sites or projects that need different email text per user or context.

---

# Visual Grid Builder

Source: https://academy.bricksbuilder.io/builder/features/visual-grid-builder/

*Design CSS Grid layouts in Bricks with the Visual Grid Builder instead of hand-writing grid-template values.*

https://youtu.be/V-YTXvwg6Fc

The new **Visual Grid Builder **allows you to visually design and manage your grid layouts. The feature is available for any element with the `display` control set to `grid`, and allows you to:

- **Adjust grid size**: Modify the number of columns and rows to fit your design needs.
- **Resize and move elements**: Easily adjust the size and position of elements within your grid through simple drag and drop.
- **Query loop support**: Tweak any query loop item inside your grid.
- **Breakpoint support**: Create different grid layouts for various breakpoints to ensure responsiveness.
- **Rename elements**: Organize your layout by renaming elements for better identification.
- **Edit elements**: Hover over any grid item and click the pencil icon to continue editing it in the element panel.
- **Reset options**: Reset the entire grid or individual elements on the current breakpoint.
- **History**: Use history buttons to go back and forth between changes.
- **Fill grid**: Auto-fill any empty grid cells with one click using Block elements.
- **ID & class level**: Visually design your grid on the element ID or class-level.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-21.17.50@2x-1.png)

<figcaption>

Visual Grid Builder modal

</figcaption>

## How it works {#how-it-works}

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-21.39.14@2x.png)

### Accessing the Visual Grid Builder {#access}

Begin by setting the `display` property of your grid layout element to `grid`. Once activated, the Visual Grid Builder icon appears next to the `grid` value.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-21.43.02@2x.png)

> **Note**
>
> *NOTE: The visual grid builder (icon) is not available when bulk-editing elements.*

### Styling elements

The Visual Grid Builder allows you to style both individual elements and elements that are part of a query loop. The approach to styling depends on whether you are working at the class or ID level. Here’s an overview of how this works:

**Static elements:**

- **ID level**: When you resize or move a static element, the changes are reflected in the `Grid Item` controls, specifically updating the `Grid Column` and `Grid Row` properties. This approach is straightforward and directly modifies the element's grid positioning.
- **Class level**: If you have defined the grid at the class level, any resizing or movement of the element will save the changes as custom CSS. These custom styles are applied to the `Custom CSS` control of the main element.

**Query loop element:**

- **ID or class level**: When working with elements that are part of a query loop, changes to size or position are saved as custom CSS in the `Custom CSS` control of the main element, regardless of whether you are styling at the ID or class level.

**Important**: It is crucial not to alter the auto-generated CSS styles, as they are essential for maintaining the layout's integrity. These styles are clearly marked with code comments, making them easy to identify and preserve. After moving or resizing an element, the CSS will automatically update to reflect the new values. If you choose to reset an element, the auto-generated custom CSS will be cleared, reverting the element to its original state.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-22.04.21@2x.png)

## Controls {#controls}

**Grid actions:**

1. **Reset (Grid)**: Resets all grid styles for the currently selected breakpoint.
2. **Breakpoints**: Toggle between different breakpoints without leaving the editor.
3. **History**: Undo or redo actions.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-22.06.50@2x.png)

**Grid controls: **

1. **Columns and rows**: Adjust the number of columns and rows within the grid.
2. **Gap**: Modify the gap between grid elements using any valid CSS value, including variables.
3. **Use min/max**: Toggle to set column or row size to `minmax(0, 1fr)` for better flexibility.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-22.11.56@2x.png)

When you open the Visual Grid Builder, it will automatically detect and adjust the column and row controls to match your existing grid configuration.

**Grid panel controls: **

1. **Individual Columns and rows**: Precisely control the size of columns and rows.
2. **Elements**: Edit the elements within the grid.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-22.20.35@2x.png)

Sizes aure automatically calculated from your main element settings. For instance, `repeat(3, 2fr)` is converted to `2fr 2fr 2fr`. You can also customize sizes using values like `1fr`, `300px`, or `minmax(0, 1fr)` or any other valid value, to adjust the design to your needs.

**Single element controls: **

1. **Resize**: Click and drag the borders to resize elements.
2. **Move**: Click and drag within the element to reposition it.
3. **Rename**: Click on the element label to rename it.
4. **Reset**: Reset all styling for the element on the current breakpoint.
5. **Edit**: Close the Visual Grid Builder and select the element in the structure panel for further editing.

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-04-04-at-22.31.58@2x.png)

You can also view the index of each element, and if an element is part of a query loop, its specific index within the loop will be displayed, starting at 0.

## When columns or rows cannot be reduced {#grid-reduction}

Since Bricks 2.5, the Visual Grid Builder shows a notice when an item’s placement prevents reducing the number of columns or rows. Items causing the issue are highlighted in orange when identified.

Move or resize those items to fit within the desired grid, then reduce the count again.

---

# Wireframe Templates

Source: https://academy.bricksbuilder.io/builder/features/wireframe-templates/

*Start from Bricks wireframe templates to speed up structure planning before you commit to final styling and content.*

https://youtu.be/B53_o8GfpvQ

## What are Wireframes

Wireframes are premade layouts that allow you to build your templates and pages quickly and effortlessly.

Focusing on structure, layout, and functionality. They contain minimal styling, use placeholder texts, and only represent the overall structure of a specific area on your website such as a section, grid, or card.

Get an overview of all currently available wireframe templates: [https://templates.bricksbuilder.io/wireframes/](https://templates.bricksbuilder.io/wireframes/)

Primarily intended for building new pages, but can also be used in existing websites.

![](https://academy.bricksbuilder.io/assets/Wireframes-Sample-Page-Builder_4.jpg)

Bricks wireframes are based on classes and variables to keep them as flexible, maintainable, and extensible as possible.

In other words, most don't contain styles on the element ID (see [Styling: Classes, IDs and CSS variables](#styling-classes-ids-variables)), but almost every element is assigned a class.

If you have never worked with classes or variables before, we recommend the following free courses and articles:

- [https://www.youtube.com/watch?v=NtRmIp4eMjs](https://www.youtube.com/watch?v=NtRmIp4eMjs)
- [https://www.youtube.com/playlist?list=PL4-IK0AVhVjOT2KBB5TSbD77OmfHvtqUi](https://www.youtube.com/playlist?list=PL4-IK0AVhVjOT2KBB5TSbD77OmfHvtqUi)
- [https://css-tricks.com/a-complete-guide-to-custom-properties/](https://css-tricks.com/a-complete-guide-to-custom-properties/)
- [https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

- [/builder/styling/global-class-manager/](https://academy.bricksbuilder.io/builder/styling/global-class-manager/)
- [/builder/styling/global-variables-manager/](https://academy.bricksbuilder.io/builder/styling/global-variables-manager/)

## Prerequisites

Please enable the necessary settings to use the wireframes to their full extent.

### Required settings

**Bricks > Settings > General:**

1. SVG Uploads (Administrator) must be activated
2. Class Manager & Variable Manager not deactivated

### Optional settings

**Bricks > Settings > Performance:**

1. Disable chaining element & global class

**Bricks > Settings > WooCommerce:**

1. Miscellaneous: Enable Bricks WooCommerce "Notice" element
2. Products: Set Product badge "Sale" to percentage or text
3. Ajax Add to cart: Enable AJAX add to cart

## Types of wireframes

By default, the wireframe templates are organised through **Template bundle**, **Template type**, and **Template tags**.

Use these filters to find the most suitable wireframe template quickly.

![](https://academy.bricksbuilder.io/assets/Wireframes-Sample-Page-Builder_5.jpg)

### Template bundles

Template bundles categorize templates by theme/topic.

The **Blog** bundle, for instance, includes Article/Post layouts along with individual Article Cards, Article Sections, and Article Grids. Similarly, the **FAQs** bundle features individual (FAQ) accordions and FAQ sections.

| **Bundle** |
| --- |
| 404 |
| Avatars |
| Blog |
| Contact |
| Content |
| CTAs |
| FAQs |
| Features |
| … |

### Template Types

A template type is assigned to each wireframe template. The template types are comparable to the [WordPress Template Hierarchy](https://developer.wordpress.org/themes/basics/template-hierarchy/) and let WordPress know what kind of template it is (e.g., a single template for single posts, an archive, a WooCommerce cart, ...).

Using [Template Conditions](https://academy.bricksbuilder.io/builder/features/template-settings/#template-conditions), you can specify in detail where and when most template types are displayed. Section templates are inserted manually unless you assign them to a hook; hook-injected Section templates can still use conditions.

| **Type** |
| --- |
| Header |
| Footer |
| Single |
| Section |
| Archive |
| Popup |
| WooCommerce - Single Product |
| WooCommerce - Account - Orders |
| … |

Additional information: [/builder/features/an-intro-to-templates/#template-types](https://academy.bricksbuilder.io/builder/features/an-intro-to-templates/#template-types)

### Template Tags

Template tags organize the templates according to their function.

| **Tag** | **Tag Description** |
| --- | --- |
| Single | A single element or a small group of elements, such as a custom list, feature card, image/media groups, forms, intros, etc., that can be used anywhere. |
| Grid | A layout grid, usually with CSS grid or flexbox, grouping single templates, e.g., feature cards. |
| Section | A section usually contains one or more grid templates or individual layouts. |
| Template | A fully functional template (see template types) such as a single post/product, archive, header, footer, 404, … |
| Popup | A popup layout is, strictly speaking, a template, too, but it has its tag, so it’s easier to find |

## Template structure and layout

Most Bricks Wireframe templates have a modular structure, i.e., several templates are combined into one template. Imagine a section that contains a grid with various cards. This results in a total of three templates:

1. A card template (tag "Single")
2. A grid template (tag "Grid"), which contains the cards
3. The section template (tag "Section"), which contains the grid template including cards

Each of these templates is available as an individual template.

For example, you can use the card in a different context or place the grid template with cards in a different section ("mix and match").

### Example: "Feature Section 01"

![](https://academy.bricksbuilder.io/assets/Wireframes-Sample-Page-Builder_3.jpg)

"Feature Section 01" contains a total of three templates:

1. Intro 01 (template tag "Single")
2. Feature Grid 01 (template tag "Grid")
3. Feature Card 01 (template tag "Single")

In this case, all templates have the same index (01) because they were created within the same context. You may also see templates with different or no indexes, which is perfectly fine and doesn’t affect how you can use them.

### Example: "Feature Section 04"

If we take a closer look at "Feature Section 04", we can see that the "Content Wrapper" block has no index - "Media Group 04", on the other hand, does.

This means that the content wrapper only applies to this template (Feature Section 04) and does not exist as a separate template. "Media Group 04", on the other hand, exists as a separate template and can, therefore, also be used in different places.

![](https://academy.bricksbuilder.io/assets/Wireframes-Sample-Page-Builder_2.jpg)

### When do I use a section template, and when do I use a grid?

Each page of your website should be divided into sections.

Sections represent, semantically speaking, a new topic. For example, your homepage could contain the following sections: Hero Section, Feature Section, About Us Section, and a CTA or Contact Section.

Make sure to not place sections within sections.

Grid templates are placed within sections. If they belong together thematically, you can put several grids in a section.

A negative example is adding a blog post grid and a product grid to the same section. Both grids should be placed in a separate section because they make no semantic sense together.

### Can I customize the templates and add additional elements or delete elements that are not needed?

Of course, you can customize the templates and add or delete elements you don't need.

It is best to save the customized template in your custom templates so that you can reuse it. If you import the template from the Template Library again, it will not contain the structural changes you have made. However, changes to imported classes or variables will persist across the site unless you delete or override them by re-importing the original class (more on that later).

Remember that the templates are only a starting point and are by no means finished, complete, or 100% suitable for every project. You are welcome to add your own sections, grids, and single templates to adapt them to your project.

## Styling: Theme Styles / CSS Variables / Color Palette Import

When importing a wireframe, you will be asked whether you want to import the associated CSS variables, theme style, and color palette.

### CSS Variables

Since CSS variables are used almost exclusively, importing the variables is strongly recommended for the intended styling. When Bricks asks whether to import the associated variables, choose **Yes** for wireframes unless you intentionally want to map or recreate the variables yourself. You can choose **No** and continue the import, but the wireframe may not look as intended until those variables exist on your site.

### Theme Style

The theme style contains basic settings like responsive font sizes using the default 62.5% HTML font size, section padding, container width, gaps, and others. If you already use a custom theme style, transfer the settings to your theme style (if necessary) and leave the brxwireframes theme style as a reference without a condition. This way, you can always fall back on it in case of doubt. If you are not yet using a custom theme style, don't forget to assign a condition “entire website” to the wireframes theme style.

### Color Palette

In some templates it is necessary to use colors (e.g. for overlays, border-, background- or text-colors). For this purpose, we created 12 neutral color variables (--brxw-color-neutral-xxx), which are also available in a "Bricks Wireframes" color palette. We recommend importing the color palette, as this gives you a visual reference of the [existing variables](#styling-colors) and allows you to quickly assign the colors to other elements.

## Styling: Classes, IDs and CSS variables {#styling-classes-ids-variables}

As mentioned in the introduction, the Bricks wireframes are class- and variable-based to keep them as flexible, maintainable, and extendable as possible.

All classes and CSS variables use `**brxw-**` as a prefix to prevent overlaps with existing classes and variables.

Almost every element within a template is assigned at least one class whose naming convention is based on the [BEM ("Block Element Modifier") methodology](https://getbem.com/).

**Blocks **are independent parent elements. An example could be a card, a menu, or a grid. Block classes only contain hyphens. *Example:* .brxw-article-card-01

**Elements** are the child elements within a block. They are connected to the block by two underscores. *Example:* .brxw-article-card-01__title

**Modifiers** are variants of a block or element that change the status or appearance. Modifiers are connected to the block or element by two hyphens.
*Example:* .brxw-article-card-01--dark.

Block, element, and modifier classes can be easily distinguished based on the spelling alone. However, it may be confusing that BEM uses the terms "block" and "element" just like Bricks. If you need clarification, just remember this: BEM Block classes can be used on all Bricks parent elements - it doesn't matter if the parent element is a Bricks block, div, section, container, nav menu, or icon list.

BEM element classes are applied to Bricks elements within a BEM block, regardless of which Bricks elements you use.

### Example: Article Card 01

| **Block Class** | **Element Classes** |
| --- | --- |
| .brxw-article-card-01 | .brxw-article-card-01__body |
|  | .brxw-article-card-01__title |
|  | .brxw-article-card-01__taxonomy |
|  | .brxw-article-card-01__text |
|  | .brxw-article-card-01__footer |
|  | .brxw-article-card-01__date |
|  | .brxw-article-card-01__author |
|  | .brxw-article-card-01__media-wrapper |
|  | .brxw-article-card-01__media |

### Important to know:

- **Not all blocks must have children - they can exist independently**
- **Blocks can have other blocks as children**
*Example:* The section element in the “Article section 04 template” is an independent block (.brxw-article-section-04) and contains two different blocks: .brxw-intro-02 and .brxw-article-grid-04, which in turn have children.
- **Elements cannot exist without a parent block.**
*Example:* .brxw-intro-02__title cannot exist without its parent block .brxw-intro-02

#### When do I style on the existing brxw-classes, when on custom classes, and when on the ID?

You should consider carefully where and how often you want to insert the relevant template. There are different possibilities depending on this.

For templates that are used multiple times (e.g., a section placed various times, cards in a loop, etc.), styling on classes (brxw- or custom) is preferable to ID styling, as the CSS ID must be unique and may, therefore, only occur once per page.

##### Existing brxw-classes

Styling on the existing brxw-classes is the standard method for giving the elements the desired styling. You can also adjust the values, such as the number of grid columns within the templates, to your needs - they are not set in stone.

If you import the same template again from the Template Library elsewhere, it will automatically receive the same styling and the exact customizations that you have applied to the brxw-class.

##### Custom classes

In addition to the brxw-classes, you can add custom classes containing your custom styles. In most cases, this also makes it possible to overwrite the existing values of the brxw-classes.

However, if you insert the same template elsewhere from the Template Library, you must add your custom classes manually, if desired. Alternatively, you can save the customized template including the custom classes in your templates to reuse it later.

##### IDs

Sometimes, you can use the ID to style your elements or to overwrite class styles.

Imagine you place the same section template twice on your homepage. You select the section class and assign it a background color that applies to both sections accordingly. To "exceptionally" give the second section a different background color, you can style on the section ID to overwrite the class.

**Remember:** IDs always have a higher specificity than classes. Accordingly, it is impossible to overwrite an ID style with a class but the other way around. If you re-import the same template from the Template Library, the section will not contain any ID styles but will include the changed class styles.

#### Can I rename the existing classes?

You can rename the `brxw-` classes if you wish. However, remember to do this for the block and contained element classes of the child elements, if available ([Class Manager](https://academy.bricksbuilder.io/builder/styling/global-class-manager/)).

If you import the same template again, it will use your class names and style changes. However, this also means you cannot re-import the original template unchanged.

Suppose you want to retain the option of re-importing the original template **without** changes to the class name or styles. In that case, it is not enough to rename the classes, as they still have the same ID in the database, i.e., the same unique identifier. In this case, you would have to duplicate the classes ([Class Manager](https://academy.bricksbuilder.io/builder/styling/global-class-manager/)) so that they each have a new, unique identifier, reassign them to the elements, and remove the "old" classes from the elements.

#### I have accidentally deleted a brxw-class. Can I restore it?

Yes. In the first step, look in the Class Manager’s trash (top right), and if the class is still there, you can restore it directly.

If you have emptied the trash, you can simply re-import the template.

In both cases, remember to reassign the class to the elements on which it is missing, as it will be removed from the elements as soon as it is deleted.

### CSS variables

If values are assigned to a `brxw-` class (or theme style settings), the values are defined as CSS variables, with few exceptions. You can find the variables and values in the [Global Variables Manager](https://academy.bricksbuilder.io/builder/styling/global-variables-manager/).

![](https://academy.bricksbuilder.io/assets/Variable-Manager.png)

CSS variables offer the advantage of reusability, flexibility, and easy maintenance of styles, as they define central values that all elements in the CSS can use. For example, if you want to increase or decrease the gap of your grids, you only need to adjust the value of the variable `–brxw-grid-gap`. The change now affects every grid in which the variable is used.

#### Variable categories

The available variables cover essential areas such as CSS grids, font sizes, spacing, gaps, border radius, and others, which are sufficient for the "start" of a project. If you need additional categories or variables, you can create them as per your requirements in the variable manager.

| **Variable Category** | **Examples** | **Purpose** |
| --- | --- | --- |
| Grids | –brxw-grid-1, –brxw-grid-2, …, –brxw-grid-12 | Used within CSS Grids to set the number of columns |
| Spacing | –brxw-space-xs, –brxw-space-2xl, … | Used within margins, paddings, widths, heights, gaps, … |
| Typography | –brxw-text-xs, –brxw-text-m, –brxw-text-2xl | 9 (fluid) font sizes from xs to 5xl |
| … |  |  |

#### Variable values

The brxw-variables use [CSS clamp functions](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp) for font sizes, spacing, and border-radius, which calculate the value based on a minimum, preferred, and maximum value depending on the viewport (minimum/maximum width). This has the advantage that you do not manually adjust the font size or padding in the mobile breakpoint, for example, as it is automatically adjusted (reduced or enlarged).

As a basis for this calculation, the wireframe templates assume a minimum viewport of 320px, and a maximum viewport of 1440px, which should be a good starting point for typical websites.

#### I already use a framework and CSS variables (e.g., ACSS, Frames, or CoreFramework). Can I continue to use my variables?

Of course, you can continue to use your existing variables. However, remember that the values of your variables will probably differ from those of the brxw-variables.

As there is a lot of overlap with other frameworks, you can use your existing variables as the brxw-variable value. This allows you to adapt the wireframe templates to your existing layout and spacing without editing each template.

##### Example ACSS

| **ACSS Variable** | **brxw-Variable** | **Extended brxw-variable** |
| --- | --- | --- |
| --container-gap: var(--space-xl) | --brxw-container-gap: var(--brxw-space-2xl) | –brxw-container-gap: var(--container-gap) |
| --grid-gap: var(--space-l) | --brxw-grid-gap: var(--brxw-space-l) | –brxw-grid-gap: var(--grid-gap) |
| –space-m: clamp(2rem, calc(1.09375vw + 1.65rem), 3.4rem) | –brxw-space-m: clamp(1.6rem, calc(0.36vw + 1.49rem), 2rem) | –brxw-space-m: var(--space-m) |
| –h2: clamp(2.592rem, calc(1.725vw + 2.04rem), 4.8rem) | –brxw-text-fluid-3xl: clamp(2.56rem, calc(1.04vw + 2.23rem), 3.73rem) | –brxw-text-3xl: var(--h2) |
| … |  |  |

##### Example Core Framework

| **Core Framework Variable** | **brxw-Variable** | **Extended brxw-Variable** |
| --- | --- | --- |
| --space-m:clamp(1.6rem, calc(1.11vw + 1.24rem), 2.8rem) | --brxw-space-m: clamp(1.6rem, calc(0.36vw + 1.49rem), 2rem) | –brxw-space-m: var(--space-m) |
| --radius-m: clamp(1rem, calc(-0.19vw + 1.26rem), 1.2rem) | –brxw-radius-m: clamp(1rem, calc(-0.18vw + 1.26rem), 1.2rem) | –brxw-radius-m: var(--radius-m) |
| … |  |  |

##### Custom responsive variable values (clamp)

If you want to use other viewport sizes (instead of 320px min, 1440px max), all variable values that use clamp /Fluid Typography, Spacing, Radius) must/should be customized/regenerated.

We do not recommend doing this manually (unless you are a math genius). Instead, you can use the built-in **Fluid Typography Scale Generator** located in the Variable Manager to create new text or spacing variables. The radius variables were created with CoreFramework (free) because they are not based on a base value but should have individual min and max values.

![](https://academy.bricksbuilder.io/assets/Fluid-Variables.png)

Alternatively, you can use generators that provide you with the ready-made clamp functions. Depending on which generator you use, you can adjust the variable name/prefix directly in the generator, or you have to do this later in a code editor of your choice.

All generators mentioned are currently (September 2025) free of charge and are not affiliated or connected with Bricks:

1. [fluid-type-scale.com](https://www.fluid-type-scale.com/calculate?minFontSize=16&minWidth=320&minRatio=1.25&maxFontSize=18&maxWidth=1440&maxRatio=1.333&steps=xs,s,m,l,xl,2xl,3xl,4xl,5xl&baseStep=m&prefix=brxw-text&useContainerWidth=false&includeFallbacks=false&useRems=true&remValue=10&decimals=2&previewFont=Inter&previewText=Almost+before+we+knew+it,+we+had+left+the+ground&previewWidth=1280)
2. [utopia.fyi](https://utopia.fyi/type/calculator/?c=320,16,1.25,1440,18,1.333,4,2,&s=0.75%7C0.5%7C0.25,1.5%7C2%7C3%7C4%7C6,s-l&g=s,l,xl,12)
3. [coreframework.com](https://coreframework.com)

## Styling: Color Palettes {#styling-colors}

Most wireframes do not contain any colors unless absolutely necessary or beneficial (e.g., overlays, borders, backgrounds, text-colors). For this purpose, we have created a neutral color palette (shades of grey) with 12 color-steps from light to dark, which can be imported during template import.

The colors are defined in CSS variables, located in the Variable Manager (--brxw-color-neutral-25, --brxw-color-neutral-50, --brxw-color-neutral-100, ..., --brxw-color-neutral-950) and can be adjusted there. If you don't want to use any predefined colors at all, delete the color variables from the variable manager.

There are various free generators for creating custom color palettes (to add primary or secondary colors, or change the existing neutral color values). We have had good experiences with these generators, for example:

- [https://components.ai/color-scale/rnjyBVIn24NiNNH0ob2W](https://components.ai/color-scale/rnjyBVIn24NiNNH0ob2W)
- [https://uicolors.app/create](https://uicolors.app/create)

## Custom CSS / JS / Code

### Custom CSS

We try to avoid custom CSS. However, some layouts or customizations would not be possible without it.

### Custom JS / Code

Custom JS or PHP is only used if the use case requires it. We've commented the code used in as much detail as possible. When using a template with a Code element, remember to enable code execution and sign the code.

## Frequently asked questions

- **Why are there no wireframes for Category X or Y?**
  - Bricks is designed to give you the flexibility to create exactly what you need. New wireframes may be added over time, but you can also create your own wireframes for any category or design.
- **Can I request new wireframes?**
  - Of course! We’re always open to hearing your ideas. While we can't guarantee every suggestion will be implemented, your input helps us better understand what’s important to the community. Feel free to contact us by email (subject: "Wireframes") or share your suggestions in the forum under the Feature Requests/Improvements category (prefix your title with "Wireframes").
- **Who can I contact if I have found a potential bug?**
  - Please contact us by email (subject "Wireframes") or create a new report in the forums bugs category (title prefix: "Wireframes"). Please tell us the name of the template and the issue in as much detail as possible.

Happy wireframing!
