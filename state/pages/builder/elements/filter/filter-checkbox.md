*Filter query results with multiple selections, include child-term counts, and show collapsible taxonomy branches with Show more/less controls.*

Creates a checkbox filter interface for AJAX-powered content filtering. Users can select multiple options to narrow down query results. Supports taxonomy terms, WordPress fields, and custom fields as filter sources.

For initial setup, see [Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#setup).

## Settings

- **Target query** (query-list) - Select the post, term, or user query this filter should target. Available sources depend on the query type.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific field to filter by (varies based on field type).
- **Taxonomy** (select) - Taxonomy to use for filtering when source is taxonomy.
- **Order by** (select) - How to order taxonomy terms. Options: Name, Slug, Term ID, Description, Parent, Count, Include, Menu Order, Meta Value, Meta Value Num.
- **Order meta key** (text) - Meta key for ordering when using meta value ordering.
- **Order** (select) - Sort direction. Options: ASC, DESC. Default: ASC.
- **Terms: Include** (select) - Specific taxonomy terms to include in filter options.
- **Terms: Exclude** (select) - Specific taxonomy terms to exclude from filter options.
- **Top level terms only** (checkbox) - Display only top-level terms (parent = 0) when source is taxonomy.
- **Hide count** (checkbox) - Hide the result count for each option.
- **Count: Include children** (checkbox, Bricks 2.5) - Include descendant-term posts in parent taxonomy counts. Off by default. Requires a target query and a selected taxonomy. See [taxonomy child counts](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts).
- **Hide empty** (checkbox) - Hide options with zero results.
- **Hide count bracket** (checkbox) - Remove brackets around count values. Style count via .brx-option-count.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key for filtering.
- **Compare** (select) - Comparison operator for filtering. Options: IN, NOT IN, BETWEEN, NOT BETWEEN.
- **Mode** (select) - Display mode for checkboxes. Options: Default (traditional checkboxes), Button (modern button style).
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Collapsible Taxonomy Branches {#collapsible-hierarchy}

Starting with **Bricks 2.5**, visitors can expand and collapse child branches in a hierarchical taxonomy Checkbox filter. This is useful for category lists where showing every nested term would make the filter too long.

1. Set **Target query**, choose **Taxonomy** as the source, and select a taxonomy with parent and child terms.
2. Open the **Hierarchy** control group and enable **Hierarchical**.
3. Turn on **Enable expand/collapse**.
4. Leave **Show expanded** off to start with branches collapsed, or enable it to show all branches expanded initially.
5. Save and check the frontend. Parent terms with visible children have a separate expand/collapse button beside the checkbox.

| Hierarchy setting | Behavior |
| --- | --- |
| Hierarchical | Arrange taxonomy terms under their parents. |
| Auto toggle child terms | Toggle child checkboxes when a parent checkbox changes. This is separate from expanding a branch. |
| Enable expand/collapse | Add buttons to open and close child branches. Off by default. |
| Show expanded | Expand all branches initially. Off by default. |
| Expand icon / Collapse icon | Choose the disclosure icons. Defaults are plus and minus. |
| Icon typography / Icon gap | Set the icon appearance and spacing. |
| Indent: Prefix / Indent: Gap | Set child-term indentation in the default display mode. |

The disclosure button opens or closes a branch without selecting its checkbox. Visitors can focus the button and use Enter or Space to toggle it. Selected child terms open their ancestor branches on page load, including selections loaded from URL parameters. Bricks preserves each element's expanded branches through AJAX updates and opens the path to selected terms when needed.

Only terms present in the filter's options can appear in a branch. **Top level terms only**, term exclusions, and **Hide empty** can remove child options. If a parent has no visible children, it has no expand/collapse button. Use [Count: Include children](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts) if parent counts should include posts assigned to descendants.

<div className="screenshot screenshot--control-panel">

![Hierarchy settings with expand/collapse enabled, Show expanded off, and plus and minus icons selected.](https://academy.bricksbuilder.io/assets/filter-checkbox-hierarchy-settings.webp)

</div>

### Show More/Less With Branches {#show-more-less}

In the **Show more / Show less** control group, set **Visible options limit** to limit the initial list. Leave it empty to show all options.

When **Enable expand/collapse** is on, this limit counts whole root branches, not individual child terms. For example, a limit of three shows the first three root branches. Expanding one of them reveals its children without using up another place in the limit. **Show more** reveals the remaining root branches; **Show less** returns to the initial limit.

A branch containing a selected term stays visible even beyond the limit, so the list can show more than the configured number of roots. **Show more: Text** accepts `%number%` for the number of hidden root branches. In the collapsed list, the Show more button is hidden when no additional branches remain hidden. Without expand/collapse, the limit counts individual options.

![The Hoodies child term remains visible under Clothing beyond the two-branch limit, with Show 1 more available and three matching products.](https://academy.bricksbuilder.io/assets/filter-checkbox-collapsible-branches.webp)

### Linked Desktop and Mobile Filters {#linked-hierarchies}

When using a [global filter](https://academy.bricksbuilder.io/builder/dynamic-content/global-filters-filter-manager/), **Hierarchical**, **Auto toggle child terms**, and **Count: Include children** are shared settings. Expand/collapse, Show expanded, icons, indentation, and Show more/less limits stay on each element.

Linked elements targeting the same query synchronize their checkbox selections. Each copy keeps its own expanded branches and Show more/less state, so a mobile filter can start collapsed while the desktop copy starts expanded.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Use **Default value** to preselect exact option values, separated by commas, such as `cotton, wool`. Use taxonomy slugs or raw stored values rather than display labels. Wrap a value containing a comma in double quotes. Dynamic data is supported.

<div className="screenshot screenshot--control-panel">

![A Checkbox filter's Default value set to cotton, wool.](https://academy.bricksbuilder.io/assets/query-filter-default-values.webp)

</div>

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

> **Developer reference**
>
> See the [Filter - Checkbox Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-checkbox/) for the full JSON schema of this element's settings and controls.