# Dynamic Data

Source: https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/

*Use Bricks dynamic data to render WordPress fields, custom-field values, and other live content inside text, media, links, and supported element settings.*

Use dynamic data to render all sorts of data from your WordPress database with Bricks.

For example: Featured image, post title, post date, author name, categories, tags, site title, all of your custom fields, etc.

You'll most likely use dynamic data when creating templates in Bricks. Such as your blog post template, and custom post type templates (e.g. single property listing).

## How to insert dynamic data

The dynamic data picker for text shows up when typing a "\{" onto the canvas. You can also click the "bolt" icon in the settings panel to reveal it:

https://youtu.be/DcWIQo2eYdI

Dynamic data for non-text settings such as images, videos, etc. is available from the "Select dynamic data" dropdown menu in the panel settings.

Below you can see an Advanced Custom Fields gallery (named "Gallery") rendered inside the Bricks image gallery element:

![](https://academy.bricksbuilder.io/assets/builder-dynamic-data-panel-1024x576.png)

All dynamic data tags are available in all elements that support dynamic data. This means that you may insert a gallery field (like an ACF gallery field type) inside a text element and it will be rendered as a set of `img` tags (using the filter `:image`), like so:

![](https://academy.bricksbuilder.io/assets/dynamic-data-gallery-text-element.png)

![](https://academy.bricksbuilder.io/assets/dynamic-data-gallery-output-text-element.png)

## Custom Fields Integrations {#integrations}

You can render much more than just standard dynamic WordPress data. Bricks supports the most popular custom fields plugins such as:

- [Advanced Custom Fields](#acf)
- [Meta box](#metabox)
- [Crocoblock (JetEngine)](#jetengine)
- Pods
- CMB2
- Toolset

This allows you to design templates for even the most complex custom post type layouts and data requirements.

### Advanced Custom Fields {#acf}

Bricks integrates with all the ACF and ACF Pro fields, including Flexible Content and Nested Groups.

The fields will be listed in the Dynamic Data dropdown inside of the Bricks builder so you can use them while building your pages and templates with Bricks.

The Relationship (including the [bidirectional](https://www.advancedcustomfields.com/resources/bidirectional-relationships/) implementation) and the Repeater field types are also available inside the Query Loop builder, so you could loop through the output of these fields while rendering the sub-fields as dynamic data.

The ACF field type "[True / False](https://www.advancedcustomfields.com/resources/true-false/)" is great for conditional checks inside the element conditions. By default, the localized "True / False" label is returned. When using it in your element conditions, make sure to apply the `:value` filter. To check for false, you can compare against `== 0`. Or `== 1` to check for true.

![](https://academy.bricksbuilder.io/assets/bricks-acf-field-type-true-false.png)

<figcaption>

Check if ACF True / False field is false

</figcaption>

The following dynamic data can be used together with [Element conditions](https://academy.bricksbuilder.io/builder/features/element-conditions/) effectively.

`{acf_get_row_layout}` - Returns the ACF Flexible layout name

### Meta Box {#metabox}

Bricks is compatible with the Meta Box Post Types, Taxonomies, Custom Fields, and Relationships. Regarding the Custom Fields, Bricks will list the fields inside the builder in the Dynamic Data dropdown. According to the custom field contents, these tags will be rendered properly in the front end.

The Group field (when cloneable) and the Relationships will also be available inside the Query Loop builder. You can iterate through these values and render the sub-fields as dynamic data.

It is also possible to build nested non-clone-able Group fields in Bricks Query Loop.

### Crocoblock JetEngine {#jetengine}

Bricks is compatible with Crocoblock JetEngine Post Types, Meta Boxes (Custom fields), Taxonomies, Relations, and Options pages.

[Custom Content Types](https://crocoblock.com/knowledge-base/jetengine/how-to-showcase-cct-meta-fields-using-dynamic-tags-in-bricks/) (CCT) has been supported since April 2024 by the JetEngine plugin, not Bricks itself. For any CCT questions, please get in touch with the JetEngine support directly.

Bricks integration with the JetEngine plugin makes the custom fields available as dynamic data inside the Bricks builder.

This includes fields from JetEngine meta boxes where **Source** is set to **WooCommerce Product Data** or **WooCommerce Product Variation**.

Bricks uses a separate tag prefix for each source:

- WooCommerce Product Data: `{je_woo_product_<field-name>}`
- WooCommerce Product Variation: `{je_woo_product_variation_<field-name>}`
- Post fields assigned to the Product post type: `{je_product_<field-name>}`

For example, a Product Data field named `delivery_note` uses `{je_woo_product_delivery_note}`. A regular Product post field with the same name uses `{je_product_delivery_note}`. The separate prefixes prevent the two fields from registering the same dynamic data tag.

Bricks also integrates with the JetEngine Relations and Repeaters to feed the Bricks builder query loop.

## Standard WordPress data {#wordpress}

By default, you may use the following dynamic data tags.

### Post fields {#post-fields}

The following fields are related to the posts or custom post types.

`{post_title}` - Returns the post title

`{post_id}` - Returns the post ID

`{post_url}` - Returns the post link

`{post_slug}` - Returns the post slug

`{post_type}` - Returns the post type (@since 1.12)

`{post_date}` - Returns post published date

`{post_modified}` - Returns post modified date

`{post_time}` - Returns post publish time

`{post_comments_count}` - Returns number of comments

`{post_content}` - Returns post content (Gutenberg editor)

`{post_excerpt}` - Returns the post excerpt

`{read_more}` - Renders an anchor tag (link) to the post with the label "Read more"

`{featured_image}` - Renders an image tag with the featured image

These fields support the following **dynamic data filters**:

`{post_title:link}` - Renders the post title as a link to the post

`{post_title:link:3}` - Same as before but the title is limited to 3 words

`{post_title:link:newTab}` - Open post title in new tab

`{post_date:human_time_diff}` - outputs the date difference in a human readable format such as "1 hour", "5 mins", "2 days"

`{post_excerpt:55}` - Limit post excerpt to 55 words. Using the ":" followed by a number limits the output to that number of words

`{post_excerpt:format:10}` - Keep the HTML format and limit post excerpt to 10 words.

`{featured_image:medium_large}` - Renders an image tag with the featured image of size medium_large (defaults to thumbnail size)

`{featured_image:large:link}` - Renders an image tag (within text context) of the featured image, size "large2, wrapped by an anchor tag to the post

### Taxonomies {#taxonomies}

The following dynamic data tags render a list of the taxonomy terms assigned to a post. A link to the term archive wraps each term:

`{post_terms_category}`

`{post_terms_post_tag}`

`{post_terms_my_taxonomy_slug}` - Replace the "my_taxonomy_slug" part with the slug of the actual taxonomy you want to use

`{post_terms_category:plain}` - Remove the links via :plain filter

If you already use a link around your element, you can disable the terms' links output using the [`bricks/dynamic_data/post_terms_links`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-post_terms_links/) filter.

### Terms {#terms}

The following dynamic data tags render data related to taxonomy terms.

`{term_id}` - Renders the term ID

`{term_name}` - Renders the term name

`{term_slug}` - Renders the term slug

`{term_count}` - Renders the term count

`{term_taxonomy_slug}` - Renders the term's taxonomy slug. (@since 1.11)

`{term_parent}` - Renders the current term's parent term name. Returns an empty value if the current term has no parent. (@since 2.4)

`{term_children}` - Renders the current term's direct child term names, separated by a comma. Only direct children are returned, not grandchildren, and empty child terms are included. (@since 2.4)

`{term_url}` - Renders the term archive link

`{term_description}` - Renders the term description

`{term_meta:my_term_meta_key}` - Renders the "my_term_meta_key" meta value

`{term_parent:value}` or `{term_children:value}` - Renders term IDs

`{term_parent:slug}` or `{term_children:slug}` - Renders term slugs

`{term_parent:link}` or `{term_children:link}` - Renders linked term names

You can use `{term_children:value}` in element conditions to check if the current term has child terms. For example, check if `{term_children:value}` is not empty to show an element only for parent terms.

### Author Fields {#author}

`{author_id}` - Returns the post author ID

`{author_name}` - Returns the post author name

`{author_bio}` - Returns the post author biographical info

`{author_email}` - Returns the post author email

`{author_website}` - Returns the post author website

`{author_archive_url}` - Returns the post author url

`{author_avatar}` - Returns the post author avatar as an image tag (text) or an image url (link)

`{author_meta:meta_key}` - Returns the specified author meta value. Set the author meta key as the filter. Example. author_meta:first_name returns the author's first name. See [here](https://developer.wordpress.org/reference/functions/get_the_author_meta/#description) for available author meta keys.

These fields support dynamic data filters like the following:

`{author_bio:20}` - Post author biographical info limited to 20 words

`{author_name:link}` - Post author name rendered as a link to the author profile page

`{author_email:link}` - Post author email rendered as a link

`{author_website:link}` - Post author website rendered as a link

`{author_avatar:200}` - Post author avatar image tag limited to the width/height of 200px

### Query fields {#query}

`{query_loop_index}` - Returns the index of the current loop item, starting at 0. Use the `@start-at` argument to start the index from any other number. Example: `{query_loop_index @start-at:1}` to start the index at 1 instead of 0. The `@pad` argument pads the value to the width you define. Using `{query_loop_index @pad:3}` results in an index output of `001` and `010` instead of `1` and `10`. Using `{query_loop_index @pad:2}` outputs `01` and `10`.

`{query_results_count}` – Use inside or outside a query loop to return the query results count. When used outside a loop you have to pass the query loop ID as a filter to this tag like this: `{query_results_count:quer34}`. "quer34" in this example is the Bricks ID, which you can copy to your clipboard from the right-click context menu.

### Site & Archive fields {#site-archive}

`{site_title}` - Returns site title as defined in the WordPress settings > General > Site Title

`{site_tagline}` - Returns site tagline as defined in the WordPress settings > General > Tagline

`{site_url}` - Returns site URL as defined in the WordPress settings > General > Site address (URL)

`{site_login}` - Returns site login URL. Redirect after login URL can be set by specifying the post ID as the filter like this: `{site_login:3}`

`{site_logout}` - Returns site logout URL. Redirect after logout URL can be set by specifying the post ID as the filter like this: `{site_logout:3}`

`{archive_title}` - Returns archive title

`{archive_title:context}` - Add context to the archive title

`{archive_description}` - Returns archive description (author, post type or term)

You can get dynamic data from the URL parameters like so:

`{url_parameter:my_key}` - Returns the value of the `my_key` parameter in the url (https://mydomain.pt/?my_key=value)

### User profile fields {#user-profile}

`{wp_user_id}` - Returns current user context ID

`{wp_user_login}` - Returns current user context username

`{wp_user_email}` - Returns current user context email address

`{wp_user_url}` - Returns current user context website

`{wp_user_author_url}` - Returns current user context author URL

`{wp_user_role}` - Returns current user context primary role. Use `:value` to return the role slug. (@since 1.12)

`{wp_user_registered_date}` - Returns current user context registered date (@since 1.12)

`{wp_user_nicename}` - Returns current user context nicename

`{wp_user_description}` - Returns current user context biographical info

`{wp_user_first_name}` - Returns current user context first name

`{wp_user_last_name}` - Returns current user context last name

`{wp_user_display_name}` - Returns current user context display name

`{wp_user_picture}` - Returns current user context avatar image tag or url

`{wp_user_meta:my_user_meta_key}` - Returns current user context "my_user_meta_key" meta value

### Native WordPress custom fields

To render your own custom field entries, you have to prefix them with `cf_`.

If your custom field name is `phone_number`, you'd use `{cf_phone_number}` to render this custom field on the front end.

Your `phone_number` custom field entry should also be available in the dynamic data picker dropdown under "Custom fields".

## Date Dynamic Tags {#date}

### Current Date fields {#current-date}

You can render the current date through dynamic data.

`{current_date}` - Returns the current date (UTC) with the format defined at WordPress > Settings > General > Date Format

`{current_wp_date}` - Returns the current date (WordPress timezone) with the format defined at WordPress > Settings > General > Date Format

You may specify a different date format using the PHP date format, for example:

`{current_date:Y}`

`{current_date:Ymd}`

`{current_date:Y-m-d}`

`{current_date:Y.m.d}`

`{current_date:Y/m/d}`

`{current_date:Y m d}`

`{current_date:g:i A}`

`{current_date:timestamp}`

### Format Date {#format-date}

Bricks 2.2 introduces a new dynamic tag `{format_date}` that allows you to convert a date string from one format to another — directly within the builder, without writing any PHP.

`{format_date @date:'your-date-value' @from:'input-format' @to:'output-format'}`

Parameters

- `@date`: The original date string to convert. This can be a raw date or another dynamic tag
- `@from`: The input format (e.g., `Y-m-d`, `Y/m/d`, `Y-m-d\TH:i:s.v\Z`, etc. [https://www.php.net/manual/en/datetime.format.php](https://www.php.net/manual/en/datetime.format.php) )
- `@to`: The desired output format (e.g., `d M Y`, `timestamp`, `Y-m-d (l)`)

##### Example 1: Simple Date format conversion

`{format_date @date:'2025-01-10' @from:'Y-m-d' @to:'d M Y'}`

**Output:** `10 Jan 2025`

##### Example 2: Format from API Response

Assume this dynamic tag returns an ISO-formatted datetime string:

`{query_api @key:'registered'}` → 2025-04-30T09:41:02.053Z

`{format_date @date:'{query_api @key:'registered'}' @from:'Y-m-d\TH:i:s.v\Z' @to:'Y m d (l)'}`

**Output:** `2025 04 30 (Wednesday)`

---

`{query_api @key:'publishDate'}` → 2025-09-22T11:22:33.0123456Z

`{format_date @date:'{query_api @key:'publishDate'}' @from:'Y-m-d\TH:i:s.u\Z' @to:'Y-m-d H:i'}`

**Output:** `2025-09-22 11:22`

##### Example 3: Convert to Timestamp

This is useful especially when you want to use in condition to compare 2 different dates.

Assume a custom field (by your custom plugin) dynamic tag returns a date:

`{cf_my_date}` → 2025/03/25

You can convert it to a UNIX timestamp for comparison:

`{format_date @date:'{cf_my_date}' @from:'Y/m/d' @to:'timestamp'}`

**Output:** `174277440`

### Advanced: echo {#advanced}

> **Note**
>
> Starting at Bricks 1.9.7, you have to explicitly allow any function names that you want to call via Bricks’ dynamic data `echo` tag using the new `bricks/code/echo_function_names` filter. Which you can add to your Bricks child theme or the code snippet plugin of your choice. You can find more information in this article: [/developer/hooks/filters/filter-bricks-code-echo_function_names/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-echo_function_names/)

Bricks 1.4 introduces the `echo` tag to render the output of any PHP function:

`{echo:my_custom_function}` - Echoes the value of the PHP function `my_custom_function()`

It accepts arguments, with or without single quotes, like so:

`{echo:get_the_date('Y-m-d', '55')}` - Echoes the date of the post 55 formatted to `Y-m-d`

### Argument Formatting Rule

When passing arguments to functions inside `{echo:}` tags, all arguments must be enclosed in single quotes, regardless of whether they are static values or dynamic tags. (`@since 1.9.3`)

`{echo:my_function('static value')}`

`{echo:my_function('{post_title}')}`

> **Note**
>
> Please note that the `echo` tag does not support double quotes, and the custom PHP function should `return` the value (do not `echo` the value inside of the custom function).

https://www.youtube.com/watch?v=ajAXEZoyk0E

### Advanced: do_action {#do_action}

The `do_action` tag enables developers and other plugins to integrate with your template designs seamlessly. With this tag, you can place action hooks such as `{do_action:my_custom_hook}` anywhere.

For example, you can insert the `{do_action:woocommerce_after_single_product}` in your WooCommerce single product template, allowing other plugins to hook into it. This enhances the flexibility of your template design.

> **Note**
>
> It is important to note that the `do_action` tag does not support passing arguments to the action. If the `add_action()` function expects additional arguments, an error in PHP will occur. The `do_action` only runs on the front end of the website, not inside the builder.

### WooCommerce {#user-profile}

When the WooCommerce plugin is installed and active, you'll get access to an extra set of Dynamic Data tags related to the products and orders. Please refer to the [WooCommerce builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/#dynamic-data) article for more details.

Bricks 2.4 also adds WooCommerce v2 dynamic tags for cart totals, checkout steps, WooCommerce URLs, account addresses, orders, downloads, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete context-aware reference.

## Filters {#filters}

You can change the output of certain dynamic data tags by using the following filters:

- `:*numeric value*` - When used on a text field, it trims the content to the number of words specified (e.g. `{post_excerpt:10}`). When used with an avatar field like `author_avatar` it specifies the width/height of the avatar image
- `:context` *or* `:prefix` - Add context to the archive title
- `:image `- Outputs the field as an image tag, *e.g.* ``
- `:link` - Output the field as an anchor tag, *e.g.* [`*value*`](https://...)
- `:newTab` - Sets the link to open in a new tab
- `:tel` - The URL of the anchor will be formatted as a telephone number,
*e.g.* [`+123456789`](tel:+123456789)
- `:*text value *`- Depending on the context, it could mean the following:
  - User or term custom field meta key
  - The URL parameter key
  - Post terms separator
  - Date format
  - Image size slug (e.g., thumbnail or full)
  - The echo tag function name
- `:value` - Outputs the value instead of the label. Useful for comparing choices field types like MetaBox checkbox list, etc. inside element conditions, or with ACF choice fields (set the return type to "Both (Array)") such as Select, Checkbox, Radio Button, and Button Group. ACF field types that supporting this filter: True/False, User, Taxonomy, Image, Gallery, Post Object, Relationship (`@since 1.12`) MetaBox field types that supporting this filter: File Input, File, File Upload, File Advanced, Video, Image, Image Advanced, Image Upload, Single Image, Image Select Taxonomy, Taxonomy Advanced, Post, User (`@since 1.12`)
- `:raw` - Skip parsing dynamic data tag
- `:url` - Return URL from post ID. Useful to return URL for `file` field, etc.
- `:format` - Keep HTML format or show empty Star rating for [WooCommerce dynamic data](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/#dynamic-data)
- `:plain` - Removes HTML tags using `wp_strip_all_tags`, which can be helpful when you need to extract plain text from a dynamic tag result. For example, you may want to remove links from a post term dynamic tag.
- `:array_value|{KEY}` - Returns the value of a specific array key within a dynamic tag result. It can be particularly useful for custom fields such as ACF Google Map and ACF Link types. The filter can also be applied to an echo dynamic tag. In cases where the value is a nested array, Bricks will flatten it as a JSON string to allow for seamless output without any errors. It's important to note that this filter should only be used when you are certain that the dynamic tag result is an array. Another important point to keep in mind is that if the specified array key does not exist, this filter will return an empty string. [Examples](#array_value-filter-examples)
- `:timestamp` - Convert the date or time related dynamic data to timestamp value.
- `:slug` and `:term_id` - Used in `{post_terms_xxxx}` dynamic tags, to output slug or term ID, instead of the term name. It can also be helpful in combination with `:plain` filter, like `{post_terms_xxxx:slug:plain}`, when using it inside conditions, taxonomy query, ... to compare the correct values (`@since 2.0`).

##### Examples of :array_value filter {#array_value-filter-examples}

`{acf_place_map:array_value|lat}` - Echoes the `$value['lat']` of the ACF google map type field

`{acf_place_map:array_value|post_code}` - Echoes the `$value['post_code']` of the ACF google map type field

`{acf_ext_link:array_value|title}` - Echoes the `$value['title']` of the ACF link type field

`{je_football-team_logo:array_value|id}` - Echoes the `$value['id']` of the JetEngine media field (Value format set as Array with media ID and URL)

`{mb_testimonials_user_image:array_value|name}` - Echoes the `$value['name']` of the Metabox single image field

`{echo:custom_function:array_value|hello}` - Echoes the `$value['hello']` of PHP `custom_function()` function

## Key-value pair arguments {#arguments}

This feature allows for greater flexibility and customization in displaying dynamic content. The general syntax for using key-value pair arguments is: `{dynamic_data_tag @key:value}`.

- Wrap text with spaces in single quotes.
- The value can include other dynamic data tags (e.g., `{acf_text_field @fallback:'No content was found for {post_title}'}`).

### Available arguments:

<span id="fallback"></span>

`@fallback` – Provides fallback text if the dynamic data tag doesn't return any data. This argument can be used with any dynamic data tag (`@since 1.10`).

- **Example:** `{acf_text_field @fallback:'This is the fallback text!'}`. If `acf_text_field` is empty, "This is the fallback text!" will be displayed.
- **Example**: `{acf_page_builder_cta_modul_options_css_id @fallback:'{acf_get_row_layout}-{query_loop_index}'}`. If `acf_page_builder_cta_modul_options_css_id` is empty, use current ACF flexible layout concatenate with current loop index as return string. Good use case when using this on dynamic CSS ID.

<span id="fallback-image"></span>

`**@fallback-image**` – Used for image dynamic data tags. It accepts either an attachment ID or a URL.

- **Examples:** `{acf_image @fallback-image:554}` or `{acf_image @fallback-image:'https://example.com/placeholder.png'}`. If `acf_image` is not available, the specified image (by attachment ID or URL) will be displayed.

<span id="sanitize"></span>

`@sanitize` - Available `@since 1.11.1` it allows you to control the sanitization method applied to all dynamic tags within a "text" context. By default, all dynamic tags are sanitized using `wp_kses_post`, which helps secure output by stripping unwanted HTML and scripts.

This argument is particularly useful if you have a shortcode outputting JavaScript—such as a form shortcode from plugins—stored within a custom field. In earlier versions, this JavaScript would be sanitized, preventing the form from functioning when the field is output via `{acf_custom_field}`.

**Examples:**

- `{acf_my_wysiwyg @sanitize:false}` – Disables sanitization, allowing scripts to be output if stored in the custom field. **Use carefully, ensuring that the content is safe for output without sanitization.**
- `{acf_my_wysiwyg @sanitize:sanitize_email}` – Applies `sanitize_email` to the `my_wysiwyg` field. If the value doesn’t pass as a valid email, it returns empty.
- `{acf_my_wysiwyg @sanitize:sanitize_email @fallback:'abc@gmail.com'}` – Applies `sanitize_email` to the `my_wysiwyg` field. If the result is empty, it falls back to `'abc@gmail.com'`.

> **Note**
>
> **Note:** The `@sanitize` argument only accepts methods listed in the [WordPress Sanitizing API](https://developer.wordpress.org/apis/security/sanitizing/) , `**false**` or `wp_kses`. If using `@sanitize:false`, be cautious, as this will output the field content without sanitization.

## Bricks hooks related to Dynamic Data {#hooks}

[`bricks/dynamic_data/exclude_tags`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-exclude_tags/) - exclude a list of tags from the Bricks dynamic data logic

[`bricks/dynamic_data/replace_nonexistent_tags`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-replace_nonexistent_tags/) - Disable the default Bricks behavior of replacing the non-existent dynamic data tags with an empty string

---

# Global Queries & Query Manager

Source: https://academy.bricksbuilder.io/builder/dynamic-content/global-queries-query-manager/

*Create, manage, reuse, import, and export global query definitions in Bricks.*

https://youtu.be/b4nGPJIE5rE

Starting with **Bricks 2.1**, Global Queries let you save a Query Loop configuration once and reuse it across your site. The Query Manager is the builder interface for creating, editing, organizing, importing, and exporting those reusable queries.

Use a Global Query when several loops should use the same query logic:

- "Latest news" cards used on multiple landing pages
- A consistent product carousel query
- A reusable team-member query
- A directory listing query with specific roles, ordering, and pagination
- A complex PHP Query Editor setup that should stay centralized
- A shared API query configuration

Global Queries are not required for ordinary one-off loops. Use a local query when the query only belongs to one element.

## Local Query vs Global Query {#local-vs-global}

A **local query** stores all query settings directly on the loop element.

A **global query** stores the full query settings in the site's global Bricks data. The loop element stores only a reference to the global query ID.

When Bricks renders a loop that references a global query, it resolves the global query first and then runs the resolved settings as if they were the loop's query settings.

That means:

- Editing a global query updates every loop that references it.
- Disconnecting a global query copies its current settings into the local loop.
- Deleting or missing global query data leaves referencing loops without the saved global settings.
- Global query settings can include regular query controls, API query settings, and PHP Query Editor settings.

## Create A Global Query From A Loop {#create-from-loop}

<span id="create"></span>

1. Select a supported loop element, such as a Container or Block.
2. Enable **Query Loop**.
3. Configure the query as a local query.
4. In the Query control, click the **Create Global Query** icon.
5. Enter a name.
6. Optionally enter a description and category.
7. Create the query.

![](https://academy.bricksbuilder.io/assets/bricks-global-query-save-button.png)

After creating the global query, Bricks assigns the new global query ID to the loop. The loop now references the global query instead of storing the full local settings.

Use clear names. "Latest Three Properties" is better than "Query 1".

## Create A Global Query In Query Manager {#create-in-manager}

<span id="query-manager"></span>

You can also create a global query directly in Query Manager.

Open Query Manager from:

- Toolbar: **Manage > Query Manager**
- Command Palette: **Manage Queries**
- Query control: globe/gear controls

![](https://academy.bricksbuilder.io/assets/bricks-query-manager-scaled.png)

In Query Manager:

1. Create a new query.
2. Select the query.
3. Enter a name, category, and description.
4. Configure the query settings.
5. Save the builder.

The query is available to any loop that can use Global Queries.

## Use A Global Query {#use}

1. Select a loop element.
2. Enable **Query Loop**.
3. Open the Query control.
4. Click the globe/select control.
5. Choose a global query.

If no global queries exist, the globe selection control is not shown.

After selection, the loop stores the global query ID. The query settings are read from the global query when the builder renders and when the frontend renders.

## Edit A Global Query {#edit}

You can edit a global query in two places:

- Query Manager
- The Query control on a loop that references the global query

When editing a global query inline, Bricks indicates that you are editing a shared query. Changes are global. They affect every loop that references that query ID.

Use inline editing for small, obvious adjustments. Use Query Manager when you need to compare names, categories, descriptions, imports, exports, or several saved queries.

## Disconnect A Global Query {#disconnect}

Disconnect converts a global query reference back into a local query.

When you disconnect:

1. Bricks finds the active global query.
2. It copies the global query settings into the current loop.
3. It removes the global query ID from the loop.
4. Future edits on this loop no longer affect the original global query.

Use Disconnect when one instance needs to become a variation. For example, if five pages use "Latest Three Posts" but one page should show six posts, disconnect that one loop first.

## Query Manager Organization {#organization}

Global queries can have:

- **Name**: Required for identifying the query.
- **Description**: Optional context for teams.
- **Category**: Optional grouping.
- **Settings**: The query configuration itself.

Categories help on larger sites where global queries are used for several areas such as blog, products, events, and members.

Avoid creating too many near-duplicates. If two queries differ only by Posts Per Page, decide whether that difference should be local or whether the shared query should be renamed to match its real purpose.

## Import And Export {#import-export}

Query Manager can export selected global queries as JSON.

Exported data includes:

- Selected queries
- Categories used by those selected queries

Importing adds missing queries and categories to the current site. If an imported query already exists by ID, Bricks treats it as an existing query instead of blindly duplicating it.

Use import/export for:

- Moving reusable query definitions between sites
- Sharing a starter query library across client projects
- Backing up global query definitions before major edits

After importing, open each query and verify post types, taxonomies, meta keys, API endpoints, and any dynamic-data assumptions. A query that is valid on one site can still return nothing on another site if the data model differs.

## Permissions {#permissions}

Access to Query Manager is controlled by the builder permission **Access query manager**.

Users without this permission cannot create, edit, disconnect, or manage global queries through the Query Manager controls. They can still select an existing global query when global queries are available. This matters for teams because changing a global query can affect many pages at once.

Give this permission only to users who understand the site-wide effect of shared query edits.

## Multisite Storage {#multisite}

On multisite installations, Bricks can read Global Queries from the main site when the multisite configuration is set to use main-site global queries. Global Query categories have their own main-site configuration.

The normal builder save path stores query and category changes on the current site. If a multisite query appears missing, unexpectedly shared, or unexpectedly local, check both the main-site query configuration and where the latest save was made.

## Global Queries And PHP Query Editor {#query-editor}

A Global Query can include Query Editor PHP.

Important behavior:

- Code execution must be enabled for PHP query editor code to run.
- Query Editor code is signed.
- Missing or invalid signatures prevent the code from running.
- Code Review can include global query Query Editor code.
- Editing Query Editor code inside a global query can affect every loop using that query.

Use a Global Query for PHP editor code only when centralization is worth the blast radius. For one-off special queries, a local query can be safer.

## Global Queries And API Queries {#api}

Global Queries can store API query settings. This is useful when several loops should read from the same endpoint with the same response path, auth method, cache duration, and pagination settings.

When editing API settings from a loop that references a global query, Bricks can update the global query settings rather than only the local loop. Treat this like any other global edit: every instance may change.

API query shortcuts created in the API popup are stored in browser localStorage. They are not saved as global query data and are not shared with other users.

## Global Queries And Query Filters {#query-filters}

Query Filters target the loop element, not the global query definition.

That means you can reuse one global query in several places and use different filter layouts around each loop. Each filter element still needs the correct target query ID for the loop instance it should control.

If you change the global query's object type or base query settings, all filtered instances may be affected.

## Template Import And Remote Templates {#templates}

Templates and imported content can include loops that reference global queries or include global query data. After importing templates, verify whether the expected global queries came with the import and whether the local site data supports them.

Common checks after import:

- Does the loop still reference a valid global query?
- Does the global query use post types that exist on this site?
- Do taxonomy and meta field names exist?
- Does API authentication need new constants or credentials?
- Does Query Editor code need a valid signature?

## Practical Workflow {#workflow}

For a reusable query:

1. Build and test the query locally on one loop.
2. Confirm the output, pagination, filters, and dynamic data.
3. Save it as a Global Query.
4. Name it according to its purpose.
5. Add a description that explains where it should be used.
6. Apply it to other loops.
7. When editing later, check every major place where it is used.

For a one-off variation:

1. Apply the global query.
2. Disconnect it.
3. Make local changes.
4. Rename the local wrapper/section so future editors know it is intentionally different.

## Troubleshooting {#troubleshooting}

### The globe icon is missing

No global queries exist yet, or the current loop already references a global query. Users without **Access query manager** can select existing global queries, but cannot create, edit, disconnect, or manage them.

### A loop changed on several pages

The loop probably uses a Global Query. Open the Query control and check whether it references a global query ID. If only one page should change, disconnect that loop before editing.

### A global query is selected but output is empty

Check the global query settings, then check the local site data. Missing post types, terms, user roles, meta keys, API responses, or query editor signatures can all produce empty output.

### A disconnected loop still seems linked

After disconnecting, save the builder and reopen the Query control. The loop should show local query settings instead of only a global query ID.

### Imported queries are not organized

Imported categories are included only for selected queries that use those categories. Reassign categories in Query Manager if the current site uses a different organization.

### Team members cannot edit queries

Check the user's builder permissions and enable **Access query manager** only for users who should be allowed to make site-wide query changes.

---

# Query Sort, Filter & Live Search

Source: https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/

*Build sortable, filterable, and searchable query listings in Bricks with query filters, live search, URL parameters, and indexed filter data.*

Query Sort, Filter & Live Search lets visitors change a Bricks Query Loop without a full page reload. You can add search inputs, checkboxes, radio buttons, selects, range sliders, date pickers, submit/reset buttons, active-filter displays, and AJAX pagination.

https://youtu.be/5oDHG-bTAfQ

Use Query Filters for interactive listings such as:

- Blog archive filters
- Product filters
- Directory search
- Team/member filters
- Taxonomy, custom-field, and WordPress-field filters
- Sort controls
- Per-page controls
- Live search boxes

Query Filters target a specific Query Loop. The filter elements can live anywhere on the page as long as each filter points to the correct target query.

## Enable Query Filters {#enable}

1. Go to **Bricks > Settings > Query filters**.
2. Turn on **Enable query sort / filter / live search**.
3. Save settings.
4. Open the builder.
5. Add elements from the **Filter** element group.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.6-filter-elements.png)

When the feature is enabled, Bricks also checks and maintains the custom database tables used for filter elements, filter values, and background indexing jobs.

## Mental Model {#mental-model}

Query Filters are a three-part system:

1. **Filter elements** collect visitor input.
2. **A target query loop** receives the filter state.
3. **Bricks converts filter state into query vars** and refreshes the target loop.

On the initial page load, Bricks can read filter values from URL parameters. During interaction, JavaScript stores the selected filter state, updates the browser URL when needed, sends an AJAX request, receives updated loop HTML, updates dynamic filter elements, and restores focus.

On the server, Bricks sanitizes the selected values, builds query vars for the target query type, merges those vars into the original query, and renders the target query again.

## Supported Query Types {#supported-query-types}

Query Filters support these Query Loop types:

- Posts
- Terms
- Users

They do not support:

- API query loops
- Array query loops
- Deeply nested query targets

In nested query scenarios, filters target the outer supported query layer. Do not expect a filter outside the loop to target a deeply nested child query.

![](https://academy.bricksbuilder.io/assets/scope-limitation-posts-query.png)

<span id="important-notes"></span>

## Component Limitation {#components}

Filter elements should not be placed inside a Bricks component.

The target query loop also should not be a loop inside a component unless the component root itself is the query loop. This limitation exists because filters target concrete query element IDs and AJAX needs to find and render the matching query element reliably.

## Basic Setup {#setup}

<span id="how-to"></span>

1. Create a Query Loop.
2. Copy the target query ID. This is usually the six-character Bricks element ID without `#brxe-`.
3. Add one or more Filter elements.
4. Set **Target Query** on each filter element.
5. Add a Pagination element if the listing should paginate.
6. Enable **AJAX** on Pagination if it should work together with filters.
7. Test the initial page load, AJAX update, browser back button, and direct URL parameter load.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.6-filter-target-query-setting-594x1024.png)

Filters do not need to be inside the same wrapper as the query loop. You can place filters in a sidebar, header, offcanvas, or above the listing.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.6-filter-and-sort-woo-products.png)

## Apply On Input Or Submit {#apply-mode}

<span id="filter-on-input-or-submit"></span>

Filter elements can apply immediately or wait for a submit button.

- **Input**: The query refreshes as soon as the visitor changes the filter.
- **Submit**: The filter value is stored, but the query refresh waits until the visitor clicks a Filter - Submit element that targets the same query.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.6-filter-apply-on-submit.png)

Use **Input** for lightweight listings and search. Use **Submit** when the page has many filters, expensive queries, or a mobile/offcanvas filter UI.

## Filter Elements {#elements}

### Filter - Search {#filter-search-element}

The Search filter sends a text value to the target query.

For post queries, the default search uses the `s` query var. For term and user queries, it uses the query type's search parameter. You can also configure custom search criteria for posts, terms, and users.

Important controls:

- **Target Query**: The query loop to refresh.
- **URL parameter**: The frontend parameter name. Use `s` when the filter should integrate with native WordPress search.
- **Debounce**: Delay before running the search after typing.
- **Min. characters**: Minimum input length before the search runs.
- **Search Criteria**: Custom fields, post fields, term fields, user fields, taxonomies, and weighting options where supported.
- **Clear icon**: Lets visitors clear the search value.
- **Enter action** (Bricks 2.4): Run an AJAX search (default) or redirect to a URL with the current query's filter parameters. A target query is required.
- **Trigger Filter Submit interactions** (Bricks 2.4): Optionally run submit start/end interactions for an Enter-key AJAX search. Ordinary typing and redirects do not run these interactions.

Pressing Enter submits immediately, including with **Apply on: Submit**, without waiting for the typing debounce or minimum character threshold. See [Filter Search](https://academy.bricksbuilder.io/builder/elements/filter/filter-search/#search-with-enter) for redirect and interaction setup.

![](https://academy.bricksbuilder.io/assets/example-filter-search-clear-icon.png)

When the URL parameter is `s` on the main search query, Bricks can use the active Search template's search criteria instead of only the individual filter element settings.

### Filter - Checkbox {#filter-checkbox-element}

Use Checkbox filters when visitors can select multiple values.

Supported sources:

- Taxonomy
- WordPress field
- Custom field

Checkbox filters support hierarchical taxonomy display, include/exclude term options, top-level terms only, count display, child-term auto toggle, and button-style display.

For multiple selected taxonomy or custom-field values, Bricks can combine values with OR or AND logic depending on the filter settings.

![](https://academy.bricksbuilder.io/assets/filter-checkbox-1.11.png)

### Filter - Radio {#filter-radio-element}

Use Radio filters when visitors should choose one value.

Radio filters can act as:

- A filter
- A sort control
- A per-page control

They support taxonomy, WordPress-field, and custom-field sources, plus button-style display.

### Filter - Select {#filter-select-element}

Use Select filters for compact dropdown filtering, sorting, or per-page controls.

Select filters can be single-value or multi-value when Choices.js and multiple selection are enabled. Multi-value filtering uses the same source rules as checkbox filters.

### Filter - Range {#filter-range-element}

Use Range filters for numeric custom fields such as price, area, rating, or score.

Range filters use custom-field source data and build a numeric BETWEEN query. Bricks can use indexed min/max values to set the slider range automatically.

Set decimal places when the values contain decimals. Without the right decimal setting, values can compare incorrectly.

![](https://academy.bricksbuilder.io/assets/filter-range-slider-control-section.png)

### Filter - Datepicker {#filter-datepicker-element}

Use Datepicker filters for date fields.

Datepicker supports single date and date range modes. Bricks sanitizes datepicker values and converts ranges into a two-value format before building query vars.

### Filter - Active Filters {#filter-active-filters-element}

The Active Filters element displays selected filters and lets visitors remove them.

Options include:

- Excluding specific filter IDs from the active filter list
- Prefix, suffix, and title labels configured on individual filters
- Styling active-filter labels and remove buttons

### Filter - Submit / Reset {#filter-submit-reset-element}

Use Submit when filters should wait before refreshing the query. Use Reset to clear active filters for the target query.

Submit can redirect to another URL while preserving current filter values. This is useful for a homepage live-search input that sends visitors to a search results page.

Since Bricks 2.4, **Exclude filter IDs** lets a Reset button preserve selected filters. Enter their Bricks element IDs, separated by commas. For example, exclude a Search filter to keep the search term while clearing category and price refinements. This is separate from the Active Filters element's display exclusions.

With **Hide if no active filter** enabled, Reset hides when no non-excluded filters are active. An excluded search term can remain active while the reset button is hidden. Bricks adds the `brx-no-active-filter` class to this button. See [Filter Submit / Reset](https://academy.bricksbuilder.io/builder/elements/filter/filter-submit/#preserve-a-search-while-resetting-refinements).

![](https://academy.bricksbuilder.io/assets/filter-submit-controls-1.11.png)

Since Bricks 2.4, the Submit element also emits dedicated submit start/end events for AJAX submissions. Use the [Filter Submit interaction triggers](https://academy.bricksbuilder.io/builder/features/interactions/#filter-submit-triggers) when another element should react only to a deliberate submit action, for example closing an Offcanvas after mobile filter results finish loading.

### Pagination {#pagination-element}

Pagination participates in the filter system when AJAX is enabled and it targets the same query. Bricks treats pagination as filter state during AJAX requests so selected filters and the current page stay together.

![](https://academy.bricksbuilder.io/assets/pagination-filter-enable-ajax.png)

If several Pagination elements target the same query, Bricks updates the current page state across those pagination instances.

## URL Parameters {#url-parameters}

Query Filters can be loaded from URL parameters.

Bricks supports two parameter styles:

- `brx_FILTERID=value`
- A custom nice name configured on the filter, such as `category=shirts`

When the page loads, Bricks reads URL parameters, finds matching filter elements, sanitizes the values by filter type, sets each filter's current value, and merges the resulting query vars into the target query.

Use custom nice names when the URL should be human-readable. Use the default `brx_` format when you want a low-friction internal parameter.

On the target Query Loop, enable **Disable URL Params Filter** when the loop should ignore URL parameters even if matching filters exist.

## Browser History {#browser-history}

When URL parameters are enabled, Bricks tracks filter changes in the browser history. Visitors can use the browser back and forward buttons to move between previous filter states.

Bricks listens for browser navigation, restores the selected filter values for the target query, and refreshes the listing through the same AJAX filter flow. Test this when the page also has custom scripts that update the URL.

## Interactions {#interactions}

Bricks adds interaction triggers for filter state and filter submission:

- **Filter: Empty**
- **Filter: Not empty**
- **Filter Submit (Start)**
- **Filter Submit (End)**

Use **Filter: Empty** and **Filter: Not empty** to show or hide helper UI based on whether a filter element has options or values available.

For example, add a wrapper around an "Active Filters" heading and a Filter - Active Filters element. Then add interactions to that wrapper:

- **Filter: Empty**: Hide element
- **Filter: Not empty**: Show element

The trigger checks the selected filter element. When the Active Filters element has nothing to show, the wrapper can stay hidden. When at least one filter is active, the heading and active-filter list appear.

![](https://academy.bricksbuilder.io/assets/filter-empty-trigger-with-active-filters-example.png)

Use **Filter Submit (Start)** and **Filter Submit (End)** to run an action only when a Filter - Submit element starts or finishes an AJAX filter submission for the selected query.

See [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-filter-empty-or-not-empty) for filter option triggers and [Filter Submit triggers](https://academy.bricksbuilder.io/builder/features/interactions/#filter-submit-triggers) for submit-specific triggers.

## How Filter Values Become Query Vars {#query-vars}

Filter values are converted according to their action and source.

| Filter action | Result |
| --- | --- |
| Filter - taxonomy | Adds a taxonomy query |
| Filter - custom field | Adds a meta query |
| Filter - WordPress field | Adds the relevant post, term, or user query var |
| Search | Adds search vars or a custom search result ID list |
| Sort | Adds orderby/order vars |
| Per page | Sets `posts_per_page` or `number` |
| Pagination | Sets `paged` |

Bricks merges filter vars late so active filters can narrow or override the original query. Page-level route context, such as the current taxonomy archive, can also be preserved and merged unless disabled.

## Custom Fields And Indexing {#custom-fields}

<span id="custom-fields-integration"></span>

Bricks Query Filters work best with simple values that can be indexed and compared.

By default, simple custom fields are indexed as plain values. Complex provider-specific fields may need **Custom fields integration** to be indexed correctly. Fields stored as serialized arrays or complex objects are not reliable as default filter sources.

Supported indexed filter element types:

- Checkbox
- Datepicker
- Radio
- Range
- Select

Search, Submit, Active Filters, and Pagination are dynamic filter controls but are not indexed in the same way.

Enable **Custom fields integration** under **Bricks > Settings > Query filters** when filters should use field settings from supported providers.

![](https://academy.bricksbuilder.io/assets/query-filters-custom-fields-integration.png)

When the filter source is **Custom Field**, Bricks shows a **Provider** control if supported providers are active. Choose the provider, then use the dynamic data picker in the **Meta key** control to select the field. Bricks uses the dynamic tag to read the field settings. It does not parse the tag as frontend dynamic data.

![](https://academy.bricksbuilder.io/assets/query-filters-custom-fields-integration-builder-provider-control.png)

Built-in integrations are available for Advanced Custom Fields and Meta Box. They help Bricks index provider-specific field values, generate filter options from field choices, handle date formats, and build the correct custom-field query for fields that do not behave like plain WordPress meta.

ACF support includes fields such as relationship, post object, user, true/false, choice, date picker, and date time picker fields. Meta Box support includes multiple-choice fields and post, taxonomy, user, and date fields. Meta Box custom table fields are not supported by this integration.

## Filter Index {#filter-index}

Bricks stores filter data in custom tables so filter options and counts can be generated efficiently.

The index system tracks:

- Filter elements and their settings
- Whether each filter element is active and indexable
- Indexed values for posts, terms, and users
- Background indexing jobs and progress

The index updates when relevant Bricks data, posts, terms, users, and metadata change. Large sites can require background jobs to finish before every filter option is accurate.

You can manage indexing under **Bricks > Settings > Query filters**.

![](https://academy.bricksbuilder.io/assets/query-filters-regenerate-continue-index-job.png)

Available actions:

- **Regenerate filter index**: Rebuilds index records for all indexable filter elements.
- **Continue index job**: Runs pending index jobs immediately instead of waiting for cron.
- **Fix corrupted database**: Rebuilds stored filter-element metadata when filter elements are missing, stale, or moved.

> **Note**
>
> If index jobs remain pending without progress, check the Query Filter indexer entry in [Known Issues](https://academy.bricksbuilder.io/builder/setup/known-issues/#query-filter-indexer-no-progress).

If your site is protected by HTTP Authentication, background indexing can fail because Bricks cannot reach its own background endpoint. Add authentication headers to Bricks remote requests for the indexing action.

```php
add_filter( 'bricks/remote_post', function( $args, $url ) {
  if ( strpos( $url, 'action=bricks_background_index_job' ) === false && strpos( $url, 'action=bricks_system_info_wp_remote_post_test' ) === false ) {
    return $args;
  }

  $username = 'USERNAME';
  $password = 'PASSWORD';

  $args['headers']['Authorization'] = 'Basic ' . base64_encode( $username . ':' . $password );

  return $args;
}, 10, 2 );
```

## Live Search {#live-search}

Live Search shows query results only after a search interaction.

Setup:

1. Add a Filter - Search element.
2. Create a post, term, or user Query Loop.
3. Set the Search filter's **Target Query** to the loop.
4. Enable **Live Search** in the target query settings.
5. Set **Live Search Wrapper Selector** to the wrapper that should show/hide the result area.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.6-query-control-is-live-search.png)

The wrapper selector is usually the parent around the result loop. Bricks uses it to hide empty live-search results, show the loader during AJAX requests, and hide the result box when the visitor clicks outside the search/results area.

Live Search still prepares the query on page load so required scripts, styles, templates, and popup content are available. On the frontend, Bricks suppresses the initial output until the visitor searches.

## Dynamic Data Tags {#dynamic-data}

Query Filters include dynamic tags that update with AJAX.

### `search_term_filter`

Use this to display the current search term for a target query:

```text
{search_term_filter:abc123}
```

Bricks wraps the value in an AJAX-updatable span tied to the target query.

### `query_results_count_filter`

Use this to display the current result count for a target query:

```text
{query_results_count_filter:abc123}
```

### `search_term`

<span id="search_term"></span>

Use this on a static search results page:

```text
{search_term}
{search_term:abc123}
```

For the value from a Filter - Search element, use `search_term_filter` instead.

### `active_filters_count`

<span id="active_filters_count"></span>

Use this to display the number of active filters for a target query:

```text
{active_filters_count:abc123}
{active_filters_count:abc123 @exclude:'filter1,filter2'}
```

You can style the generated span:

```css
span[data-brx-af-count] {
  /* Your styles here */
}
```

![](https://academy.bricksbuilder.io/assets/active-filters-count-example.png)

## Search Criteria {#search-criteria}

The Search filter can use default search behavior or custom criteria.

For posts, custom criteria can search:

- Post fields
- Post meta keys
- Assigned terms and taxonomies

For terms, custom criteria can search:

- Term fields
- Term meta keys

For users, custom criteria can search:

- User fields
- User meta keys

Weighted search returns IDs in weighted relevance order. Bricks preserves that order unless a sort filter is active.

Every added field or taxonomy can make the query more expensive. Keep the search surface focused.

## Custom Option Labels {#label}

Custom labels are available for Checkbox, Radio, and Select filters.

Use them when the stored value is not visitor-friendly. For example, map `_stock_status` values to "In stock" and "Out of stock".

![](https://academy.bricksbuilder.io/assets/bricks-1.9.6-custom-label-mapping.png)

## Results Per Page {#results-per-page-action}

Filter - Select and Filter - Radio elements can use the **Results per page** action for post, term, and user queries.

![](https://academy.bricksbuilder.io/assets/results-per-page-action.png)

By default, Bricks offers these values:

```text
10, 20, 50, 100
```

Change the values in **Options: Results per page**. Enter a comma-separated list of allowed page sizes.

![](https://academy.bricksbuilder.io/assets/results-per-page-action-example.png)

The active value changes the target query page size for the filtered request. It does not rewrite the original query loop setting. If you show an Active Filters element and do not want the per-page filter listed there, exclude the filter element ID in the Active Filters settings.

## WooCommerce Filter Source {#woocommerce}

When WooCommerce is active, Bricks adds **WooCommerce** as a source for supported filter elements.

![](https://academy.bricksbuilder.io/assets/woocommerce-filter-source.png)

WooCommerce sorting options are also available for supported select and radio filters.

![](https://academy.bricksbuilder.io/assets/woocommerce-sort-source.png)

Supported WooCommerce sources depend on the filter element:

| WooCommerce option | Filter - Radio | Filter - Select | Filter - Checkbox | Filter - Range |
| --- | --- | --- | --- | --- |
| On sale | Yes | Yes | Yes | No |
| In stock | Yes | Yes | Yes | No |
| Featured products | Yes | Yes | Yes | No |
| Product type | Yes | Yes | Yes | No |
| Rating | Yes | Yes | No | No |
| Price | No | No | No | Yes |
| Sort by price | Yes | Yes | No | No |
| Sort by rating | Yes | Yes | No | No |

![](https://academy.bricksbuilder.io/assets/frontend-example-woo-filters.png)

Use WooCommerce filters on product query loops. Common setups combine product category or attribute filters with stock state, price range, rating, and price sorting.

## Practical Patterns {#patterns}

### Archive filter sidebar

Use a Query Loop as the archive main query, add taxonomy filters in a sidebar, and enable AJAX pagination. Keep query merge enabled so the loop still respects the current archive route.

### Product filters

Use taxonomy filters for product categories and attributes, a range filter for price, a checkbox/select for stock state, and a sort select. Regenerate the filter index after adding new product filters.

### Search page with native `s`

Set the Filter - Search URL parameter to `s`, target the main search query, and configure search criteria on the Search template when the filter is part of the main search experience.

### Homepage live search

Use a Filter - Search element with Submit redirect, or use Live Search with a wrapper selector if results should appear inline.

## Troubleshooting {#troubleshooting}

### Filters do not affect the listing

Check that every filter has the correct **Target Query** ID. Then verify that the target loop is a post, term, or user query.

### Filter options are empty or outdated

Regenerate the filter index. If the filter element was duplicated, imported, translated, or moved between templates, also fix the filter element DB.

### URL parameters load but filters do not appear active

Check the filter's URL parameter/nice name, and make sure the filter element still exists and targets the same query ID.

### Search works on input but not on a direct URL

If you expect native search behavior, use `s` as the URL parameter and test the Search template settings. Also check whether **Disable URL Params Filter** is enabled on the query.

### AJAX updates the loop but not the filters

Only dynamic update elements are refreshed after AJAX. Make sure the filter element type is supported and not hidden by element conditions that fail outside the normal page load.

### Filters conflict with another filtering plugin

Avoid combining Bricks Query Filters with plugins or custom code that force-reruns or heavily rewrites the same query. Conflicts are especially likely when another plugin overrides query execution for AJAX filtering.

### Browser back/forward feels wrong

Test whether filters are updating URL state as expected. Bricks restores selected filter state on browser navigation, but custom scripts that rewrite URLs can interfere.
