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

Dynamic data availability depends on the element, output type, and context. Component property tags, for example, require a component instance. For gallery output, you may insert a gallery field (like an ACF gallery field type) inside a text element and it will be rendered as a set of `img` tags (using the filter `:image`), like so:

![](https://academy.bricksbuilder.io/assets/dynamic-data-gallery-text-element.png)

![](https://academy.bricksbuilder.io/assets/dynamic-data-gallery-output-text-element.png)

## Distance from a location search {#filter-geo-distance}

Starting with Bricks 2.5, place `{filter_geo_distance}` inside a Posts, Terms, or Users query loop to show each result's distance from an applied Geolocation filter's origin. It uses the filter's unit and label format with one decimal place by default.

```text
{filter_geo_distance}
{filter_geo_distance @to:'mi' @decimals:'2'}
{filter_geo_distance @fallback:'Select a location'}
```

The tag returns nothing when no distance is available unless you provide a fallback. It also works in AJAX-rendered map Info Boxes for the filtered results. See [Geolocation distance arguments](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geo-distance) for unit conversion, precision, and value-only output.

## Component property values {#component-properties}

Since Bricks 2.5, use `{prop.key}` in supported content and settings inside a component to read a value from the current instance. For example, `From {prop.price}` combines a price property with fixed text. Copy the tag from the property's **Reference key** control.

These tags require a component instance context. Image and Link properties offer supported fields such as `{prop.photo.url}` and `{prop.cta.url}` when you need a scalar value in text. See [Properties as Dynamic Data](https://academy.bricksbuilder.io/builder/features/components/#property-dynamic-data) for scope, defaults, conditions, and output limitations.

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

Since Bricks 2.5, Meta Box relationships can also supply options for Select, Radio, and Checkbox query filters. See [Meta Box Relationship Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#metabox-relationship-filters) for setup and relationship direction.

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

#### JetEngine Values and Labels {#jetengine-values}

The output of a JetEngine tag depends on its field type. Use `:value` when you need choice keys or object IDs, for example in an element condition.

| Field type | Default output in text | With `:value` |
| --- | --- | --- |
| Select, Radio | Stored choice key, or keys for a multiple Select | The same stored keys |
| Checkbox | Labels of the checked choices | Keys of the checked choices |
| Posts | Linked post titles | Referenced post IDs |
| Relationship | Linked post titles for relationships between posts | Connected object IDs |
| Media, Gallery | Attachment titles | Attachment IDs |

Select and Radio tags return stored keys by default, so adding `:value` does not change their output. Starting with **Bricks 2.5**, use `:label` to return the selected choice's display label.

For example, a Villa Select field named `country` stores `fr` with the label "France":

| Tag | Output |
| --- | --- |
| `{je_villa_country}` | `fr` |
| `{je_villa_country:value}` | `fr` |
| `{je_villa_country:label}` | `France` |

For a Checkbox field named `amenities`, `{je_villa_amenities}` keeps its existing label output, while `{je_villa_amenities:value}` outputs the checked keys. `{je_villa_amenities:label}` explicitly requests labels from the field's configured option source, including manual choices, glossaries, and registered option sources. Multiple choice keys or object IDs appear as a comma-separated list in text. See [Labels for Choice and Status Values](#label-modifier) for all supported providers and modifier combinations.

For Media and Gallery fields, `:value` resolves attachment IDs from JetEngine's ID, URL, or ID-and-URL array formats. A URL must resolve to a WordPress attachment to return an ID. Image and gallery controls render the selected media according to the control's context.

Dates use Bricks' date formatting. Use a date format or `:timestamp` when you need a specific date representation.

Bricks 2.5 adds [JetEngine Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#jetengine-filters). Those filters match stored keys or IDs while displaying choice labels or related object names. Their supported field types and storage formats are more limited than dynamic data.

## Standard WordPress data {#wordpress}

By default, you may use the following dynamic data tags.

### Post fields {#post-fields}

The following fields are related to the posts or custom post types.

`{post_title}` - Returns the post title

`{post_id}` - Returns the post ID

`{post_url}` - Returns the post link

`{post_slug}` - Returns the post slug

`{post_type}` - Returns the post type (@since 1.12). From Bricks 2.5, `{post_type:label}` returns its registered singular label, such as "Villa" instead of `villa`.

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

`{wp_user_role}` - Returns current user context primary role. Use `:value` to return the role slug. (@since 1.12) From Bricks 2.5, `:label` explicitly requests the primary role's display name.

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
- `:value` - Outputs stored values or object IDs instead of labels where the field type supports it. Use it in element conditions when comparing choice keys or IDs. For ACF choice fields, set the return type to "Both (Array)". Supported ACF types include Select, Checkbox, Radio Button, Button Group, True/False, User, Taxonomy, Image, Gallery, Post Object, and Relationship (`@since 1.12`). Supported Meta Box types include Checkbox List, File Input, File, File Upload, File Advanced, Video, Image, Image Advanced, Image Upload, Single Image, Image Select, Taxonomy, Taxonomy Advanced, Post, and User (`@since 1.12`). See [JetEngine Values and Labels](#jetengine-values) for JetEngine's field-specific output.
- `:label` - Returns the selected choice or status label for supported JetEngine, ACF, Meta Box, WordPress, and WooCommerce tags. Added in Bricks 2.5. See [Labels for Choice and Status Values](#label-modifier) for supported fields, examples, and precedence.
- `:raw` - Skip parsing dynamic data tag
- `:url` - Return URL from post ID. Useful to return URL for `file` field, etc.
- `:format` - Keep HTML format or show empty Star rating for [WooCommerce dynamic data](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/#dynamic-data)
- `:plain` - Removes HTML tags using `wp_strip_all_tags`, which can be helpful when you need to extract plain text from a dynamic tag result. For example, you may want to remove links from a post term dynamic tag.
- `:array_value|{KEY}` - Returns the value of a specific array key within a dynamic tag result. It can be particularly useful for custom fields such as ACF Google Map and ACF Link types. The filter can also be applied to an echo dynamic tag. In cases where the value is a nested array, Bricks will flatten it as a JSON string to allow for seamless output without any errors. It's important to note that this filter should only be used when you are certain that the dynamic tag result is an array. Another important point to keep in mind is that if the specified array key does not exist, this filter will return an empty string. [Examples](#array_value-filter-examples)
- `:timestamp` - Convert the date or time related dynamic data to timestamp value.
- `:slug` and `:term_id` - Used in `{post_terms_xxxx}` dynamic tags, to output slug or term ID, instead of the term name. It can also be helpful in combination with `:plain` filter, like `{post_terms_xxxx:slug:plain}`, when using it inside conditions, taxonomy query, ... to compare the correct values (`@since 2.0`).

### Labels for Choice and Status Values {#label-modifier}

Starting with **Bricks 2.5**, append `:label` to a supported dynamic data tag to output the selected option's display text. For example, `{je_villa_country:label}` returns "France" for a choice stored as `fr`. The label is the selected option's text, not the field title, such as "Country".

Adding this modifier is optional. Existing tags keep their default output, and `:value` keeps its existing behavior.

| Provider | Supported fields or tags |
| --- | --- |
| JetEngine | Select, Radio, and Checkbox, including multiple selections and configured option sources. |
| ACF | Select, Radio Button, Checkbox, and Button Group, with Value, Label, or Both return formats. True/False uses its existing True/False display. |
| Meta Box | Radio, Select, Select Advanced, Checkbox List, Autocomplete, and Button Group. Single Checkbox uses its existing Yes/No display, including customizations. Clone selections are supported. |
| WordPress | `{post_type:label}` returns the registered singular post-type label. `{wp_user_role:label}` returns the primary role's display name. |
| WooCommerce | `{woo_product_type:label}` returns the registered product-type label. `{woo_product_stock_status:label}` returns a stock-status label, such as "In stock". `{woo_order_status:label}` explicitly requests the order-status display name. |

WordPress and WooCommerce labels follow the registered labels, including translations and customizations. Tags still require their normal object context. For example, `{woo_order_status:label}` needs an [order context](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#order-tags), just like the plain order-status tag.

When combining modifiers:

- `:value` takes precedence over `:label` in either order. Both `{je_villa_country:label:value}` and `{je_villa_country:value:label}` return `fr`.
- `:raw` keeps its existing bypass behavior. `:array_value|key` extracts the array value before label conversion.
- Normal text formatting still applies, including `:plain`, word limits, and text separators.

Multiple selections keep their selected order. A selected key with no matching label keeps its original value. A zero key remains valid, an empty selection stays empty, and an explicitly configured empty label stays empty.

This modifier does not add label lookup to generic `cf_*` metadata, relationship titles, media, dates, prices, or fields from CMB2, Pods, or Toolset. On unsupported tags, `label` keeps its existing positional meaning. For example, `{wp_user_meta:label}` still reads the user meta key named `label`.

### Examples of :array_value filter {#array_value-filter-examples}

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

Starting with Bricks 2.5, [Global Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#global-filters) share a filter's behavior across elements of the same type. They are separate from Global Queries. Two linked filters targeting the same loop synchronize selections. Reusing that filter definition on another loop shares its settings while keeping the second loop's selections independent.

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

# Global Filters & Filter Manager

Source: https://academy.bricksbuilder.io/builder/dynamic-content/global-filters-filter-manager/

*Reuse query filter settings across elements, synchronize desktop and mobile filters, and manage global filters in Bricks.*

Starting with **Bricks 2.5**, Global Filters let several filter elements share one saved configuration. Use them for desktop sidebar and mobile Offcanvas filters that should filter the same listing and show the same selections.

The **Filter manager** creates, edits, organizes, imports, and exports global filters. Each linked element keeps its own **Target query**, styling, and presentation.

Enable [Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#enable) before setting up filter elements. Creating and editing global filters requires the **Access filter manager** [builder permission](https://academy.bricksbuilder.io/builder/interface/builder-access/#general).

## How Global Filters Work {#behavior}

A global filter stores shared behavior, such as the source, taxonomy, comparison, URL parameter, and when to apply the filter. An element links to that configuration through its **Global filter** control.

| Setup | Behavior |
| --- | --- |
| Two elements use the same global filter and target the same query | Selections synchronize, and Bricks applies the filter once to that query. |
| Two elements use the same global filter and target different queries | Settings are shared. Each query keeps its own selections and results. |
| Two elements have matching settings but no shared global filter | They remain independent filters. Matching URL parameter names do not link them. |

Global filters are specific to an element type. A Checkbox global filter can be selected by other Checkbox elements, but not by Radio or Select elements.

Supported types are Checkbox, Radio, Select, Range, Search, Datepicker, Geolocation, Submit/Reset, and Active Filters. Pagination is configured separately through its own [Query setting](https://academy.bricksbuilder.io/builder/elements/wordpress/pagination/).

Global Filters do not require a [Global Query](https://academy.bricksbuilder.io/builder/dynamic-content/global-queries-query-manager/). A Global Query shares a loop's query settings. A Global Filter shares a filter's settings. Each filter element still targets the particular loop it should control.

## Create From an Existing Filter {#create-from-element}

1. Select a configured filter element in the builder.
2. Click the save icon beside **Global filter** to open **Create global filter**.
3. Enter a name, such as "Product categories".
4. Optionally add a description and category.
5. Click **Create**.
6. Save the builder.

Bricks moves the supported shared settings into the global filter and links the element to it. The element keeps its target query and presentation settings.

<div className="screenshot screenshot--control-panel">

![Create a global filter from a Checkbox element using the Name, Description, and Category fields.](https://academy.bricksbuilder.io/assets/global-filter-create-popover.webp)

</div>

## Create in Filter Manager {#create-in-manager}

Open **Browser** from the builder toolbar and select **Filter manager**. The settings icon beside an element's **Global filter** control opens the manager directly.

1. Enter a name in the new-filter field below the filter list.
2. Click the save icon or press Enter.
3. In the editor, choose the **Type**. New filters start as Checkbox filters.
4. Set the source and other shared behavior.
5. Optionally assign a category and description.
6. Save the builder.

Creating a global filter in the manager does not add an element to the page. Add a matching filter element and select the saved global filter to use it.

![Filter manager with Product categories selected, organized under Products, and configured as a Checkbox filter using the product category taxonomy.](https://academy.bricksbuilder.io/assets/global-filter-manager-editor.webp)

## Link and Edit Filter Elements {#link-and-edit}

Select a filter element, choose a compatible entry under **Global filter**, and set **Target query** for that element. The dropdown only lists global filters of the same element type.

On a linked element, settings marked with a globe icon belong to the global filter. Editing them updates the shared configuration for every linked element, including elements on other pages. Use the edit icon beside **Global filter** to open that configuration in Filter manager.

| Shared settings | Settings kept on each element |
| --- | --- |
| Source, field mapping, comparison, taxonomy restrictions and ordering | Target query |
| Hierarchical display, Auto toggle child terms, and Count: Include children | Expand/collapse controls, initial expansion, icons, and indentation |
| Filter, sort, or results-per-page action and its options | Styling, classes, layout, and button-style display |
| URL parameter and Apply on | Labels, placeholders, icons, and accessibility group labels |
| Search criteria, debounce, minimum characters, and Enter behavior | Show more/less limits and presentation |
| Range and date behavior, including Datepicker's End date meta key | Choices dropdown/search presentation |
| Default values, range/date endpoints, and Geolocation default location | Geolocation map connection and appearance |
| Reset exclusions and active-filter prefix, suffix, and title | The element's current selection, scoped to its target query |

The available settings depend on the filter type. The globe icon identifies shared controls on the selected element.

[Default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) belong to the global filter. Linked copies targeting the same query start with one shared selection. Copies targeting different queries resolve their defaults independently in the page context. Clearing a shared default leaves linked elements without that default; an older local default is not used instead.

For a [Datepicker with separate start and end fields](https://academy.bricksbuilder.io/builder/elements/filter/filter-datepicker/#separate-date-fields), the provider, field type, and both field selections belong to the global filter. Native metadata and supported ACF, Meta Box, and JetEngine date fields work on posts, terms, and users. Linked elements share those settings and one index. Source, provider, or field-type changes clear the retained end field; select a compatible replacement. If you link an element to a global filter without an **End date meta key**, it uses one-field behavior. An older local end key is not used, including after unlinking.

For a [hierarchical Checkbox filter](https://academy.bricksbuilder.io/builder/elements/filter/filter-checkbox/#collapsible-hierarchy), linked desktop and mobile copies share selections while keeping their own expanded branches and Show more/less state. For example, enable **Show expanded** on the desktop copy and leave it off on the mobile copy. **Count: Include children** uses the shared index. Edit it on the global filter to update every linked copy. See [taxonomy child counts](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts) for an example.

When several elements in the current editing context use the same global filter, **Linked filter elements** lists them below the control. Click an entry to select it. Matching rows are highlighted in Structure. This list does not show every use across the site.

<div className="screenshot screenshot--control-panel">

![A Checkbox element linked to Product categories, with Desktop categories and Mobile categories listed as linked elements and globe icons beside shared settings.](https://academy.bricksbuilder.io/assets/global-filter-linked-controls.webp)

</div>

## Example: Desktop and Mobile Product Filters {#desktop-mobile}

1. Create a product Query Loop and a Checkbox filter that targets it.
2. Set the Checkbox source to **Taxonomy** and choose the product category taxonomy.
3. Create a global filter from this element named "Product categories".
4. Add a second Checkbox filter inside an Offcanvas.
5. Select "Product categories" under **Global filter** and target the same product query.
6. Style the sidebar and Offcanvas copies separately, then save the builder.

Selecting a category in either copy updates the other copy. Both control one category selection for the product query. Test the selection after an AJAX update and after reloading a filtered URL.

**Apply on** is shared. If it is set to **Submit**, both copies wait for a Submit button targeting that query. A desktop copy using Input and a mobile copy using Submit cannot share one global filter configuration.

## URL Parameters and Separate Queries {#url-parameters}

For one target query, the default parameter uses the global filter ID:

```text
?brx_glob01=shirts
```

A custom **URL parameter**, such as `product_category`, uses that name instead. Duplicate controls for one query and reuse on separate pages retain this format.

When the same global filter targets multiple URL-enabled queries on one page, Bricks adds each target query ID to keep their selections separate:

```text
?brx_glob01_querya=shirts&brx_glob01_queryb=shoes
```

With a custom parameter:

```text
?product_category_querya=shirts&product_category_queryb=shoes
```

These IDs are examples. Component queries use their rendered instance IDs. Array-valued filters retain the `[]` URL format.

Bricks derives the suffixes automatically. Reloads, resets, active-filter removal, submit/search redirects, and browser back/forward use the same query ownership. Existing unscoped links remain supported; an explicit query-scoped value takes precedence for that query.

## Unlink, Delete, or Change Type {#unlink-delete}

Clear **Global filter** on an element to unlink it. Bricks copies the current shared settings into that element, preserving its target query and presentation. Save the builder. Future edits on that element are independent.

Bricks blocks deleting a global filter or changing its type while saved content still references it. Unlink the affected elements and save those changes first. References in saved templates, components, legacy global elements, and trashed posts can also prevent removal.

The manager's linked-element list is local to the current editing context, so an empty list there does not prove the global filter is unused elsewhere.

If a save reports that global filters changed since the builder loaded, preserve any work you need, reload the builder, and reapply the changes against the current configuration. Bricks rejects stale global-filter saves to prevent overwriting another saved edit.

## Import and Export {#import-export}

Filter manager's header exports the global filters and categories as JSON. To export only specific filters, select them and use the export icon in the filter-list toolbar. That export includes categories used by the selected filters.

The manager accepts supported JSON and ZIP imports. Imported filters stay unsaved until you save the builder. An imported filter with an existing ID replaces that definition when its type matches. A same-ID filter with a different type is skipped.

For a ZIP package with item selection and **Keep existing** or **Replace** conflict review, use [Global Import / Export](https://academy.bricksbuilder.io/builder/features/global-import-export/). Global filters appear as **Filters**. This import applies selected changes through the bundle importer.

Global filter definitions can move between sites. Elements that still link to a global filter cannot be transferred through cross-site clipboard or template/component imports. Unlink the elements on the source site and save before copying or exporting them. After import, select the destination site's global filter on each matching element and check its target query. Same-site clipboard reuse can retain the link.

Check that the destination has the required taxonomies, custom fields, and plugin data. Importing a definition does not create that content model or transfer generated filter indexes.

## Indexing {#indexing}

Indexable global filters share one index owned by the global filter ID. Adding another linked element does not create a second copy of that index. Counts still reflect each element's target query.

Checkbox, Datepicker, Radio, Select, and Range global filters using the **Filter** action can own value indexes. Search, Submit/Reset, Active Filters, sorting, and results-per-page behavior do not generate their own value indexes.

Source and behavior changes can queue indexing work. Renaming a global filter, changing its category, or editing only its default selections does not rebuild its index. Default-only edits preserve existing index data and indexing progress. Use the existing [indexing tools](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index) to regenerate indexes or continue pending jobs.

## Permissions and Compatibility {#compatibility}

- **Access filter manager** controls creation, shared-setting edits, organization, deletion, and definition import/export. Users without it can select an existing compatible global filter and edit local settings.
- Existing unlinked filter elements stay independent. Bricks does not automatically convert them into global filters.
- Query Filter elements still cannot be placed inside components. Filters outside a component can target its query loops, including supported slot queries. Select the actual rendered loop instance as the target.
- WPML and Polylang do not register global filter settings as translatable strings. Use separate definitions for languages that need different shared labels, values, or term restrictions, and link translated elements to the matching definition.
- On multisite, definitions and categories follow their respective main-site sharing settings. Generated indexes remain separate for each site's content. Shared definition changes synchronize index ownership on each site's next applicable request, rather than immediately rebuilding every site's index.

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
