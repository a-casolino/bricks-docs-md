# Color Manager

Source: https://academy.bricksbuilder.io/builder/features/color-manager/

*Manage saved colors in Bricks with Color Manager so you can organize, reuse, and maintain consistent color values.*

The Color Manager is where you create and maintain the reusable colors for a Bricks site. Use it to turn repeated color values into a color system: named variables, optional dark-mode values, generated shades, and utility classes that can be reused throughout the builder.

Instead of setting isolated hex, RGB, or HSL values on individual elements, save the color once and then select it from color controls. When you later update the saved color, every control that references that color can use the updated value.

https://youtu.be/u8p8olaPXY8

## How Color Manager works

Color Manager stores colors in palettes. A palette is a named group of colors, and each color has:

- A generated internal ID.
- A CSS variable name, such as `var(--primary)` or `var(--brand-blue)`.
- A light-mode value, such as `#0057ff`, `rgb(0, 87, 255)`, or `hsl(220 100% 50%)`.
- Optional dark-mode value.
- Optional generated shade entries.
- Optional utility-class settings.

Bricks outputs color palette values as CSS custom properties. Modern Color Manager colors use the variable name you provide, so a color named `primary` is output as `--primary`. Older saved colors can still use the legacy `--bricks-color-{id}` variable format until you convert them.

Dark-mode values are output separately under `:root[data-brx-theme="dark"]`. Utility classes and Color Manager variables are also written into the generated Style Manager CSS file, so utility classes can be used consistently on the frontend.

> **Note**
>
> Color Manager access depends on the **Access color manager** builder permission. Users without this permission cannot open the Color Manager or manage palettes from color controls.

## Getting started

To access the Color Manager:

1. Open the builder
2. Click the **Styles** icon in the builder toolbar (or press `CMD + .` / `CTRL + .`) to open the Style Manager
3. Open the **Colors** tab

![](https://academy.bricksbuilder.io/assets/bricks-2.2-color-manager-scaled.png)

On a new site, the Colors tab shows a palette named **Default** with generic variable names such as `var(--bricks-color-grey-100)`. To use names that fit your project, create your own palette. A new, empty palette asks you to add its first color.

## Palettes

A palette is only an organizational group. It does not limit where colors can be used. Any saved palette color can be selected from color controls throughout the builder.

### Create a palette

1. Click the **Add Palette** button (plus icon)
2. Enter a palette name, such as `Brand`, `Neutral`, or `Client colors`
3. Click **Create**

### Select, rename, and delete palettes

- Use the palette dropdown to switch between palettes.
- Click the edit icon to rename the active palette.
- Click the trash icon while editing the palette name to delete it.

Deleting a palette removes the saved colors in that palette. Existing element settings that referenced deleted colors may no longer resolve to the expected palette value, so review important templates before deleting a production palette.

Bricks remembers the last active palette in your browser, so the same palette is selected the next time you open Color Manager on that machine.

## Adding colors to your palette

Each saved color needs a variable name and a color value.

1. Open a palette.
2. Enter a variable name, such as `primary`, `surface`, or `brand-blue`.
3. Enter a color value or choose one from the color picker.
4. Click **Add color**.

You can enter the variable name as `primary`, `--primary`, or `var(--primary)`. Bricks normalizes it to `var(--primary)`. If you leave the variable name empty, Bricks generates a variable name in the `var(--bricks-color-{id})` format.

Bricks blocks duplicate variable names across Color Manager palettes and Global Variables. This prevents two different tokens from fighting for the same CSS custom property name.

### Editing existing colors

Click the edit icon on a color to edit its variable name, light value, dark value, shades, or utility classes.

To see a change on the page while you edit, turn on **Toggle canvas preview** (eye icon) in the Style Manager header. The canvas preview appears next to the palette and updates as soon as you change a color value.

When you rename a color variable, Bricks also updates the generated shade variable names for that color. For example, if `var(--primary)` has light shades, those shades use names such as `var(--primary-l-1)`. Renaming the base variable updates those shade names to match.

### Adding a color from a color control

Color controls include a palette popup. When a control has a custom value, users with Color Manager access can add that current value to the active palette directly from the color control.

This is useful when you discover a useful color while designing, but the better long-term workflow is to create intentional color names in Color Manager and then select them from the palette.

## Selecting palette colors in controls

Most color controls can open the color palette popup. The popup lets you:

- Choose the active palette.
- Switch between list view and grid view. List view shows each color's variable name and value, with its generated shades below it.
- Select root colors and generated shades.
- Add the current color value to a palette if you have permission.
- Open Color Manager from the settings icon if you have permission.

When you select a palette color, the element stores a reference to that saved color instead of only storing a raw color value. This is what lets later palette edits update the visual result across the site.

If a saved color cannot be found anymore, Bricks can no longer resolve that palette reference. This usually happens when a color or palette was deleted after being used.

## Using dark mode

Dark mode lets a single color variable use one value in light mode and another value in dark mode.

1. Click the "Edit" icon on any color
2. Enable **Dark mode**
3. Adjust the generated dark value or enter your own
4. Save the builder when you are done

When you enable dark mode, Bricks generates an initial dark value from the light value. Treat that value as a starting point, not as final design guidance. Review contrast manually, especially for text and interactive states.

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-color-manager-dark-mode-scaled.png)

When you disable dark mode for a color, Bricks asks for confirmation and removes the dark value. Dark-mode shade values for that color are also removed.

## Creating color shades

Shades are generated child colors that stay connected to a root color. A root color can have three shade groups:

- **Light shades**: mixed toward white.
- **Dark shades**: mixed toward black.
- **Transparent shades**: same hue with varying opacity.

To generate shades:

1. Click the "Edit" icon on any color
2. Enable a shade type
3. Set the number of steps
4. Adjust individual generated shade values if needed

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-color-manager-shades-scaled.png)

Bricks supports 1 to 20 steps per shade group. When you change the root light or dark color, Bricks regenerates the enabled shades for that mode. If you manually fine-tuned a shade, changing the root color or shade step count can replace that manual adjustment.

Shade variables follow the base variable name:

- `var(--primary-l-1)` for light shades
- `var(--primary-d-1)` for dark shades
- `var(--primary-t-1)` for transparent shades

The number at the end is the shade step.

Shades are useful for interaction states. For example, set a button's **Background color** to `var(--primary)` and its `:hover` background to `var(--primary-d-1)`. When you later change `primary`, the hover color is regenerated from the new value.

Disabling a shade group removes the generated shade entries for that root color.

## Generating color harmonies

Color harmonies create additional root colors from a selected base color.

1. Select a base color
2. Click the **Harmony** icon
3. Choose a harmony model
4. Review the previewed colors
5. Edit generated variable names if needed
6. Click **Generate colors**

- **Analogous**: Colors next to each other on the color wheel
- **Monochromatic**: Different shades of the same color
- **Complementary**: Colors opposite each other
- **Split Complementary**: One complementary color split into two
- **Triadic**: Three colors evenly spaced
- **Tetradic**: Four colors in a rectangle pattern

Harmony colors are added to the current palette as normal root colors. They are not automatically linked to the source color after generation.

## Setting up utility classes

Utility classes generate reusable class names from your saved colors. Enable them per root color and per CSS property.

1. Edit a color
2. Scroll to **Utility classes**
3. Enable one or more utility types

Available utility types:

| Utility type | CSS property | Example class |
| --- | --- | --- |
| Background | `background-color` | `.bg-primary` |
| Text | `color` | `.text-primary` |
| Border | `border-color` | `.border-primary` |
| Outline | `outline-color` | `.outline-primary` |
| Fill | `fill` | `.fill-primary` |
| Stroke | `stroke` | `.stroke-primary` |

Utility classes are generated for the root color and for that color's shades. If `primary` has light shades and you enable the Text utility, Bricks can generate classes such as `.text-primary` and `.text-primary-l-1`.

Bricks also creates or updates matching global class records for generated utility classes. The CSS rules for those classes are written to the generated Style Manager CSS file.

If you rename a color variable, Bricks updates the generated global class names for that color. If you disable a utility type after assigning its classes to elements, review those elements because the generated CSS for that utility type will no longer be produced.

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-color-utility-classes-scaled.png)

## Importing and exporting palettes

### Import palettes

1. Click the **Import** icon
2. Drop or select a JSON file
3. Review the import result messages

Imported palette files must contain the expected palette shape: `id`, `name`, and `colors`. Bricks blocks imports when a palette with the same name already exists.

Imported color data should still be reviewed before using it on a production site. Bricks checks the file shape and palette name conflict, but the imported palette may still contain naming conventions or utility-class choices that do not match your site.

### Export palettes and CSS

There are two export options:

- Export the active palette as JSON for use on another Bricks site.
- Open **Generated CSS** and export the active palette CSS.

The generated CSS preview includes variable declarations and utility classes for the active palette. Use this as an inspection or handoff tool. Do not manually edit the generated Style Manager CSS file, because Bricks regenerates it from saved Color Manager data.

