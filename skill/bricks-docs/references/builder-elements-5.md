# Product stock

Source: https://academy.bricksbuilder.io/builder/elements/product/product-stock/

*Displays the WooCommerce product stock status and quantity information.*

Displays the WooCommerce product stock status and quantity information.

## Settings

### In stock
- **Custom text** (text) - Custom text to display when product is in stock.
- **Typography** (typography) - Typography settings for in stock text.
- **Background color** (color) - Background color for in stock status.

### Low stock / On backorder
- **Custom text** (text) - Custom text to display when product has low stock or is on backorder.
- **Typography** (typography) - Typography settings for low stock/backorder text.
- **Background color** (color) - Background color for low stock/backorder status.

### Out of stock
- **Custom text** (text) - Custom text to display when product is out of stock.
- **Typography** (typography) - Typography settings for out of stock text.
- **Background color** (color) - Background color for out of stock status.

---

# Product tabs

Source: https://academy.bricksbuilder.io/builder/elements/product/product-tabs/

*Displays WooCommerce product tabs such as description, additional information, and reviews.*

Displays WooCommerce product tabs such as description, additional information, and reviews.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Direction** (direction)
- **Alignment** (justify-content)
- **Padding** (spacing)
- **Typography** (typography)
- **Background color** (color)
- **Border** (border)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product title

Source: https://academy.bricksbuilder.io/builder/elements/product/product-title/

*Displays the title of the current WooCommerce product.*

Displays the title of the current WooCommerce product.

## Settings

- **HTML tag** (select) - HTML tag for the title. Options: h1, h2, h3, h4, h5, h6. Default: h1.
- **Prefix** (text) - Text to display before the title.
- **Prefix block** (checkbox) - Display prefix as block element.
- **Suffix** (text) - Text to display after the title.
- **Suffix block** (checkbox) - Display suffix as block element.
- **Link to product** (checkbox) - Make the title a link to the product.

---

# Product up/cross-sells

Source: https://academy.bricksbuilder.io/builder/elements/product/product-upsells/

*Displays up-sell and cross-sell products linked to the current product.*

Displays up-sell and cross-sell products linked to the current product.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Type** (select)
- **Heading** (text)
- **Heading typography** (typography)
- **Max. products** (number)
- **Columns** (number)
- **Gap** (number)
- **Order by** (select)
- **Order** (select)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Query results summary

Source: https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/

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

