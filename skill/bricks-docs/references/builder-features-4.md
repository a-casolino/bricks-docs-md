# Popup Builder

Source: https://academy.bricksbuilder.io/builder/features/popup-builder/

*Build popups in Bricks with popup templates, template conditions, popup settings, interactions, limits, AJAX rendering, looping context, JavaScript helpers, and popup events.*

The Popup Builder lets you create fully custom popups in Bricks. A popup is a Bricks template with the template type **Popup**. Bricks renders the popup HTML on the front end, keeps it hidden by default, and opens or closes it through [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/) or JavaScript.

Use popups for modals, newsletter forms, exit-intent offers, quick views, map info boxes, and contextual content in query loops.

## Create a popup template {#create-popup-template}

Create a new template and choose the **Popup** template type.

![](https://academy.bricksbuilder.io/assets/popup-template-type.png)

Save the template, then edit it with Bricks.

Popup templates look different from normal page templates:

- The popup content is centered on the canvas.
- Template Settings includes a **Popup** group.
- The template does not use Populated Content.

![](https://academy.bricksbuilder.io/assets/popup-template-type-screen.png)

Build the popup body like any other Bricks layout: add sections, containers, forms, buttons, icons, images, or dynamic data to the canvas.

## Popup availability and template conditions {#popup-template-conditions}

Template conditions decide where Bricks renders a popup template. Open **Settings > Template Settings > Conditions** and choose the pages where the popup should be available.

![](https://academy.bricksbuilder.io/assets/popup-condition.png)

For example, a newsletter popup that can open from the global footer usually needs a condition such as Entire website. A product quick-view popup may only need to be available on shop or product archive pages.

If a popup is not rendered on the current page, an interaction cannot open it because there is no popup element in the DOM. If a page has **Disable popups** enabled in Page Settings, Bricks does not render page popups.

You can render multiple popup templates on the same page.

## Popup settings {#popup-settings}

Popup-specific settings are under **Settings > Template Settings > Popup**.

![](https://academy.bricksbuilder.io/assets/popup-settings.png)

You can also define global popup defaults in Theme Styles under the Popup control group. Template settings can override those defaults for one popup.

The main popup settings include:

- **Padding**: padding on the popup wrapper.
- **Align main axis** and **Align cross axis**: position the popup content inside the viewport.
- **Close on**: choose Backdrop click, ESC key, None, or the default Backdrop and ESC behavior.
- **Z-index**: controls popup stacking.
- **Scroll (body)**: allow the page body to scroll while the popup is open. If disabled, Bricks adds `no-scroll` to the body while the popup is open.
- **Scroll to top**: scroll popup content to the top when opening.
- **Disable auto focus**: prevent Bricks from focusing the first focusable element inside the popup.
- **Fetch content via AJAX**: render popup content on demand instead of in the initial DOM.
- **AJAX loader**: choose a loader animation and optional selector, color, and scale for AJAX popups.
- **Breakpoints**: choose where the popup is allowed to display.
- **Backdrop**: configure or disable the backdrop.
- **Content**: style the `.brx-popup-content` wrapper.
- **Popup limit**: restrict how often the popup can open.

On the front end, Bricks traps keyboard focus inside open popups, restores focus after closing, supports ESC/backdrop closing according to the **Close on** setting, and emits popup JavaScript events.

> **Note**
>
> Clicking outside the popup or pressing ESC only closes the popup if the **Close on** setting includes that behavior. If you set Close on to None, add your own close interaction or JavaScript.

## Popup interactions {#popup-interactions}

Further down the popup settings panel, the **Interactions** group lets the popup react to events. Popup template interactions use the same interaction system as elements, plus two popup-specific triggers:

- **Show popup**: runs after this popup opens.
- **Hide popup**: runs after this popup closes.

Use these triggers when the popup itself should run follow-up actions, such as starting an animation, setting storage, or updating another element after the popup has opened or closed.

> **Note**
>
> For **Hide popup**, target a CSS selector rather than the popup directly. The trigger runs after the popup has already closed.

Most popups are opened by an interaction on another element. For example, add a Click interaction to a Button, set **Target** to Popup, select the popup template, and use **Show element**.

A common automatic popup uses **Content loaded**:

![](https://academy.bricksbuilder.io/assets/bricks-popup-builder-interaction-content-loaded-465x1024.png)

If no popup interaction exists on the popup itself and no other element interaction opens the popup, the popup stays hidden.

## Popup open and close lifecycle {#popup-lifecycle}

When Bricks opens a popup, it follows this front-end flow:

1. Resolve the popup element by template ID or element node.
2. Check popup limits.
3. Check popup breakpoint rules.
4. Remove the `hide` class.
5. Add `no-scroll` to the body unless body scroll is allowed.
6. Fetch AJAX popup content if the popup is configured for AJAX.
7. Insert AJAX content into `.brx-popup-content`, if content was fetched.
8. Emit `bricks/ajax/popup/loaded`, only for AJAX content that was inserted.
9. Emit `bricks/popup/open`.
10. Increment the popup counters.

When Bricks closes a popup, it adds the `hide` class, removes `no-scroll` from the body if no other non-body-scroll popup is open, and emits `bricks/popup/close`.

This lifecycle matters for custom code:

- Listen to `bricks/ajax/popup/loaded` when you need newly fetched AJAX popup DOM to exist.
- Listen to `bricks/popup/open` when you need the popup to be open.
- Listen to `bricks/popup/close` when you need cleanup after close.

## Popup limit {#limit}

By default, a popup can open every time it is triggered. Use **Settings > Template Settings > Popup > Popup limit** to restrict how often it opens.

Bricks checks limits before opening the popup. Once a limit is reached, the popup does not open and the open event is not emitted.

There are four popup limit controls:

| Limit type | Browser storage | Description |
| --- | --- | --- |
| Per page load | `window.brx_popup_{id}_total` | Resets after the page reloads. |
| Per session | `sessionStorage.brx_popup_{id}_total` | Resets when the browser session/tab storage is cleared. |
| Across sessions | `localStorage.brx_popup_{id}_total` | Persists until local storage is cleared. |
| Show again after hours | `localStorage.brx_popup_{id}_lastShown` | Stores the last shown timestamp and waits the configured number of hours before allowing another open. |

![](https://academy.bricksbuilder.io/assets/bricks-1.6-popup-limit.png)

The page-load, session, and across-session counters increment each time the popup is successfully opened. The hour-based setting stores the last shown timestamp when the popup passes its limit check.

## Popup breakpoints {#popup-breakpoints}

Popup breakpoint settings control whether a popup is allowed to display at the current viewport width.

Bricks supports two modes:

- **Start display at breakpoint**: show the popup at or above the selected breakpoint width.
- **Display on breakpoints**: show the popup only inside the selected breakpoint ranges.

If the current viewport does not match the popup breakpoint rule, Bricks does not open the popup.

## Closing a popup {#closing-popup}

You can close a popup in several ways:

- Use the popup **Close on** setting for backdrop click and/or ESC.
- Add a close icon or button inside the popup and give it a Hide element interaction targeting the popup.
- Use a reusable close element that targets `.brx-popup`.
- Call `bricksClosePopup()` from JavaScript.

### Example: Add popup close icon {#example-close-icon}

Add an Icon element to your popup. Set its cursor to pointer under **Styles > Layout > Misc**.

Open the Icon element's Interactions panel and add:

- Trigger: Click
- Target: Popup
- Popup: the current popup
- Action: Hide element

![](https://academy.bricksbuilder.io/assets/popup-close-icon-interaction.png)

If you want to reuse the same close icon in different popups, create it as a [Component](https://academy.bricksbuilder.io/builder/features/components/). Then use:

- Target: CSS selector
- CSS selector: `.brx-popup`
- Action: Hide element

![](https://academy.bricksbuilder.io/assets/popup-global-close-icon-interaction.png)

## JavaScript helper functions and events {#events-functions}

Bricks exposes popup helper functions and custom events on the front end.

### Open or close a popup via JavaScript {#popup-js-functions}

Use `bricksOpenPopup` and `bricksClosePopup` to open or close Bricks popups.

Both functions accept a popup template ID or a popup element node:

```php
bricksOpenPopup(3321)
bricksClosePopup(3321)
```

```php
const popup = document.querySelector('.brx-popup[data-popup-id="3321"]')

bricksOpenPopup(popup)
bricksClosePopup(popup)
```

### Example: Open popup by selector {#open-popup-by-selector}

```php
document.querySelectorAll('.brxe-heading, .my-custom-selector').forEach((el) => {
  el.addEventListener('click', () => {
    bricksOpenPopup(3321)
  })
})
```

### Listen to popup open or close events {#popup-js-events}

Use `bricks/popup/open` and `bricks/popup/close` to run code when a popup opens or closes.

<span id="bricks-popup-open-close-code"></span>

```php
document.addEventListener('bricks/popup/open', (event) => {
  const popupId = event.detail.popupId
  const popupElement = event.detail.popupElement

  if (popupId == 3321) {
    console.log('3321 popup is opened')
  }
})

document.addEventListener('bricks/popup/close', (event) => {
  const popupId = event.detail.popupId
  const popupElement = event.detail.popupElement

  if (popupId == 3321) {
    console.log('3321 popup is closed')
  }
})
```

Use `event.detail.popupId` and `event.detail.popupElement`. The property is `detail`, not `details`.

## Popup inside query loop {#query-loop}

You can add a popup inside a query loop with the **Template** element. Inside the popup template, dynamic data can reference the current loop item.

The example below shows a Quick View button inside a product query loop. The button uses an interaction to show the selected Quick View popup.

![](https://academy.bricksbuilder.io/assets/bricks-1.6-popup-inside-query-loop-1024x403.jpg)

For Bricks 1.7.1 and newer, Bricks can build loop-specific popup HTML for query loop popups. For older versions, do not set the interaction on the Query Loop div itself; set it on an element inside the loop item.

![](https://academy.bricksbuilder.io/assets/query-loop-popup-template-interaction-structure.png)

<figcaption>

Example layout structure to trigger a looping popup for Bricks versions earlier than 1.7.1

</figcaption>

### Example: Open a looping popup by query element ID and loop index {#open-looping-popup-by-query-element-id-and-loop-index}

If a looping popup is already rendered on the page, you can target it by its query element ID and loop index:

```php
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const queryId = 'vfiqrn'
    const targetPopup = document.querySelector(
      `.brx-popup[data-popup-loop="${queryId}"][data-popup-loop-index="7"]`
    )

    bricksOpenPopup(targetPopup)
  }, 200)
})
```

The small delay is useful in custom code elements because it gives Bricks frontend globals and popup markup time to initialize.

## AJAX popup {#ajax}

AJAX popups were introduced in Bricks 1.9.4. Enable **Fetch content via AJAX** when you want Bricks to keep the initial DOM lighter and fetch popup content only when the popup opens.

This is especially useful for popups inside query loops, where rendering every popup's full content on initial page load can be expensive.

![](https://academy.bricksbuilder.io/assets/ajax-popup-controls-in-popup-template.png)

When AJAX is enabled:

- The popup wrapper is rendered on the page.
- `.brx-popup-content` starts empty outside the builder preview.
- Bricks fetches the content from the REST endpoint when the popup opens.
- Returned HTML and dynamic CSS are inserted into `.brx-popup-content`.
- Additional nested popup HTML can be appended to the body if the AJAX content contains looping AJAX popups.

AJAX popup rendering supports post, term, and user context. Dynamic data that does not have a stable object ID, such as some repeater rows, cannot always be resolved as an AJAX popup context.

### AJAX popup context settings {#ajax-context-settings}

When an interaction opens a popup, Bricks exposes context controls for AJAX popups:

![](https://academy.bricksbuilder.io/assets/context-controls-in-interactions-ui.png)

Bricks tries to infer the current context automatically. Inside normal post, term, and user loops, this often works. In nested query loops, component instances, custom field repeaters, or more complex dynamic data setups, automatic context can be wrong or unavailable.

Use these fields when dynamic data in the AJAX popup renders empty or from the wrong object:

- **Context type**: Post, Term, or User.
- **Context ID**: the object ID to render dynamic data against.

You can use dynamic data such as `{post_id}`, `{term_id}`, or a custom field value that resolves to a post, term, or user ID.

![](https://academy.bricksbuilder.io/assets/example-for-woo-product-quick-view-setup.png)

<figcaption>

A looping product quick-view popup structure in Bricks

</figcaption>

> **Note**
>
> Do not use a repeater row number as popup context. AJAX popup context expects an object Bricks can resolve, such as a post, term, or user.

### Open an AJAX popup with context in JavaScript {#open-ajax-popup}

Since Bricks 1.9.4, `bricksOpenPopup` accepts three parameters:

- `object`: popup ID or popup element node.
- `timeout`: timeout in milliseconds used by popup animation/counter logic.
- `additionalParams`: AJAX popup context data.

```php
bricksOpenPopup(
  1190,
  0,
  {
    popupContextId: 668,
    popupContextType: 'post'
  }
)

bricksOpenPopup(
  2350,
  0,
  {
    popupContextId: 39,
    popupContextType: 'term'
  }
)
```

For users, the Interactions panel usually handles these parameters. Use JavaScript when you are opening popups from custom scripts.

### AJAX popup events {#ajax-events}

AJAX popups emit three AJAX-specific events:

- `bricks/ajax/popup/start`: emitted before the AJAX popup request is made.
- `bricks/ajax/popup/end`: emitted after the AJAX popup request finishes.
- `bricks/ajax/popup/loaded`: emitted after fetched popup content is inserted into the DOM.

Each event uses `event.detail.popupId` and `event.detail.popupElement`.

```php
document.addEventListener('bricks/ajax/popup/loaded', (event) => {
  const popupId = event.detail.popupId
  const popupElement = event.detail.popupElement

  if (popupId == 3321) {
    console.log('3321 AJAX popup content DOM loaded')
  }
})
```

The AJAX popup open sequence is:

1. `bricks/ajax/popup/start`
2. `bricks/ajax/popup/end`
3. `bricks/ajax/popup/loaded`
4. `bricks/popup/open`

`bricks/ajax/popup/loaded` only fires when AJAX content is inserted. Non-AJAX popups emit `bricks/popup/open` directly after opening.

## Popup setup examples {#popup-setup-examples}

### Example: Show popup when the mouse leaves the browser window {#example-mouse-leaves}

After creating the popup template and layout, open **Settings > Template Settings > Popup**, scroll to Interactions, and add a **Mouse leave window** interaction that shows the popup.

![](https://academy.bricksbuilder.io/assets/popup-builder-mouse-leave-open.png)

For a real exit-intent popup, combine this with popup limits or browser storage conditions so the popup does not appear too often.

### Example: Show popup before a date/time {#example-date-time}

Template conditions decide where the popup template is available. Element Conditions can decide whether the popup content renders.

To show a popup only before a specific date, add an [Element Condition](https://academy.bricksbuilder.io/builder/features/element-conditions/) to the outermost popup element.

![](https://academy.bricksbuilder.io/assets/bricks-popup-builder-element-conditions-1536x624.png)

If that condition is not fulfilled, Bricks does not render the popup content and skips the popup HTML. A trigger that targets that popup has no popup element to open on the page.

### Example: Use popup open/close as triggers {#example-popup-open-close-trigger}

Popup template interactions can react after the popup opens or closes.

For example:

1. Open **Settings > Template Settings > Popup > Interactions**.
2. Add a **Show popup** trigger.
3. Set the action to Browser storage: Count.
4. Store a key such as `newsletter_popup_opened`.

You can then use interaction conditions elsewhere to check that key and adjust page behavior.

---

# Remote Components

Source: https://academy.bricksbuilder.io/builder/features/remote-components/

*Share Bricks components between sites, review their dependencies, and import updates from the Component Manager.*

Remote Components let one Bricks site expose selected components and another Bricks site import them from the Component Manager. Use this for component libraries that you maintain across client sites, staging sites, or related projects.

Remote Components are available in Bricks 2.4. Both sites need Bricks 2.4 or later for remote component browsing and dependency-complete imports.

A remote import creates a local component. It does not keep a live connection to the source site, but Bricks records where the component came from so a later import can detect and apply source changes.

## Before You Start

You need:

- A **source site** that contains the components you want to share.
- A **destination site** where you want to import them.
- A non-Plain WordPress permalink structure on the source site.
- Permission to configure Bricks settings on both sites.
- The required [builder permissions](#permissions) for the user importing the component.

## 1. Expose Components on the Source Site

On the source site:

1. Go to **Bricks > Settings > Templates & components**.
2. Under **My components**, enable **My components access**.
3. If needed, choose components under **Exclude components**.
4. Configure the shared **Remote access** controls.
5. Save the settings.

![Remote component access and shared remote access settings in Bricks](https://academy.bricksbuilder.io/assets/remote-components-source-access-settings.webp)

### Exclude Components

Components selected under **Exclude components** do not appear in the remote catalog.

Bricks also blocks the import of any component that depends on an excluded component. For example, if a Card component contains an excluded Button component, the Card may appear in the catalog, but the destination site cannot import it until the Button is allowed or removed from the Card.

### Restrict Remote Access

The **Remote access** settings apply to both remote templates and remote components:

- **Whitelist URLs** allows only the listed destination sites to connect. Enter one URL per line. Leave it empty to allow requests from any site that meets the other access requirements.
- **Password protection** requires destination sites to send the same password. Use the password generator or enter your own value.

Enabling **My components access** without a whitelist or password allows other Bricks sites that know the source URL to browse the exposed component catalog.

## 2. Add the Source to the Destination Site

On the destination site:

1. Go to **Bricks > Settings > Templates & components**.
2. Find **Remote libraries** and click **Add**.
3. Enter the source site's full **URL**.
4. Enter a **Name** to control how the source appears in the builder. This is optional.
5. If the source uses password protection, enter its **Remote access** password.
6. Save the settings.

The same remote-library entry can provide templates, components, or both, depending on what the source site exposes.

![A configured HappyFiles remote library on the destination Bricks site](https://academy.bricksbuilder.io/assets/remote-components-remote-library-settings.webp)

## 3. Browse the Remote Component Library

Open the builder, click the folder icon to open the [Builder Browser](https://academy.bricksbuilder.io/builder/features/builder-browser/), and select **Components**.

Use the **Source** dropdown to switch from **My components** to a configured remote site. Remote libraries appear only when the current user has **Access remote components** permission.

For a remote source, you can:

- Search by component name.
- Filter by category.
- Switch between grid and list view.
- Click **Refresh** to request the catalog again.
- Click **Load more** when the catalog has additional pages.
- View source-provided component thumbnails.

![A HappyFiles remote component library open in the Bricks Builder Browser](https://academy.bricksbuilder.io/assets/remote-components-builder-browser.webp)

If the source cannot be reached or does not support Remote Components, the Component Manager shows the returned source error instead of a component list.

## 4. Review and Import a Component

Click the import icon on a remote component. Bricks first inspects the package and opens a review for the component and any related design-system data.

Save pending component, global class, global variable, and color changes before importing. Bricks blocks the import when these local changes are unsaved so it does not overwrite a newer in-memory design system with an older saved version.

The review can include:

- Nested components.
- Global classes and their categories.
- Global variables, their categories, and variables referenced by other variables.
- Color palettes containing referenced colors.

Matching local dependencies are skipped automatically. You can skip the Global classes, Global variables, or Color palettes step. The skipped group is not added. When you skip global classes, Bricks also removes those class assignments from the imported component. Review the component after using **Skip**.

Referenced images hosted on the configured source site are downloaded to the destination Media Library when the importing user can upload files. Images from other hosts are left unchanged.

![The Global classes step of the remote component import review](https://academy.bricksbuilder.io/assets/remote-components-import-review.webp)

### Name Conflicts

If an unrelated local component already has the same name, Bricks asks for a name for the imported component and suggests one based on the remote-source name. The local component is left unchanged.

Nested components with conflicting names are renamed during the import. Their references are remapped to the imported local copies.

### Previously Imported Components

Bricks tracks each imported component by its remote source and remote component ID.

- If the remote package is unchanged, Bricks reports that the component is already imported.
- If the remote component or one of its nested components changed, the review marks the existing local copy for replacement.
- Replacing a previously imported component keeps its local identity, so existing instances use the updated definition.

Local components that merely share the same name are not treated as previous imports. Provenance, not the label, controls repeat-import behavior.

After a successful import, Bricks returns to **My components**, refreshes the affected components and design-system data, and highlights the imported component.

On a multisite installation configured to use main-site components, the import uses that shared component store instead of creating a separate child-site copy.

Bricks validates the package before writing it and prevents concurrent remote imports. If an import fails after changes begin, Bricks restores the saved component and design-system data.

## What Does Not Transfer Automatically

The package includes the component graph and the referenced Bricks design-system data listed above. Some site-specific features need attention on the destination site.

Bricks shows portability warnings when it detects items such as:

- Query or Global Query settings.
- Icons.
- Executable code.
- Dynamic data.
- Custom fonts.
- Element types that the destination site does not support.

A warning does not always block the import. It tells you to verify the imported component against the destination site's plugins, content model, fonts, icon sets, queries, and code permissions.

Code signatures from the source are not trusted. Bricks removes source signatures and runs imported code through the destination site's normal signing and code-permission flow. Users without code-execution permission receive redacted code-sensitive settings.

### Missing Global Classes

If a component references a global class ID that no longer exists on the source site, the review shows the missing ID and blocks the normal import.

Fix the source component before trying again:

1. Edit the component on the source site.
2. Remove or replace the missing class reference.
3. Save the component and design-system data.
4. Refresh the remote library on the destination site.
5. Import the component again.

Skipping the Global classes step skips every class listed in that step, not only the missing class. Bricks removes those class assignments from the imported component.

## Permissions

Remote component operations combine separate [builder permissions](https://academy.bricksbuilder.io/builder/interface/builder-access/#components):

| Task | Required permissions |
| --- | --- |
| See configured remote sources and browse their catalogs | **Access remote components** |
| Import a component from a remote source | **Access remote components** and **Import/export components** |
| Insert the imported local component onto a page | **Insert components** |
| Insert a remote template that contains components | **Access remote templates**, **Insert templates**, **Access remote components**, **Import/export components**, and **Insert components** |
| Save a remote template to My Templates when it contains components | **Access remote templates**, **Import/export templates**, **Access remote components**, and **Import/export components** |

Administrators have full builder access. Other users need a custom builder capability with the permissions required for their workflow.

## Troubleshooting

### A Remote Site Is Missing From the Source Dropdown

- Confirm the remote library is saved under **Bricks > Settings > Templates & components**.
- Confirm the current user has **Access remote components** permission.
- Reload the builder after saving the settings.

### The Source Loads, but No Components Appear

- Enable **My components access** on the source site.
- Check whether the components are selected under **Exclude components**.
- Confirm the destination URL matches the source whitelist exactly after URL normalization.
- Confirm the destination has the current **Remote access** password.
- Confirm both sites run Bricks 2.4 or later.

### An Import Says the Component Depends on an Excluded Component

Allow the nested dependency under **Exclude components**, or remove that nested component from the component you are sharing. Bricks will not create an incomplete component graph.

### Bricks Asks You to Save Changes First

Save the current component, class, variable, and color changes, then start the import again. If another import changed the saved design system while the review was open, inspect the component again to create a current import plan.

For local component creation, properties, variants, slots, and instance behavior, see [Components](https://academy.bricksbuilder.io/builder/features/components/). For sharing templates between sites, see [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/).

---

# Remote Templates

Source: https://academy.bricksbuilder.io/builder/features/remote-templates/

*Connect Bricks sites, browse shared template libraries, and transfer templates with their component dependencies.*

Remote Templates let you browse and insert templates from another Bricks installation without exporting and importing files manually.

The workflow has two sides:

- The **source site** exposes selected templates through its remote library.
- The **destination site** adds that site under **Remote libraries** and accesses its templates from the Builder Browser.

## 1. Expose Templates on the Source Site

On the site that contains the templates:

1. Go to **Bricks > Settings > Templates & components**.
2. Under **My templates**, enable **My templates access**.
3. Use **Exclude templates** to hide any templates that should not be shared.
4. Configure the shared **Remote access** controls.
5. Save the settings.

![Bricks Templates and components settings with My templates access enabled and Exclude templates visible](https://academy.bricksbuilder.io/assets/bricks-settings-remote-templates-access.webp)

The **Remote access** settings apply to remote templates and remote components:

- **Whitelist URLs** restricts access to the listed destination sites. Enter one URL per line.
- **Password protection** requires destination sites to provide the same password.

If both fields are empty, any Bricks site that knows the source URL can request the templates exposed by **My templates access**.

The source site's WordPress permalink structure must not be set to **Plain**.

![](https://academy.bricksbuilder.io/assets/permalink-structure-not-plain-type-for-remote-templates-01.png)

## 2. Add a Remote Site on the Destination Site

On the site where you want to use the templates:

1. Go to **Bricks > Settings > Templates & components**.
2. Under **Remote libraries**, click **Add**.
3. Enter the source site's full **URL**.
4. Optionally enter a **Name**. Bricks shows this instead of the URL in source dropdowns.
5. Enter the source site's **Remote access** password, if it uses one.
6. Save the settings.

You can add multiple remote sites. The same entry can provide templates, components, or both.

![Remote libraries settings with Name, URL, and Password fields](https://academy.bricksbuilder.io/assets/bricks-settings-remote-libraries.webp)

## 3. Browse Remote Templates

Open the builder, click the folder icon, and select **Templates** in the [Builder Browser](https://academy.bricksbuilder.io/builder/features/builder-browser/).

Choose the remote site under **Source**. You can search the library, filter its templates, switch between grid and list view, and use **Reload** to request the source again.

The current user needs **Access remote templates** permission to see configured remote sites.

![Builder Browser Templates view with HappyFiles selected as the remote source](https://academy.bricksbuilder.io/assets/bricks-browser-remote-templates.webp)

## Insert a Remote Template

Click **Insert** to add the template to the current canvas. The **Replace content** control decides whether Bricks replaces the current canvas or adds the template to it.

Use **Import images** to download eligible template and component images to the destination Media Library. Leave it disabled to use placeholder images where the normal template import flow supports them.

When the remote template includes related design-system data, Bricks may open additional reviews for theme styles, color palettes, variables, global classes, or Style Manager settings.

Remote code signatures are not trusted. Bricks removes source signatures, and users without code-execution permission do not receive executable Code, SVG, or custom-query settings from the remote template.

### Templates That Use Components

In Bricks 2.4 and later, inserting a remote template also requests the components used by that template. The dependency package includes nested components and their referenced global classes, variable categories and variables, and color palettes.

Bricks remaps the template to the imported local component and design-system IDs before inserting it. Save pending component, class, variable, and color changes before starting the insert.

If a component from this source was imported before and changed remotely, Bricks asks whether to replace the local component before inserting the template. Replacing it updates the existing local component definition and its instances.

If the template depends on a component excluded from remote access on the source site, Bricks blocks the dependency package instead of inserting an incomplete component graph.

## Import to Templates

Click **Import to templates** on a non-local template to save it into **My Templates** instead of inserting it directly onto the current canvas.

For a configured Bricks remote site, Bricks first localizes supported component and design-system dependencies, then passes the template through the regular template import flow. The current user needs **Import/export templates** permission.

## Compatibility With Older Remote Sites

Bricks 2.4 introduces a versioned remote-library package for templates with component dependencies.

When a configured source does not support that package protocol, Bricks falls back to the legacy Remote Templates response. The template can still use the older insertion workflow, but the legacy response does not provide the dependency-complete component package. Update the source site before sharing templates that use components.

## Permissions

Remote template operations use separate builder permissions:

| Task                                                                 | Required permissions                                                                                                     |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| See configured remote sites                                          | **Access remote templates**                                                                                              |
| Insert a remote template without component dependencies              | **Access remote templates** and **Insert templates**                                                                     |
| Save a remote template under My Templates                            | **Access remote templates** and **Import/export templates**                                                              |
| Insert a remote template with component dependencies                 | The insert permissions above, plus **Access remote components**, **Import/export components**, and **Insert components** |
| Import a remote template with component dependencies to My Templates | The template import permissions above, plus **Access remote components** and **Import/export components**                |

See [Builder Access & Capabilities](https://academy.bricksbuilder.io/builder/interface/builder-access/) for assigning these permissions.

## Fetching and Caching

Bricks keeps fetched template data outside the WordPress database. Remote template data can be cached in the builder browser for up to seven days per source. Use **Reload** when you need the source again before that cache expires.

Remote-library capability checks and component catalogs use shorter server-side caches. In the Component Manager, **Refresh** bypasses those short caches and requests the source again.

## Troubleshooting

### A Remote Site Does Not Appear

- Confirm the remote library row is saved under **Templates & components**.
- Confirm the current user has **Access remote templates** permission.

### A Remote Site Appears but Does Not Load

Check the source site:

- **My templates access** is enabled.
- Permalinks are not set to **Plain**.
- The destination site's URL is included under **Whitelist URLs**, when used.
- The password saved on the destination matches **Remote access > Password protection**.
- The expected templates are not selected under **Exclude templates**.

### A Template With Components Cannot Be Inserted

- Save pending component, class, variable, and color changes on the destination.
- Confirm the user has the required component permissions.
- Confirm every component dependency is available and not excluded on the source.
- Update the source to Bricks 2.4 or later if it only supports the legacy template response.

For the template library controls and local template actions, see [Template Library](https://academy.bricksbuilder.io/builder/features/template-library/).

---

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

You can use t-shirt sizing, numeric steps, or custom names. Generated variables can be used directly or via utility classes.

Manual mode allows overriding calculated values when precise control is required.

## Spacing

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-spacing-scales-scaled.png)

The Spacing tab generates fluid spacing values for margins, padding, and gaps using the same scale-based system as typography.

This helps enforce consistent layout rhythm across pages.

You can generate utility classes such as `gap-m` or `p-l`, but only generate what you actually use.

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

You can also open and close the Style Manager popup using:

`CMD + .` (macOS)
`CTRL + .` (Windows/Linux)

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

Click the **Import template** icon to import existing template files. You can import a single template as JSON or multiple templates in ZIP format.

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
