*Display a query's reported starting position, ending position, and total result count, with updates for pagination, Load More, Infinite Scroll, and Query Filters.*

The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which items they are currently viewing in relation to the total number of results. This is particularly useful for search results, archive pages, and paginated lists where users navigate through multiple pages of content. It can be found in the elements panel under the "Query" category.

**Note:** If a third-party plugin disables Bricks Query history via the [`bricks/query/force_run`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-force_run/) hook, the results summary may display incorrect information.

## Compatibility

The **Query Results Summary** element updates with Bricks' native AJAX actions, including:

- AJAX Pagination
- Load More
- Infinite Scroll
- Query Filters

This ensures that the summary updates dynamically as users interact with query-based elements on the page.

Example:

![](https://academy.bricksbuilder.io/assets/query-results-summary-element-example.png)

## Settings

![](https://academy.bricksbuilder.io/assets/query-results-summary-element-controls.png)

### Query

Select the **target query** for which the summary should be displayed.

### Format

Customize the summary text using placeholders:

- `%start%`: The numeric starting position reported by the query.
- `%end%`: The numeric ending position reported by the query.
- `%total%`: The total number of results.

Default format: `Results: %start% - %end% of %total% posts`

Example output: Results: 1 - 5 of 14 posts

Native post, term, and user queries normally report one-based positions. A query without a populated range, including a provider-backed ACF loop, can report `0` for the start or end position.

Developers can override the reported positions with [`bricks/query/result_start`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/) and [`bricks/query/result_end`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/). These filters change summary metadata only. They do not skip or limit items, change the total count, or fetch another page.

### Text: One Result

Define a custom message when the query returns exactly **one** result to handle singular/plural differences.

Default text: One post found

### Text: No Results

Specify a custom message when the query returns **zero** results.

Default text: No posts found

> **Developer reference**
>
> See the [Query Results Summary Schema](https://academy.bricksbuilder.io/developer/schema/elements/query-results-summary/) for the full JSON schema of this element's settings and controls.