*Use dropdown query filters for single or multiple selections, sorting, and results per page, with optional child-term counts for taxonomy filters.*

Creates a dropdown select filter interface for single or multiple selection filtering. Supports taxonomy terms, WordPress fields, and custom fields. Can also function as a sorting or results-per-page control.

## Settings

- **Target query** (query-list) - Select the post, term, or user query this filter should target. Available sources depend on the query type.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Action** (select) - Filter behavior. Options: Filter (traditional filtering), Sort (sorting control), Results per page (pagination control).
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific field to filter/sort by (varies based on field type and action).
- **Taxonomy** (select) - Taxonomy to use for filtering when source is taxonomy.
- **Order by** (select) - How to order taxonomy terms. Options: Name, Slug, Term ID, Description, Parent, Count, Include, Menu Order, Meta Value, Meta Value Num.
- **Order meta key** (text) - Meta key for ordering when using meta value ordering.
- **Order** (select) - Sort direction. Options: ASC, DESC. Default: ASC.
- **Terms: Include** (select) - Specific taxonomy terms to include in filter options.
- **Terms: Exclude** (select) - Specific taxonomy terms to exclude from filter options.
- **Top level terms only** (checkbox) - Display only top-level terms (parent = 0) when source is taxonomy.
- **Hide count** (checkbox) - Hide the result count for each option.
- **Count: Include children** (checkbox, Bricks 2.5) - Include descendant-term posts in parent taxonomy counts. Off by default. Available with Action set to Filter, a target query, and a selected taxonomy.
- **Hide empty** (checkbox) - Hide options with zero results.
- **Hierarchical** (checkbox) - Display taxonomy terms in hierarchical structure.
- **Indent: Prefix** (text) - Prefix text for hierarchical indentation. Default: —.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key for filtering.
- **Compare** (select) - Comparison operator for filtering. Default: Equal.
- **Input** - Settings for the select dropdown.
  - **Placeholder** (text) - Placeholder text for the select dropdown.
- **Sort options** (repeater) - Configure sorting options when Action is set to Sort.
  - **Source** (select) - Sort field, including **Distance** in Bricks 2.5.
  - **Label** (text) - Display label for the sort option.
  - **Order** (select) - Ascending or Descending. For Distance, nearest first or farthest first.
  - **Meta key** (text) - Meta key for meta-based sorting.
- **Results per page options** (text) - Comma-separated list of results per page options when Action is set to Results per page. Default: 10, 20, 50, 100.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Parent-Term Counts {#parent-term-counts}

Enable **Count: Include children** when a parent option should count posts assigned to its child terms and deeper descendants. Posts assigned to both a parent and a descendant count once for the parent. The setting works independently of **Hierarchical** display and is shared when the element uses a global filter. See [taxonomy child counts](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts) for setup, indexing, and an example.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Use **Default value** for one exact option value. With Choices.js and multiple selection enabled, separate values with commas, such as `cotton, wool`, and wrap values containing commas in double quotes. For Sort, enter a configured sort value such as `title_ASC` or `distance_ASC`; for Results per page, enter a configured page size such as `20`. Dynamic data is supported.

A Distance default such as `distance_ASC` also requires a valid location from a Geolocation filter targeting the same query. Without one, Bricks clears the Distance selection and uses the query's normal order.

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

## Distance sorting {#distance-sorting}

Starting with **Bricks 2.5**, set **Action** to **Sort** and add **Distance** as a sort option's **Source**. Set **Order** to **Ascending** for nearest first or **Descending** for farthest first, and give the option a descriptive **Label**.

<div className="screenshot screenshot--control-panel">

![Sort options with Nearest first configured to use Distance in Ascending order, and Farthest first available as a second option.](https://academy.bricksbuilder.io/assets/query-filter-distance-sort-options.webp)

</div>

A [Geolocation filter](https://academy.bricksbuilder.io/builder/elements/filter/filter-geolocation/) must target the same query and provide a valid location, including a default location. Sorting keeps its radius constraint.

Distance options remain visible but disabled without a valid location, in both native and Choices.js dropdowns. A valid location enables them even when no results match. Clearing the location also clears a selected Distance sort and restores the query's normal order. Choosing a sort option never requests device location.

With this filter set to **Submit** and Geolocation set to **On submit**, a resolved pending location enables Distance before submission so visitors can apply both together. See [Distance sorting setup](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#distance-sorting) for apply modes, URL behavior, and failed requests.

> **Developer reference**
>
> See the [Filter - Select Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-select/) for the full JSON schema of this element's settings and controls.