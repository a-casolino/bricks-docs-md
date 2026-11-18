*Display selected query filters as removable buttons and exclude filters from the active list.*

Displays the currently active or selected filters, allowing users to easily remove a filter with a single click for faster navigation. This element shows all active filters from the connected target query and provides quick access to clear individual filters.

**Tip:** Use this element alongside other filter elements to give users clear visibility of their current filter selections and easy ways to modify their search criteria.

## Settings

- **Target query** (query-list) - Select the query whose active filters should be displayed.
- **Global filter** (Bricks 2.5) - Reuse the shared behavior of another Active Filters configuration. The target query and styling remain local.
- **Exclude filter IDs** (text) - Enter filter element IDs, separated by commas, to exclude from the active filters list. From Bricks 2.5, accepts global filter IDs too. A linked element's ID excludes its shared filter for the target query.
- **Button** - Settings for the remove filter buttons.
  - **Padding** (spacing) - Padding for filter remove buttons.
  - **Gap** (number) - Gap between filter buttons.
  - **Size** (select) - Button size preset. Options: Default, Small, Medium, Large, Extra Large.
  - **Style** (select) - Button style. Options: None, Primary, Secondary, Success, Info, Warning, Danger, Dark, Light.
  - **Circle** (checkbox) - Make buttons circular.
  - **Outline** (checkbox) - Use outline button style.
  - **Background color** (color) - Custom background color for buttons.
  - **Border** (border) - Border styling for buttons.
  - **Typography** (typography) - Typography settings for button text.
- **Icon** - Settings for filter remove icons.
  - **Icon** (icon) - Icon to display on filter buttons.
  - **Color** (color) - Icon color.
  - **Size** (number) - Icon size.
  - **Gap** (number) - Gap between icon and text.
  - **Position** (select) - Icon position. Options: Left, Right. Default: Right.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Default selections

Starting with Bricks 2.5, [configured default values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) appear as active selections on the first page load. Visitors can remove them like other selections. Removing a default does not immediately reapply it; a fresh visit or reload without filter parameters applies it again. Display exclusions still apply.

## Excluding a Global Filter

Starting with Bricks 2.5, use a [global filter](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#global-filters) ID or any linked element's ID in **Exclude filter IDs**. For example, exclude a shared results-per-page filter to keep it out of the active-filter list across desktop and mobile copies. This hides the entry without clearing its selection or changing the query.

Copy a definition ID from Filter manager, or use the Bricks ID from a linked element's panel. Do not use a target query ID or URL parameter name. This display exclusion is separate from a Reset button's exclusions, which preserve values when resetting.

> **Developer reference**
>
> See the [Filter - Active Filters Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-active-filters/) for the full JSON schema of this element's settings and controls.