For a listing with synced map markers, select the results loop containing [Map Connectors](https://academy.bricksbuilder.io/builder/elements/general/map-connector/). The summary describes that loop's results. See [map queries and interactive listings](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#map-queries).

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

---

# Author

Source: https://academy.bricksbuilder.io/builder/elements/single/author/

*Display the current post author in Bricks, including avatar, name, bio, and optional links to the author archive or website.*

Displays information about the post author.

## Settings

### Avatar
- **Show avatar** (checkbox) - Display author avatar. Default: true.
- **Avatar size** (number) - Avatar dimensions. Default: 60px.
- **Avatar position** (select) - Avatar placement. Options: Top, Right, Bottom, Left. Default: Left.
- **Avatar border** (border) - Avatar border settings.
- **Avatar box shadow** (box-shadow) - Avatar shadow settings.

### Name
- **Show name** (checkbox) - Display author name. Default: true.
- **Link to website** (checkbox) - Make name link to author website. Default: true.
- **Typography** (typography) - Name typography.
- **HTML tag** (text) - HTML tag for name. Default: h2.

### Bio
- **Show bio** (checkbox) - Display author biography. Default: true.
- **Typography** (typography) - Bio typography.

### Posts
- **Show link to author posts** (checkbox) - Display button linking to all author posts. Default: true.
- **Padding** (spacing) - Button padding.
- **Text** (text) - Button text. Default: "All author posts".
- **Size** (select) - Button size.
- **Style** (select) - Button style. Default: primary.
- **Background** (color) - Button background color.
- **Border** (border) - Button border.
- **Typography** (typography) - Button typography.

> **Developer reference**
>
> See the [Author Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-author/) for the full JSON schema of this element's settings and controls.

---

# Comments

Source: https://academy.bricksbuilder.io/builder/elements/single/comments/

*The Comments element displays post comments and comment form. It offers two display modes: custom styling with full control over appearance, or default.*

The Comments element displays post comments and comment form. It offers two display modes: custom styling with full control over appearance, or default WordPress styling.

## Settings

### Source

- **Source** (select) - Choose comment display mode. Options: Bricks (custom styling), WordPress (WordPress default styling). Default: Bricks.

### Custom styling controls

When **Source** is set to "Bricks", the following controls are available for customizing the comment display and form:

#### Title

- **Show title** (checkbox) - Display comments section title. Default: true.

- **HTML tag** (select) - HTML tag for title. Options: div, h1-h6. Default: h3. Only available when Show title is enabled.

- **Typography** (typography) - Title typography. Controls `font` property for `.comments-title` selector. Only available when Show title is enabled.

#### Avatar

- **Show avatar** (checkbox) - Display commenter avatars. Default: true.

- **Size** (number with units) - Avatar dimensions. Default: 60px. Triggers re-render.

- **Border** (border) - Avatar border settings. Controls `border` property for `.avatar` selector.

- **Box shadow** (box-shadow) - Avatar shadow settings. Controls `box-shadow` property for `.avatar` selector.

#### Comment

- **Author: HTML tag** (select) - HTML tag for commenter names. Options: div, h1-h6. Default: h5. Triggers re-render.

- **Author: Typography** (typography) - Commenter name typography. Controls `font` property for `.comment-author .fn` selector.

- **Meta: Typography** (typography) - Comment meta typography. Controls `font` property for `.comment-meta` selector.

- **Content: Typography** (typography) - Comment content typography. Controls `font` property for `.comment-content` selector.

#### Form

##### Form title

- **Show** (checkbox) - Display comment form title. Default: true.

- **HTML tag** (select) - HTML tag for form title. Options: div, h1-h6. Default: h4. Triggers re-render. Only available when Show is enabled.

- **Text** (text) - Form title text. Default placeholder: "Leave your comment". Only available when Show is enabled.

##### Label

- **Show** (checkbox) - Display form field labels. Default: true.

- **Typography** (typography) - Label typography. Controls `font` property for `label` selector. Only available when Show is enabled.

- **Placeholder typography** (typography) - Placeholder text typography. Controls `font` property for `::placeholder` selector. Only available when Show is enabled.

##### Cookie consent

- **Show** (checkbox) - Display cookie consent checkbox.

- **Required** (checkbox) - Make cookie consent required. Only available when Show is enabled.

- **Text** (text) - Cookie consent text. Only available when Show is enabled.

##### Fields

- **Fields** (select, multiple) - Form fields to display. Options: Name, Email, Website. Default: Name, Email, Website.

##### Field styling

- **Background color** (color) - Form field background color. Controls `background-color` property for `.form-group input` and `.form-group textarea` selectors.

- **Border** (border) - Form field border settings. Controls `border` property for `.form-group input` and `.form-group textarea` selectors.

- **Typography** (typography) - Form field typography. Controls `font` property for `.form-group input` and `.form-group textarea` selectors.

- **Textarea: Resize** (select) - Textarea resize behavior. Options: None, Vertical, Horizontal, Both. Default: Vertical. Controls `resize` property for `.form-group textarea` selector.

#### Submit button

- **Text** (text) - Submit button text. Default placeholder: "Submit Comment". Supports dynamic data.

- **Size** (select) - Button size. Options from button sizes control options. Default placeholder: "Default".

- **Style** (select) - Button style. Options from styles control options. Default: primary.

- **Background** (color) - Button background color. Controls `background-color` property for `.bricks-button` selector.

- **Border** (border) - Button border settings. Controls `border` property for `.bricks-button` selector.

- **Typography** (typography) - Button typography. Controls `font` property for `.bricks-button` selector.

### WordPress default styling

When **Source** is set to "WordPress", the element uses your theme's default comment styling and form layout. No additional styling controls are available - WordPress handles all comment display through the standard `comments_template()` function.

> **Developer reference**
>
> See the [Comments Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-comments/) for the full JSON schema of this element's settings and controls.

---

# Excerpt

Source: https://academy.bricksbuilder.io/builder/elements/single/excerpt/

*Displays the excerpt of the current post or page.*

Displays the excerpt of the current post or page.

## Settings

- **Excerpt length** (number) - Number of words to display. Default: 15.
- **More text** (text) - Text to append when excerpt is truncated. Default: "...".
- **Keep formatting** (checkbox) - Preserve HTML formatting in the excerpt.

> **Developer reference**
>
> See the [Excerpt Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-excerpt/) for the full JSON schema of this element's settings and controls.

---

# Meta data

Source: https://academy.bricksbuilder.io/builder/elements/single/meta-data/

*Displays post meta information like author, date, comments, etc.*

Displays post meta information like author, date, comments, etc.

## Settings

- **Meta** (repeater) - Dynamic data fields to display. Default includes: `{author_name}`, `{post_date}`, `{post_comments}`.
- **Direction** (direction) - Flex direction for meta items layout.
- **Gap** (number) - Spacing between meta items. Default: 20px.
- **Separator** (text) - Text to display between meta items.
- **Separator color** (color) - Color of the separator text.

> **Developer reference**
>
> See the [Meta Data Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-meta/) for the full JSON schema of this element's settings and controls.

---

# Post content

Source: https://academy.bricksbuilder.io/builder/elements/single/post-content/

*The Post Content element is a placeholder in the builder that tells Bricks to fetch the post content into the layout you're building.*

The **Post Content** element is a placeholder in the builder that tells Bricks to fetch the post content into the layout you're building.

Since Bricks 1.3.5 you can select the source from which to pull the content:

- WordPress Editor (Gutenberg/Classic editor)
- Bricks Data

The **Data Source** control is only visible when the Post Content element is used in Bricks templates.

If the **Post Content** element is placed in a Page/Post, etc. the WordPress content is fetched by default.

## How to use the Post Content element

Inside the builder, go to the Elements panel and look for the **Post Content** element in the Single elements group or use the element search bar in the panel header. Click or drag the Post Content element onto the canvas.

![](https://academy.bricksbuilder.io/assets/post-content-element.png)

If the element is inserted when editing a post or page, it will automatically show the WordPress editor content on the canvas unless there is no Page/Post content. That content is also shown on the front end.

This is useful when creating a **Single Post template** in which you want to show the WordPress content (e.g. a single blog post).

## Lightbox for Gutenberg images

Since Bricks 2.5, the **Lightbox** setting opens media-linked Gutenberg images in the Bricks lightbox. It is off by default and available when the Post Content element uses WordPress as its data source.

1. In the WordPress block editor, link the images in your Image or Gallery blocks to **Media file**.
2. In Bricks, select the **Post Content** element. If you are editing a template, set **Data source** to **WordPress**.
3. Enable **Lightbox** in the element's **Content** tab, save, and check the images on the frontend.

<div className="screenshot screenshot--control-panel">

![Post Content settings with Lightbox enabled for media-linked Gutenberg images.](https://academy.bricksbuilder.io/assets/post-content-lightbox.webp)

</div>

Images within each Gallery block are grouped together so visitors can navigate between them. Separate galleries stay in separate groups, and standalone Image blocks open individually.

The image must come from the WordPress Media Library and link to its full-size media file URL. Custom links, attachment-page links, and images without valid attachment dimensions keep their existing behavior. Unlinked images using WordPress's native **Expand on click** lightbox are unaffected.

This setting changes the rendered output without rewriting your saved Gutenberg blocks. It does not apply when **Data source** is **Bricks**. For more on working with both editors, see [Gutenberg integration](https://academy.bricksbuilder.io/integrations/gutenberg/).

## Fetching Bricks Data with the Post Content element

In certain scenarios, you'd like to edit each post with Bricks instead of using the WordPress editor such as when using more complex layouts that aren't possible with WordPress.

In this case, you need to set the **Data Source** to "Bricks" in the Post Content settings:

![](https://academy.bricksbuilder.io/assets/post-content-data-source.png)

## Creating different page layouts using the Post Content

When using a Bricks template as your page layout this template is rendered on the frontend instead of the individual page created with Bricks.

If you use the **Post Content** element and set the **Data Source** to Bricks, you can design different page templates and still fetch each page content built with Bricks.

A common use case would be to build a page template with two areas: the main area (which is populated with the page content), and a fixed sidebar for all the pages.

To get the Bricks-built content of each page, the Data Source of the Post Content element needs to be set to "Bricks":

<figure>

![](https://academy.bricksbuilder.io/assets/page-template-post-content-element-1024x636.png)

<figcaption>

Bricks Page Template using a Post Content element to fetch page bricks data

</figcaption>

</figure>

## Settings

- **Data source** (select) - Choose content source. Options: WordPress, Bricks. Default: WordPress. The select is only available for templates, since on pages it automatically uses WordPress as the source.
- **Lightbox** (checkbox) - Open media-linked Gutenberg images in the Bricks lightbox. Default: Off. Available for the WordPress data source. Each Gallery block forms its own group.

> **Developer reference**
>
> See the [Post Content Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-content/) for the full JSON schema of this element's settings and controls.

---

# Post navigation

Source: https://academy.bricksbuilder.io/builder/elements/single/post-navigation/

*Displays navigation links to previous and next posts.*

Displays navigation links to previous and next posts.

The element uses WordPress adjacent-post navigation. **Previous** points to the previous post according to WordPress's post-date order, and **Next** points to the next one. This can look reversed when visitors arrive from a posts list sorted by date in descending order.

## Settings

- **Direction** (direction) - Layout direction for navigation items.
- **Max. post width** (number) - Maximum width for post navigation items.
- **In same term** (checkbox) - Navigate within same taxonomy term.
- **Excluded terms** (select) - Terms to exclude from navigation.
- **Taxonomy** (select) - Taxonomy for same term navigation. Default: category.

### Label
- **Show label** (checkbox) - Display navigation labels. Default: true.
- **Prev label** (text) - Label for previous post. Default: "Previous post".
- **Next label** (text) - Label for next post. Default: "Next post".
- **Label typography** (typography) - Typography for navigation labels.

### Title
- **Show title** (checkbox) - Display post titles in navigation. Default: true.
- **Title tag** (text) - HTML tag for post titles. Default: h5.
- **Title typography** (typography) - Typography for post titles.
- **Alignment: Previous post** (justify-content) - Alignment for previous post section.
- **Alignment: Next post** (justify-content) - Alignment for next post section.

### Arrows
- **Prev arrow** (icon) - Icon for previous post navigation.
- **Next arrow** (icon) - Icon for next post navigation.
- **Typography** (typography) - Typography for arrow icons.

You can change the labels and arrows to match the wording used by your design. The element does not include a setting that reverses the underlying adjacent-post lookup. Changing that order requires custom PHP through WordPress's adjacent-post filters, or a custom navigation implementation.

### Image
- **Show image** (checkbox) - Display post featured images. Default: true.
- **Size** (select) - WordPress image size. Default: Thumbnail.
- **Height** (number) - Image height. Default: 60px.
- **Width** (number) - Image width. Default: 60px.
- **Border** (border) - Image border settings.

> **Developer reference**
>
> See the [Post Navigation Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-navigation/) for the full JSON schema of this element's settings and controls.

---

# Post reading progress bar

Source: https://academy.bricksbuilder.io/builder/elements/single/post-reading-progress-bar/

*Shows a progress bar indicating how much of the post has been read.*

Shows a progress bar indicating how much of the post has been read.

## Settings

- **Content** (select) - Choose the content to track reading progress for. Options: post_content, post_excerpt, custom_content. Default: post_content.
- **Position** (select) - Position of the progress bar. Options: top, bottom. Default: top.
- **Height** (number) - Height of the progress bar in pixels. Default: 4.
- **Background color** (color) - Background color of the progress bar.
- **Progress color** (color) - Color of the progress indicator.
- **Show percentage** (checkbox) - Display the reading percentage as text.

> **Developer reference**
>
> See the [Reading Progress Bar Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-reading-progress-bar/) for the full JSON schema of this element's settings and controls.

---

# Post reading time

Source: https://academy.bricksbuilder.io/builder/elements/single/post-reading-time/

*Displays the estimated reading time for a post based on the selected content.*

Displays the estimated reading time for a post based on the selected content.

## Settings

- **Content** (select) - Choose the content to calculate reading time from. Options: post_content, post_excerpt, custom_content. Default: post_content.
- **Prefix** (text) - Text to display before the reading time. Default: "Reading time:".
- **Suffix** (text) - Text to display after the reading time. Default: "min".
- **Words per minute** (number) - Average reading speed in words per minute. Default: 200.
- **Calculation method** (select) - Method to use for calculation. Options: words, characters. Default: words.

> **Developer reference**
>
> See the [Reading Time Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-reading-time/) for the full JSON schema of this element's settings and controls.

---

# Post title

Source: https://academy.bricksbuilder.io/builder/elements/single/post-title/

*Displays the title of the current post or page.*

Displays the title of the current post or page.

## Settings

- **HTML tag** (select) - HTML tag for the title. Options: h1, h2, h3, h4, h5, h6. Default: h1.
- **Type** (select) - Title type. Options: Hero, Lead.
- **Style** (select) - Title style from theme styles.
- **Link to post** (checkbox) - Make the title a link to the post.
- **Add context** (checkbox) - Add context to title on archive/search templates (for template use only).

### Prefix
- **Prefix** (text) - Text to display before the title.
- **Spacing** (number) - Spacing between prefix and title.
- **Block** (checkbox) - Display prefix as block element.
- **Typography** (typography) - Typography settings for prefix text.

### Suffix
- **Suffix** (text) - Text to display after the title.
- **Spacing** (number) - Spacing between title and suffix.
- **Block** (checkbox) - Display suffix as block element.
- **Typography** (typography) - Typography settings for suffix text.

> **Developer reference**
>
> See the [Post Title Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-title/) for the full JSON schema of this element's settings and controls.

---

# Post table of contents

Source: https://academy.bricksbuilder.io/builder/elements/single/post-toc/

*Generates a table of contents based on the headings in the post content.*

Generates a table of contents based on the headings in the post content.

## Settings

- **Content** (select) - Choose the content to generate table of contents from. Options: post_content, post_excerpt, custom_content. Default: post_content.
- **Heading selectors** (text) - CSS selectors for headings to include. Default: "h1,h2,h3,h4,h5,h6".
- **List style** (select) - Style for the list items. Options: none, disc, circle, square, decimal, decimal-leading-zero, lower-roman, upper-roman, lower-greek, lower-latin, upper-latin, armenian, georgian, lower-alpha, upper-alpha. Default: none.
- **Item typography** (typography) - Typography settings for list items.
- **Item padding** (dimensions) - Padding for list items.
- **Item background color** (color) - Background color for list items.
- **Item border** (border) - Border settings for list items.
- **Active item typography** (typography) - Typography settings for active list items.
- **Active item background color** (color) - Background color for active list items.
- **Active item border** (border) - Border settings for active list items.

> **Developer reference**
>
> See the [Table Of Contents Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-toc/) for the full JSON schema of this element's settings and controls.

---

# Related posts

Source: https://academy.bricksbuilder.io/builder/elements/single/related-posts/

*Displays posts related to the current post based on shared taxonomies.*

Displays posts related to the current post based on shared taxonomies.

## Settings

### Title
- **Title** (text) - Section title text.
- **HTML tag** (select) - HTML tag for title. Options: h2, h3, h4, h5, h6. Default: h2.
- **Margin** (spacing) - Title margin.
- **Typography** (typography) - Title typography.

### Query
- **Post type** (select) - Post type to query.
- **Max. related posts** (number) - Maximum number of related posts. Default: 3.
- **Order** (select) - Sort order. Default: Descending.
- **Order by** (select) - Sort criteria. Default: Random.
- **Common taxonomies** (select) - Taxonomies posts must share. Default: category, post_tag.

### Layout
- **Gap** (number) - Spacing between posts. Default: 30px.
- **Posts per row** (number) - Number of posts per row. Default: 3.

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes: `{post_title:link}`, `{post_date}`, `{post_excerpt:20}`.
  - **Dynamic data** (text) - Dynamic data expression.
  - **HTML tag** (select) - HTML tag for field. Default: div.
  - **Margin** (spacing) - Field margin.
  - **Padding** (spacing) - Field padding.
  - **Background color** (color) - Field background color.
  - **Border** (border) - Field border.
  - **Typography** (typography) - Field typography.

### Image
- **Disable** (checkbox) - Hide post images.
- **Aspect ratio** (text) - Image aspect ratio.
- **Image size** (select) - WordPress image size.
- **Position** (select) - Image position. Options: Top, Right, Bottom, Left. Default: Top.
- **Height** (number) - Image height.
- **Width** (number) - Image width.
- **Margin** (spacing) - Image margin.

### Content
- **Width** (number) - Content area width.
- **Padding** (spacing) - Content area padding.
- **Background color** (color) - Content area background color.
- **Overlay content** (checkbox) - Overlay content on image.
- **Horizontal alignment** (align-items) - Content horizontal alignment (overlay mode).
- **Vertical alignment** (justify-content) - Content vertical alignment (overlay mode).

> **Developer reference**
>
> See the [Related Posts Schema](https://academy.bricksbuilder.io/developer/schema/elements/related-posts/) for the full JSON schema of this element's settings and controls.

---

# Social sharing

Source: https://academy.bricksbuilder.io/builder/elements/single/social-sharing/

*Displays social media sharing buttons for the current post.*

Displays social media sharing buttons for the current post.

## Settings

- **Share via** (repeater) - Social media services to include. Default includes: Facebook, X, LinkedIn, WhatsApp, Pinterest, Telegram, VKontakte, Bluesky, Viber (since Bricks 2.5), Email.
  - **Service** (select) - Social media platform.
  - **Excerpt** (checkbox) - Include post excerpt in share (WhatsApp only).
  - **Icon** (icon) - Custom icon for the service.
  - **Background** (color) - Button background color.
  - **Color** (color) - Button text/icon color.
- **Use brand colors** (checkbox) - Apply default brand colors to buttons. Default: true.
- **Direction** (direction) - Layout direction for sharing buttons.
- **Open in new tab** (checkbox) - Open sharing links in new tabs.
- **Rel attribute** (text) - Link rel attribute. Default: "nofollow".

> **Developer reference**
>
> See the [Social Sharing Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-sharing/) for the full JSON schema of this element's settings and controls.

---

# Taxonomy

Source: https://academy.bricksbuilder.io/builder/elements/single/taxonomy/

*Displays taxonomy terms for the current post.*

Displays taxonomy terms for the current post.

## Settings

- **Taxonomy** (select) - Taxonomy to display terms from. Default: post_tag.
- **Disable link** (checkbox) - Remove links from taxonomy terms.
- **Separator** (text) - Text to display between terms.
- **Order by** (select) - Sort terms by criteria. Default: Name.
- **Order** (select) - Sort direction. Default: Ascending.
- **Size** (select) - Button size for terms.
- **Style** (select) - Button style for terms. Default: dark.
- **Spacing** (number) - Gap between terms. Default: 10px.
- **Icon** (icon) - Icon to display with each term.

> **Developer reference**
>
> See the [Taxonomy Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-taxonomy/) for the full JSON schema of this element's settings and controls.

---

# Nav menu

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/nav-menu/

*The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile.*

The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile responsiveness, and various animation effects.

## Settings

### Menu Selection

- **Menu (WordPress)** (select) - Select a WordPress navigation menu to display. Options are populated from available WordPress menus. Includes a link to manage menus in WordPress admin.

- **Alignment** (direction) - Layout direction of the menu. Controls `flex-direction` property for `.bricks-nav-menu` selector.

### Top level

- **Justify content** (justify-content) - Horizontal alignment of menu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Gap** (number with units) - Gap between menu items. Controls `gap` property for `.bricks-nav-menu` selector.

- **Margin** (spacing) - Margin around menu items. Controls `margin` property for `.bricks-nav-menu > li` selector.

- **Padding** (spacing) - Padding inside menu items. Controls `padding` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

- **Background** (background) - Background styling for menu items. Excludes video. Controls `background` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for menu items. Controls `border` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Typography** (typography) - Font settings for top-level menu items. Controls `font` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Active background** (background) - Background styling for active/current page items. Controls `background` property for current menu item selectors including `.bricks-nav-menu > .current-menu-item > a`, `.bricks-nav-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active items. Controls `border` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active items. Controls `font` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for icon controls.

- **Icon (Sub menu)** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu > li.menu-item > .brx-submenu-toggle svg` selector.

- **Icon transform** (transform) - Transform settings for submenu icons when closed. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="false"] > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu > li.menu-item-has-children > .brx-submenu-toggle button[aria-expanded]` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

### Sub menu

- **Position: Static** (checkbox) - Enable to position submenus in document flow (e.g. inside offcanvas). Description: "Enable to position in document flow (e.g. inside offcanvas)."

- **Background** (background) - Background styling for sub-menus. Excludes video. Controls `background` property for `.bricks-nav-menu .sub-menu` selector.

- **Border** (border) - Border styling for sub-menus. Controls `border` property for `.bricks-nav-menu .sub-menu` selector.

- **Box shadow** (box-shadow) - Shadow effect for sub-menus. Controls `box-shadow` property for `.bricks-nav-menu .sub-menu` selector.

- **Transform** (transform) - Transform settings for sub-menus. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu` and `.bricks-nav-menu > li > .brx-megamenu` selectors.

- **Transform (Open)** (transform) - Transform settings for sub-menus when open. Controls `transform` property for `.bricks-nav-menu > li.open > .sub-menu` and `.bricks-nav-menu > li.open > .brx-megamenu` selectors.

#### Caret

- **Caret** (separator) - Separator for caret controls.

- **Size** (number with units) - Size of the caret (triangle pointer). Triggers re-render. Controls `border-width` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector.

- **Color** (color) - Color of the caret. Controls `border-bottom-color` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Transform** (transform) - Transform settings for the caret. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Position** (dimensions) - Position settings for the caret. Controls positioning properties for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

#### Item

- **Item** (separator) - Separator for submenu item controls.

- **Justify content** (justify-content) - Horizontal alignment of submenu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Padding** (spacing) - Padding inside submenu items. Controls `padding` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Background** (background) - Background styling for submenu items. Controls `background` property for `.bricks-nav-menu .sub-menu .menu-item` selector.

- **Border** (border) - Border styling for submenu items. Controls `border` property for `.bricks-nav-menu .sub-menu > li` selector.

- **Typography** (typography) - Font settings for submenu items. Controls `font` property for `.bricks-nav-menu .sub-menu > li > a` and `.bricks-nav-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Separator for submenu active state controls.

- **Active background** (background) - Background styling for active submenu items. Controls `background` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active submenu items. Controls `border` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active submenu items. Controls `font` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for submenu icon controls.

- **Icon** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector.

- **Icon size** (number with units) - Size of submenu icons. Controls `height` and `width` properties for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector, and `font-size` for `.bricks-nav-menu .sub-menu .brx-submenu-toggle i` selector.

- **Icon transform** (transform) - Transform settings for submenu icons. Controls `transform` property for `.bricks-nav-menu .sub-menu button > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu .sub-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle > a + button` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

### Mobile menu

- **Mobile menu** (separator) - Separator for mobile menu controls.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Position** (select) - Position of mobile menu. Options: Right, Left. Default placeholder: "Left".

- **Top** (number with units) - Top position of mobile menu. Controls `top` property for `.bricks-mobile-menu-wrapper` selector.

- **Width** (number with units) - Width of mobile menu. Controls `width` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "300px".

- **Height** (number with units) - Height of mobile menu. Controls `height` property for `.bricks-mobile-menu-wrapper` selector.

- **Fade in** (checkbox) - Enable fade-in animation for mobile menu.

- **Vertical** (justify-content) - Vertical alignment of mobile menu content. Controls `justify-content` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "Top".

- **Horizontal** (align-items) - Horizontal alignment of mobile menu content. Excludes stretch option. Controls `align-items` and `justify-content` properties for `.bricks-mobile-menu-wrapper` selector, and sets `width` to `auto` for `.bricks-mobile-menu-wrapper a`. Default placeholder: "Top".

- **Text align** (text-align) - Text alignment in mobile menu. Controls `text-align` property for `.bricks-mobile-menu-wrapper` selector.

- **Background** (background) - Background styling for mobile menu wrapper. Controls `background` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Background filters** (filters) - Background filters for mobile menu. Controls `filter` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Box shadow** (box-shadow) - Shadow effect for mobile menu. Controls `box-shadow` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Overlay** (background) - Background styling for mobile menu overlay. Excludes video. Controls `background` property for `.bricks-mobile-menu-overlay` selector.

#### Top level

- **Top level** (separator) - Separator for mobile menu top-level controls.

- **Padding** (spacing) - Padding for top-level mobile menu items. Controls `padding` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors. Default placeholder: top 0, right 30, bottom 0, left 30.

- **Background** (color) - Background color for mobile menu items. Controls `background-color` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile menu items. Controls `background-color` property for `[aria-current="page"]` and `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for mobile menu items. Controls `border` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Border (Active)** (border) - Border styling for active mobile menu items. Controls `border` property for current menu item selectors.

- **Typography** (typography) - Font settings for mobile menu items. Excludes text-align. Controls `font` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors.

- **Typography (Active)** (typography) - Typography settings for active mobile menu items. Excludes text-align. Controls `font` property for various current menu item selectors.

#### Icon

- **Icon (Sub menu)** (icon) - Icon for mobile submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg` selector.

- **Close icon (Sub menu)** (icon) - Close icon for mobile submenu toggles. Triggers re-render. Only available when main icon is set. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg.close` selector.

- **Icon typography** (typography) - Typography settings for mobile submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-mobile-menu > .menu-item-has-children .brx-submenu-toggle button` selector. Only available when icon is set.

- **Icon position** (select) - Position of mobile submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around mobile submenu toggle buttons. Controls `margin` property for `.bricks-mobile-menu .menu-item-has-children .brx-submenu-toggle button` selector.

#### Sub menu

- **Sub menu** (separator) - Separator for mobile submenu controls. Description: "Keep open while styling".

- **Padding** (spacing) - Padding for mobile submenu items. Controls `padding` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle > *` selectors.

- **Background** (color) - Background color for mobile submenu items. Controls `background-color` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile submenu items. Controls `background-color` property for current submenu item selectors.

- **Border** (border) - Border styling for mobile submenu items. Controls `border` property for `.bricks-mobile-menu .sub-menu > .menu-item` selector.

- **Border (Active)** (border) - Border styling for active mobile submenu items. Controls `border` property for current submenu item selectors.

- **Typography** (typography) - Font settings for mobile submenu items. Controls `font` property for `.bricks-mobile-menu .sub-menu > li > a` and `.bricks-mobile-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

- **Active typography** (typography) - Typography settings for active mobile submenu items. Controls `font` property for current submenu item selectors.

#### Hamburger toggle

- **Hamburger toggle** (separator) - Separator for hamburger toggle controls.

- **aria-label** (text) - Accessibility label for hamburger toggle button. Default placeholder: "Open mobile menu".

- **Toggle width** (number with units) - Width of hamburger toggle bars. Controls `width` property for `.bricks-mobile-menu-toggle`, `.bricks-mobile-menu-toggle .bar-top`, `.bricks-mobile-menu-toggle .bar-center`, and `.bricks-mobile-menu-toggle .bar-bottom` selectors with `!important`.

- **Color** (color) - Color of hamburger toggle bars. Controls `color` property for `.bricks-mobile-menu-toggle` selector.

- **Hide close** (checkbox) - Hide hamburger toggle when mobile menu is open. Controls `display` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector (sets to `none` with `!important`).

- **Color close** (color) - Color of hamburger toggle when mobile menu is open. Controls `color` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector with `!important`.

- **Close position** (dimensions) - Position of hamburger toggle when mobile menu is open. Controls positioning properties for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector.

### Mega menu

- **Enable** (checkbox) - Enable mega menu functionality.

- **Width** (since Bricks 2.5) - Set a responsive mega menu width directly, such as `900px`, `80%`, a CSS variable, or a `clamp()` value. Leave empty to use the horizontal reference width.

- **Alignment** (since Bricks 2.5) - Position a custom-width menu at the left, center, or right of the horizontal reference area. Default: Left.

- **CSS selector (Horizontal)** (text) - Choose the horizontal reference element. Leave empty to use the page body. Percentage widths are relative to this area. See [Set a custom mega menu width](https://academy.bricksbuilder.io/builder/features/menu-builder/#mega-menu-width) for examples.

- **Toggle on** (select) - How mega menus are triggered. Options: Click, Hover, Click or hover. Default placeholder: "Hover". Only available when mega menu is enabled.

- **Transition** (text) - Transition settings for mega menus. Supports dynamic data. Controls `transition` property for `.brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform** (transform) - Transform settings for mega menus. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu > .brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform (Open)** (transform) - Transform settings for mega menus when open. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu` selector. Only available when mega menu is enabled.

### Multilevel

- **Enable** (checkbox) - Enable multilevel navigation functionality.

- **Back: Text** (text) - Text for back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for back button. Controls `font` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

- **Back: Background** (color) - Background color for back button. Controls `background-color` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

> **Developer reference**
>
> See the [Nav Menu Schema](https://academy.bricksbuilder.io/developer/schema/elements/nav-menu/) for the full JSON schema of this element's settings and controls.

---

# Posts

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/posts/

*The Posts element displays a list or grid of posts with customizable query, layout, and styling options.*

The Posts element displays a list or grid of posts with customizable query, layout, and styling options.

## Settings

- **Query** (query) - Configure which posts to display with filters for post type, categories, tags, etc.

- **Link entire post** (checkbox) - Make the entire post card clickable.

### Layout

- **Layout** (select) - Display style. Options: `list`, `grid`, `masonry`, `metro`.

- **Columns** (number) - Number of columns in grid layout.

- **Spacing** (number with units) - Gap between posts.

- **Image height** (number with units) - Fixed height for images.

- **Image ratio** (text) - Aspect ratio for images.

### Image

- **Image size** (select) - Size of post images.

- **Image position** (select) - Position of images in post cards.

- **Image width** (number with units) - Custom image width.

- **Image height** (number with units) - Custom image height.

### Fields

- **Post title** (checkbox) - Display post titles.

- **Post title tag** (select) - HTML tag for titles.

- **Meta data** (checkbox) - Display post meta (date, author, etc.).

- **Meta data** (repeater) - Configure which meta fields to show.

- **Excerpt** (checkbox) - Display post excerpts.

- **Excerpt length** (number) - Number of words in excerpt.

- **Read more text** (text) - Custom read more link text.

### Content

- Typography and styling controls for post content.

### Overlay

- Overlay settings for post images.

### Filter

- **Filter** (checkbox) - Enable category/tag filtering.

- **Filter taxonomy** (select) - Which taxonomy to filter by.

- **Filter position** (select) - Where to display filters.

### Pagination

- **Pagination** (select) - Pagination type. Options: `none`, `numbers`, `load more`, `infinite scroll`.

- **Load more text** (text) - Text for load more button.

- **Loading text** (text) - Text shown while loading.

- **No more posts text** (text) - Text when no more posts available.

> **Developer reference**
>
> See the [Posts Schema](https://academy.bricksbuilder.io/developer/schema/elements/posts/) for the full JSON schema of this element's settings and controls.

---

# Pagination

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/pagination/

*The Pagination element displays page navigation for query results with customizable styling.*

The Pagination element displays page navigation for query results with customizable styling.

To paginate a listing and its map markers, select the results loop containing [Map Connectors](https://academy.bricksbuilder.io/builder/elements/general/map-connector/), enable **AJAX**, and select the same loop under the map's **Sync with query** setting. See [map queries and interactive listings](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#map-queries).

## Settings

- **Query** (query-list) - Select which query this pagination controls.

- **Enable AJAX** (checkbox) - Refresh the target query without a full page reload. Enable this when using Pagination with [Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#pagination-element).

- **Alignment** (justify-content) - Horizontal alignment of pagination links.

- **Height** (number with units) - Height of pagination buttons.

- **Width** (number with units) - Width of pagination buttons.

- **Spacing** (number with units) - Gap between pagination buttons. Default: 20px.

- **Background** (color) - Background color of pagination buttons.

- **Border** (border) - Border styling for pagination buttons.

- **Typography** (typography) - Font settings for pagination buttons.

### Current

- **Background** (color) - Background color of the current page button.

- **Border** (border) - Border styling for the current page button.

- **Typography** (typography) - Font settings for the current page button.

### Icons

- **Previous Icon** (icon) - Icon for the previous page button.

- **Next Icon** (icon) - Icon for the next page button.

### Miscellaneous

- **End Size** (number) - Number of page numbers shown at the start and end. Default: 1.

- **Mid Size** (number) - Number of page numbers shown on each side of current page. Default: 2.

## AJAX pagination and browser history

In Bricks 2.5, **Enable AJAX** also lets a standalone Pagination element restore its query results and active page when visitors use the browser's Back and Forward buttons. No Query Filter element is required. For example, after visiting pages 1, 2 and 3, Back returns both the URL and results to page 2.

This uses the existing AJAX setting; there is no separate history or scroll-restoration control. Bricks retains the browser's native scroll restoration. Review any **Pagination completed** interactions that scroll the page, since they can also run during standalone history restoration. Developers can use the [pagination history event](https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks/#bricks-ajax-pagination-history-code) after the asynchronous results have been restored.

Queries with Query Filter elements use the filter history workflow. The standalone history event does not signal completion of those filtered queries. Restoring accumulated **Load more** or **Infinite scroll** results is outside this Pagination workflow. If a standalone history request fails, Bricks loads the target URL to recover the matching results.

## Multiple Pagination Elements {#multiple-queries}

Several Pagination elements can target the same query, such as navigation above and below a product listing. They stay on the same page while keeping their own icons and display settings.

Starting with **Bricks 2.5**, Pagination elements targeting different queries on the same page keep independent page numbers. Bricks adds query-specific parameters for custom queries automatically:

```text
?brx_page_querya=2&brx_page_queryb=3
```

Here, `querya` and `queryb` represent the rendered target query IDs. Returning one listing to page one removes only its page parameter. Other queries retain their page and committed filter selections.

This URL format applies when Pagination elements target more than one distinct query on the page. Multiple loops alone do not activate it. Two Pagination elements targeting one query retain the existing URL format.

The main WordPress archive query keeps its normal `/page/N/` or `?paged=N` route. Secondary queries use their own parameters. Bricks chooses an unused suffixed parameter if a filter already uses the expected name. Custom pagination base/format hooks still apply.

Independent pagination works with or without Query Filters enabled. Test the links, reload, and browser back/forward when a page contains several listings.

![Two product listings with independent pagination: Newest arrivals is on page 2 and Products A–Z is on page 3. The address bar includes a separate brx_page parameter for each query.](https://academy.bricksbuilder.io/assets/independent-query-pagination.webp)

> **Developer reference**
>
> See the [Pagination Schema](https://academy.bricksbuilder.io/developer/schema/elements/pagination/) for the full JSON schema of this element's settings and controls.

---

# Search

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/search/

*Display an inline search form or an icon that opens a search overlay, with separate input, submit, and close controls.*

The Search element displays a search form or an icon that opens a search overlay. Set **Type** to **Input** for an inline form or **Icon & Overlay** for an overlay. **Input** is the default.

## Settings

- **Action URL**: Where the form submits. Leave it empty to use your site's home URL.
- **Additional parameters**: Add hidden fields to the submitted search request.

In Bricks 2.5, the controls are grouped by the part of the search form they affect. The overlay's opening icon, submit button, and close button have separate controls.

<div className="screenshot screenshot--control-panel">

![Search controls in Icon & Overlay mode, with Keep open while styling enabled and separate Icon, Input, Overlay, Submit button, and Close button groups.](https://academy.bricksbuilder.io/assets/builder/release-2.5/search-controls-panel.webp)

</div>

## Input

Use **Input** to style the search field in either mode. Set its height, width, placeholder, background, border, box shadow, and typography. The default placeholder is “Search ...”.

Enable **Show label** to display a label above the field, then set **Label text** and **Label typography**.

## Inline submit button

With **Type** set to **Input**, open **Submit button** to set the button's text, icon, size, spacing, colors, border, box shadow, and typography.

If the button uses an icon without visible text, provide an **aria-label** that describes its action, such as `Search`.

## Icon and overlay

With **Type** set to **Icon & Overlay**, choose the opening icon under **Icon**. Its **aria-label**, such as `Open search`, names the button for screen-reader users.

Enable **Keep open while styling** to keep the overlay visible in the Builder while adjusting its controls. This preview setting does not force the overlay open on the frontend.

![The Search overlay visible on the Builder canvas with a Search Atelier North title, search field, submit button, and close icon.](https://academy.bricksbuilder.io/assets/builder/release-2.5/search-overlay-builder.webp)

### Overlay layout and title

Under **Overlay**, set the form direction, gap, title, title tag, title typography, and background.

The default title is **Search site**, using an `h4` tag. Enable **Hide title** to remove the visible title. The overlay and search field keep their accessible names when the title is hidden.

### Overlay submit button

Open **Submit button** to set the overlay form's submit text, icon, **aria-label**, and styling. These controls affect the button inside the overlay, separately from the icon that opens it.

For example, use a magnifying-glass icon to open the overlay and a text button labelled `Search` to submit the form.

### Close button

Open **Close button** to choose its icon, **aria-label**, size, spacing, colors, background, border, and box shadow. Bricks uses a close icon and the accessible name **Close search** when you leave those settings empty.

### Existing search elements

Existing opening icons and button styles retain their saved values. After updating to Bricks 2.5, review any custom CSS targeting the search form, especially rules that style every button in the overlay. Use the separate control groups when each button needs different styling.

> **Developer reference**
>
> See the [Search Schema](https://academy.bricksbuilder.io/developer/schema/elements/search/) for the full JSON schema of this element's settings and controls.

---

# Shortcode

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/shortcode/

*The Shortcode element executes WordPress shortcodes within your Bricks pages.*

The Shortcode element executes WordPress shortcodes within your Bricks pages.

## Settings

- **Shortcode** (textarea) - Enter the shortcode to execute, including the square brackets (e.g., `[gallery ids="72,73,74,75" columns="3"]`). Supports dynamic data.

- **Don't render in builder** (checkbox) - Show a placeholder instead of rendering the shortcode in the builder. Useful for shortcodes that slow down the builder or cause conflicts.

- **Placeholder: Width** (number with units) - Width of the placeholder when "Don't render in builder" is enabled.

- **Placeholder: Height** (number with units) - Height of the placeholder when "Don't render in builder" is enabled.

> **Developer reference**
>
> See the [Shortcode Schema](https://academy.bricksbuilder.io/developer/schema/elements/shortcode/) for the full JSON schema of this element's settings and controls.

---

# Sidebar

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/sidebar/

*Displays a WordPress sidebar with its widgets.*

Displays a WordPress sidebar with its widgets.

## Settings

- **Sidebar** (select) - Select which sidebar to display. Default: none.
- **Widget margin** (spacing) - Set the margin for widgets. Default: 0 0 40px 0.
- **Title typography** (typography) - Typography settings for widget titles.
- **Content typography** (typography) - Typography settings for widget content.
- **Search background color** (color) - Background color for search inputs in widgets.
- **Search border** (border) - Border settings for search inputs in widgets.

> **Developer reference**
>
> See the [Sidebar Schema](https://academy.bricksbuilder.io/developer/schema/elements/sidebar/) for the full JSON schema of this element's settings and controls.

---

# WordPress

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/wordpress/

*The WordPress element displays various WordPress widgets with customizable styling.*

The WordPress element displays various WordPress widgets with customizable styling.

## Settings

- **Widget** (select) - Type of WordPress widget to display. Options: `archives`, `calendar`, `categories`, `pages`, `recent comments`, `recent posts`, `tag cloud`, `taxonomy`. Default: `posts`.

- **Icon** (icon) - Optional icon for the widget. Available for most widget types.

- **Icon typography** (typography) - Font settings for the icon.

### Widget-specific settings

- **Show count** (checkbox) - Display item counts. Available for archives, categories, tag cloud, taxonomy.

- **Sort by** (select) - Sort order for pages. Options: `page title`, `page date`, `page modified`, `page order`, `page ID`. Available for pages.

- **Include** (select) - Specific pages to include. Available for pages.

- **Exclude** (select) - Specific pages to exclude. Available for pages.

- **Number of comments** (number) - How many recent comments to show. Available for recent comments.

- **Number of posts** (number) - How many recent posts to show. Available for recent posts.

- **Direction** (direction) - Layout direction for posts. Available for recent posts.

- **Show date** (checkbox) - Display post dates. Available for recent posts.

- **Show featured image** (checkbox) - Display post thumbnails. Available for recent posts.

- **Featured image sizes** (select) - Size of featured images. Available for recent posts.

- **Featured image width** (text) - Custom width for images. Available for recent posts.

- **Featured image height** (text) - Custom height for images. Available for recent posts.

- **Post title typography** (typography) - Font settings for post titles. Available for recent posts.

- **Post meta typography** (typography) - Font settings for post meta. Available for recent posts.

- **Taxonomy** (select) - Which taxonomy to display. Available for tag cloud and taxonomy.

### Title

- **Title** (text) - Custom title for the widget.

- **HTML tag** (select) - HTML tag for the title. Options: `p`, `h1`-`h6`. Default: `h3`.

- **Border** (border) - Border styling for the title.

- **Typography** (typography) - Font settings for the title.

> **Developer reference**
>
> See the [WordPress Schema](https://academy.bricksbuilder.io/developer/schema/elements/wordpress/) for the full JSON schema of this element's settings and controls.

---

# Account - Add payment method

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-add-payment-method/

*Displays the Add payment method endpoint content inside My Account templates.*

Displays the Add payment method endpoint content inside My Account templates.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Wrapper** (separator)
- **Payment Methods List** (separator)
- **Payment Method Item** (separator)
- **Label** (separator)
- **Custom Radio (Checked)** (separator)
- **Color** (color)
- **Payment Box** (separator)
- **Add Payment Method Button** (separator)
- **Margin** (spacing)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Addresses

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-addresses/

*Displays the customer addresses section inside My Account.*

Displays the customer addresses section inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Direction** (direction)
- **Gap** (number)
- **Title** (separator)
- **Address** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Downloads

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-downloads/

*Displays customer downloadable products inside My Account.*

Displays customer downloadable products inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Table** (separator)
- **Head** (separator)
- **Body** (separator)
- **Links** (separator)
- **Button** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Edit account

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-edit-account/

*Displays the Edit account form inside My Account.*

Displays the Edit account form inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Label typography** (typography)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Width** (number)
- **Gap** (number)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Edit address

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-edit-address/

*Displays the Edit address form inside My Account.*

Displays the Edit address form inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Hide** (checkbox)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Label typography** (typography)
- **Placeholder typography** (typography)
- **Field** (separator)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Login form

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-login/

*Displays the WooCommerce My Account login form.*

Displays the WooCommerce My Account login form.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Lost password

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-lost-password/

*Displays the Lost password request form used in My Account flows.*

Displays the Lost password request form used in My Account flows.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Register form

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-register/

*Displays the WooCommerce account registration form.*

Displays the WooCommerce account registration form.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Generate password** (separator)
- **Typography** (typography)
- **Privacy policy** (separator)
- **Link** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Reset password

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-reset-password/

*Displays the Reset password form used after password reset link validation.*

Displays the Reset password form used after password reset link validation.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Orders

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-orders/

*Displays the customer orders table inside My Account.*

Displays the customer orders table inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Head** (separator)
- **Body** (separator)
- **Body - Heading** (separator)
- **Links** (separator)
- **Button** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Page

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page/

*Displays the full My Account layout including navigation and endpoint content.*

Displays the full My Account layout including navigation and endpoint content.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Align items** (align-items)
- **Justify content** (justify-content)
- **Background** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Item** (separator)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Page v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/

*Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.*

Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.

https://youtu.be/M1ZZLgnZOjM

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**. The generated states also use the Bricks WooCommerce Notice element, so enable **Enable Bricks WooCommerce "Notice" element** on the same tab.

## Set up the account page

1. Go to **Bricks > Settings > WooCommerce**, enable **Enable advanced modular elements** and **Enable Bricks WooCommerce "Notice" element**, and save.
2. Open **Bricks > Woo Setup Wizard** and choose **My account**. **Advanced (v2)** is selected by default.
3. Click **Setup** and confirm that the existing page content will be replaced.

The wizard adds **Account - Page v2** to the assigned My Account page with a generated structure for every state. See [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) for the other options.

## Where this element works

My Account page.

## Key settings

- **State** (radio) - Switches the builder preview between My Account endpoint states.
- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Navigation** - Direction, Align items, Justify content, Gap, Border, and Box shadow for the menu; Background, Item padding, Border, Box shadow, and Typography for each item; Active background, Border, Box shadow, and Typography for the current item.
- **Content** - Padding, Background, Border, Box shadow, and Typography for the content area.

Navigation and Content styles apply to every logged-in state at once. Set **Direction** to row to place the menu beside the content, then set the navigation **Direction** to column for a sidebar menu.

The navigation is not shown on the **Login**, **Lost password**, **Lost password (Confirmation)**, **Reset password**, and **Order withdrawal** states.

## Navigation items

The menu items come from the WooCommerce account endpoints. To remove an item, for example **Downloads** in a store without downloadable products, go to **WooCommerce > Settings > Advanced**, clear the endpoint's slug under **Account endpoints**, and save.

## Builder preview

- **Orders** and **View order** use the orders of the account you are logged in with. If that account has no orders, the canvas shows the generated dynamic tags and the empty orders message. Customers see their own orders on the frontend.
- Sample WooCommerce notices (error, success, and info) appear above the states in the builder so you can style them. They are not shown to customers.

## States

- **Dashboard**
- **Orders**
- **View order**
- **Downloads**
- **Addresses**
- **Edit address**
- **Edit account**
- **Payment methods**
- **Add payment method**
- **Login**
- **Lost password**
- **Lost password (Confirmation)**
- **Reset password**
- **Order withdrawal** (requires WooCommerce 11.1 or later with Order Withdrawal enabled)

<div className="screenshot screenshot--control-panel">

![Account Page v2 State controls, including Order withdrawal and the Add missing states button.](https://academy.bricksbuilder.io/assets/account-page-v2-states-with-missing-state.webp)

</div>

## Generated structures

Each state can generate a complete starter block for that endpoint from **Insert a structure**.

Generated structures are appended to the current state content and do not overwrite existing content.

> **Note**
>
> Account Page v2 uses support elements for generated account forms and account orders pagination. Account orders, downloads, addresses, and order actions use v2 query loops and dynamic tags inside the matching account state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/account-v2-view-orders-structure-example.png)

## Add missing states

If an expected state element is missing, select **Account - Page v2** and click **Add missing states**. Bricks checks all currently available account states and appends any missing state elements without replacing existing states or their content. This can restore an unexpectedly missing state or add a state introduced after the page was built.

The button appears only when states are missing and your builder permissions allow adding elements. States that depend on a disabled WooCommerce feature are excluded. For an Account Page v2 inside a component, edit the component definition to repair its states.

Added states start empty. Select each added state and use **Insert a structure** to generate its starter content. This tool does not restore deleted custom layouts or refill existing empty states; generate content inside an empty state separately.

## Order withdrawal

This public state requires WooCommerce 11.1 or later with **Order Withdrawal** enabled under **WooCommerce > Settings > Advanced > Features**. It lets guests and logged-in customers enter, review, and confirm a withdrawal request.

Select **Order withdrawal (State)** and generate **Complete order withdrawal block** under **Insert a structure**. If the state is missing, use **Add missing states** first. The generated block includes **Your details**, **Review**, and **Confirmation** sections. All three appear together with sample data in the builder; their **Order withdrawal screen** conditions select the matching section on the frontend.

Keep the generated **Account order withdrawal form** wrappers, submit buttons, and screen conditions when customizing the layout. WooCommerce handles validation and submission. Use the [withdrawal dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#order-withdrawal-tags) to display submitted details. A missing or empty withdrawal state falls back to WooCommerce's native form.

Add a visible link using `{woo_url:order-withdrawal}` so customers can find the endpoint; WooCommerce does not add one automatically. A withdrawal request does not cancel an order or issue a refund.

## Field maintenance

The Edit address state can audit and sync generated account address fields against the current WooCommerce account address field registry.

Use the field maintenance actions after plugins or WooCommerce settings change account address fields:

- **Check address fields**
- **Generate missing fields**
- **Remove invalid fields**
- **Remove duplicate fields**

The Edit address state uses one set of address fields for billing and shipping, so the elements are named without a prefix, for example **Address: Company name**. **Check address fields** compares them with the billing and shipping address fields WooCommerce currently uses. The other buttons appear once the check has found something to fix.

**Generate missing fields** adds the new elements at the top of the Edit address state, outside the edit address form. Drag each one into the **Address field wrapper**, for example below **Address: Last name**, so it renders inside the form.

In Bricks 2.4.3, a field removed with **Remove invalid fields** can stay in the builder canvas until you reload the builder. For the Phone field, the canvas keeps showing "Field not available for the current address." The Structure panel is already correct, and the field is gone from the page once you save.

See [Checkout v2 field maintenance](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#field-maintenance) for the same workflow on the checkout.

![](https://academy.bricksbuilder.io/assets/account-v2-sync-address-fields.png)

## Query loops and dynamic data

Account Page v2 supports WooCommerce v2 query loops for account orders, order actions, account downloads, and account addresses.

Use account and order tags such as `{woo_account_address_title}`, `{woo_account_address}`, `{woo_order_number}`, `{woo_order_view_url}`, `{woo_order_download_name}`, and `{woo_order_action_url}` in the matching state or query loop.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#account-tags) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Account Page v2 structure.
- Review each state after setup so logged-in, logged-out, password reset, payment method, and order views all match your store design.
- Floating labels are available for the account forms in the Edit address, Edit account, Login, Lost password, Reset password, and Order withdrawal states. The Edit account and Edit address forms generated by the Woo Setup Wizard have them turned on.
- WooCommerce form buttons, such as **Save changes**, **Log in**, and **Register**, do not pick up your theme's button styles. Style them in the element settings or with a global class.
- Use the classic [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/) workflow if you prefer separate endpoint templates.

---

# Account - Payment methods

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-payment-methods/

*Displays saved payment methods inside My Account.*

Displays saved payment methods inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Head** (separator)
- **Body** (separator)
- **Delete button** (separator)
- **Make default button** (separator)
- **Add payment method** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - View order

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-view-order/

*Displays order details for a selected order in My Account.*

Displays order details for a selected order in My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Preview order ID** (number)
- **Hide** (checkbox)
- **Typography** (typography)
- **Mark** (separator)
- **Padding** (spacing)
- **Background color** (color)
- **Title** (separator)
- **Meta** (separator)
- **Description** (separator)
- **Table** (separator)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# WooCommerce Breadcrumbs

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/breadcrumbs/

*Display WooCommerce breadcrumb navigation in Bricks and customize the home link, prefixes, suffixes, separators, and spacing.*

Displays WooCommerce breadcrumb navigation.

## Settings

- **Before** (text) - Text to display before breadcrumbs.

- **Home: URL** (text) - Custom URL for home link. Default: home URL.

- **Home: Label** (text) - Label for home link. Default: "Home".

- **Home: Icon** (icon) - Icon for home link.

- **Home: Gap** (number with units) - Gap between home icon and label.

- **Home: Icon Size** (number) - Size of home icon.

- **Hide label** (checkbox) - Hide home label when icon is present. Only available when Home: Icon is set.

- **Prefix** (text) - Text to display before each breadcrumb item.

- **Suffix** (text) - Text to display after each breadcrumb item.

### Separator

- **Type** (select) - Separator type. Options: Text, Icon. Default: Text.

- **Separator** (text) - Separator text. Default: "/". Only available when Type is not Icon.

- **Icon** (icon) - Separator icon. Only available when Type is Icon.

- **Icon typography** (typography) - Typography for separator icon. Only available when Icon is set. Excludes: font-family, font-weight, font-style, text-align, text-decoration, text-transform, line-height, letter-spacing.

- **Gap** (number with units) - Gap between breadcrumb items.

- **Margin** (spacing) - Margin around separators.

---

# Cart totals

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-collaterals/

*Displays cart totals and related collateral content from the Cart page.*

Displays cart totals and related collateral content from the Cart page.

## Where this element works

Cart page templates.

## Key settings

- **Disable cross sells** (checkbox)
- **Hide title** (checkbox)
- **Title** (typography)
- **Subtotal** (typography)
- **Total** (typography)
- **Table** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Border** (border)
- **Button** (separator)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart coupon

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-coupon/

*Displays the coupon input section for the Cart page.*

Displays the coupon input section for the Cart page.

## Where this element works

Cart page templates.

## Key settings

- **General** (separator)
- **Update cart via AJAX** (checkbox)
- **Direction** (direction)
- **Input** (separator)
- **Placeholder** (text)
- **Width** (number)
- **Background color** (color)
- **Border** (border)
- **Placeholder typography** (typography)
- **Button** (text)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart items

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-items/

*Displays the cart items table with product rows and quantity controls.*

Displays the cart items table with product rows and quantity controls.

## Where this element works

Cart page templates.

## Key settings

- **Disable link** (checkbox)
- **Header** (separator)
- **Hide** (checkbox)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)
- **Body** (separator)
- **Image** (separator)
- **Disable** (checkbox)
- **Width** (number)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/

*Displays the WooCommerce cart page as editable Filled cart and Empty cart states.*

Displays the WooCommerce cart page as editable Filled cart and Empty cart states.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

Cart page. The element only appears in the Elements panel while you edit the page that WooCommerce uses as its cart page.

## Key settings

- **State** (radio) - Switches the builder preview between Filled cart and Empty cart.

## States

- **Filled cart** - Used when the cart contains products.
- **Empty cart** - Used when the cart has no products.

The generated Cart v2 structure keeps both states as internal child elements, so you can edit each state from the Structure panel. The top of the Structure panel shows the state you are editing. Click **Switch** there to change the previewed state.

![](https://academy.bricksbuilder.io/assets/cart-v2-states.png)

## Generated structures

Each state can generate starter content from **Insert a structure**:

- **Complete cart block**
- **Complete empty cart block**

Generated structures are appended to the current state content and do not overwrite existing content.

For a step-by-step setup, see [Cart v2 workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/#cart-v2-workflow).

The complete cart block contains a cart loop with one row per product (image, title, price, excerpt, item data, Cart quantity and a remove icon), a cross-sells section, a free shipping progress bar, summary rows for subtotal, coupons, fees, taxes, shipping and total, a checkout button and the Cart coupon element.

> **Note**
>
> In Bricks 2.4.3 the complete cart block includes a WooCommerce Notice element, but generating it from **Insert a structure** does not enable that element. Enable **Bricks > Settings > WooCommerce > Enable Bricks WooCommerce "Notice" element** first, or the canvas shows that the element doesn't exist. The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) enables it for you.

![](https://academy.bricksbuilder.io/assets/cart-v2-state-insert-structure.png)

> **Note**
>
> Cart v2 uses the Cart form and Cart quantity support elements inside the Filled cart state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/cart-v2-filled-cart-structure-example.png)

## Builder preview and frontend behavior

While you edit the Filled cart state, the builder previews a sample cart with sample notices. Loops without data, such as coupons or fees, show their dynamic tags on the canvas. Check the real values on the frontend.

On the frontend, the Cart quantity element updates the cart via AJAX (a quantity of zero removes the product), the Cart coupon element applies coupons via AJAX, and each applied coupon gets its own summary row with a remove icon.

The **Coupon total row** below the applied coupons shows the total of all coupons. If your store only allows one coupon at a time, it repeats the coupon amount, so you can delete it.

> **Note**
>
> In Bricks 2.4.3, lazy-loaded images in the Empty cart state stay blank when the last product is removed on the frontend, until the page is reloaded. If your empty state contains images, such as a Products element, disable lazy loading under **Bricks > Settings > Performance**.

## Query loops and dynamic data

Use the **Cart contents** query loop for custom cart item rows. Cart v2 layouts can also use cart total tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Cart v2 structure.
- Design both states so the cart page is complete whether the customer has products in the cart or not.
- Use the classic [Cart template workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/) if you prefer separate Cart and Empty Cart templates.

---

# Checkout coupon

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-coupon/

*Displays the coupon prompt and form on the Checkout page.*

Displays the coupon prompt and form on the Checkout page.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Location** (select)
- **Toggleable form** (checkbox)
- **Text** (text)
- **Justify content** (justify-content)
- **Gap** (number)
- **Button** (separator)
- **Disable text** (checkbox)
- **Icon** (icon)
- **Icon typography** (typography)
- **Icon expanded** (icon, since 2.5) - Alternate icon while the toggleable form is open.
- **Icon expanded typography** (typography, since 2.5) - Styling for the expanded icon.
- **Transition (ms)** (number, since 2.5) - Opening and closing duration when **Toggleable form** is enabled. Set `0` for an immediate change.
- **Disable coupon message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout customer details

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-customer-details/

*Displays billing and shipping customer detail fields on Checkout.*

Displays billing and shipping customer detail fields on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Remove billing fields** (select)
- **Remove shipping fields** (select)
- **Title** (separator)
- **Hide** (checkbox)
- **Typography** (typography)
- **Labels** (separator)
- **Margin** (spacing)
- **Fields** (separator)
- **Placeholder typography** (typography)
- **Hide additional information** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout login

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-login/

*Displays the returning customer login prompt on Checkout.*

Displays the returning customer login prompt on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Location** (select)
- **Toggleable form** (checkbox)
- **Text** (text)
- **Justify content** (justify-content)
- **Gap** (number)
- **Button** (separator)
- **Disable text** (checkbox)
- **Icon** (icon)
- **Icon typography** (typography)
- **Icon expanded** (icon, since 2.5) - Alternate icon while the toggleable form is open.
- **Icon expanded typography** (typography, since 2.5) - Styling for the expanded icon.
- **Transition (ms)** (number, since 2.5) - Opening and closing duration when **Toggleable form** is enabled. Set `0` for an immediate change.
- **Disable login message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order payment

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-payment/

*Displays available payment methods and payment actions on Checkout.*

Displays available payment methods and payment actions on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Label typography** (typography)
- **Description** (separator)
- **Typography** (typography)
- **Privacy** (separator)
- **Button** (separator)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order review

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-review/

*Displays the order review section on Checkout.*

Displays the order review section on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Hide title** (checkbox)
- **Title** (text)
- **Title typography** (typography)
- **Subtitles typography** (typography)
- **Items** (separator)
- **Typography** (typography)
- **Padding** (spacing)
- **Border** (border)
- **Margin** (spacing)
- **Background** (color)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.
