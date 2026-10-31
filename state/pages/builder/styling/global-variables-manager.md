*Manage reusable design tokens in Bricks with Global Variables Manager for consistent spacing, sizing, and color values.*

The Global Variables Manager lets you create and maintain reusable CSS custom properties in Bricks.

Use global variables for values that should stay consistent across controls, classes, templates, and pages: spacing sizes, typography sizes, radii, layout widths, color values, shadows, or any repeated design token.

For example, instead of typing `clamp(1rem, 2vw, 1.5rem)` into several controls, create a variable named `text-m` and use `var(--text-m)` wherever that value is needed.

https://www.youtube.com/watch?v=K-c6OFHVhpQ

## Accessing the Variable Manager

To access the Variable Manager, click the **Style Manager** icon in the builder toolbar. Then select the **Variables** tab.

The **Categories** column lists your variable categories next to **All** and **Uncategorized**. Color palettes from the [Color Manager](https://academy.bricksbuilder.io/builder/features/color-manager/) appear there too, marked with a **COLORS** badge, because every palette color is also a CSS variable (for example `moss` for `var(--moss)`).

![Style Manager Variables tab with the categories All, Uncategorized, Radius, Shadows, Layout and two color palettes, next to the variable list.](https://academy.bricksbuilder.io/assets/bricks-style-manager-variables-categories.webp)

You can disable the Variable Manager under `Bricks > Settings > General > Disable CSS variables manager`.

The variable picker value display can be hidden under `Bricks > Settings > Builder > Variable dropdown: Hide value`.

## The mental model

Global variables are stored as site-level Bricks data. A variable has:

- An internal ID.
- A name, stored without the leading `--`.
- A value.
- An optional category.

On the frontend, Bricks outputs variables as CSS custom properties with the `--` prefix:

```css
:root {
  --text-m: clamp(1rem, 2vw, 1.5rem);
}
```

In a Bricks control or CSS field, use the variable like this:

```css
var(--text-m)
```

Bricks only outputs variables that have a name and a non-empty value.

## Create a variable

1. Open **Style Manager > Variables**.
2. Optional: select the category the variable belongs to. A new variable is added to the selected category. To create a category, type its name into **New category name** below the list and press `Enter`; the new category is selected right away.
3. In the **New variable name** field, enter a name without the leading `--`, such as `space-m`. Bricks adds the `--` prefix for you.
4. In the **Value** field, enter the value, such as `clamp(1rem, 2vw, 2rem)`.
5. Press `Enter` or click the save icon at the end of the row.
6. Click **Save** in the Style Manager toolbar to store your changes.

If you paste a name that starts with `--` or `var(--...)`, Bricks normalizes it to the stored variable name.

Variable names must be unique. Bricks also prevents duplicate variable names that conflict with variable-based colors in the Color Manager.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager.png)

## Use variables in controls

Many builder controls include a variable picker: the small CSS icon at the end of the field. Open the picker and select a variable to insert it into the active control.

The picker has a search field and groups the variables by category, including **Uncategorized** and your color palettes. Open a group to see its variables.

The picker inserts a `var(--name)` reference. If the sides of a control are linked, such as the four corners of **Border > Radius**, picking a variable for one side sets all linked sides. You can also type `var(--name)` manually in controls that accept CSS values.

<div className="screenshot screenshot--control-panel">

![Border settings of an image. The radius fields show var(--radius-card), and the open variable picker lists the groups Uncategorized, Radius, Shadows, Layout, Default and Fernlow.](https://academy.bricksbuilder.io/assets/bricks-variable-picker-categories.webp)

</div>

Variables are useful in:

- Element ID styles.
- Global class styles.
- Theme Styles.
- Page settings.
- Custom CSS fields.
- Other Bricks-managed style settings that accept CSS values.

## Update, rename, duplicate, and delete variables

Click a variable in the list to select it. A selected variable's name and value become editable in place: change them and press `Enter`. Clicking the same row again clears the selection.

To select several variables, click the first one and `Shift`-click the last one, or use the select-all checkbox in the list header. With more than one variable selected, an **Edit** panel opens next to the list with three tabs:

- **Rename**: rename the selected variables at once with **Find** and **Replace with**, **Add prefix**, or **Add suffix**. The **Preview** shows the new names before you click **Rename**.
- **Categorize**: move the selected variables into a category. Choose it under **Category** and click **Update**. This tab appears once at least one category exists.
- **Duplicate**: create copies of the selected variables.

The list header also has icons to export the selected variables, move them to the trash, and clear the selection. You can reorder variables by drag and drop.

![Variables tab with card-shadow and card-shadow-hover selected. The Edit panel shows the Rename tab with Find card-shadow, Replace with shadow-card, and the preview of the new names.](https://academy.bricksbuilder.io/assets/bricks-variables-bulk-rename.webp)

When a variable is renamed, Bricks updates Bricks-managed references from `var(--old-name)` to `var(--new-name)` in builder data. This update runs in the builder and again on save.

> **Note**
>
> Variable rename updates apply to Bricks-managed data. A `var(--old-name)` typed into an element's **Custom CSS** field keeps the old name, and so does CSS written outside Bricks-managed settings. Update those references manually.

## Categories

Categories organize variables in the manager and picker. They do not change the variable name by themselves.

You can:

- Create categories.
- Rename categories.
- Reorder categories.
- Filter variables by category.
- Export categories with selected variables.

If a variable has no category, or its category no longer exists, Bricks treats it as uncategorized.

## Search, sorting, and usage filters

Use the manager header to narrow the variable list:

- **Name (Include)** shows only variables whose names contain the text.
- **Name (Exclude)** hides variables whose names contain the text. Combine both, for example `shadow` included and `hover` excluded.
- **Sort** orders the list alphabetically.
- **Filter** shows only the variables **Used on this page** or **Unused on this page**. A selected filter appears as a tag in the field; click its remove icon to clear it.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-subheader.png)

Usage filters are helpful for cleanup, but review before deleting. A variable can be unused on the current page and still be used elsewhere.

## Scales and utility classes

Style Manager scales use variable categories. A typography or spacing scale is stored as a variable category with scale settings.

A scale can generate variables such as:

```text
text-xs
text-s
text-m
text-l
space-xs
space-s
space-m
space-l
```

Scale categories can also define utility class patterns. For example:

```text
Class name: text-*
CSS property: font-size
```

For a variable named `text-m`, Bricks can generate:

```css
.text-m {
  font-size: var(--text-m);
}
```

If a class pattern does not contain `*`, Bricks appends the scale step name to the class pattern.

Generated utility classes are part of the Style Manager CSS output and are also reflected in the builder preview.

## CSS output

Global variables with non-empty values are output as `:root` CSS custom properties.

Bricks also generates a Style Manager CSS file when relevant Style Manager data changes. That file can contain:

- Color palette variables.
- Color utility classes.
- Variables from scale categories.
- Utility classes generated from scale categories.

If the Style Manager CSS file exists, Bricks enqueues it on the frontend. If file generation fails because of filesystem permissions, cache configuration, or another environment issue, regenerate Bricks CSS files and check the site's file permissions.

## Exporting and importing variables

Export and import variables to reuse the same set across Bricks sites.

### Exporting variables

You have two options for exporting variables:

1. **Export all:** Click the export button at the top of the manager to export all variables and categories.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-export-all.png)

2. **Export selected:** Select one or more variables and click the export-selected icon in the variables column.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-export-selected-1024x682.png)

