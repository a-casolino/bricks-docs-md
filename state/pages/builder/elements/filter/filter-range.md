*Filter query results by numeric ranges using sliders or input fields, with optional default minimum and maximum values.*

Creates a range slider or input interface for filtering content by numeric ranges. Perfect for price filtering, numeric custom fields, or any data that has minimum and maximum values. Supports both slider and input field display modes.

**Tip:** Essential for e-commerce price filtering or any scenario where users need to filter by numeric ranges.

## Settings

- **Target query** (query-list) - Select the Posts, Terms, or Users query this filter should target.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Currently limited to Custom field.
- **Field type** (select) - Type of field when using custom field source. Options: Post, Term, User.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key containing numeric values for range filtering.
- **Disable auto min/max value** (checkbox) - Manually set min/max values instead of auto-detecting from query results.
- **Mode** (select) - Display mode for the range filter. Options: Slider (visual slider), Input (text inputs).
- **Step** (number) - Increment step for range values. Default: 1.
- **Decimal places** (number) - Number of decimal places to display. Default: 0.
- **Thousand separator** (checkbox) - Add thousand separators to displayed values.
- **Separator** (text) - Thousand separator character. Default: ,.
- **Label** - Settings for range value labels.
  - **Min** (text) - Label for minimum value.
  - **Max** (text) - Label for maximum value.
  - **Direction** (direction) - Layout direction for min/max labels (row/column).
  - **Gap** (number) - Spacing between min/max labels.
- **Input** - Settings for input field mode.
  - **Placeholder** (text) - Placeholder text for input fields.
  - **Typography** (typography) - Typography for input field text.
- **Slider** - Settings for slider mode.
  - **Track color** (color) - Color of the slider track.
  - **Range color** (color) - Color of the selected range on the slider.
  - **Handle color** (color) - Color of the slider handles.
  - **Handle size** (number) - Size of the slider handles.
  - **Track height** (number) - Height of the slider track.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Under **Default value**, enter numeric **Minimum** and **Maximum** values. Leave one endpoint empty to use the original range boundary. Defaults are limited to the original available range and support dynamic data.

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

> **Developer reference**
>
> See the [Filter - Range Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-range/) for the full JSON schema of this element's settings and controls.