## Saving and generated output

Color Manager data is global builder data. Normal palette edits are saved when you save the builder. Importing a palette also persists the updated palette data after the import completes.

When Color Manager data is saved, Bricks regenerates the Style Manager CSS file. That generated file contains:

- Color variables from palettes.
- Utility classes from colors with enabled utility types.
- Scale utility classes from Global Variables categories when those are configured.

Color variables are also included in Bricks generated CSS so selected palette colors can resolve on the frontend.

## Troubleshooting

### A color does not update everywhere

Check whether the elements use the saved palette color or a raw color value. A manually typed `#0057ff` does not stay linked to `var(--primary)`.

### A variable name cannot be saved

The name may already exist in another Color Manager palette or in Global Variables. Use one unique variable name per token.

### A dark-mode value is not visible

Dark-mode values are output for `:root[data-brx-theme="dark"]`. Confirm that the page is actually using the dark-theme attribute and that the color has a dark value.

### Utility classes exist but have no visible effect

Confirm that the utility type is still enabled for the root color. Also check that the generated CSS file was regenerated after the change and that the class is assigned to the element you are inspecting.

### Imported palettes look correct but behave unexpectedly

Review variable names, duplicate naming conventions, dark-mode values, shade groups, and utility-class settings after import. Imported palettes are not automatically adapted to your existing naming system.

---

# Creating Your First Template

Source: https://academy.bricksbuilder.io/builder/features/create-template/

*Create your first Bricks template, choose the right template type, and prepare it for conditions and reusable content.*

Templates let you design parts of your site once and let Bricks render them in the right place. A header template can render above your content, a footer template below it, and a single template can replace the main layout for posts, pages, or custom post types.

This article walks through the first three templates most sites need:

- A site header
- A site footer
- A single post layout

The same workflow applies to archive, search, error, popup, password protection, WooCommerce product archive, and WooCommerce single product templates. The important decisions are usually the same: choose the right template type, build the layout, set the preview content, decide where the template should render, then publish and test it on the frontend.

Other WooCommerce route templates, such as cart, checkout, thank-you, and account templates, use the same create-build-publish flow, but Bricks renders them automatically on the matching WooCommerce route. Those route templates do not use the normal Conditions or Populate Content controls.

https://youtu.be/bLZDN9UcUyo

## Create a template

You can create templates from the WordPress dashboard or from inside the builder.

From the WordPress dashboard:

1. Go to **Bricks > Templates**.
2. Click **Add New Template**.
3. Enter a clear name, such as "Main Header", "Main Footer", or "Single Post".
4. Select the **Template type** in the sidebar.
5. Publish the template.
6. Click **Edit with Bricks**.

From inside the builder:

1. Open the **Templates** popup from the folder icon in the toolbar.
2. Open **My Templates**.
3. Click **New template**.
4. Enter a title and select the template type.
5. Create the template, then start editing it.

The template type controls how Bricks treats the template. For example, a **Header** template is stored and rendered as the site header area, while a **Single** template is stored and rendered as the main content area for matching pages.

## Create a header template

Use a header template for the site area that appears before the main content. A normal header usually contains a logo, navigation, call-to-action button, search, account links, or similar site-wide elements.

1. Create a new template named "Main Header".
2. Set **Template type** to **Header**.
3. Publish it and open it with Bricks.
4. Build the header layout on the canvas.
5. Open **Settings > Template Settings > Populate Content**.
6. Select content that makes sense for previewing the header, such as a page or single post.
7. Open **Settings > Template Settings > Conditions**.
8. Add **Entire website** if the header should appear everywhere.
9. Save the template and test a normal frontend page.

By default, Bricks can use a published header template even if it has no conditions. This default-template behavior is controlled from **Bricks > Settings > Templates & components > Disable default templates**.

If default templates are enabled and you have a published header without conditions, Bricks can use it as the site header. If default templates are disabled, set template conditions explicitly.

## Header settings

Header templates have an additional **Header** settings group under **Settings > Template Settings**.

Use it to control:

- **Header location:** top, left, or right.
- **Header width:** available for left and right headers.
- **Sticky header:** available for top headers.
- **Sticky on scroll:** keeps the header in normal flow on page load, then makes it sticky after scrolling.
- **Slide up after:** lets a sticky header hide after a scroll distance.
- **Scrolling styles:** text color, hover color, background, box shadow, and transition while the sticky header is in its scrolling state.

Left and right headers affect the layout beside the content and footer. Top headers are the usual choice for most websites.

## Create a footer template

Use a footer template for the site area that appears after the main content. A normal footer contains copyright text, footer navigation, contact links, social links, newsletter forms, or legal links.

1. Create a new template named "Main Footer".
2. Set **Template type** to **Footer**.
3. Publish it and open it with Bricks.
4. Build the footer layout.
5. Use **Populate Content** to preview the footer with a real page or post.
6. Add a condition, usually **Entire website**.
7. Save and test the frontend.

Like headers, published footer templates can be used by default when no conditions are set, unless default templates are disabled in Bricks settings.

## Create a single post template

Use a **Single** template when you want Bricks to control the layout for posts, pages, or custom post type entries. For a blog post template, the canvas usually contains elements such as Post Title, Featured Image, Post Content, Author, Date, Terms, Comments, and related content.

1. Create a new template named "Single Post".
2. Set **Template type** to **Single**.
3. Publish it and open it with Bricks.
4. Open **Settings > Template Settings > Populate Content**.
5. Set **Content type** to **Single (Post/Page/CPT)**.
6. Select a real post to preview.
7. Build the post layout using dynamic data and post elements.
8. Open **Settings > Template Settings > Conditions**.
9. Add **Post type** and select **Posts**.
10. Save and test several published posts on the frontend.

The preview post only controls what you see while editing the template. The condition controls where the template is used on the frontend.

## Conditions or default templates?

For production sites, set conditions deliberately. Conditions make the template assignment visible and predictable.

Default templates are useful while getting started because Bricks can automatically use published templates of certain types when no conditions are set. This is most common for headers and footers, but Bricks also supports default behavior for archive, search, error, and supported WooCommerce route templates.

Disable default templates when you want every rendered template to be controlled by explicit conditions. You can do this in **Bricks > Settings > Templates & components > Disable default templates**.

## Disable a header or footer on one page

Landing pages and campaign pages often need no global header or footer.

To disable the header or footer for a specific page:

1. Open the page with Bricks.
2. Open **Settings > Page Settings > General**.
3. Enable **Disable header** or **Disable footer**.
4. Save the page.

This page setting applies to the page being rendered. It does not delete or change the template.

## Preview content vs frontend output

Template editing needs a preview context. For example, a single post template needs one post to show dynamic data on the canvas. An archive template needs an archive context. A header or footer may need a page or post behind it so you can judge spacing and overlap.

Preview content does not assign the template to that content. It only changes the canvas context while editing.

Use conditions to control frontend assignment.

## Common mistakes

**The template is published but not visible:** Check whether it has matching conditions. If default templates are disabled, a template without conditions will not be used automatically.

**The wrong template appears:** Look for a more specific matching template. Individual conditions outrank broad conditions such as Entire website. Exclude conditions can also disqualify a template.

**The canvas looks empty or the dynamic data is wrong:** Set **Populate Content** to a real page, post, archive, or search context that matches the template you are building.

**A header or footer is missing on one page:** Check that page's **Page Settings > General** for **Disable header** or **Disable footer**.

**A Single template does not affect posts:** Make sure the template type is **Single**, the template is published, and the condition targets the correct post type or individual entries.

**A Section template does not update inserted copies:** Section templates are reusable library items. They do not sync inserted content between pages. Use Components for linked reusable structures.

---

# Components

Source: https://academy.bricksbuilder.io/builder/features/components/

*Create reusable Bricks components, customize each instance through properties, and manage them from the Components library.*

Components let you create reusable elements. Each instance can be customized through properties.

While templates serve as blueprints for pages, components serve as blueprints for a specific element or group of elements, such as a button, card, navigation, or hero section. You can reuse a component throughout your site and customize each instance only where needed.

Any change to the main component automatically applies to every instance of that component. This keeps repeated structures and styles consistent across your website while still letting each instance use its own content, query, variant, or slot content.

https://www.youtube.com/watch?v=nNvcrK-vDDs

## How Components Work

A component is a saved element tree with one root element. Bricks stores the component definition separately from the page content. Each instance on a page points to that definition through its component ID and stores only its own instance-specific values, such as property overrides, a selected variant, and slot children.

When Bricks renders the page, it expands the referenced component definition into the page and applies the instance values. If an instance points to a component that no longer exists, that instance is skipped on the frontend.

## How to Create a Component

Create a component from most elements, except Template and Query Filter elements, by right-clicking the element and selecting the `Save as component` action. You need the **Create components** builder permission to create new components.