Selected exports include the categories used by the selected variables.

### Importing variables

You can import variables in three ways:

**Importing via JSON file:** In the import popup, drag and drop a JSON file containing exported variables.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-import-1024x682.png)

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-import-file-1024x682.png)

When importing a JSON file, Bricks adds variables that do not already exist by name. If the file includes categories, Bricks can also import categories that do not already exist by name.

**Manual text entry:** You can manually enter variables into a textarea. This is useful for quickly importing variables from a child theme, custom plugin, stylesheet, or snippet.

The expected format is a semicolon-separated list of CSS variable definitions:

```css
--bricks-color-primary: #ffd64f;
--bricks-color-secondary: #fc5778;
--bricks-text-dark: #212121;
```

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-import-textarea-1024x682.png)

Manual imports add variables that do not already exist by name.

**Importing from remote templates:** When inserting a remote template, Bricks can offer to import variables from the remote source. Remote template variables are matched by name. New variables can be imported; existing local variables with the same name are not duplicated.

Remote template variable categories are not imported with the template variables, so imported variables may appear uncategorized.

## Best practices

- Name variables by purpose: `space-m`, `radius-card`, `text-step-2`.
- Use variables for repeated values, not every one-off value.
- Keep values valid CSS for the controls where you plan to use them.
- Prefer scale-generated variables for typography and spacing systems.
- Avoid renaming variables casually on production sites with lots of custom CSS.
- After large variable changes, regenerate Bricks CSS files and review important templates.

## Troubleshooting

### A variable does not appear in the picker

Check whether the variable exists, has a valid name, and whether the current control supports variable insertion.

### A variable exists but does not output CSS

Check whether it has a non-empty value. Bricks skips variables with empty values.

### A renamed variable still appears in custom CSS

Bricks updates Bricks-managed `var(--old-name)` references. External stylesheets, child theme CSS, custom plugin CSS, or manually written code outside Bricks-managed data may still need manual updates.

### Imported variables are uncategorized

Remote template variable imports do not import variable categories. JSON imports can import categories when the file includes them and you confirm the category import.

### Utility classes are missing

Check that the variable category is a scale, that utility classes are configured for that scale, and that Bricks can generate and enqueue the Style Manager CSS file.