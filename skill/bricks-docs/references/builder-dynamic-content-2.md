# Query Loop

Source: https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/

*Use the Bricks Query Loop to repeat layouts from posts, terms, users, arrays, or API data while keeping every repeated item fully designable.*

https://www.youtube.com/watch?v=GQicN9DWEVg

The **Query Loop** builder is available for [layout elements](https://academy.bricksbuilder.io/builder/styling/layout/) such as Container, Section, Block, and Div. It is also available on the classic Accordion and Slider elements.

The Map element has its own query loop controls for dynamic addresses. Nestable elements such as Accordion (Nestable), Tabs (Nestable), and Slider (Nestable) use their own child repeaters, so they do not expose the same full Query Loop control as layout elements.

It lets you query content and render each result through the same design. Everything inside the loop can use dynamic data from the current result.

### Dynamic data in nested loops

Dynamic data uses the current loop result. In a nested loop, the inner result becomes the current result for elements inside that loop.

For example, `{term_name}` can return the current term in an outer Terms loop. Inside a nested Posts or Media loop, the current result is a post or attachment, so the same term tag does not read the outer term.

Bricks does not provide parent-loop syntax for output tags. Keep values that belong to the parent result outside the inner loop when possible. Inner query controls can use dynamic data while Bricks is building that nested query, but output inside the inner loop still resolves against the inner result. Accessing the parent result from inner-loop markup requires custom PHP or a custom dynamic data tag.

You can query post types, taxonomy terms, users, API responses, and arrays. Some typical use cases are:

- **Posts**: Latest posts, related posts (works for any registered & public post type)
- **Terms**: Post categories & tags, product categories, etc.
- **Users**: List blog authors, community members, and team members
- **API**: Render items from an external JSON API
- **Array**: Render items from a PHP or JSON-style array

## Important {#important}

Bricks Query Loop automatically generates HTML comments such as `<!--brx-loop-start-abc123-->` on the frontend. These comments are essential for features like AJAX Pagination, Query Filters, Load More, and Infinite Scroll to function correctly.

> **Note**
>
> **Do not remove these comments**, as doing so may cause these features to stop working.

Some **performance optimization plugins** may remove all HTML comments by default. If you are using such a plugin, ensure that Bricks-generated comments are preserved to avoid breaking dynamic query functionality.

## How to create a query loop {#custom-loop}

Add a "Container" element to the canvas. Enable the **Use Query Loop** setting to turn your container into a loop (repeater) item.

![](https://academy.bricksbuilder.io/assets/container-query-loop-control.png)

<figcaption>

Container element: new query loop control

</figcaption>

Once you've enabled the **Use Query Loop** setting, you'll see a **Query** control (loop/infinity icon).

Open the query control to set the query parameters for retrieving the content from your database.

This container now serves as your repeater item. All elements inside this container are repeated as often as there are query results.

## Query control {#query-control}

The **Query** control supports five built-in query types: `posts`, `terms`, `users`, `api`, and `array`.

![](https://academy.bricksbuilder.io/assets/query-control-object-type.png)

- **Posts** enable a [WP_Query](https://developer.wordpress.org/reference/classes/wp_query/) type of query. This is the default query type and should be used when you want to display a loop of posts, pages, media files, or custom post types.
- **Terms** enable the [WP_Term_Query](https://developer.wordpress.org/reference/classes/wp_term_query/). This should be used when you want to loop through the different terms of a taxonomy. Useful to list all the product categories that contain products.
- **Users** enable the [WP_User_Query](https://developer.wordpress.org/reference/classes/WP_User_Query/). This should be used when you want to loop through a set of site users. Useful to list the blog authors or a list of team members (as long as they are inserted as site users).
- **API** lets you render items returned by an external API. See [Query data from APIs](https://academy.bricksbuilder.io/builder/dynamic-content/query-data-from-apis/) for the full API query workflow.
- **Array** lets you render items from PHP or JSON-style array data. See [Query Type: Array](#array) below.

The query controls adapt according to the selected query type.

### ACF Repeater source context

An ACF Repeater query uses the active post or query context to retrieve its rows. If the repeater field is assigned to an ACF Options Page, Bricks retrieves the rows from that options page instead.

Selecting an ACF Repeater query does not store or provide a control for an arbitrary source post or page ID. For repeatable data shared across pages, assign the field to an ACF Options Page. To retrieve rows from a specific different post or page, use custom PHP or a custom query or dynamic-data solution that passes the required ACF source post ID. See [Dynamic Data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/) for ACF field support in Bricks.

## Query editor (PHP) {#query-editor}

Bricks 1.9.1 introduces a new `Query editor` control that lets you write your own queries in PHP for maximum flexibility and querying capabilities.

The query editor appears after enabling the "Query editor (PHP)" control.

> **Note**
>
> Note: You must enable code execution in [Bricks settings](https://academy.bricksbuilder.io/builder/setup/settings/) to access this feature.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.1-query-editor-php.png)

<figcaption>

Custom query using dynamic data (ACF) for the post type, returning all posts for September 2023.

</figcaption>

You have to **return a PHP array** containing the [WordPress query arguments](https://developer.wordpress.org/reference/classes/wp_query/#parameters) you'd like to use for your query.

As shown in the screenshot above, the query editor supports dynamic data.

Bricks signs Query editor code. If the signature is missing or invalid, Bricks will not run the code. Keep the returned array focused on query arguments. Do not echo output or run unrelated database writes inside a Query editor.

## Posts query {#posts-query}

![](https://academy.bricksbuilder.io/assets/post-query-1-6-3.png)

**Post type**: Select one or multiple post types (default: posts)

**Order by**: Order the results by post ID, author, title, published or modified date, comment count, relevance, menu order, or random (default: published date). (Support multiple values `@since 1.11.1`)

**Order**: Ascending or Descending (default). (Support multiple values `@since 1.11.1`)

**Posts Per Page**: The number of posts to show per page (default: WordPress settings > Reading > Blog pages show at most)

**Offset**: The number of posts to skip.

**Ignore Sticky Posts**: Turn this on if do not want to move sticky posts to the start of the set.

**Disable Query Merge**: Turn this on if do not want the query to be auto-merged by Bricks in archive pages, search pages, etc. Usually, you will turn this on for the Query loops in the footer, header, or non-main query. This is the GUI for the [bricks/posts/merge_query](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-merge_query/) filter.

**Child Of**: Set the parent ID to return all its children only. (`post_parent` in WP_Query)

**Include/Exclude**: Include or exclude one or multiple posts from the query. These controls support [dynamic data](#include-exclude-dynamic-data) (`@since 1.12`).

**Include authors / Exclude authors**: Include or exclude posts by author. Select users manually, or use supported dynamic data tags to pass author IDs (`@since 2.4`).

**Exclude Current Post**: If enabled it will exclude the current post from the loop (useful to build a "related posts" section)

**Terms Include/Exclude**: Include or Exclude posts that have one or multiple terms.

**Taxonomy Query**: Add one or multiple taxonomy queries to filter the posts.

**Tax Query Relation**: Define if the taxonomy queries should be inclusive (OR) or exclusive (AND).

**Meta Query**: Add one or multiple meta queries to filter the posts based on the custom fields.

#### ACF date fields in a meta query

A meta query compares the value stored in the WordPress database. It does not compare the formatted value shown by an ACF field or a rendered dynamic data tag.

For an ACF Date Picker field, use the field name as the meta key, without braces or an `acf_` prefix. ACF stores this field as `Ymd`, regardless of its return or display format. To return upcoming posts, for example, use:

- **Meta key:** `event_date`
- **Meta value:** `{current_wp_date:Ymd}`
- **Compare:** `>=`
- **Type:** `NUMERIC`

Use `{current_date:Ymd}` instead when the comparison should use UTC rather than the WordPress site timezone.

ACF Date Time Picker values are stored as `Y-m-d H:i:s`. Use a value such as `{current_wp_date:Y-m-d H:i:s}` with **Type** set to `DATETIME`.

Fields inside an ACF Group normally use the stored `parent_child` meta key. You can keep any return or display format needed on the frontend because it does not change the raw value used by the query.

**Relation**: Define if the meta queries should be inclusive (OR) or exclusive (AND).

**No Found Rows**: Improve performance when the loop does not need pagination, result counts, or max page counts.

**Disable update_post_meta_cache** and **Disable update_post_term_cache**: Performance options for post queries that do not need post meta or term cache data.

**Random seed TTL**: Duration in minutes for which the random seed exists. Set to prevent duplicate post results (only needed & available when using a random order query loop).  Set "0" to turn this feature off.

If you set the TTL to 10 minutes, the query result remains the same for the next 10 minutes. This ensures that no duplicate posts are displayed on different pages or when the infinite scroll is active. (`@since 1.7.1`)

**Is main query (Archive, Search)**: When creating an archive or search template, choose one of the loops as the main query. This will prevent a 404 error from occurring when visitors navigate to different pages. Turn on to designate the main query. Remember to set the correct query on your pagination element as well.

However, do not turn on this option for multiple queries on the same page, as only the first one will be set as the archive main query. `(@since 1.8)`

Watch this example to build a custom post type archive with a main query loop and pagination:

https://youtu.be/PeemZuvI3Fc

### Enhanced Ordering Options {#enhanced-ordering-options}

Starting with version 1.11.1, the **Order By** and **Order** settings in Bricks Query Loop have been improved to support multiple ordering criteria. This allows you to define complex ordering rules directly within Bricks, eliminating the need for a custom PHP filter that was previously required.

![](https://academy.bricksbuilder.io/assets/enhanced-query-loop-order-by-example-1.png)

This update is particularly useful in scenarios where you want to order query results by more than one criterion. For example, you can now order by **name** in descending order and then by **ID** in descending order. Bricks will process these criteria sequentially, applying each in the order specified to deliver the desired result.

**Example Scenarios:**

- **Multi-Criteria Ordering**: Suppose you have a directory listing and want to display results by popularity first (custom field) and then by date added. With this update, you can set the query to order first by the popularity meta field in descending order and then by date added in ascending order, ensuring that the most popular and newest items appear at the top.
- **Custom Order Clauses with Meta Queries**: Bricks now supports more complex ordering directly aligned with meta query conditions. For instance, if you're working with a meta query to order posts by **performance date** and **time**, you can define this directly in the order clause. Code example in [this article](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-query_vars/#orderby-with-multiple-fields).

![](https://academy.bricksbuilder.io/assets/enhanced-query-loop-order-by-example-2.png)

### Best Practice for Pagination & Order By {#best-practice-for-pagination-and-order-by}

When using multiple ordering criteria, include **ID** as a secondary ordering criterion to avoid duplicate results across paginated pages. For example, if you're displaying 5 posts per page and have 15 posts with the same **price**, ordering by **price** alone may cause posts to appear on multiple pages. Set the query to order by **price** in ascending or descending order, followed by **ID** in ascending or descending order.

### Example 1: Latest Posts

In this example, we'll list the latest four posts (each item shows the featured image, post title, and excerpt) using the Query Loop Builder.

![Custom Query Loop Builder - latest posts](https://academy.bricksbuilder.io/assets/container-loop-latest-posts-1024x399.png)

<figcaption>

Display the latest posts using a custom query loop

</figcaption>

We start by adding a container to the canvas. This container holds our loop and serves as the blueprint for each query item.

Next, we enable the "**Use Query Loop**" setting to turn our simple container into a query loop.

We add an image element inside our container and set it to "Featured Image" using the Dynamic Data dropdown.

Add another container with a Heading and Text element in the same container.

For the Heading element, we add the `{post_title}` tag.

For the Text element, we add `{post_excerpt}` tag.

You could use the Post Title element or the Post Excerpt element instead if you like.

By default, the query control shows the latest posts. But because we want to restrict the number of posts shown, we need to edit the Query setting and set the Posts Per Page control to 4 to restrict the output to four rows.

## Media query {#media-query}

Bricks 1.5 introduces the possibility to query for media files (the attachment post type). You'll now find the `Media` (attachment) post type in the Posts query type.

After selecting `Media` in the post type control, you'll get a new control to define the mime type. By default, Bricks automatically queries for images, but you may define other mime types (separated by a comma, e.g., *image/jpeg,image/png,image/gif*).

To query for the images attached to a post, you may use the **Child of** control to specify the post ID. To do it dynamically, you may use dynamic data to fetch the current post id: `{post_id}`.

![](https://academy.bricksbuilder.io/assets/bricks-media-query-loop-settings.png)

### Example 2: Media gallery

The media query opens the possibility of building a custom media gallery using the Query Loop builder. To start, you need to add a Container element, insert a Block element inside it, and finally, an image element inside of the Block.

In the container, you'll set the flex-wrap to `wrap` and the direction to horizontal (row). In the Block, you must activate the Query Loop and set the Media post type and the number of images you'll want to get (posts per page). In the Block layout, you must set the width and the height (e.g. 300px).

In the Image, you'll set the dynamic data as `{post_id}` - note that the query returns the attachment posts (media files), so the image ID is the post ID. To complete the layout, set the image object-fit to `cover` and the height to 300px.

![](https://academy.bricksbuilder.io/assets/bricks-media-query-loop-1024x618.jpg)

<figcaption>

The final result of a media gallery using the Query Loop builder

</figcaption>

## WooCommerce Products Query {#woocommerce}

Since 1.10, Bricks introduced new settings for WooCommerce products query. Once selected Products post type, you will be able to see the WooCommerce section. (Only available if WooCommerce is activated)

### Example 1: WooCommerce Featured Products {#example-woocommerce-featured-products}

To show latest 10 featured products on your homepage, just set a query loop with below settings.

![](https://academy.bricksbuilder.io/assets/woo-featured-products-query-settings.png)

### Example 2: WooCommerce Related Products {#example-woocommerce-related-products}

To show 4 related products on your single product template.

![](https://academy.bricksbuilder.io/assets/woo-related-products-query-settings.png)

### Example 3: WooCommerce Upsells Products {#example-woocommerce-upsells-products}

To show 3 upsells product in  a single product template.

![](https://academy.bricksbuilder.io/assets/woo-upsell-products-query.png)

### WooCommerce v2 query loops {#woocommerce-v2}

Bricks 2.4 adds WooCommerce query loops for advanced modular Cart, Checkout, and My Account layouts.

These loops cover cart coupons, fees, taxes, order items, order totals, order downloads, customer notes, account orders, account order actions, account downloads, and account addresses.

Advanced v2 query loops require **Bricks > Settings > WooCommerce > Enable advanced modular elements**. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#query-loops) for the complete list and matching dynamic tags.

## Terms query {#terms-query}

![](https://academy.bricksbuilder.io/assets/bricks-query-control-terms-341x1024.png)

**Taxonomies**: Select one or multiple taxonomies to query (default: none).

**Order by**: Order the results by term ID, term name, term parent, count, or include list.

**Order**: Ascending (default) or Descending.

**Number**: The number of terms to show per page. WordPress default is all, but Bricks defaults to the number defined in the WordPress settings > Reading > Blog pages show at most. Use 0 to display all the results.

**Offset**: The number of terms to skip.

**Parent**: Parent term ID to retrieve direct-child terms. Set this to 0 to fetch only the terms that have children. Ex.: Given this structure, entering 55 would get only the T-shirts.

**Child of**: Term ID to retrieve child terms of. Ex.: Given [this](https://academy.bricksbuilder.io/assets/sample-terms-structure.png) structure, entering 55 would get T-shirts and Tees.

**Childless**: (bool) True to limit results to terms with no children. This parameter has no effect on non-hierarchical taxonomies. Default false.

**Disable Query Merge**: Turn this on if do not want the query to be auto-merged by Bricks. (@since 1.7.1)

**Terms Include/Exclude**: Include or Exclude terms from the query

**Show empty**: Whether to show terms not assigned to any posts.

**Meta Query**: Add one or multiple meta queries to filter the posts based on the custom fields.

**Relation**: Define if the meta queries should be inclusive (OR) or exclusive (AND).

**No Results**: Text to be shown when there are no matching results.

<span id="current-post-term"></span>

**Current post term**: Enable to get the terms assigned to the current post only. `(@since 1.8.4)` Only use in single post context. Only visible if "Type" is set to "Term". This is the same logic as the example in [bricks/terms/query_vars](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars/#get-terms-assigned-to-a-post)

![](https://academy.bricksbuilder.io/assets/term-query-current-post-term.png)

### Example 3: Product categories {#example-2}

In this example, we'll build a dynamic list of product categories (product category image + a link to the category archive).

The example is based on the WooCommerce plugin and the sample products. We'll need one container to hold the container loop. Inside the container loop, we've added a Basic Text element that contains the Dynamic Data `{term_name}` tag.

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-terms-1024x499.png)

<figcaption>

Display the product categories with a link

</figcaption>

After setting the Query to loop through "terms" and selecting the Taxonomy "Product Categories", you'll get in the canvas as many containers as the existing categories. Inside the loop, you'll be able to use several dynamic data tags to fetch the term's data, such as the term ID, the term name, the term archive URL, the term description, and any term meta.

In this example, we set the loop container background image as the product category thumbnail, using the Dynamic Data dropdown and selecting the Product Category Image tag:

![](https://academy.bricksbuilder.io/assets/bricks-query-terms-bg-image.png)

<figcaption>

Set the container background image

</figcaption>

We also set the loop container as a link to the product category archive page (using the Term Archive URL dynamic data tag). You'll need to set the HTML tag to "a (link)" and the link type to Dynamic Data, which will enable the Dynamic Data dropdown:

![](https://academy.bricksbuilder.io/assets/bricks-query-terms-link-1.png)

## Users query {#users-query}

![](https://academy.bricksbuilder.io/assets/bricks-query-control-users.png)

**Roles**: Select one or multiple user roles to query (default: any)

**Order by**: Order the results by user ID, name, username, nicename, login, email, registered date, post count, or include list.

**Order**: Ascending (default) or Descending.

**Number**: The number of users to show per page. WordPress defaults to all, but Bricks defaults to the number defined in the WordPress settings > Reading > Blog pages show at most. Use -1 to display all the results.

**Offset**: The number of users to skip.

**Current post author:** Enable to query the current post author (@since 1.9.1)

**Disable Query Merge**: Turn this on if do not want the query to be auto-merged by Bricks. (@since 1.7.1)

**Meta Query**: Add one or multiple meta queries to filter the posts based on the custom fields.

**Relation**: Define if the meta queries should be inclusive (OR) or exclusive (AND).

**No Results**: Text to be shown when there are no matching results.

### Example 4: The blog authors {#example-3}

In this example, we want to build a section to list all the blog authors.

The blog authors are website users with the role of author. As in the other examples, we've used a container to loop through the users. In that container, we've set a query of user type, setting roles to "Author" to pull only the website's authors.

We've added an Image and a Basic Text element inside the query loop container.

The image we've set to display an ACF Dynamic Data field containing the profile image.

In the Basic Text, we've used the Dynamic Data `{wp_user_display_name}` tag.

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-users-1024x467.png)

<figcaption>

Display the blog authors

</figcaption>

## The Pagination element {#pagination}

The perfect companion to the custom query loop builder. You'll find the Pagination element under the **WordPress** group of the elements panel.

![](https://academy.bricksbuilder.io/assets/bricks-pagination-element.png)

Having pagination as a separate element offers you the most flexibility to build any layout.

After adding the Pagination element to the canvas, you'll need to link this pagination element to one of the elements that run a query. To do so, please select the element in the **Related Query** control by editing the Pagination element:

![](https://academy.bricksbuilder.io/assets/bricks-pagination-related-query.png)

Tip: to make it easier to recognize elements, give descriptive element names to the containers that have a query enabled.

## Load more (button) {#load-more}

Besides the infinite scroll, which automatically loads more results as you scroll down the page, you can also give any element (typically the Button) a "Load more" functionality by adding a "Load more" click [interaction](https://academy.bricksbuilder.io/builder/features/interactions/) to it like this:

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-load-more-button-scaled.jpg)

## Query IDs, Filters, and Live Search {#query-ids}

Each query loop is identified by the element ID of the loop element. On the frontend this is usually the six-character Bricks ID without the `#brxe-` prefix. If the loop element ID is `#brxe-abc123`, the target query ID is usually `abc123`.

Use that ID when you connect:

- Query Filter elements
- A Pagination element
- AJAX pagination, Load More, or Infinite Scroll behavior
- Filter-aware dynamic tags such as `{query_results_count_filter:abc123}`

Query Filters and Live Search support post, term, and user query loops. They do not target API or array query loops.

For Live Search:

1. Add a Filter - Search element.
2. Assign it to the target query.
3. Enable **Live Search** on the target query loop.
4. Set the **Live Search Wrapper Selector** to the element that should show or hide the live-search results.

The wrapper selector is usually the parent element around the loop output.

## Query loop in Accordions & Sliders {#query-accordions-or-sliders}

The classic Accordion and Slider elements also allow to pull data dynamically through the Query Loop to feed the element parts.

You'll find a Query Loop control in the Accordion element to configure a query. The query creates as many accordion items as there are results.

You'll be able to configure the accordion title, subtitle, and content of the "master" accordion item, and this will be used as a template for the dynamic accordion items:

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-accordion.png)

<figcaption>

Use the query loop in the accordion element

</figcaption>

The same happens in the Slider element. If the Query Loop is enabled, you'll have access to a Query control and a slide item, which will behave as the template for all the slides.

![](https://academy.bricksbuilder.io/assets/bricks-query-control-slider.png)

<figcaption>

Use the query loop in the slider element.

</figcaption>

## Include/Exclude Controls: Dynamic Data Tag Support {#include-exclude-dynamic-data}

Starting with Bricks 1.12, the **Include** and **Exclude** post query controls support dynamic data tags.

Starting with Bricks 2.4, the **Include authors** and **Exclude authors** controls accept selected users and dynamic tags that return user IDs.

These controls let the query read IDs from dynamic values instead of only using IDs selected manually in the builder.

- **Include**: Adds post IDs to the `post__in` parameter.
- **Exclude**: Adds post IDs to the `post__not_in` parameter.
- **Include authors**: Adds user IDs to the `author__in` parameter.
- **Exclude authors**: Adds user IDs to the `author__not_in` parameter.

![](https://academy.bricksbuilder.io/assets/include-exclude-authors.png)

The author controls are available for **Posts** queries when **Query editor (PHP)** is turned off. Use them to show posts from selected authors, hide posts from selected authors, or match the loop to the current user or current post author.

![](https://academy.bricksbuilder.io/assets/query-loop-include-supports-dynamic-values.png)

Use dynamic data in these controls when IDs are stored in a custom field or come from the current page context. The query can still use other settings, such as **meta queries** or **taxonomy queries**.

#### Supported Field Types

- **WordPress:** `{wp_user_id}` and `{author_id}` for author include/exclude controls
- **ACF:** Relationship, Post Object, Gallery, User
- **Meta Box:** Relationship, Post, Image Advanced, Image, Image Upload, Single Image, User
- **JetEngine:** Relationship, Post, Gallery, Media (`@since 2.2`)

> **Note**
>
> Important: When using dynamic data in the Include field, ensure the selected Post Type matches the field values. For example, if you are using a Gallery field, set the Post Type to Media to ensure the dynamic value aligns correctly.

For author include/exclude controls, the dynamic tag must return one or more user IDs. Bricks supports native user-related tags such as `{wp_user_id}` and `{author_id}`, plus ACF and Meta Box fields with the **User** field type.

When both include and exclude author rules are present, Bricks removes excluded author IDs from the include list before running the query. If no author remains after that comparison, the query returns no posts.

### Example 1: Retrieve ACF Relationship Posts by Post Type and Order by Post IDs {#filter-acf-relationship-by-post-type}

For an ACF Relationship field that connects to multiple post types, you can limit the returned posts to the "Book" post type and keep the same order defined in the relationship field.

![](https://academy.bricksbuilder.io/assets/query-loop-include-supports-dynamic-values-example-1.png)

### Example 2: Use Meta Box Image Advanced Field for a Slider Query Loop {#query-loop-for-metabox-image-field}

Previously, retrieving images saved in the **Meta Box Image Advanced** field required using a PHP filter to pass the image IDs into the `post__in` parameter. Now, you can achieve this directly within the Query Loop UI.

Simply choose your dynamic field, set the **Post Type** to **Media** and, if needed, add an additional **Mime Type** filter to ensure only the correct image types are included.

> **Note**
>
> Note: Inside the loop, use dynamic tags like `{post_id}` for the image source and `{post_title}` to retrieve the image title. Avoid using `{featured_image}`, as this is not applicable in this context.

![](https://academy.bricksbuilder.io/assets/query-loop-include-supports-dynamic-values-example-2.png)

### Example 3: Query ACF Gallery with Random Order {#query-acf-gallery-with-random-order}

To display images from an **ACF Gallery** field in a random order, set the Post Type to **Media**. (Add an additional Mime Type filter if necessary to ensure only specific file types are included.) Select **Random (rand)** to randomize the order of the images in the gallery.

> **Note**
>
> Note: Inside the loop, use dynamic tags like `{post_id}` for the image source and `{post_title}` to retrieve the image title. Avoid using `{featured_image}`, as this is not applicable in this context.

![](https://academy.bricksbuilder.io/assets/query-loop-include-supports-dynamic-values-example-3.png)

![](https://academy.bricksbuilder.io/assets/query-loop-include-supports-dynamic-values-example-3-result.png)

## Query Type: API {#api-query}

The **API** query loop type lets you render array items returned by an external JSON API. Configure the API request in the API settings popup, including the URL, method, authorization, headers, URL parameters, request body, response path, cache duration, and pagination.

Use `{query_api @key:'fieldName'}` inside the loop to render a field from the current API result.

For full setup details, see [Query data from APIs](https://academy.bricksbuilder.io/builder/dynamic-content/query-data-from-apis/).

Important limitations:

- API query loops do not support Query Filters.
- API query loops do not support Live Search.
- API query loops use their own API settings popup instead of the standard post, term, or user query controls.

## Query Type: Array {#array}

The **Array** query loop type lets you loop through any PHP or JSON array. (`@since 2.2`)

This is useful for:

- Rendering API response arrays. ([API query](https://academy.bricksbuilder.io/builder/dynamic-content/query-data-from-apis/) loop)
- Combining data from multiple sources (e.g. posts + custom arrays).
- Displaying values returned by custom functions in loop format.

![](https://academy.bricksbuilder.io/assets/query-array-control.png)

Once configured, the loop behaves like any other Bricks query: you can style each item using the builder, use dynamic tags to access values, and enable pagination features.

*Supported features: AJAX/non-AJAX pagination, Load More, Infinite Scroll*

#### Use Case 1: Looping Nested Arrays from API Responses

If your API response contains nested arrays (e.g. `cars: ['BMW', 'Mazda']`), use a **nested array loop** and set the correct path in the Array Editor.

![](https://academy.bricksbuilder.io/assets/query-array-nested-loop-with-dynamic-tag.png)

#### Use Case 2: Looping Custom PHP Arrays

If you have a custom PHP function that returns an array, you can use it in the loop using a dynamic tag like `{echo:my_custom_array()}`.

```php
// Ensure that my_custom_array is whitelisted via the bricks/code/echo_function_names hook
function my_custom_array() {
  return [
    ['name' => 'John', 'age' => 30],
    ['name' => 'Jane', 'age' => 25],
  ];
}
```

#### Use Case 3: Render ACF Checkbox Choices as a List

An ACF Checkbox field returns its selected choices as an array. Use that array as the query source to render each choice as a separate list item without custom PHP.

The pattern is not limited to ACF Checkbox fields. Enter any dynamic-data tag that returns a flat array in the **Array Editor**. Bricks creates one loop item for each array value, and `{query_array}` outputs the current value inside the loop.

When you insert `{acf_FIELD_NAME}` directly into a text field, Bricks joins all selected choices into one string with a comma and space between each choice. There is no builder setting for this separator. Changing it requires the [`bricks/dynamic_data/text_separator`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-text_separator/) PHP hook.

The Array query approach keeps every selected choice as a separate loop item. This gives you semantic list markup and lets you style or add content to each choice independently without changing the separator in PHP.

Use **Div** elements for both levels of the list. A Block uses `display: flex` by default, which overrides the browser's normal `ul`, `ol`, or `li` display behavior and can remove list markers. A Div has no default layout styles, so the semantic list elements retain their normal display behavior.

1. Add a **Div** for the list container. Set its **HTML tag** to `ul`, or use `ol` when the order of the choices matters. Leave **Use Query Loop** disabled on this parent element.
2. Add another **Div** inside the list container and set its **HTML tag** to `li`.
3. Enable **Use Query Loop** on the `li` element. Open its **Query** control, set **Type** to **Array**, and enter `{acf_FIELD_NAME}` in the **Array Editor**. Replace `FIELD_NAME` with the Checkbox field name.
4. Add a **Basic Text** element inside the `li` and set its content to `{query_array}`.

The parent `ul` or `ol` renders once. The child `li` is the loop element, so Bricks repeats it for every selected checkbox choice. If the field contains "Breakfast included", "Parking", and "Wi-Fi", the visible result is:

- Breakfast included
- Parking
- Wi-Fi

The ACF field's **Return Format** determines what the loop receives:

- **Label** outputs the choice labels.
- **Value** outputs the stored choice values.
- **Both (Array)** outputs labels by default in Bricks. Use `{acf_FIELD_NAME:value}` in the **Array Editor** when you need the stored values instead. The `:value` modifier is not needed when the field already uses the **Value** return format.

Use the **Style** tab on the parent list element for list-wide spacing and indentation. Style the looping `li` element to apply the same typography, spacing, background, or border to every repeated item.

For nested or associative arrays, use the `{query_array @key:'keyName'}` syntax described below.

![Bricks Structure and Array query settings for rendering ACF Checkbox selections as an ordered list.](https://academy.bricksbuilder.io/assets/acf-checkbox-array-query-use-case.webp)

### Dynamic Data Tag: `{query_array}`

`{query_array}` - Output the current array value (array items are a simple list of strings).

`{query_array @key:'age'}` - Output a specific key from the array item.

#### Example 1: Flat List

```php
[
  'Apple',
  'Banana',
  'Cherry',
  'Donut'
]
```

Use `{query_array}` inside the loop to display each fruit name.

#### Example 2: Associative Array

```php
[
  ['name' => 'John', 'age' => 30],
  ['name' => 'Alan', 'age' => 25],
  ['name' => 'Pony', 'age' => 66]
]
```

Use `{query_array @key:'name'}` and `{query_array @key:'age'}`

#### Example 3: Nested Arrays

```json
[
  {
    "name": "John",
    "age": 30,
    "cars": ["Ford", "BMW", "Fiat"]
  },
  {
    "name": "Elbert",
    "age": 66,
    "cars": ["Mazda", "Benz"]
  }
]
```

To loop through each `cars` array inside the main loop:

1. Nest another **Array Loop** inside the parent loop.
2. In the nested loop's **Array Editor**, set: `{query_array @key:'cars'}`
3. Use `{query_array}` inside the nested loop to output each car.

## Results Filter {#results-filter}

The **Results Filter** feature allows you to filter loop results using conditions **after the array is fetched but before rendering begins**. It is similar to the [bricks/query/result](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/) PHP filter. (`@since 2.2`)

**Supported Loop Types:** Array, ACF Repeater

Use this feature to:

- Remove unnecessary or invalid results based on your requirement
- Prevent rendering of unwanted loop items

![](https://academy.bricksbuilder.io/assets/results-filter-control.png)

#### Example: Filter by Age

For this array:

```php
[
  ['name' => 'John', 'age' => 30],
  ['name' => 'Alan', 'age' => 25],
  ['name' => 'Pony', 'age' => 66]
]

```

You only want to display people whose **age is less than 50**. You can configure a result filter like this:

| Field | Operator | Value |
| --- | --- | --- |
| `{query_array @key:'age'}` | `<` | `50` |

This filter excludes the last item (`Pony`, age 66) from rendering, so only `John` and `Alan` appear in the loop output.

> **Note**
>
> You can add multiple filter rules if needed. Each rule is evaluated with `AND` logic. Use the `bricks/query/result` hook for more complex filtering.

## No Results {#no-results}

Each Query Loop can show fallback content when no results match the query.

You can use:

- **No Results** text for a short message
- A no-results template where that option is available

Bricks may still process loop child elements internally when there are no results so required scripts, styles, and popup assets can be prepared for the page. That does not mean fake loop content is shown to visitors.

## Performance Guidance {#performance}

Use the smallest query that gives you the result you need.

Good defaults:

- Set a realistic **Posts Per Page**, **Number**, or **Items per page** value.
- Avoid `-1` on large datasets.
- Disable query merge on secondary loops.
- Use **No Found Rows** when you do not need pagination or total counts.
- Disable post meta or term cache updates only when the loop does not use that data.
- Add a stable secondary sort when paginating.
- Keep nested loops small.

## Troubleshooting {#troubleshooting}

### The loop shows the wrong posts on an archive

Check whether the loop should merge with the current archive query. For the main archive listing, enable **Is main query (Archive, Search)** and do not disable query merge. For unrelated loops, enable **Disable Query Merge**.

### Pagination shows a 404 on an archive

Make sure only one loop is marked as the main archive/search query, and make sure the Pagination element targets that loop.

### Filters do not change the loop

Check the target query ID on every filter element. Then verify that the target query type is post, term, or user.

### AJAX pagination or Infinite Scroll stopped working

Check whether an optimization plugin is removing Bricks query loop HTML comments such as `<!--brx-loop-start-abc123-->`. Those comments are required markers.

### Dynamic data shows the page instead of the loop item

Make sure the element with the dynamic tag is inside the loop element, and make sure the tag supports the query type.

## Query loop hooks {#hooks}

- [bricks/query/run](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-run/) (filter)
- [bricks/terms/query_vars](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars/) (filter)
- [bricks/users/query_vars](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-users-query_vars/) (filter)
- [bricks/posts/merge_query](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-merge_query/) (filter)
- [bricks/posts/query_vars](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-query_vars/) (filter)
- [bricks/query/loop_object](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object/) (filter)
- [bricks/query/loop_object_id](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object_id/) (filter)
- [bricks/query/loop_object_type](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object_type/) (filter)
- [bricks/query/no_results_content](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-no_results_content/) (filter)
- [bricks/query/before_loop](https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-query-before_loop/) (action)
- [bricks/query/after_loop](https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-query-after_loop/) (action)
- [bricks/query/result](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/) (filter)
- [bricks/query/result_count](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_count/) (filter)
- [bricks/query/result_max_num_pages](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_max_num_pages/) (filter)
- [bricks/query/init_loop_index](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-init_loop_index/) (filter)

---

# Query Data from APIs

Source: https://academy.bricksbuilder.io/builder/dynamic-content/query-data-from-apis/

*Fetch JSON data from external APIs in Bricks and render the returned array inside a Query Loop.*

Starting with Bricks 2.1, the Query Loop can fetch JSON from an external API and render the returned array as loop items.

https://youtu.be/84jlX9gSz7o

Use an API query loop when the data does not live in WordPress:

- Products from an external inventory system
- Recipes, books, events, or jobs from a public API
- Data from another WordPress site's REST API
- Structured data from a custom backend
- A spreadsheet or no-code tool that exposes JSON through an endpoint

> **Note**
>
> API query loops are experimental. They do not support Query Filters, live search, or Bricks components.

## How API Queries Work {#how-it-works}

An API query loop follows this lifecycle:

1. The loop element is set to Query Type **API**.
2. You configure the API request in the API Settings popup.
3. Bricks parses dynamic data in most API settings.
4. Bricks builds the request URL, headers, authorization, body, and pagination parameters.
5. Bricks checks the cache if caching is enabled.
6. Bricks sends the request through WordPress.
7. Bricks decodes the JSON response.
8. Bricks extracts the configured response path.
9. The extracted array becomes the query result.
10. Each array item is rendered once by the loop.

Only array data can be looped. If the response path resolves to an object, a string, a number, or a missing path, the loop cannot render the intended result set.

## Create An API Query Loop {#create}

1. Add a supported loop element such as a Container, Block, or Div.
2. Enable **Query Loop**.
3. Set **Type** to **API**.
4. Click **API Settings**.
5. Enter the API URL and request settings.
6. Click **Fetch** in the preview panel.
7. Set the response path so it resolves to the array you want to loop.
8. Save the API settings.
9. Add child elements inside the loop.
10. Use `{query_api}` dynamic tags to render fields from each item.

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-type-api.png)

## API Settings Popup {#settings-popup}

The API Settings popup has controls on the left and a response preview on the right.

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-api-settings.png)

Use the preview before building the design. If Bricks cannot fetch or parse the response, fix the request first.

## Request Settings {#request-settings}

### Name

The name is an internal label for the API configuration. It is optional, but useful when a page has more than one API query.

Examples:

- `Books API`
- `Events endpoint`
- `Remote WP posts`

### URL

The URL is required. It must point to the endpoint that returns JSON.

Example:

```text
https://example.com/wp-json/wp/v2/posts
```

Dynamic data is supported in the URL. The name and response path are not parsed as dynamic data.

### HTTP Method

Supported methods:

- `GET`
- `POST`

Use `GET` for typical read-only API listings. Use `POST` only when the API requires a body.

### Headers

Bricks sends these default headers:

```text
Content-Type: application/json
User-Agent: BricksBuilder/{CURRENT_VERSION}
```

You can add custom headers or override defaults in the Headers repeater.

### URL Parameters

URL parameters are appended to the endpoint query string.

Example:

| Key | Value |
| --- | --- |
| `limit` | `5` |
| `category` | `news` |

If the URL already contains query parameters, Bricks merges the existing parameters with the configured parameters.

### Request Body

Request Body settings appear for `POST` requests.

Supported body types:

- JSON
- Form Data
- x-www-form-urlencoded

For JSON, enter the raw JSON body. For form modes, use key/value rows.

Pagination parameters can also be added to the body when pagination is configured to use body location.

## Authorization {#authorization}

Bricks supports:

- API key
- Bearer token
- Basic Auth

API keys can be sent in either the request header or URL parameters. Bearer and Basic Auth use the `Authorization` header.

For sensitive values, enable **Use PHP Constant**. Bricks then reads the secret from a PHP constant instead of storing the value in the builder.

Constant names are based on the query element ID:

```php
define( 'BRX_QUERY_API_KEY_ABC123', 'your-api-key' );
define( 'BRX_QUERY_BEARER_TOKEN_ABC123', 'your-token' );
define( 'BRX_QUERY_BASIC_AUTH_USERNAME_ABC123', 'username' );
define( 'BRX_QUERY_BASIC_AUTH_PASSWORD_ABC123', 'password' );
```

Replace `ABC123` with the uppercase query element ID.

Use constants for production credentials. Builder-stored secrets are easier to expose through exports, screenshots, or team access.

## Dynamic Data In API Settings {#dynamic-settings}

Most string settings in the API configuration can use Bricks dynamic data. This includes URL, headers, parameters, body values, and auth values when they are stored directly in settings.

The following are intentionally not parsed as dynamic data:

- API name
- Response path

Dynamic API settings are parsed at request time using the current page context. This is useful for endpoints that depend on the current post, user, term, or URL state.

Examples:

```text
https://example.com/api/events?city={acf_city}
```

```json
{
  "postId": "{post_id}"
}
```

## Response Preview {#preview}

Click **Fetch** to preview the response.

The preview can show:

- Full response tree
- Extracted response path
- Raw JSON view
- Last fetch time
- Error state

If settings changed since the last fetch, Bricks asks you to fetch again before relying on the preview.

Only the first part of large extracted arrays may be shown in the preview, but the saved API query still uses the configured response at render time.

## Response Path {#response-path}

The **Response path** tells Bricks which part of the JSON response should become the loop result.

Leave it empty when the top-level response is already the array you want to loop.

Use dot notation for nested data:

```text
data.results
```

Example response:

```json
{
  "data": {
    "results": [
      {
        "name": "Recipe A"
      },
      {
        "name": "Recipe B"
      }
    ]
  }
}
```

For that response, set:

```text
data.results
```

> **Note**
>
> The response path must resolve to an array. If the path is missing, Bricks falls back to the full decoded response. If that full response is not the intended array, the loop will not render as expected.

## Render API Fields {#render-fields}

Use the `query_api` dynamic data tag inside the API query loop.

Basic field:

```text
{query_api @key:'name'}
```

Nested field:

```text
{query_api @key:'title|rendered'}
```

The pipe character separates nested keys inside the current array item.

![](https://academy.bricksbuilder.io/assets/bricks-query-loop-api-response.png)

In the API response preview, hover a field to copy a ready-to-use dynamic data tag. You can also create a shortcut that appears in the Dynamic Data picker.

> **Note**
>
> API dynamic-data shortcuts are saved in your browser localStorage. They are not saved to the database and are not shared with other users.

## Pagination {#pagination}

API query loops support pagination when the API can receive page or offset parameters and the response exposes a page count or item count.

To enable pagination:

1. Enable **Pagination** in API settings.
2. Add a Pagination element to the page.
3. Set the Pagination element to target the API query.
4. Choose the pagination method.
5. Configure where Bricks should send the pagination parameter.
6. Configure the total items/pages path.

Supported parameter locations:

- URL parameter
- Header
- Request body

### Page Number Pagination

Use page-number pagination when the API expects a page number.

Example:

```text
page=3
```

For the WordPress REST API:

| Setting | Example |
| --- | --- |
| URL parameter | `page` |
| Items per page parameter | `per_page=10` |
| Total path | `header.x-wp-totalpages` |

![](https://academy.bricksbuilder.io/assets/wp-api-pagination-example-new.png)

For page-number pagination, Bricks treats the extracted total value as the total number of pages.

### Offset Pagination

Use offset pagination when the API expects an offset or skip value.

Example:

```text
limit=5&skip=10
```

For offset pagination:

- Configure **Page parameter** as the offset or skip parameter Bricks should update.
- Configure **Offset key** as the parameter or header that contains the items-per-page value.
- Keep that items-per-page value in a URL parameter or header so Bricks can calculate page count.
- Set the total path to a numeric total item count.

![](https://academy.bricksbuilder.io/assets/offset-api-pagination-example-new.png)

For offset pagination, Bricks calculates total pages by dividing total items by items per page.

## Cache Duration {#cache}

API responses are cached with WordPress transients when cache duration is greater than `0`.

Default cache duration:

```text
300 seconds
```

Set cache duration to:

- `0` to disable caching
- A short value while developing
- A longer value for slow or rate-limited APIs

The cache key includes request details such as endpoint, method, headers, URL parameters, and body. Different request parameters create different cache entries.

If an API response does not update as expected, reduce the cache duration, temporarily set it to `0`, or click **Fetch** in the API settings popup to clear that element's API cache.

## Error States {#errors}

Bricks can show or return errors for:

- Missing or invalid API endpoint
- WordPress request errors
- HTTP errors such as 401, 403, 404, or 500
- Empty response body
- JSON decode errors
- Invalid pagination setup
- Missing total path for pagination
- Response path not resolving to the expected data

Common fixes:

- Test the endpoint in a browser or API client.
- Confirm the API returns JSON, not HTML.
- Check authentication values or PHP constants.
- Check CORS only if custom frontend scripts call the API directly. Bricks server-side requests are made through WordPress.
- Set the response path to the array, not to a single object.
- Temporarily set cache duration to `0` while debugging.

## Limitations {#limitations}

API query loops are intentionally narrower than post, term, and user queries.

Current limitations:

- No Query Filters
- No live search
- No Bricks components
- JSON responses only
- Response data must resolve to an array
- No built-in schema mapping beyond `query_api` dynamic tags
- No automatic media import from remote URLs
- No automatic retry/backoff for rate-limited APIs
- Secrets should be handled carefully through PHP constants

If you need filtering, searching, sorting, or complex data joins, consider syncing the external data into WordPress or building a custom integration.

## Practical Examples {#examples}

### WordPress REST API posts

URL:

```text
https://example.com/wp-json/wp/v2/posts
```

URL parameters:

| Key | Value |
| --- | --- |
| `per_page` | `6` |

Response path:

Leave this empty because the WordPress REST API returns an array at the top level.

Render fields:

```text
{query_api @key:'title|rendered'}
{query_api @key:'excerpt|rendered'}
```

### DummyJSON products

URL:

```text
https://dummyjson.com/products
```

URL parameters:

| Key | Value |
| --- | --- |
| `limit` | `8` |

Response path:

```text
products
```

Render fields:

```text
{query_api @key:'title'}
{query_api @key:'price'}
{query_api @key:'thumbnail'}
```

## Troubleshooting {#troubleshooting}

### The loop renders nothing

Check that the response path resolves to an array. If the API returns an object with an array inside it, set the response path to that nested array.

### The preview works but frontend output is stale

Check the cache duration. The preview and frontend can reuse cached responses while caching is enabled.

### Authentication works for one user but not another

Use PHP constants for credentials instead of storing secrets in builder settings. Confirm the constants use the uppercase query element ID.

### Pagination always shows one page

Check **Total items path**. For page-number pagination it should resolve to total pages. For offset pagination it should resolve to total items and Bricks must be able to determine items per page.

### Offset pagination returns the wrong page

Make sure the offset key is the parameter that should receive the calculated offset. For `limit=5&skip=10`, the offset key is `skip`, while `limit` is the items-per-page value.

### Dynamic tags are missing from another browser

Shortcuts created in the API popup are stored in browser localStorage. Recreate the shortcut in that browser, or type the `query_api` tag manually.

### Query Filters do not appear in the API query settings

This is expected. API query loops do not support Query Filters or live search.