![](https://academy.bricksbuilder.io/assets/bricks-save-as-components.png)

In the popup, enter a name (required), category (optional), and description (optional) for your new component. Click `Create` to finish creating the component.

![](https://academy.bricksbuilder.io/assets/bricks-create-component-popup.png)

Once created, the selected element becomes a component instance. Bricks moves the original element tree into the component definition, replaces the page element with an instance that points to that component, and adds the component to the Components library.

## Components Library

![](https://academy.bricksbuilder.io/assets/bricks-components-panel.png)

You can access your components from the `Components` tab, located next to the `Elements` panel tab.

From here you can add a component to the canvas or structure panel via drag and drop or click, the same as any other element.

In Bricks 2.4, you can also manage components from the Builder Browser. Open the Browser from the folder icon in the builder toolbar, then select **Components**.

You can perform the following actions from the Components tab:

- **Import:** Import component JSON or ZIP files from another installation.
- **Export:** Export all components of your site as a JSON file. To export a specific component, hover over it and click the export action icon.
- **Delete:** Click the delete icon to enter delete mode. Once activated, hover over the component you want to delete and click the delete icon.
- **Edit:** Open the component properties panel from the component action icons.
- **Duplicate:** Create a copy of an existing component.
- **Use in block editor:** Toggle whether a component can be used as a block in the WordPress block editor, when the block editor integration is enabled.

Component actions are permission-gated. Inserting components, creating components, deleting components, editing component definitions, setting instance property values, and importing/exporting components are separate builder permissions.

Imported components with duplicate IDs are skipped. Exported component JSON also includes global classes used by the component's element settings and class properties.

## Component Manager in the Builder Browser

The Browser's Components view gives you a wider management screen for existing components.

From there you can:

- Search components.
- Filter by category.
- Filter by usage: all usage, used on current page, used elsewhere, or unused.
- Switch between grid and list view.
- Import component JSON or ZIP files.
- Edit, duplicate, export, delete, or generate a screenshot for a component.
- Generate screenshots for the currently filtered component list.

Generating component screenshots requires the **Edit components** builder permission. Component import and export require the **Import/export components** builder permission. The **Used elsewhere** filter only shows components that are not used on the current page but are used on another page or template.

**Component screenshots** are enabled by default on new installations under **Bricks > Settings > Templates & components**. Disable the setting to stop automatic and manual generation and hide stored local thumbnails. Disabling it does not delete existing screenshot files. Use **Delete screenshots** in the same settings section to remove all generated component screenshots.

![](https://academy.bricksbuilder.io/assets/bricks-browser-component-manager.webp)

### Instance Count and Location

![](https://academy.bricksbuilder.io/assets/bricks-components-panel-instances-count.png)

Below the name of the component is the instance count. For example, `Instances: 3/6` means the component is used three times on the page you are currently editing and six times across the site.

In the Components panel, hover over the component and click the globe icon to see all instances of this component on the current page, plus a list of other pages where the component is used.

In the Builder Browser's Components view, click the instance badge to open the usage popover. The popover separates **Current page** instances from **Other pages**. Current-page items take you to the matching instance in the builder. Other-page items open the matching page or template in Bricks in a new browser tab.

## Instances: How to Reuse a Component

Every time you add a component to a page, Bricks creates an instance of that component.

Changes to the main component automatically reflect in all instances of this component throughout your site. Instance-specific property values, variants, and slot content affect only the selected instance.

The following screenshot shows three instances of the same Card component:

![](https://academy.bricksbuilder.io/assets/bricks-components-panel-instances.png)

## Editing the Main Component

To view and edit the elements of the main component, which is the source of truth for all its instances, right-click any instance and select `Edit component`.

![](https://academy.bricksbuilder.io/assets/bricks-component-edit-context-menu.png)

Alternatively, click the gear icon in the control panel header of the instance to enter component editing mode:

![](https://academy.bricksbuilder.io/assets/bricks-component-instance-edit-component.png)

You are now editing the main component, indicated by the purple color in the control panel header.

As mentioned before, any change you perform on the main component applies to all instances of this component on your site.

![](https://academy.bricksbuilder.io/assets/bricks-components-editing-main-component.png)

The main component header contains the following actions:

- **Description** (info icon): Show or hide the component description.
- **Category** (folder icon): Show or hide the component category.
- **Block editor** (WordPress icon): Show or hide block editor settings when the component is enabled as a block.
- **Variants** (layers icon): Open the variants panel.
- **Properties** (box icon): Open the component properties panel.
- **Instance** (arrow icon): Exit component edit mode and return to the instance you were editing before, or to the Components library. Pressing the Escape key also exits the main component.

When editing the main component, you can see and edit all elements of this component in the structure panel:

![](https://academy.bricksbuilder.io/assets/bricks-components-main-component-structure-panel.png)

To edit the title of a Card component, select the Heading element inside the component and change its text to `Just a card`.

All instances of the Card component automatically reflect this change:

![](https://academy.bricksbuilder.io/assets/bricks-components-edit-component-heading.png)

This is useful for shared structure and design. The real power of components comes from combining shared structure with properties that can be customized per instance.

## Properties {#properties}

Properties let you expose controls for customization on each instance.

For example, a Card component can expose a card title property and a card image property. Each Card instance can then use different content while still sharing the same component structure and styling.

There is a two-step process:

1. Create a property.
2. Connect that property to one or more compatible controls inside the component.

Creating and editing property definitions requires the **Edit components** [builder permission](https://academy.bricksbuilder.io/builder/interface/builder-access/#components). Setting property values on an instance requires the **Edit properties (Instance)** permission.

### 1. Creating a Property

To access the properties panel, select any instance of the component you want to edit. Then click the edit icon in the properties control panel on the left-hand side:

![](https://academy.bricksbuilder.io/assets/bricks-components-instance-edit-property-1.png)

If there are no instances of the component on the current page, go to the Components library, hover over the component, and click the edit icon.

If you are already editing the main component, you can access the Properties panel by clicking the box icon in the panel header.

### Property Types {#property-types}

You can choose from these property types and connect them to compatible controls inside your component:

| **Property type**             | **Connectable to**                             | **Example**                       |
| ----------------------------- | ---------------------------------------------- | --------------------------------- |
| Text                          | Text and textarea controls                     | Heading or Basic text             |
| Rich text                     | Rich text controls                             | Rich text or Accordion content    |
| Icon                          | Icon controls                                  | Icon or Icon Box element          |
| Image                         | Image controls                                 | Image or Logo element             |
| Image gallery                 | Image gallery controls                         | Image gallery or Carousel element |
| Link                          | Link controls                                  | Button or Heading link            |
| Select _(@since 2.0)_         | Select, text, textarea, and rich text controls | HTML tag, Button style            |
| Toggle _(@since 2.0)_         | Checkbox and toggle controls                   | Hide element toggle               |
| Query loop                    | Query controls                                 | Layout elements                   |
| Global classes _(@since 2.0)_ | Global classes controls                        | Element global classes            |

![](https://academy.bricksbuilder.io/assets/bricks-2.0-components-create-property-form.png)

The **property name** is mandatory. Choose a descriptive name, especially for complex components with many properties.

The **property description** is optional, but it helps other builders understand how the property should be used.

The **property group** is optional and helps organize properties inside the instance panel.

The **default property value** is optional. It is used when an instance has not set its own value. If an instance value is cleared or reset, Bricks removes the override so the default value can apply again.

### 2. Connecting a Property to a Control

After creating a property, connect it to the control that should be editable on the instance.

Unconnected properties show a broken-link icon next to their name:

![](https://academy.bricksbuilder.io/assets/bricks-components-unconnected-properties.png)

To connect a text property to a Heading element:

1. Edit the main component.
2. Select the Heading element inside the component.
3. Find the text control.
4. Click the purple `+` property icon.
5. Select the property you want to connect.

![](https://academy.bricksbuilder.io/assets/bricks-components-control-property-indicator.png)

Clicking the `+` icon reveals a list of properties that can connect to this control:

![](https://academy.bricksbuilder.io/assets/bricks-components-control-property-options.png)

> **Note**
>
> **Workflow boost:** Quickly create a new property by clicking the `+` icon at the top right of the "Connect property" dropdown.

Once selected, the control shows the name of the property that is connected:

![](https://academy.bricksbuilder.io/assets/bricks-components-control-property-connected.png)

When an instance changes that property, Bricks applies the instance value to every connected control. For nested components, Bricks can also connect a child component property to a property from the parent component.

Most connected controls can use one non-class property. Global class properties are the exception and can be combined with other class property connections.

### Disconnecting a Property

To disconnect a property from a setting, click the connected property setting, hover over the connected property name, and click the unlink icon.

![](https://academy.bricksbuilder.io/assets/bricks-component-disconnect-property.png)

## Customizing an Instance

Select a component instance to customize the properties exposed by the main component. Only connected properties appear in the instance controls.

![](https://academy.bricksbuilder.io/assets/bricks-components-instances-custom-values.png)

For example:

- One Card instance can use a custom heading.
- Another Card instance can use a different image.
- Another Card instance can keep the default property values.

![](https://academy.bricksbuilder.io/assets/bricks-components-instance-default-property-values-2.png)

Instance changes do not affect the main component or other instances. They only affect the selected instance.

## Components as Loops and Inside Loops {#loops}

Components are compatible with query loops. You can enable a loop on the component root or place a query loop inside the component.

In the following screenshot, the Card component is used inside a loop. The Card title uses the `post_title` dynamic data tag and the Card image uses the `featured_image` tag to render the post title and featured image of the loop results.

![](https://academy.bricksbuilder.io/assets/bricks-component-inside-query-loop.png)

There is also a `Query loop` property type, which allows each component instance to customize an in-component query loop.

<span id="variations" aria-hidden="true"></span>

## Component Variants {#variants}

Bricks supports native component variants. When editing the main component, open the Variants panel to name the base variant and add custom variants. Each component instance can then select one of those variants.

Use native variants for formal component states or designs. Variant-specific settings are saved on the component definition, and the selected variant is saved on the instance.

Examples:

- Primary and secondary button styles.
- Card layouts with different spacing.
- Light and dark versions of the same component.
- Compact and expanded versions of a component.

For more flexible changes, expose settings as component properties instead.

## Property-Based Variation Patterns {#property-based-variations}

The following patterns use component properties to customize each instance. They are useful when you want instance-level choices without creating formal component variants.

### Show or Hide Elements {#visibility}

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-toggle-hide-element.png)

Bricks 2.0 introduces a Hide element feature, available by clicking the eye icon in the element panel header or from the context menu.

You can create a `Toggle` property and connect it to the **Builder: Hide element** and/or **Frontend: Hide element** controls to show or hide elements inside your component on an instance basis.

The frontend hide control is not just a visual CSS helper. Hidden frontend component elements are excluded from the frontend render/settings output.

### Global Classes {#global-classes}

The `Global classes` property type, available since Bricks 2.0, lets you create styling variations through global classes. Assign a collection of default and/or custom classes on the instance for any element of your component.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-global-classes-connectable-property.png)

In the following example, we create a global classes property with the custom options `Small`, `Medium`, and `Large`. Each option has a different global class assigned to it. You can also assign multiple classes.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-global-classes-custom-options.png)

Once you have created the new `Heading size` property, connect it to the global classes control of the element of your choice. In this example, it is connected to the Heading:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-global-classes-connect-property.png)

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-global-classes-connected-property.png)

Once connected, the property becomes available on every instance. In the following screenshot, the `Large` option adds the global class `prop-text-lg` to the Heading element of the instance.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-global-classes-instance-scaled.png)

You can connect as many global class properties to an element as needed.

When defining custom options, you can leave the label empty to show the selected global class names instead. User-friendly labels are usually the preferred option.

You can change the global class selection of an option any time. The newly selected global classes are added to the instance if the corresponding option is selected.

### Local Classes {#local-classes}

If you are not working with global classes, you can use the `Select` property type to define custom options that users can choose from, then apply those class names through an attributes control inside the component.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-select-local-classes.png)

Next, create a `Select` property with class name options:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-select-custom-options.png)

Once you create and connect this select property to the attributes value, it becomes available on the instance. You can then apply the local class with one click, which adds the `color-red` class to the Heading element inside the component.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-component-property-type-select-instance-scaled.png)

You can also connect a `Text` control to the attributes value if you want users to enter plain class names directly instead of choosing from predefined options.

## Slots {#slots}

https://youtu.be/OiCHwfRSiLY

The Slot element lets a component define a placeholder for instance-specific children. Add a Slot inside the main component where instance content should appear, then add elements to that slot from a component instance.

A Slot element in the main component is a placeholder. When you select an instance, Bricks exposes virtual slot areas where you can add instance-specific children. Those children are saved on the instance and rendered inside that slot for that instance only.

To add a slot, edit the main component and select the element that should hold the instance content. While you edit a component, the Elements panel shows the `Slot` element in the `Component` group. Click it to add the slot. To name the slot, double-click it in the Structure panel, for example `Actions`. Every instance shows this name for its slot.

<div className="screenshot screenshot--control-panel">

![Elements panel in component edit mode with the Slot element in the Component group.](https://academy.bricksbuilder.io/assets/bricks-component-slot-element.webp)

</div>

To fill a slot, select the instance. In the Structure panel, select its slot row and click an element in the Elements panel, drag an existing element onto the slot row, or right-click the slot row and select `Paste`. Elements in a slot are regular elements of the page, so you can edit and style them like any other element.

<div className="screenshot screenshot--control-panel">

![Structure panel with a component instance, its Actions slot and two elements inside the slot.](https://academy.bricksbuilder.io/assets/bricks-component-instance-slot-structure.webp)

</div>

> **Shared text styles for slot content**
>
> New elements start with the default element styles. Set shared typography, such as text color and font size, on an outer element of the component. Elements you add to a slot then inherit it on every instance.

- A slot adds no wrapper element. Bricks renders only the instance's elements in its place.
- An empty slot outputs nothing. A slot has no default content.
- If you delete a slot from the main component, the elements that instances added to it are no longer rendered.
- Component blocks in the block editor do not support slots. See [Components as Blocks](https://academy.bricksbuilder.io/integrations/gutenberg/components-as-blocks/).

## Components as Blocks

Components can be used as blocks in the WordPress block editor if the Gutenberg integration is enabled.

To use a component as a block:

1. Enable the Gutenberg integration in Bricks settings.
2. Enable the component for the block editor.
3. Configure the component block title, category, icon, and preview image.
4. Insert the component from the WordPress block editor.

Block editor controls are generated from component properties that are connected to controls inside the component, including direct and nested property connections.

For the full setup, see [Components as Blocks](https://academy.bricksbuilder.io/integrations/gutenberg/components-as-blocks/).

## Unlinking a Component {#unlink}

To unlink an instance from a component, right-click the instance and select the `Unlink component` icon under the `Edit component` menu item.

Once unlinked, the instance is no longer tied to the main component and can be edited independently, like any other element.

## Global Element to Component Converter

Global elements are deprecated since Bricks 2.0. You cannot create new global elements, but you can convert existing global elements to components from `Bricks > Settings > General > Global elements`.

## Component Data Model

These details explain how Bricks stores and renders component instances:

- Component definitions live in Bricks component data, not as ordinary copied children on every page instance.
- A component must have one root element. The root element ID is the component ID.
- A page instance references its component through the component ID.
- Instance-specific property values are stored on the instance by property ID.
- Component properties are definitions. A property controls an instance value only after it is connected to one or more compatible controls inside the component.
- Variant selections live on the instance. Variant-specific settings live on the component definition.
- Slot children live on the instance, not in the main component definition.
- A missing component reference should be treated as invalid. Bricks skips instances whose component definition no longer exists.

## Notes & Tips

- Components are best for repeated design patterns.
- Properties are best for values that change per instance.
- Use categories to keep the component library organized.
- Use descriptions to make components easier to understand for teams and future maintenance.
- Use variants for design presets.
- Use slots for flexible inner content.
- Use component properties instead of duplicating components for small content differences.
- Export important components before deleting or heavily changing them.
- Keep components simple and focused. Very large components can become harder to maintain.

---

# Create & Update Posts on the Frontend

Source: https://academy.bricksbuilder.io/builder/features/create-update-posts-on-the-frontend/

*Build frontend forms in Bricks that create or update WordPress posts without sending users into wp-admin.*

Bricks 2.1 introduced the **Create post** and **Update post** form actions. They let a frontend Form element create a new WordPress post or update an existing one without sending the user to wp-admin.

Use these actions for workflows such as property listings, classifieds, member-submitted posts, profile pages, or client portals. The examples below use a custom post type named `property`, but the same rules apply to any public post type that exists on your site.

> **Note**
>
> **IMPORTANT:** By default, Bricks checks permissions twice: when rendering the form and again when processing the submission.
>
> - **Create post** requires the current user to have the selected post type's `edit_posts` capability.
> - **Update post** requires the current user to have `edit_post` for the target post.
>
> Do not enable **Disable capability checks** unless the form is protected another way. When disabled, non-logged-in or unauthorized visitors can create or edit content through that form.

https://www.youtube.com/watch?v=c9JcrLEVbnM

## Before you start

Decide these things before building the form:

- Which post type the form creates or updates.
- Which users are allowed to submit the form.
- Whether new posts should be saved as draft, pending review, published, or another available post status.
- Which core post fields, custom fields, and taxonomies the form may change.
- Whether uploads should be saved to the Media Library. Featured images, attachment posts, and many ACF/Meta Box media fields need attachment IDs.

## How to create or update posts via form submission

The create and update workflows use the same pattern: add fields, choose the form action, then map the fields to the WordPress data that should change.

### Step 1: Add form fields for post data

Create form fields for all the post data that you want to save when creating or updating a post through the Form element:

| Post data | Recommended field type |
| --- | --- |
| Post title | Text |
| Post content | Rich text |
| Post excerpt | Textarea |
| Featured image | Image |
| Post meta | The most suitable field type for the custom field |
| Taxonomy terms | Checkbox, radio, or select |

#### Post meta

Make sure to select the most suitable field type for every piece of post meta data you want to modify. Bricks stores mapped meta through ACF, Meta Box, or `update_post_meta()` depending on the meta key and the integrations available on the site.

For checkbox, radio, and select fields, Bricks can automatically load choices from ACF or Meta Box when:

- The field is mapped to a matching meta key.
- The form field has no manual options.
- ACF or Meta Box can resolve that field for the post or post type.

If you add manual options to the form field, Bricks uses your manual options instead.

#### Taxonomy

Use checkbox, radio, or select fields for taxonomies such as categories, tags, or custom taxonomies. You can leave the form field options empty. When the field is mapped in the **Taxonomies** repeater, Bricks automatically populates the field with terms from the selected taxonomy.

If you manually add options, use term IDs as the submitted values. On submission, Bricks stores taxonomy terms by ID. If the mapped taxonomy field is empty, Bricks clears the terms for that mapped taxonomy.

### Step 2: Select the form action

Edit the Form element and select **Create post** or **Update post** in the **Actions** control group.

![](https://academy.bricksbuilder.io/assets/bricks-form-action-create-update-post.png)

The order of actions matters. If an action returns an error, Bricks stops processing the remaining actions. The **Redirect** action is always moved to the end of the action list so other selected actions can run first.

### Step 3: Configure the action

When creating a new post, select the post type that you want to create a new post for under the "Create post" control group:

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-09-16-at-14.07.14@2x.png)

<figcaption>

Create new post for post type "Property" on form submission

</figcaption>

When updating an existing post, select the specific post that you want to update under the "Update post" control group:

![](https://academy.bricksbuilder.io/assets/bricks-form-update-post-control-group.png)

Leave **Post to update** empty to update the current post. If the form is inside a query loop, Bricks uses the submitted loop object ID so each repeated form can update its own loop item.

Both actions include a **Post status** setting. For **Create post**, leaving it empty lets WordPress use its default insert behavior. For **Update post**, leaving it empty keeps the current post status.

When **Create post** runs for a logged-in user, that user becomes the post author. If you disable capability checks and allow anonymous submissions, Bricks falls back to the site's first super admin user when assigning the author.

## Step 4: Field mapping

The last, and most important step is to map/connect your form fields with the post data that should be modified when the form is submitted. The mapping controls are also located within the "Create post" and "Update post" control groups.

### Mapping simple post data

For simple post data such as the Post title, Post content, Post excerpt, and Featured image you just have to select the corresponding form field from the select dropdown:

![](https://academy.bricksbuilder.io/assets/bricks-form-create-post-field-mapping-simple-post-data.png)

For featured images and attachment posts, use fields that save uploads to the Media Library so Bricks can work with the uploaded attachment ID.

Bricks verifies that the mapped featured image value is an image attachment ID before calling WordPress' featured image logic. If the mapped field has no value, Bricks removes the featured image.

### Mapping post meta

When updating post meta via a form field, add an item under **Post meta** and provide:

- **Meta key**: The custom field key to update. Bricks sanitizes this key before saving.
- **Meta value**: The form field whose submitted value should be saved.
- **Sanitization method**: How Bricks should sanitize the submitted value before saving it.

![](https://academy.bricksbuilder.io/assets/bricks-form-create-post-field-mapping-post-meta.png)

Available sanitization methods include text, integer, float, email, URL, and post-safe HTML. Values that are not handled by ACF or Meta Box fall back to WordPress post meta.

#### ACF and Meta Box handling

When possible, Bricks updates ACF fields through `update_field()` and Meta Box fields through `rwmb_set_meta()` instead of writing raw post meta only. This matters for field types that expect a specific value shape.

For media fields, file upload fields should save files to the Media Library. Bricks processes those uploads before the create/update action so mapped fields can receive attachment IDs.

For ACF group fields, Bricks can resolve nested meta keys and update the parent group value so nested data remains structured correctly.

### Taxonomies

Mapping a form field to a taxonomy is straightforward. Under **Taxonomies**, select the taxonomy to update and the corresponding form field.

There is no need to manually enter taxonomy terms unless you want to limit the choices. Bricks will automatically populate the form field with the selected taxonomy's terms when the mapped form field has no manual options.

## Security and validation details

Bricks still runs the normal form submission checks before the create/update action:

- The AJAX submission must include a valid Bricks form nonce.
- Submitted field IDs must match fields that exist in the form settings. Unexpected or duplicate field IDs are rejected.
- Required field validation, max-length validation, honeypot checks, and enabled captcha checks run before actions.
- The action repeats capability checks server-side unless you disabled them.

The form is not rendered for unauthorized users when capability checks are enabled. If you set a custom error message in the Create post or Update post control group, Bricks displays that message instead.

## Common setups

### Let users submit posts for review

Use **Create post**, keep capability checks enabled for trusted logged-in users, and set **Post status** to **Pending** or **Draft**. Map only the fields users should control.

### Let authors edit their own posts

Use **Update post**, leave **Post to update** empty on a single post template, and keep capability checks enabled. WordPress will allow the update only if the current user can edit that post.

### Update items inside a query loop

Place the update form inside the query loop and leave **Post to update** empty. Bricks submits the loop object ID and updates the matching loop item.

### Create attachment posts from uploads

Set **Post type** to **Attachment** and use a file upload field that saves to the Media Library. Bricks uses the first uploaded attachment it finds and can update its title, content, excerpt, status, meta, and terms through the mapped fields.

## Filters

Bricks supports many ACF and Meta Box field types out of the box, but every custom setup is different. You can adjust mapped meta values before they are saved with these filters:

- [`bricks/form/create_post/meta_value`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-create_post-meta_value/)
- [`bricks/form/update_post/meta_value`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-update_post-meta_value/)

---

# Custom Attributes

Source: https://academy.bricksbuilder.io/builder/features/custom-attributes/

*Add custom HTML attributes in Bricks for integrations, JavaScript hooks, accessibility, and advanced frontend behavior.*

Bricks 1.3 introduces the possibility to add your own custom HTML attributes to any element.

You can add custom attributes under "Style > Attributes". Set a "Name" and a "Value" and your attribute(s) will be added to the elements' most relevant node. By default, your attributes are added to the element root node. Besides manually entered values you can populate custom attribute values with dynamic data, too.

In there you'll be able to insert multiple attributes (name and value). Dynamic Data is rendered for attribute values on the frontend.

![](https://academy.bricksbuilder.io/assets/feature-custom-attributes.png)

<figcaption>

Container: Custom Attributes

</figcaption>

Let's say you want to add an ARIA **role** and **label** to a container that contains multiple images that should be [considered as a single image](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/Role_Img). You'd add the following two attributes when editing your container:

- Attribute #1 name: **role**
- Attribute #1 value: **img**
- Attribute #2 name: **aria-label**
- Attribute #2 value: **Description of the overall image**

This results in the following container HTML:

```html
<div id="brxe-sfglik" class="brxe-sfglik brxe-container" role="img" aria-label="Description of the overall image">
... Container elements ...
</div>
```

Custom attributes take precedence over default attributes. So if you set a custom **alt** attribute when editing your image, this custom attribute will be used instead of the default image **alt** attribute.

Elements where custom attributes are added to the following specific HTML tags:

| **Bricks Element** | **HTML tag** |
| --- | --- |
| Nav Menu | `<nav>` |
| Heading | `<h1>` or any other heading tag |
| Text | `<div>` |
| Button | `<button>` or `<a>` depending if there is a link |
| Image | `<img>` |
| Video | `<div>` |
| Form | `<form>` |

### How To Add Tooltips {#tooltips}

Bricks comes with built-in (CSS-only) tooltips that you can set via custom attributes.

Make sure to set the attribute "Name" to `data-balloon` and the value to whatever you want your tooltip text to be. You also have to set a second HTML attribute named `data-balloon-pos` and then set the value to whatever you want your tooltip to be positioned like:

- top | top-right | top-left
- right
- bottom | bottom-right | bottom-left
- left

For a full list of all available tooltip HTML attributes please visit the official website of the Balloon.css library Bricks uses for its tooltips: [https://kazzkiq.github.io/balloon.css/](https://kazzkiq.github.io/balloon.css/)

> **Note**
>
> If you are planning to add tooltips on the Icon element, please wrap the Icon element in a Div element and set the attribute on the Div element. Otherwise, balloon library CSS will overwrite the Icon element's CSS and cause it invisible in the frontend.

#### Resources:

- HTML attribute reference: [https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)

---

# Custom Authentication Pages

Source: https://academy.bricksbuilder.io/builder/features/custom-authentication-pages/

*Build custom login, registration, lost-password, and reset-password flows in Bricks instead of relying on default WordPress screens.*

Since Bricks 1.9.2, you can assign custom Bricks-built pages for WordPress authentication flows. This lets you replace the default WordPress screens for login, registration, lost password, and reset password with pages that match your site design.

![Bricks custom authentication settings screen showing options to assign custom pages for login, registration, lost password, and reset password. The "WordPress authentication page access" dropdown is set to "Error page", and the "Disable custom authentication page bypass" toggle is enabled.](https://academy.bricksbuilder.io/assets/bricks-custom-authentication-settings.png)

> **Note**
>
> Custom authentication pages change where visitors are sent, but the form actions still use WordPress authentication functions such as login, registration, password reset email generation, and password reset validation.

## How to set custom authentication pages

1. Navigate to the WordPress dashboard
2. Navigate to **Bricks** > **Settings** > **General**
3. Scroll down to **Custom authentication pages**

Here, you can choose a custom page for the following processes:

- Login
- Registration
- Lost Password
- Reset Password

If WooCommerce handles the current authentication page, Bricks leaves that page to WooCommerce and skips its custom authentication redirect handling.

## Setting up your custom pages

Each custom page should contain a [Form element](https://academy.bricksbuilder.io/builder/elements/general/form/#actions) with the matching authentication action selected under the Form element's **Actions** control group.

| Page | Required form action | Typical fields |
| --- | --- | --- |
| Login | User login | Login, password, optional remember me |
| Registration | User registration | Email, optional username, optional password, optional first/last name |
| Lost password | Lost password | Email or username |
| Reset password | Reset password | New password |

### Login page

Add a form with the **User login** action. Map the login field, password field, and optional remember-me field in the **User Login** control group.

If your custom login URL receives a `redirect_to` query parameter, Bricks adds it as a hidden field and redirects there after successful login when your form does not already use an explicit Redirect action.

For better privacy and security, set a generic login error message. Otherwise, the default WordPress login error can reveal why the login failed.

### Registration page

Add a form with the **User registration** action. Map at least the email field. Username and password can be auto-generated if they are not mapped or submitted.

The **Role** setting cannot be set to Administrator or Super Admin. If either is selected by data manipulation, Bricks falls back to the site's default role.

If [User activation](https://academy.bricksbuilder.io/builder/features/user-activation/) is enabled, the Form element's **Auto log in user** setting is hidden and registration does not auto-login immediately. Activation controls the post-registration login flow instead.

### Lost password page

Add a form with the **Lost password** action and map the **Email or username** field.

For privacy, Bricks returns a success response even when the submitted account does not exist. If the account exists, WordPress sends the password reset email.

### Reset password page

Add a form with the **Reset password** action and map the new password field.

When a user clicks a WordPress reset link, Bricks redirects the reset URL to your custom reset password page and preserves the reset query parameters. The Form element then renders hidden `key` and `login` fields from the URL so WordPress can validate the reset key on submission.

## WordPress authentication page access {#wp-auth}

As of Bricks 1.11, you have control over what happens when someone visits a default WordPress authentication URL (such as `wp-login.php`), provided custom authentication pages are set.

To manage this:

1. Navigate to **Bricks** > **Settings** > **General** > **Custom authentication pages**.
2. Under **WordPress authentication page access**, select one of the following options:
- **Redirect to custom authentication page (default)**: The user will be redirected to the corresponding custom authentication page you have set.
- **Error page**: Bricks returns the site's 404 error page for matching default auth URLs.
- **Home URL**: Redirects visitors to the homepage.
- **Redirect to specific page**: Allows you to choose a specific page on your site to redirect visitors to.

This setting only changes behavior for a default auth URL when the corresponding custom page has been set. For example, the login behavior applies when a custom login page is selected.

If **Redirect to specific page** is selected and no valid published page is selected, Bricks falls back to the home URL.

Bricks preserves query parameters when redirecting from the default auth URL to a custom auth page. This is important for reset-password keys and login redirects.

### Logout behavior

For logged-in users, Bricks lets WordPress process logout first. If WordPress would send the user back to the default login page after logout and you have a valid custom login page, Bricks redirects to the custom login page with `?logged_out=true`.

## Bypassing custom login (since 1.9.4):

By default, when visiting any authentication page on your site, you can access the default WordPress login page by adding `brx_use_wp_login` as a URL parameter, for example:

```text
https://example.com/wp-login.php?brx_use_wp_login=1
```

This feature allows site owners to bypass the custom login page if needed.

Adding this parameter sets a bypass cookie for 5 minutes. During that window, Bricks lets the default WordPress authentication page load instead of redirecting to the custom page.

In Bricks settings, you can disable this feature:

1. Navigate to **Bricks > Settings > General > Custom authentication pages**.
2. Enable **Disable custom authentication page bypass**.

When disabled, the `brx_use_wp_login` URL parameter no longer sets the bypass cookie.

> **Note**
>
> Before disabling the bypass and blocking default auth URLs, make sure your custom login page works and that you know its URL. Otherwise you can lock yourself out of the normal login screen.

## Developer filters

Bricks exposes filters for custom redirect logic:

- `bricks/auth/custom_redirect_url`: Override the redirect URL based on the current auth URL path.
- `bricks/auth/custom_login_redirect`: Change the selected custom login page.
- `bricks/auth/custom_registration_redirect`: Change the selected custom registration page.
- `bricks/auth/custom_lost_password_redirect`: Change the selected custom lost password page.
- `bricks/auth/custom_reset_password_redirect`: Change the selected custom reset password page.

Use these filters when a multilingual, membership, or custom routing setup needs more control than the global page selectors provide.

---

# Custom Code

Source: https://academy.bricksbuilder.io/builder/features/custom-code/

*Add custom CSS, JavaScript, and PHP in Bricks, understand where each code type runs, and manage it safely.*

Bricks allows you to add custom code (CSS, JavaScript, HTML, and PHP) to different parts of your website.

https://www.youtube.com/watch?v=oJNm1AFgAGU

## Where custom code can be added

Bricks has several custom-code locations. Choose the smallest location that matches what you need:

- **Global CSS and scripts**: Use this for code that should load across the entire site.
- **Page-specific CSS and scripts**: Use this for code that should load only on one page or template.
- **Element-specific CSS**: Use this for CSS tied to one element or global class.
- **Code element**: Use this when you need to place PHP/HTML, CSS, or JavaScript at a specific point in the page output.

Executable PHP and SVG code are security-sensitive. They only run when code execution is enabled, the current user has code execution capability, and the saved code has a valid code signature.

## Global CSS and JavaScript

You can add global **Custom CSS** and **Custom JavaScript** under **Bricks > Settings > Custom code**.

Global Custom CSS is added at the end of the document `<head>`.

Custom scripts can be added in three document locations:

- **Header scripts**: Added right before the closing `</head>` tag.
- **Body (header) scripts**: Added right after the opening `<body>` tag.
- **Body (footer) scripts**: Added right before the closing `</body>` tag.

Wrap JavaScript entered in the global script fields in `<script>` tags. These fields are intended for items such as analytics snippets, third-party embeds, and other site-wide scripts.

## Page-Specific CSS and JavaScript

To apply custom CSS and JavaScript to a specific page or template, edit it with Bricks and open **Settings > Page Settings > Custom Code**. Code entered there is scoped to the page or template you are editing instead of the entire site.

## Element-Specific Custom CSS {#custom-css}

![](https://academy.bricksbuilder.io/assets/bricks-1.9.1-custom-css-root-placeholder-591x1024.png)

Extend the styles of any element and global class by adding your own custom CSS to it.

First, select the element you want to style. Then open the **Style** tab and expand the **CSS** control group.

Use the `%root%` placeholder to target the element or global class you are currently editing. Bricks automatically converts `%root%` to the element ID or global class selector.

Keyboard shortcut to insert `%root%`: type `r` and press `TAB`.

Example:

```css
%root% {
  border: 1px solid red;
}
```

### CSS code completion via Emmet

You can use CSS abbreviations to write your CSS faster. Instead of writing `margin: 10px`, type `m10` and press `TAB`.

[https://docs.emmet.io/css-abbreviations/](https://docs.emmet.io/css-abbreviations/)

## Bi-directional CSS Sync

Introduced in Bricks 2.4, Bi-directional CSS Sync keeps an element's or global class's Custom CSS synchronized with the corresponding Bricks style controls.

https://www.youtube.com/watch?v=jZZA42hcS-U

Enable this experimental feature under **Bricks > Settings > Builder > CSS Sync**.

Change a supported property in the CSS editor, and its corresponding style control updates automatically. Changes made through a style control are written back to Custom CSS. Unrelated or unsupported CSS remains untouched.

CSS Sync respects the active breakpoint and pseudo-class. If the same property is defined in Custom CSS and a style control, Custom CSS takes precedence in the builder and on the frontend.

## Code Element (PHP, HTML, CSS, JS) {#code-element}

The **Code** element lets you place PHP/HTML, CSS, and JavaScript at a specific location in the page output.

By default, code entered in the Code element is displayed as a formatted code snippet. To execute PHP/HTML output instead, enable the element's **Execute code** setting.

The Code element has separate editors for:

- **PHP and HTML**: Can be rendered as a code snippet or executed when **Execute code** is enabled.
- **CSS**: Automatically wrapped in `<style>` tags when executed, unless you already include style tags.
- **JavaScript**: Automatically wrapped in `<script>` tags when executed, unless you already include script tags.

### Enable code execution

To execute Code element PHP/HTML, first enable **Code execution** under **Bricks > Settings > Custom code**.

Code execution has two layers:

- The global **Enable code execution** setting must be enabled.
- The user must have the Bricks **Execute code** capability, either through their role or an individual user-profile override.

If code execution is disabled, or if your user does not have the capability, Bricks does not show the executable controls and displays a "Code execution not allowed" notice.

![](https://academy.bricksbuilder.io/assets/bricks-builder-code-execution-1024x803.png)

<figcaption>

Code execution enabled for the Administrator role

</figcaption>

Make sure to only enable code execution for users and roles you trust.

Code execution can also be disabled by code using the `bricks/code/disable_execution` filter. Older sites may still use the deprecated `bricks/code/allow_execution` filter set to `false`; that also disables execution.

### Code signatures

Executable code only runs when code execution is enabled and the saved code has a valid code signature. Regenerate code signatures whenever your WordPress salts or secret keys change.

Code signatures apply to executable Bricks code such as Code element PHP/HTML, SVG element source code, Query editor code, component query properties, and global query records. Changing signed code invalidates the old signature until the code is signed again.

See [Code signatures](https://academy.bricksbuilder.io/builder/features/code-signatures/) for signing workflows, global regeneration, and the dangerous automatic signing constants.

### How to add PHP and HTML code to your element {#execute}

![](https://academy.bricksbuilder.io/assets/bricks-builder-code-element-execution.png)

<figcaption>

Code Element: Executing HTML and PHP code

</figcaption>

1. Add a **Code** element to the canvas.
2. Enter PHP/HTML in the **PHP and HTML** editor.
3. Enable **Execute code**.
4. Review the code.
5. Click the **Sign code** icon at the top-right of the code editor, or use `CMD/CTRL + R`.
6. Save the page.

When **Execute code** is enabled, Bricks verifies the code signature before running the PHP/HTML. If the signature is missing or invalid, Bricks renders an error placeholder instead of executing the code.

The Code element also has optional execution settings:

- **Parse dynamic data**: Parses Bricks dynamic data inside the executable PHP/HTML.
- **Suppress PHP errors**: Hides PHP errors unless the URL includes `brx_code_errors`.
- **Render without wrapper**: Outputs the executed result without the Code element wrapper on the frontend.

## Security checklist

Before enabling or signing executable code:

- Grant code execution to the fewest trusted users possible.
- Prefer page-specific or element-specific CSS/JS when PHP is not needed.
- Review the code before signing it.
- Re-sign code after editing it.
- Regenerate signatures after changing WordPress salts.
- Run a Code review before global signature regeneration.

### HTML Code Completion via Emmet

You can use abbreviations to generate your HTML structures much faster via a familiar CSS-based syntax.

**Abbreviation:** `#header` (+ TAB key)

**Generates:**

```html
<div id="header"></div>
```

**Abbreviation:** `h$[title=item$]{Header $}*3`

**Generates:**

```html
<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>
```

[https://docs.emmet.io/cheat-sheet/](https://docs.emmet.io/cheat-sheet/)

---

# Element Conditions

Source: https://academy.bricksbuilder.io/builder/features/element-conditions/

*Use Bricks element conditions to show or hide content based on post data, user state, query results, and other runtime rules.*

Element Conditions let you define one or multiple conditions for any element. Only if those conditions are met is the element rendered on the front end.

Conditions are validated server-side and are meant to filter out/not load an element based on data (post, user, dynamic data, date & time, etc.).

Not rendering an element means **the element HTML doesn't exist in the source code**.

https://youtu.be/w8DW0VH-4pc

This is perfect for restricting content to logged-in users or users with a specific role (e.g., membership sites) to hide time-sensitive information according to a certain weekday/date/time, according to dynamic data, etc.

Element conditions are display logic. They are useful for hiding interface, marketing, membership, or product-state content, but they are not a replacement for server-side permissions around truly sensitive data, downloads, or actions. For example, hiding a download button removes the link from the page, but anyone who already has the file URL can still open the file. Protect private files and actions with your membership, file protection, or permission setup.

If you need full programmatic power to define your element conditions, use the [bricks/element/render](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-render/) Bricks filter.

## Accessing conditions

When editing an element, click the "Conditions" (toggle) icon in the panel header to open/close the element conditions interface. You'll see the "Conditions" toggle icon in the structure panel if an element has conditions. Click the icon to jump right into the conditions interface for this element.

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-toggle.png)

## How element conditions work

At least one set of conditions must be fulfilled to render the element. This means all conditions inside a condition "set" must be evaluated to be true.

So there is an OR relationship between condition sets and an AND relationship between conditions inside a set.

> **Note**
>
> Element conditions are evaluated when each element renders on the frontend. In the builder dynamic area, Bricks renders elements even when their conditions would fail, so you can keep editing them. Inside a query loop, conditions run with the current loop object, so they can show or hide that element per loop item. Use query settings or filters when you need to remove items from the query result set itself.

To add your first set of conditions, click the "+" icon next to the "Conditions" title:

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-add-condition.png)

We now have one set with one condition. Every condition consists of the following three properties:

- **Key** (post ID, user role, date, dynamic data, etc.)
- **Comparison operand** (==, !=, >, &lt;, contains, before, after, etc.)
- **Value** (numeric, text, checkbox, select option(s), etc.)

Built-in condition groups include:

- **Post**: post ID, title, parent, status, author, date, and featured image.
- **User**: login state, user ID, registration date, and role.
- **Date & time**: weekday, date, time, and datetime. These use the WordPress site timezone.
- **WooCommerce**: product type, sale/new/stock states, stock quantity, stock management, sold individually, purchased by current user, featured status, rating, product categories, and product tags. This group is available when WooCommerce is active.
- **Other**: dynamic data, browser, operating system, current URL, and referrer URL.

The **Current URL** condition includes query parameters. Browser, operating system, and referrer checks depend on request headers, so treat them as convenience targeting rules rather than trusted security checks.

Let's say we want to show an element only to logged-in users. We'd create the following condition:

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-user-is-logged-in.png)

This element is only rendered when the person viewing this page is logged in.

Non-logged-in guests, bots, crawlers, etc., will not be able to see this element (as it's not in the source code).

## Conditions indicator

Notice the highlighted "Conditions" icon in the screenshot above. It's a great indicator to see at a glance if the element you are editing has any conditions (without having to open the conditions interface).

The "Conditions" (toggle) icon is also visible next to an element in the structure panel to quickly scan for element conditions on your page. A click on it brings you right into the conditions interface.

## Checking multiple conditions

Between a set of conditions exists an **OR** relation. And conditions within a set have an **AND** relation.

Let's create a second set of conditions (by clicking the "+" icon at the top-right again) to illustrate this.

The condition in this new set is fulfilled (true) if the post title is "Account".

As there is an OR relation between condition sets, the element is rendered if (1) the user is logged in **OR** (2) the title of the post/page being viewed is "Account".

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-groups.png)

## Combining AND & OR conditions

Let's extend the conditions for this element by checking if the logged-in user has been registered before the 1st of Jan 2022.

As there is an AND relation between conditions inside a set, click the "+" button on the bottom-right of the first condition to add another condition to this first set:

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-and-or.png)

You'll also notice the vertical "**AND**" label between conditions inside a set.

And the horizontal "**OR**" label between condition sets.

This visualizes the element conditions logic.

### Repeat shared conditions in every set {#repeat-shared-conditions}

Bricks checks each set on its own. Inside a set, it stops at the first condition that fails and moves on to the next set. A condition in one set does not apply to the other sets.

If a requirement applies in every case, add it to each set. For example, a "Download recipe card" button should appear for logged-in visitors, or on recipes that are free for everyone, but only when the recipe actually has a card file:

- **Set 1**: User login **is** Logged in, AND Dynamic data `{acf_recipe_card}` **is not empty**
- **Set 2**: Dynamic data `{acf_card_access}` **==** `Everyone`, AND Dynamic data `{acf_recipe_card}` **is not empty**

Without the card check in the second set, a free recipe without a card file would still render the button.

## Show content only when a field has a value {#empty-fields}

A single post template often contains sections that only some posts can fill, such as a video, a download, or a "Chef's tip" box. Without a condition, posts that leave the field empty still render the section's heading and an empty player or box.

Add a **Dynamic data** condition to the section, pick the field, and set the comparison to **is not empty**. Leave the value empty. The section then renders only on posts where the field has content.

<div className="screenshot screenshot--control-panel">

![Conditions panel for a Section named Video with one condition: Dynamic data, {acf_recipe_video}, is not empty.](https://academy.bricksbuilder.io/assets/element-conditions-dynamic-data-is-not-empty.webp)

</div>

**is empty** and **is not empty** are available for the **Dynamic data** condition. They check whether the rendered output of the tag is an empty string, so a field that was never filled in counts as empty, the same as a field that was cleared. Use **is empty** to show fallback content in the posts that have no value.

## Comparison behavior

`==` and `!=` comparisons use PHP-style loose comparison and convert common boolean-like values such as `true`, `false`, `1`, `0`, and empty strings before comparing. Numeric comparisons (`>`, `<`, `>=`, `<=`) compare the resolved values directly.

For multi-select values such as user roles, post statuses, WooCommerce product categories, and product tags, `is` matches if any selected value overlaps. `is not` matches when there is no overlap.

The `contains` and `does not contain` comparisons are string checks. Use them for text-like values such as post titles, dynamic data output, URLs, and referrers. Both return false when the checked value is empty, so a `does not contain` condition hides the element on posts where the field has no value. Add a separate set with **is empty** if those posts should still show the element.

If you leave the comparison empty, the condition uses `==`.

### How to compare dynamic data against the value {#dynamic-data}

> **Note**
>
> The element conditions, by default, compare against the label.

Certain dynamic data provider fields allow you to specify the value & label (e.g., [ACF true false](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/#acf), Metabox checkbox list, radio, select, etc.).

To compare against the value instead, you can use the `:value` filter like this:

![](https://academy.bricksbuilder.io/assets/bricks-1.5.7-dynamic-data-value-filter.png)

In the example above, the condition is fulfilled when the Metabox checkbox list has the `blue` value selected. Without the `:value` filter, the condition would compare against the checkbox option label.

## WooCommerce checkout and order conditions {#woocommerce}

Bricks 2.4 adds WooCommerce conditions for checkout and order-aware layouts:

- **Checkout : Login step needed**
- **Checkout : Needs shipping**
- **Checkout : Needs shipping address**
- **Checkout : Order has status**
- **Order : Needs shipping address**
- **Order : Has downloads**

Use these conditions inside WooCommerce v2 checkout, pay, thank-you, order receipt, account view-order, and other order-aware layouts when content should only appear for a matching checkout or order state.

**Checkout : Login step needed** is **Yes** only for a logged-out customer when **WooCommerce > Settings > Accounts & Privacy > Enable log-in during checkout** is enabled. The generated [Checkout v2 multistep structure](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/#account-login-step-visibility) uses it to keep the Account Login navigation item, step, and Customer info Back button in sync.

**Checkout : Needs shipping** checks whether the non-empty cart contains products that require shipping. Use it for shipping methods and any Checkout v2 section or step that customers need to access to choose a shipping method.

**Checkout : Needs shipping address** checks whether WooCommerce needs a separate shipping address. This can return **No** when WooCommerce is set to force shipping to the billing address, even though the cart still requires shipping and customers still need to choose a shipping method.

For a Checkout v2 layout, apply **Checkout : Needs shipping** to the Shipping options wrapper. In a multistep layout, apply the same condition to both the Shipping step and its matching navigation item. Apply **Checkout : Needs shipping address** only to the **Ship to another address** control and shipping-address fields.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#conditions) for the related WooCommerce v2 data reference.

### Order withdrawal screen

With advanced modular elements and WooCommerce Order Withdrawal enabled, use **Order withdrawal screen** inside the [Account Page v2 withdrawal state](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/#order-withdrawal). Compare with **Your details**, **Review**, or **Confirmation** using **is** or **is not**. The generated structure includes these conditions. They control frontend output; all three sections remain visible in the builder.

## Element Conditions API {#api}

The following information is intended for developers who wish to extend the default element conditions interface programmatically (`@since 1.8.4`).

The custom element condition should resemble the following example:

![](https://academy.bricksbuilder.io/assets/custom-condition-in-bricks.png)

<figcaption>

Builder: New condition group with "Post type" option

</figcaption>

### Step 1: Add condition group via filter:  bricks/conditions/groups {#bricks-conditions-groups}

```php
add_filter( 'bricks/conditions/groups', 'add_my_condition_group' );
function add_my_condition_group( $groups ) {
  // Ensure your group name is unique (best to prefix it)
  $groups[] = [
    'name'  => 'my_group',
    'label' => esc_html__( 'My Group', 'my-plugin' ),
  ];

  return $groups;
}
```

### Step 2: Add condition options via filter: bricks/conditions/options {#bricks-conditions-lists}

In this example, create a new condition to compare the current page post type with the user's value. The compare control is a dropdown with "is" and "is not" options. The value field type is a `text` input.

```php
add_filter( 'bricks/conditions/options', 'add_my_custom_condition' );
function add_my_custom_condition( $options ) {
  // Ensure key is unique, and that group exists
  $options[] = [
    'key'   => 'my_post_type',
    'label' => esc_html__( 'Post Type (New)', 'my-plugin' ),
    'group' => 'my_group',
    'compare' => [
      'type'        => 'select',
      'options'     =>  [
        '==' => esc_html__( 'is', 'my-plugin' ),
        '!=' => esc_html__( 'is not', 'my-plugin' ),
      ],
      'placeholder' => esc_html__( 'is', 'my-plugin' ),
    ],
    'value'   => [
      'type'        => 'text',
    ],
  ];

  return $options;
}
```

![](https://academy.bricksbuilder.io/assets/custom-condition-in-bricks-example01.png)

<figcaption>

Expected result: New condition in the builder

</figcaption>

### Step 3: Execute your logic to return a Boolean result via filter: bricks/conditions/result {#bricks-conditions-result}

Based on your custom logic, return `true` or `false` for your condition. Bricks take care of the `OR` and `AND` conditions.

In this example, we check if the current post type matches the user value.

If the condition is met, return `true`.

You can access the `$condition` variable, which has been set inside the builder.

```php
add_filter( 'bricks/conditions/result', 'run_my_custom_condition', 10, 3 );
function run_my_custom_condition( $result, $condition_key, $condition ) {
  // If $condition_key is not 'my_post_type', we return the $render as it is
  if ( $condition_key !== 'my_post_type' ) {
    return $result;
  }

  // Now you can perform your logic by using the $condition variable
  // $condition['compare'] is the compare operator, might be empty
  // $condition['value'] is the user value, might be empty

  // In my example, if compare is empty, we set it to '==' as default
  $compare    = isset( $condition['compare'] ) ? $condition['compare'] : '==';
  $user_value = isset( $condition['value'] ) ? $condition['value'] : '';

  $condition_met = false;

  // Get the current post type of the page
  $current_post_type = get_post_type();

  switch( $compare ) {
    case '==': // "is"
      $condition_met = $current_post_type === $user_value;
      break;
    case '!=': // "is not"
      $condition_met = $current_post_type !== $user_value;
      break;
  }

  return $condition_met;
}
```

If you have added multiple options under the same group, you can target them like this:

```php
add_filter( 'bricks/conditions/result', 'run_my_custom_condition', 10, 3 );
function run_my_custom_condition( $result, $condition_key, $condition ) {

  $condition_options = \Bricks\Conditions::$options;
  $registered_condition = null;

  foreach ( $condition_options as $option ) {
    if ( isset( $option['key'] ) && $option['key'] === $condition_key ) {
      $registered_condition = $option;
      break;
    }
  }

  if ( ! $registered_condition || $registered_condition['group'] !== 'my_group' ) {
    return $result;
  }
  // Now you can perform your logic by using the $condition variable
  // $condition['compare'] is the compare operator, might be empty
  // $condition['value'] is the user value, might be empty

  $condition_met= false;

  switch( $condition_key ) {
    case 'my_condition_option_1':
      // Example
      $condition_met = execute_my_logic_1( $condition );
      break;
    case 'my_condition_option_2':
      // Example
      $condition_met = execute_my_logic_2( $condition );
      break;
  }

  return $condition_met;
}
```

---

# Global Elements

Source: https://academy.bricksbuilder.io/builder/features/global-elements/

*Review legacy global elements in Bricks, convert them to components, and understand why new reusable work should use Components instead.*

> **Note**
>
> **Global elements are deprecated since Bricks 2.0. Use Components for new reusable builder structures, and convert existing global elements as soon as possible.**

Global elements remain visible for sites that already use them, but they are now a legacy feature. New reusable work should be created as [Components](https://academy.bricksbuilder.io/builder/features/components/), not as global elements.

## Review existing global elements

To find existing global element instances:

1. Go to `Bricks > Settings > General`.
2. Scroll to **Global elements** under the **Convert** section.
3. Start the global-elements review to retrieve a list of global element instances.

From there, review the affected pages and templates before converting, unlinking, or deleting anything.

## Convert to components

Use the converter under `Bricks > Settings > General > Convert` to convert global elements to components.

Bricks can convert global elements individually or in bulk. Nestable global elements cannot always be converted directly to components; in those cases, unlink them manually in the builder or use the converter flow that unlinks nestable global elements.

After conversion, delete the remaining global elements from the builder's elements panel.

## When to use templates instead

If you need to reuse a larger section or layout pattern without linked shared editing, save it as a template and insert it where needed. For linked reusable structures, use Components.
