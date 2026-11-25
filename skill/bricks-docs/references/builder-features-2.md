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
- Show and filter components by element type (Bricks 2.5).
- Filter by usage: all usage, used on current page, used elsewhere, or unused.
- Switch between grid and list view.
- Import component JSON or ZIP files.
- Edit, duplicate, export, delete, or generate a screenshot for a component.
- Generate screenshots for the currently filtered component list.

Generating component screenshots requires the **Edit components** builder permission. Component import and export require the **Import/export components** builder permission. The **Used elsewhere** filter only shows components that are not used on the current page but are used on another page or template.

**Component screenshots** are enabled by default on new installations under **Bricks > Settings > Templates & components**. Disable the setting to stop automatic and manual generation and hide stored local thumbnails. Disabling it does not delete existing screenshot files. Use **Delete screenshots** in the same settings section to remove all generated component screenshots.

![](https://academy.bricksbuilder.io/assets/bricks-browser-component-manager.webp)

### Element types

Since Bricks 2.5, the Components browser can show each component's element type and filter the library by it. The element type is the component's root, its outermost element, such as a Section, Container, Block, Div, or Heading. Check it before inserting a component to see what kind of element you are adding.

Element types are hidden by default. To show them, click **More** (the three-dot icon) in the toolbar and enable **Show element type**. Bricks remembers this choice in your current browser.

![More menu in the Components browser with Show element type enabled. Element type labels appear on the component cards and the Element type filter shows All (25).](https://academy.bricksbuilder.io/assets/components-browser-show-element-type.webp)

With the setting enabled:

- Each component shows its element type as a label in the top-left corner of the card in grid and masonry views, or at the end of the row in list view.
- An **Element type** dropdown appears in the toolbar. Select a type, or choose **All** to remove the type filter.

![Components browser in list view with the Element type menu open, listing each type with its component count, and element type labels at the end of each row.](https://academy.bricksbuilder.io/assets/components-browser-element-type-filter.webp)

The menu lists the types available in the current results, with a component count for each. Search, category, and local usage filters narrow these options and counts. For example, select your page-section category, then choose **Section** to find components whose outermost element is a Section.

Changing the type returns to the first page of results. If another filter removes every component of the selected type, the type filter returns to **All**. Disabling **Show element type** also resets the filter to **All**, so a hidden filter never narrows your results.

Remote components use the element type supplied by their source site. If that information is unavailable, the component has no type label and appears under **All**, but not under a specific type.

### Sorting and importing components

Since Bricks 2.5, use **Sort by** in the Components browser toolbar to choose **Newest**, **Oldest**, **Title A–Z**, or **Title Z–A**. **Newest** is the default. Date sorting uses creation dates, including for remote components.

Click **Import** in the toolbar to import component JSON or ZIP files into the local library. This action requires the **Import/export components** builder permission. When an import switches you from a remote source to the local library, the usage filter is cleared so it does not hide the imported components.

![Components browser with the sort menu open and arrows pointing to the sorting control and Import button.](https://academy.bricksbuilder.io/assets/builder/browser-sorting/components-browser-sorting-import.webp)

### Organize components into categories {#component-categories}

Since Bricks 2.5, the Components browser has a **Categories** sidebar. It lists **All components**, **Uncategorized**, and each category with its component count. Click a row to filter the library. Drag the sidebar edge to resize it, or use the arrow button to collapse it.

Each component belongs to one category at a time. You can assign categories in three ways from **My components**:

- **Drag and drop:** Drag a component card onto a category in the sidebar. If the card is selected, Bricks moves every selected component, including selections on other pages. An unselected card moves on its own. Drop onto **Uncategorized** to remove the category. If the sidebar is collapsed, hold the dragged card over the expand button to open it.
- **Assign category:** Select components with their checkboxes. In the selection toolbar, click **Assign category**, choose a category, and click **Apply**. To create a category, type a new name in the picker and choose the `Create "name"` option before you apply it.
- **Create category:** With components selected, enter a name in the **New category name** field below the category list and click **Create category**. Bricks assigns the selected components to it. If a category with the same name already exists, ignoring letter case, Bricks uses that category instead of adding a duplicate.

Each assignment is a single undo step. Click the info icon in the sidebar header to show a short version of these instructions.

Categories exist only while at least one component uses them. If you move the last component out of a category, the category disappears from the sidebar.

Category labels are hidden on component cards by default. To show them, open the **More** (three dots) menu in the toolbar and enable **Show category**. Bricks stores this choice in your browser. Click a category label on a card to filter the library to that category.

Assigning categories requires the **Edit components** permission. Remote libraries and users without that permission can browse categories, but cannot change them. Save in the Builder to keep the changes.

![Components browser with two selected components. The Categories sidebar shows counts, the help text, and a New category name field filled with Hero sections above the Create category button.](https://academy.bricksbuilder.io/assets/builder/release-2.5/component-category-sidebar.webp)

![Assign category picker with Uncategorized, Atelier North, and Studio essentials options, plus Cancel and Apply buttons.](https://academy.bricksbuilder.io/assets/builder/release-2.5/component-category-picker-detail.webp)

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
- **Variants** (drop icon): Open the Variants panel.
- **Properties** (box icon): Open the component properties panel.
- **Instance** (arrow icon): Exit component edit mode and return to the instance you were editing before, or to the Components library. Pressing the Escape key also exits the main component.

When editing the main component, you can see and edit all elements of this component in the structure panel:

![](https://academy.bricksbuilder.io/assets/bricks-components-main-component-structure-panel.png)

To edit the title of a Card component, select the Heading element inside the component and change its text to `Just a card`.

All instances of the Card component automatically reflect this change:

![](https://academy.bricksbuilder.io/assets/bricks-components-edit-component-heading.png)

This is useful for shared structure and design. The real power of components comes from combining shared structure with properties that can be customized per instance.

## Recover an earlier component {#history}

Since Bricks 2.5, use **Revisions** on a component row in the Components panel, or on a component in the Browser, to open that component's earlier versions. Component revisions include a rendered preview and changed values named by element label. Restoring one component keeps unrelated components at their current versions. See [Global data revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/) for permissions, deleted-item recovery, and the behavior inside drafts.

## Properties {#properties}

Properties let you expose controls for customization on each instance.

For example, a Card component can expose a card title property and a card image property. Each Card instance can then use different content while still sharing the same component structure and styling.

To connect a property directly to a control, follow these two steps:

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
| Repeater _(@since 2.5)_       | Native repeater controls and Array queries      | Testimonials, FAQ or card lists    |
| Global classes _(@since 2.0)_ | Global classes controls                        | Element global classes            |

![](https://academy.bricksbuilder.io/assets/bricks-2.0-components-create-property-form.png)

The **property name** is mandatory. Choose a descriptive name, especially for complex components with many properties.

The **property description** is optional, but it helps other builders understand how the property should be used.

The **property group** is optional and helps organize properties inside the instance panel.

The **default property value** is optional. It is used when an instance has not set its own value. If an instance value is cleared or reset, Bricks removes the override so the default value can apply again. Repeater properties distinguish an intentionally empty row list from a reset; see [instance rows and defaults](#repeater-instance-defaults).

### Creating Properties from Content {#create-properties-from-content}

Since Bricks 2.5, **Create properties from content** creates and connects several properties in one step. Use it after building a component's content, such as a card with a heading, image, and button.

Open the component's **Properties** panel and click **Create properties from content**. Bricks detects these controls in the main component:

| Element | Detected content |
| --- | --- |
| Heading, Basic Text | Text |
| Rich Text | Rich text |
| Image | Image and alternative text |
| Button | Text and link |
| Icon | Icon |

The scan stops at nested component instances. Edit a nested component's own properties separately.

1. Review the detected rows and deselect content that should stay fixed. Hover a row to locate its element on the canvas and in the Structure panel.
2. Give each property a clear name. Open its **More** menu to edit its description, default value, and group. The element's existing content supplies the initial default.
3. Drag rows to change their order. Use **Groups** to create or edit groups, then assign rows with the group selector or drag them into a group.
4. Click **Create and connect** to apply the selected properties and their connections. If you are only editing existing properties, the button reads **Save**.
5. Save in the Builder, then select an instance to customize the new properties.

Search and group filters help narrow the list. **Select all** applies to the unconnected rows in the current search and group. Existing connected properties retain their connections while you edit their names, defaults, descriptions, groups, or order.

Closing and reopening **Groups** keeps your pending changes while you remain in the creation panel. **Cancel** or the back arrow leaves the creation panel without applying the pending changes.

<div className="screenshot screenshot--control-panel">

![Create properties panel with six selected properties, condition icons, and the Create and connect button.](https://academy.bricksbuilder.io/assets/bricks-components-create-properties-from-content.webp)

</div>

#### Hide If Empty {#hide-if-empty}

For newly selected content, enable **Hide if empty** from the row's condition icon or **More** menu. This requires access to element conditions. Bricks adds a connected **Dynamic data → is not empty** condition to the element. You can inspect or edit it in the element's [Conditions](https://academy.bricksbuilder.io/builder/features/element-conditions/) panel afterward.

For a Button, both its text and link must resolve to non-empty values. Image alternative text is not used to decide whether an Image should render. If the element already has multiple condition groups, the presence check is added to each group so the existing OR logic is retained.

The check uses the resolved property value, including its default. Clearing an instance's text or rich-text value restores the default. If that default contains content, the element stays visible. For an optional text field, clear its property default too, then enter text only on the instances that need it.

Rich-text markup such as `<p><br></p>` still counts as content for this comparison. Remove the markup as well if the field should be empty. Check the frontend result: element conditions keep elements available for editing in the Builder.

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

#### Disconnect All Connections {#disconnect-all}

Since Bricks 2.5, you can disconnect a property everywhere it is used inside the main component:

1. Open the component's **Properties** panel.
2. Find the connected property and click **Disconnect all** on its row.
3. Confirm the dialog, then save in the Builder.

The property, its default value, and its group remain available, so you can connect it again later. The action removes that property's control connections and connections forwarded to nested component instances inside the main component. Other properties keep their connections.

Disconnected controls return to their own saved settings. Inline references such as `{prop.title}` are replaced with the property's default value, rather than the value of the instance you happen to be editing. Review the affected content and conditions before saving, especially if the component's instances had different values.

If Bricks cannot safely replace a reference, it leaves the component unchanged and identifies the reference to resolve first. Fix or remove that reference, then try **Disconnect all** again. Choosing **Cancel** in the confirmation dialog also leaves the connections intact.

![The FAQ items property row with the Disconnect all button highlighted and its tooltip visible.](https://academy.bricksbuilder.io/assets/bricks-components-disconnect-all.webp)

## Repeater Properties {#repeater-properties}

Since Bricks 2.5, a **Repeater** property lets each component instance manage a list of structured items. Use it for FAQs, testimonials, pricing features, or cards whose layout stays the same while their content and number of items change.

A repeater property can supply an element's native repeater control or an Array query loop inside the component.

### Define fields and default items

1. Edit the main component and open **Properties**.
2. Create a property with **Type** set to **Repeater** and name it `Cards`.
3. Under **Fields**, add `Title` (Text), `Image` (Image), and `Link` (Link).
4. Use **Add item** in the default-value editor to enter the initial rows.
5. Save the property, then connect it to the content it should control.

Supported field types are **Text**, **Rich text**, **Image**, **Link**, **Select**, **Toggle**, and **Repeater**. For Select fields, enter one option per line. A nested Repeater contains another set of fields; Bricks supports two repeater levels in total.

<div className="screenshot screenshot--control-panel">

![Cards has Title, Image, and Link fields and two default items, Lake Bohinj and Soča Valley.](https://academy.bricksbuilder.io/assets/component-repeater-cards-fields.webp)

</div>

### Repeat a custom layout

Use a query loop to design each item with ordinary Bricks elements.

1. Inside the main component, create a Block containing a Heading, Image, and Button. This Block is the layout for one card.
2. Enable **Query loop** on the Block.
3. Open the property connection control for its **Query** and select `Cards`. Bricks supplies an Array query from the repeater rows.

   ![The Card Block’s Query is connected to Cards, and two destination cards appear on the canvas.](https://academy.bricksbuilder.io/assets/component-repeater-cards-query.webp)

4. Select each child element and use its property connection control to connect the Heading text to the Title field, the Image to the Image field, and the Button link to the Link field of Cards.

   ![The selected destination Heading is connected to Cards.Title and displays Lake Bohinj in the first card.](https://academy.bricksbuilder.io/assets/component-repeater-title-connection.webp)

5. Exit component editing and edit the Cards rows on the instance.

The loop repeats the Block for each row. Compatible Array-query options, including offset, results conditions, and pagination, remain available. A repeater property can supply multiple queries, but each query takes its rows from one source property.

#### Use field tags in text

Each field exposes a copyable **Field tag**. For a field whose key is `title`, the tag is:

```text
{query_array @key:'title'}
```

Use the copied tag inside the matching repeater query loop. It also works in mixed text, such as `Read more about {query_array @key:'title'}`. Copy the actual tag from the field editor: changing a field's display name does not change its saved key.

Image and Link field tags include the field type so Bricks can resolve their structured values in compatible image and link controls:

```text
{query_array @key:'image' @field-type:'image'}
{query_array @key:'link' @field-type:'link'}
```

For general Array-query syntax and nested loops, see [Query Type: Array](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#array).

### Connect a native repeater

For elements that already have an item list, such as Testimonials, connect the property directly to that repeater control.

To start from existing content, open the repeater's property connection menu and create a new property there. Bricks creates supported fields, default rows, and mappings from the native items.

To use an existing Repeater property, connect it to the item list, then open the visible template item and connect its compatible controls to the repeater fields. Field names do not need to match the element's control names. For example, a field named `Quote` can supply the testimonial content control.

Unconnected controls keep the fixed values from the first native item. Unsupported field types, such as Number and Icon, can remain fixed this way. **Auto create and populate properties** adds missing supported fields and connections without replacing existing mappings or row values.

### Edit instance rows and defaults {#repeater-instance-defaults}

Select an instance to add, edit, duplicate, remove, or drag rows into a different order. These changes affect that instance only.

An instance without its own rows uses the property's default rows. Deleting every row creates an intentionally empty list; it does not restore the defaults. Reset the property to inherit its defaults again. Repeater properties also support row editing in [Components as Blocks](https://academy.bricksbuilder.io/integrations/gutenberg/components-as-blocks/).

### Change fields and forward nested properties

Renaming a field keeps its key and existing values. Deleting a field removes it from the editable schema, so update copied tags and nested connections that reference it.

Changing a saved field to an incompatible type creates a new key and clears its default. Existing instance values are not converted. Changes between Text, Rich text, and Select preserve the field key.

When forwarding a Repeater property through a nested component, the parent and child definitions must have matching field keys and types, including nested fields. Creating the parent property from the child's connection control copies its field definitions. Disconnect the forwarding before making incompatible changes to either definition.

## Properties as Dynamic Data {#property-dynamic-data}

Since Bricks 2.5, insert a component property into dynamic-data-enabled content with `{prop.key}`. Combine a property with surrounding text, use it in a condition, or reuse it in a supported field without connecting the entire control to that property.

### Copy a property reference

Open the main component's **Properties** panel and edit a property. Its **Reference key** identifies it within that component. Use the copy button to copy its tag, such as `{prop.title}`.

Choose the key when creating the property. It must be unique within the component and contain lowercase letters, numbers, and underscores, starting with a letter or underscore. Once created, the key is read-only. Renaming the property label does not break its references.

<div className="screenshot screenshot--control-panel">

![The Title property has the reference key title and a button to copy its tag.](https://academy.bricksbuilder.io/assets/component-property-reference-key.webp)

</div>

### Mix property values with text

For a promotion component with Text properties using the keys `title` and `price`, enter this in a Basic Text element inside the main component:

```text
Book {prop.title} for {prop.price}.
```

Each instance supplies its own title and price. An instance without an override uses the property default. Clearing a text override restores the default; `0` and Toggle `false` remain explicit values.

In supported text controls, type `{prop.` to see property suggestions, or select a property from the dynamic data picker. Bricks also flags incomplete, missing, or unsupported references in the Builder.

### Images, links, and conditions

Use a full Image or Link property in a compatible image or link control. To use a single value in text, select a supported field:

| Property | Example | Value |
| --- | --- | --- |
| Image | `{prop.photo.url}` | Image URL |
| Image | `{prop.photo.id}` | Attachment ID, when available |
| Image | `{prop.photo.alt}` | Image alternative text |
| Link | `{prop.cta.url}` | Resolved link URL |

Replace `photo` and `cta` with your actual reference keys. A whole structured Image or Link value cannot be printed as ordinary text.

For a conditional offer label, add a **Dynamic data** [element condition](https://academy.bricksbuilder.io/builder/features/element-conditions/), enter `{prop.offer}`, and compare it with the value you want to match. The condition uses the current instance's resolved value, including its default when no override is present.

### Scope and supported output

Property keys belong to their component. The same key can exist in different components without sharing values. A reference outside a component instance cannot read a property from an unrelated component on the page. To pass values into a nested component, connect its properties to the parent properties.

Property references are intended for content and supported settings. They do not substitute editable values into CSS, JavaScript, executable PHP source, or executable HTML attributes such as `onclick` and `style`.

A [Code element](https://academy.bricksbuilder.io/builder/elements/general/code/#component-properties) inside a component can render property tags in its HTML output when **Execute code** and **Parse dynamic data** are enabled. PHP code can read typed values with `bricks_get_component_property()`.

Deleting a property can leave unresolved references. Review the locations shown in the deletion warning and replace or remove those references before saving. Unlinking a component replaces supported references with resolved instance values; Bricks stops the unlink operation when a reference cannot be replaced safely.

## Customizing an Instance

Select a component instance to customize the properties exposed by the main component. Properties used through control connections or [dynamic data references](#property-dynamic-data) appear in the instance controls.

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

https://youtu.be/BIjKNV_4W_Q

Variants give one component more than one look. All variants share the same content, structure, and properties. Only the styles differ. Each instance then picks the variant it uses, so a page that needs a different look does not need a second component.

Examples:

- Primary and secondary button styles.
- Card layouts with different spacing.
- Light and dark versions of the same component.
- A standard and a more prominent page hero.

Variant styles are saved on the component definition. The selected variant is saved on the instance.

### Add a Variant {#add-variant}

1. Edit the main component.
2. In the control panel header, click **Variants** (drop icon). The tooltip shows how many variants the component has.
3. The first row is the base look. Naming it is optional. Without a name, it shows as **Base**.
4. Click **Add Variant**. Bricks adds a variant named `Variant 1` (the next one is `Variant 2`, and so on) and makes it the active variant. Rename it in place, for example to `Prominent`.
5. Close the Variants panel.

<div className="screenshot screenshot--control-panel">

![Variants panel of the Page hero component in edit mode, with the Base row, a variant named Prominent, and the Add Variant button.](https://academy.bricksbuilder.io/assets/bricks-component-variants-panel.webp)

</div>

With more than one variant, drag a variant by its handle to change the order.

### Style a Variant {#style-variant}

When you close the Variants panel, a **Variant** select appears at the top of the control panel. It shows which variant you are styling. It is hidden while the Variants panel is open.

With a variant selected, select any element of the component and change its style settings, such as background, spacing, or typography. Bricks saves these settings for the selected variant only, including settings on other breakpoints.

Content, structure, and properties stay shared. If you edit a text or add an element while a variant is selected, the change applies to every variant.

To edit the base look again, set the Variant select back to **Base**.

### How Variants Inherit From the Base {#variant-inheritance}

A variant stores only the settings you change while it is selected. Everything else comes from the base.

When you later change the base, the change reaches every variant that does not set the same setting itself. For example, if you center the content in the base, both looks are centered, because the variant does not set the alignment. If you change the title color in the base, a variant that sets its own title color keeps it.

### Choose a Variant on an Instance {#instance-variant}

Select an instance on a page. If its component has variants, a **Variant** select appears above the properties. Leave it on **Base** or pick a variant. The choice applies to this instance only. Other instances of the same component keep their own variant.

When a component is enabled as a block, the component block in the block editor has the same **Variant** select.

![Page hero instance selected in the Builder, with the Variant select above Properties set to Prominent and the dark Prominent look on the canvas.](https://academy.bricksbuilder.io/assets/bricks-component-instance-variant-select.webp)

### Delete a Variant {#delete-variant}

Open the Variants panel and click the trash icon next to the variant. After you confirm, Bricks removes all styles of that variant, and instances that used it switch back to the base.

### Variants, Properties, or Global Classes {#variants-or-properties}

- Use a variant when instances need a different look of the whole component, with several style changes that belong together.
- Use a property when each instance needs its own value, such as a text, an image, a link, a query, or a toggle. See [Properties](#properties).
- Use a global class when the same style should apply to elements in different components and pages. To let each instance choose classes, use the [Global classes property](#global-classes).

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
- Component properties are definitions. A property exposes an instance value when it is connected to compatible controls or used through a supported dynamic data reference inside the component.
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

#### Date and time meta {#date-and-time-meta}

In Bricks 2.5, a **Datepicker** field with **Enable time** and **Disable calendar** turned on collects a time without a date. See the [Form date and time picker settings](https://academy.bricksbuilder.io/builder/elements/general/form/#timepicker) for the field configuration.

To save an appointment time:

1. Add a mapping under **Post meta** in the **Create post** or **Update post** action.
2. Set **Meta key** to your custom field key, such as `appointment_time`.
3. Set **Meta value** to the time-only form field.
4. Set **Sanitization method** to **Text (sanitize_text_field)** so the colon and minutes are preserved.

For ordinary WordPress post meta, selecting `14:30` saves `14:30`. **Update post** preserves time-only values instead of converting them to a date. Datepicker fields that include a calendar retain their existing `Ymd` conversion in **Update post**, so a date-only selection of October 15, 2026 is saved as `20261015`.

The **24-hour time** setting changes the picker's hour display. It does not change the submitted `H:i` time format. If the meta key belongs to an ACF or Meta Box field, choose a field type that accepts the submitted value; integration-specific handling still applies.

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
| SVG | `<svg>`, including when linked |
| Video | `<div>` |
| Form | `<form>` |

For a linked SVG, custom attributes apply to the `<svg>`, not its surrounding `<a>`. To label the link directly, use the SVG element's **Link > aria-label** field. See [Label a linked SVG](https://academy.bricksbuilder.io/builder/elements/media/svg/#label-a-linked-svg) for a File-source example linking to the homepage.

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

Since Bricks 2.5, you can select the login field under **Content > Fields > Auto-focus field** to request focus on page load. Test the frontend with saved credentials and keyboard submission in the browsers your visitors use. See [Auto-focus field](https://academy.bricksbuilder.io/builder/elements/general/form/#auto-focus-field) for eligible fields and focus behavior.

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
