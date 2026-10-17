# Filter: bricks/allowed_html_tags

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-allowed_html_tags/

*Starting at version 1.10.2 Bricks restricts the allowed HTML tags to the WordPress core logic for wpksesallowedhtml( 'post' ).*

Starting at version `1.10.2` Bricks restricts the allowed HTML tags to the WordPress core logic for `wp_kses_allowed_html( 'post' )`.

This results in the following HTML tags being allowed out-of-the-box:

address, a, abbr, acronym, area, article, aside, audio, b, bdo, big, blockquote, br, button, caption, cite, code, col, colgroup, del, dd, dfn, details, div, dl, dt, em, fieldset, figure, figcaption, font, footer, h1, h2, h3, h4, h5, h6, header, hgroup, hr, i, img, ins, kbd, label, legend, li, main, map, mark, menu, nav, object, p, pre, q, rb, rp, rt, rtc, ruby, s, samp, span, section, small, strike, strong, sub, summary, sup, table, tbody, td, textarea, tfoot, th, thead, title, tr, track, tt, u, ul, ol, var, video

For example, setting the "Custom tag" on a "Block" element to `form` is not allowed by default, and will throw the following error in the builder:

![](https://academy.bricksbuilder.io/assets/bricks-1.10.3-filter-bricks-allowed-html-tags.png)

Using the new filter as shown in the code snippet below, the `form` tag is added to the list of allowed HTML tags and can be used without throwing any errors.

```php

add_filter( 'bricks/allowed_html_tags', function( $allowed_html_tags ) {
    // Define the additional tags to be added (e.g. 'form' & 'select')
    $additional_tags = ['form', 'select'];

    // Merge additional tags with the existing allowed tags
    return array_merge( $allowed_html_tags, $additional_tags );
} );
```

> **Note**
>
> **Only allow HTML tags that are considered safe, as anyone with builder access can use them!**

---

# Filter: bricks/assets/generate_css_from_element

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-assets-generate_css_from_element/

*Add custom element names to Bricks CSS generation so looped child styles are included for supported custom elements.*

This filter allows you to include your custom query loop supported element to generate the children styles in Bricks. (@since 1.9.2)

## Parameters

- `$element_names` (array): Additional loop-capable element names. Defaults to an empty array.
- `$current_element` (array): The element currently being processed for CSS generation.
- `$css_type` (string): The CSS generation area, such as `header`, `footer`, or `content`.

```php
add_filter( 'bricks/assets/generate_css_from_element', function( $element_names, $current_element, $css_type ) {
  // $css_type is a string (e.g. header, footer, content, etc.)
  // Add your custom element name so the looping children styles are generated.
  if ( ! in_array( 'my-custom-element-name', $element_names ) ) {
    $element_names[] = 'my-custom-element-name';
  }

  return $element_names;
}, 10, 3 );
```

---

# Filter: bricks//assets/load_webfonts

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-assets-load_webfonts/

*Bricks 1.4 introduces the possibility to \"Disable Google Fonts\". Either via the Bricks settings under \"Performance\" or programmatically using the filter as.*

Bricks 1.4 introduces the possibility to "Disable Google Fonts". Either via the Bricks settings under "Performance" or programmatically using the filter as explained below:

![](https://academy.bricksbuilder.io/assets/bricks-1.4-disable-google-fonts-setting-1024x944.png)

<figcaption>

Bricks > Settings > Performance: Disable Google Fonts

</figcaption>

With the filter `bricks/assets/load_webfonts` you'll be able to prevent Google Fonts to load in the frontend by returning `false`:

```php
// Prevent Google Fonts loading
add_filter( 'bricks/assets/load_webfonts', '__return_false' );
```

If you use this filter to remove the embed of Google Fonts but you still like to use Google Fonts, just head to the [Google Fonts website](https://fonts.google.com/) and download the fonts you need. Then, add them manually to your website, using the [Custom Fonts](https://academy.bricksbuilder.io/builder/styling/custom-fonts/) screen.

---

# Filter: bricks/auth/custom_login_redirect

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_login_redirect/

*This filter allows customization of the redirect page ID for the login page.*

This filter allows customization of the redirect page ID for the login page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_login_redirect', function( $selected_login_page_id ) {
    return /* New login page ID */;
});
```

**Parameters:**

- `$selected_login_page_id` (int|false): The ID of the custom login page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for login redirection, or `false` if no custom page is designated.

---

# Filter: bricks/auth/custom_lost_password_redirect

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_lost_password_redirect/

*This filter enables the modification of the redirect page ID for the lost password page.*

This filter enables the modification of the redirect page ID for the lost password page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_lost_password_redirect', function( $selected_lost_password_page_id ) {
    return /* New lost password page ID */;
});
```

**Parameters:**

- `$selected_lost_password_page_id` (int|false): The ID of the custom lost password page if set, otherwise `false`.

**Return:**

- (int|false): The new custom lost password page ID or `false` to indicate no custom page is set.

---

# Filter: bricks/auth/custom_redirect_url

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_redirect_url/

*This filter is distinct from other authentication-related filters in that it provides a broad scope for customizing redirections during authentication.*

This filter is distinct from other authentication-related filters in that it provides a broad scope for customizing redirections during authentication processes. Unlike specific filters for [login](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_login_redirect/), [registration](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_registration_redirect/), [lost password](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_lost_password_redirect/), or [reset password pages](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_reset_password_redirect/), this filter applies to any authentication-related URL.

**Functionality:**

This filter allows overriding the default redirect URL based on custom conditions across various authentication scenarios. It offers flexibility to redirect users to different pages depending on the context or specific requirements of the authentication process.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_redirect_url', function( $custom_redirect_url, $current_url_path ) {
    if ( /* custom condition based on $current_url_path */ ) {
        return 'https://example.com/custom-redirect';
    }
    return $custom_redirect_url;
}, 10, 2 );
```

In this example, the redirection URL changes based on the current URL path, allowing for a dynamic and contextual redirection strategy.

**Parameters:**

- `$custom_redirect_url` (string|null): The initial redirect URL.
- `$current_url_path` (string): The current URL path being accessed.

**Return:**

- (string|null): The URL to redirect to, or null to follow default logic.

---

# Filter: bricks/auth/custom_registration_redirect

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_registration_redirect/

*This filter allows for the customization of the redirect page ID for the registration page.*

This filter allows for the customization of the redirect page ID for the registration page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_registration_redirect', function( $selected_registration_page_id ) {
    return /* New registration page ID */;
});
```

**Parameters:**

- `$selected_registration_page_id` (int|false): The ID of the custom registration page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for registration redirection, or `false` if no custom page is set.

---

# Filter: bricks/auth/custom_reset_password_redirect

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_reset_password_redirect/

*This filter provides a way to change the redirect page ID for the reset password page.*

This filter provides a way to change the redirect page ID for the reset password page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_reset_password_redirect', function( $selected_reset_password_page_id ) {
    return /* New reset password page ID */;
});
```

**Parameters:**

- `$selected_reset_password_page_id` (int|false): The ID of the custom reset password page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for reset password redirection, or `false` if no custom page is specified.

---

# Filter: bricks/body/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-body-attributes/

*Filter the HTML attributes Bricks adds to the body tag on the frontend.*

Filter to add HTML attributes to the `body` tag (@since 1.5).

```php
add_filter( 'bricks/body/attributes', function( $attributes ) {
  // Add 'data-is-body' HTML attribute to footer with value 'y'
  $attributes['data-is-body'] = 'y';

  return $attributes;
} );
```

---

# Filter: bricks/builder/elements

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-builder-elements/

*Determine which elements to use in Bricks by out-commenting the ones you don't want to use. There is a full example and list of all elements in the Bricks child.*

Determine which elements to use in Bricks by out-commenting the ones you don't want to use. There is a full example and list of all elements in the Bricks child theme that you can customize to your requirements.

```php
add_filter( 'bricks/builder/elements', function( $elements ) {
  // See Bricks child theme for a full list of all available elements
  // var_dump( $elements ); // To see all available elements

  return $elements;
} );
```

---

# Filter: bricks/builder/codemirror_config

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-builder-codemirror_config/

*Use this filter to customize the configuration of CodeMirror 5, the code editor used within the builder. CodeMirror 5 is used in areas such as the Custom CSS.*

Use this filter to customize the configuration of CodeMirror 5, the code editor used within the builder. CodeMirror 5 is used in areas such as the **Custom CSS** setting for elements and the **Code element** settings, where it provides an interface for editing HTML, CSS, JavaScript, PHP, and more.

You can refer to the [CodeMirror 5 configuration documentation](https://codemirror.net/5/doc/manual.html#config) for more details on available options.

## Example Usage:

```php
add_filter( 'bricks/builder/codemirror_config', function( $config ) {
    // Disable auto-close brackets
    $config['autoCloseBrackets'] = false;

    // Disable line numbers
    $config['lineNumbers'] = false;

    // Override default tab size
    $config['tabSize'] = 4;

    return $config;
});
```

In this example, the filter modifies the default CodeMirror configuration to:

- Disable **auto-close brackets**.
- Disable **line numbers**.
- Set the **tab size** to 4 spaces.

**Parameters:**

- `$config` *(array)*: An empty array by default. Define only the specific configurations you need, which will override the builder's default settings.

**Return:**

- *(array)*: The custom configuration array, applied alongside or in place of Bricks' defaults.

---

# Filter: bricks/builder/map_styles

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-builder-mapstyles/

*Filter the custom map styles available to the Bricks Map element in the builder.*

This filter allows you to define your own custom map styles for the **Map** element.

The example below shows how we added a custom map style from
[https://snazzymaps.com/style/38/shades-of-grey](https://snazzymaps.com/style/38/shades-of-grey) to the builder.

The best resource for professional predefined map styles is available under
[https://snazzymaps.com/explore](https://snazzymaps.com/explore). Open any map style and copy&paste the code under "JAVASCRIPT STYLE ARRAY" as shown in the example below.

```php
add_filter( 'bricks/builder/map_styles', function( $map_styles ) {
  // Example: Custom map style from: https://snazzymaps.com/style/38/shades-of-grey
  $map_styles['shadesOfGrey'] = [
    'label' => esc_html__( 'Shades of grey', 'bricks' ),
    'style' => '[ { "featureType": "all", "elementType": "labels.text.fill", "stylers": [ { "saturation": 36 }, { "color": "#000000" }, { "lightness": 40 } ] }, { "featureType": "all", "elementType": "labels.text.stroke", "stylers": [ { "visibility": "on" }, { "color": "#000000" }, { "lightness": 16 } ] }, { "featureType": "all", "elementType": "labels.icon", "stylers": [ { "visibility": "off" } ] }, { "featureType": "administrative", "elementType": "geometry.fill", "stylers": [ { "color": "#000000" }, { "lightness": 20 } ] }, { "featureType": "administrative", "elementType": "geometry.stroke", "stylers": [ { "color": "#000000" }, { "lightness": 17 }, { "weight": 1.2 } ] }, { "featureType": "landscape", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 20 } ] }, { "featureType": "poi", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 21 } ] }, { "featureType": "road.highway", "elementType": "geometry.fill", "stylers": [ { "color": "#000000" }, { "lightness": 17 } ] }, { "featureType": "road.highway", "elementType": "geometry.stroke", "stylers": [ { "color": "#000000" }, { "lightness": 29 }, { "weight": 0.2 } ] }, { "featureType": "road.arterial", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 18 } ] }, { "featureType": "road.local", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 16 } ] }, { "featureType": "transit", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 19 } ] }, { "featureType": "water", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 17 } ] } ]'
];

  return $map_styles;
} );
```

---

# Filter: bricks/code/allow_execution

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-allow_execution/

*An alternative to the Disable code execution setting under Bricks > Settings > Builder Access. You can use this PHP filter to disable/enable code execution.*

An alternative to the **Disable code execution** setting under `Bricks > Settings > Builder Access`. You can use this PHP filter to disable/enable code execution programmatically.

![](https://academy.bricksbuilder.io/assets/disallow-code-execution-hook.png)

```php
add_filter( 'bricks/code/allow_execution', function( $allow ) {
  // Only allows to return false to disable code execution programmatically
  return false;
} );
```

---

# Filter: bricks/builder/image_size_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-builder-image_size_options/

*The bricks/builder/imagesizes hook gives developers the ability to customize image size options in the builder.*

The `bricks/builder/image_sizes` hook gives developers the ability to customize image size options in the builder.

By default, when working within a query loop and using dynamic data for image sources, Bricks Builder displays all the registered WordPress image sizes.

This hook allows you to modify this list if you know that certain sizes are not being used, helping you streamline your image size options to fit your needs.

```php
/**
 * $image_sizes Multidimensional array (key: image size name)
 */
add_filter( 'bricks/builder/image_size_options', function( $image_sizes ) {
  // Unset thumbnail, 1536x1536, 2048x2048
  unset( $image_sizes['thumbnail'] );
  unset( $image_sizes['1536x1536'] );
  unset( $image_sizes['2048x2048'] );

  return $image_sizes;
});
```

---

# Filter: bricks/code/disable_execution

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-disable_execution/

*This PHP filter allows you to disable code execution within the Bricks builder programmatically.*

This PHP filter allows you to disable code execution within the Bricks builder programmatically.

It takes precedence over the [`bricks/code/allow_execution`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-allow_execution/) filter and any settings configured in `Bricks > Settings > Custom code > Code execution`.

```php
add_filter( 'bricks/code/disable_execution', function( $disable ) {
  // Returning true disables code execution programmatically
  return true;
} );
```

Use this filter to enforce stricter security by disabling code execution, regardless of other configurations on your site.

---

# Filter: bricks/code/disallow_keywords

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-disallow_keywords/

*This filter introduces another level of security when using the Code element to run code.*

This filter introduces another level of security when using the Code element to run code.

With the filter `bricks/code/disallow_keywords` you'll be able to prevent the code execution if specific keywords are found in the code, thus reducing the risk of using this element. To add keywords to this check, use the following example:

```php
add_filter( 'bricks/code/disallow_keywords', function( $keywords ) {
  $</meta>keywords[] = 'wpdb';

  return $</meta>keywords;
} );
```

---

# Filter: bricks/code/echo_function_names

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-echo_function_names/

*Starting at Bricks 1.9.7, you must explicitly allow any function names you want to call via Bricks' dynamic data echo tag using the new.*

> **Note**
>
> Starting at Bricks 1.9.7, you must explicitly allow any function names you want to call via Bricks' dynamic data echo tag using the new bricks/code/echo_function_names filter. You can add this to your Bricks child theme or the code snippet plugin of your choice.

```php
add_filter( 'bricks/code/echo_function_names', function() {
  return [
    'my_custom_function',
    'another_custom_function',
  ];
} );
```

To use echo functions, you must first enable “Code execution” for the appropriate user role or user in your WordPress dashboard under “Bricks – Settings – Custom code” (see the screenshot below).

![](https://academy.bricksbuilder.io/assets/bricks-builder-code-execution-1024x803.png)

<figcaption>

Code Execution: Enabled for user role "Administrator"

</figcaption>

Make sure to only enable code execution for users & user roles you trust 100%.

You can get a list of all functions on your site called through the `echo` tag as part of the "Code review" results. Here's how:

1. Go to `Bricks > Settings > Custom code`
2. Click the "Start: Code review" button
3. Once finished, select "Echo tags" from the dropdown.
4. Copy the code snippet under "Echo: Function names" and paste it into the `functions.php` file of your Bricks child name. Make sure to remove any unknown or unwanted function names from the array.

![](https://academy.bricksbuilder.io/assets/bricks-code-review-echo-function-names.png)

## Using patterns (regex) to simplify echo function calls {#patterns}

Bricks 1.9.8 offers greater flexibility when it comes to echo function calls.

While you can still return an array with the exact function names, you can also return an array that contains specific regex checks. We identify those regex calls by the `@` prefix.

If your function name matches any of those regex checks, it can be called through the `echo` tag.

**Example: Allow calling any functions that start with `brx_`:**

```php
add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return [
    '@^brx_', // Allow all functions that start with "brx_"
  ];
} );
```

## Check function names against your own custom logic

Instead of returning an array, you can also perform any custom check against the function name itself or any other logic you want to run. The filter receives the function name (`$function_name`) as an argument to assist in making more dynamic decisions. Returning a boolean (`true` or `false`)

**Example: Allow function execution based on function name prefix**

```php
add_filter('bricks/code/echo_function_names', function($function_name) {
  // Only allow functions that start with "custom_"
  return strpos($function_name, 'custom_') === 0;
});
```

This example uses a straightforward check to determine if the function starts with `custom_`. If so, it returns `true`, allowing the function to be executed; otherwise, it returns `false`.

**Example: Run any function when development mode is enabled**

```php
add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return defined( 'WP_DEVELOPMENT_MODE' ) ? WP_DEVELOPMENT_MODE : false;
} );
```

The [`WP_DEVELOPMENT_MODE`](https://make.wordpress.org/core/2023/07/14/configuring-development-mode-in-6-3/) PHP constant has been available in WordPress core since version 6.3. We use it just as an example. You can use any custom PHP constant of your choice by defining it in your child theme's functions.php file.

**Example: Run function if the current user can edit posts**

```php
add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return current_user_can( 'edit_posts' );
} );
```

---

# Filter: bricks/comments/timestamp

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-comments-timestamp/

*When using the Bricks Post Comments element, the comment default timestamp text will show the time difference since it was published in a human-readable format.*

When using the Bricks Post Comments element, the comment default timestamp text will show the time difference since it was published in a human-readable format such as "1 hour ago" or "2 days ago".

Since Bricks 1.5.1, you'll be able to customize the comment timestamp text, like so:

```php
add_filter( 'bricks/comments/timestamp', function( $timestamp, $comment ) {
  // Return the WordPress default comment timestamp
  return sprintf( __( '%1$s at %2$s' ),
    get_comment_date( '', $comment ),
    get_comment_time()
  );
}, 10, 2 );
```

---

# Filter: bricks/content/html_after_begin

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-html_after_begin/

*Available since version 1.6, this filter allows you to customize or insert HTML strings after main tag, before rendering bricks data.*

Available since version 1.6, this filter allows you to customize or insert HTML strings after `main` tag, before rendering bricks data.

```php
add_filter( 'bricks/content/html_after_begin', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }

    // Insert custom div after the main tag
    $my_additional_html = '<div class="my_notification">This is my notification</div>';

    return $html_after_begin . $my_additional_html;
}, 10, 4 );
```

---

# Filter: bricks/content/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes/

*Programmatically add HTML attributes to the main tag.*

Programmatically add HTML attributes to the `main` tag.

```php
add_filter( 'bricks/content/attributes', function( $attributes ) {
  // Add 'data-is-content' HTML attribute to main with value 'y'
  $attributes['data-is-content'] = 'y';
  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/)
- [/developer/hooks/filters/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/)

---

# Filter: bricks/content/html_before_end

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-html_before_end/

*Available since version 1.6, this filter allows you to customize or insert HTML strings before closing main tag.*

Available since version 1.6, this filter allows you to customize or insert HTML strings before closing `main` tag.

```php
add_filter( 'bricks/content/html_before_end', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }

    // Insert custom popup HTML
    $my_popup_html = '<div class="my_popup">This is my popup</div>';

    return $html_after_begin . $my_popup_html;
}, 10, 4 );
```

---

# Filter: bricks/default_page_title

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-default_page_title/

*Since 1.8, Bricks automatically adds default page titles to all non-Bricks pages. However, if you wish to customize or remove this default page title, you can.*

Since 1.8, Bricks automatically adds default page titles to all non-Bricks pages. However, if you wish to customize or remove this default page title, you can utilize this filter.

Returning an empty string, disables the default page title.

```php
add_filter( 'bricks/default_page_title', function( $title, $post_id ) {
  // If slug of current page is 'my-page': Return empty page title
  if ( is_page( 'my-page' ) ) {
    $title = '';
  }

  return $title;
}, 10, 2 );
```

---

# Filter: bricks/content/tag

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-tag/

*Filter which HTML tag Bricks uses for the #brx-content wrapper around rendered page content.*

The `bricks/content/tag` (@since 1.11.1) filter lets you set the HTML tag for the `#brx-content` node that your Bricks content data is wrapped in.

Make sure the HTML tag you return is an [allowed HTML tag](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-allowed_html_tags/).

## Example Usage:

```php
add_filter( 'bricks/content/tag', function( $tag ) {
    // Set #brx-content tag to 'div' (default: main)
    return 'div';
} );
```

**Parameters:**

- `$tag` (string): The default HTML tag, which is `main`.

**Return:**

- (string): The HTML tag you want to render instead of the default.

---

# Filter: bricks/dynamic_data/exclude_tags

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-exclude_tags/

*Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins which cause a specific tag.*

Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins which cause a specific tag to be removed by the content.

Since Bricks 1.3.5 it is possible to exclude a list of tags from the Bricks dynamic data logic using the following PHP snippet in your `functions.php` file:

```php
add_filter( 'bricks/dynamic_data/exclude_tags', function( $tags ) {
    return [
        'my_specific_tag',
        'my_other_specific_tag'
    ];
});
```

Adding this code to your child theme will prevent Bricks from replacing these tags with an empty string.

---

# Filter: bricks/dynamic_data/post_terms_links

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-post_terms_links/

*When rendering the terms assigned to a post using the dynamic data tag {posttermsmytaxonomy}, Bricks wraps each term with a link to the term archive page. To.*

When rendering the terms assigned to a post using the dynamic data tag `{post_terms_my_taxonomy}`, Bricks wraps each term with a link to the term archive page. To disable this default behavior, you may hook into the `bricks/dynamic_data/post_terms_links` filter, like so:

```php
// Disable links for all the {post_terms_my_taxonomy} tags
add_filter( 'bricks/dynamic_data/post_terms_links', '__return_false' );
```

or, for a specific taxonomy:

```php
add_filter( 'bricks/dynamic_data/post_terms_links', function( $has_links, $post, $taxonomy) {
  // Disable links for my_custom_tax taxonomy
  return $taxonomy !== 'my_custom_tax';
}, 10, 3);
```

---

# Filter: bricks/dynamic_data/post_terms_separator

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-post_terms_separator/

*Programmatically set the post term separator like so:*

Programmatically set the post term separator like so:

```php
add_filter( 'bricks/dynamic_data/post_terms_separator', function( $sep, $post, $taxonomy ) {
  return ' : ';
}, 10, 3 );
```

---

# Filter: bricks/dynamic_data/read_more

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-read_more/

*If you use the dynamic data tag {readmore} you'll get an anchor tag (link) to the post with the label \"Read more\" by default. To change this label use the.*

If you use the dynamic data tag `{read_more}` you'll get an anchor tag (link) to the post with the label "Read more" by default. To change this label use the following code:

```php
add_filter( 'bricks/dynamic_data/read_more', function( $label, $post ) {
   return 'My New Label';
}, 10, 2 );
```

Read more about [Dynamic Data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/) in the Bricks academy.

---

# Filter: bricks/dynamic_data/replace_nonexistent_tags

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-replace_nonexistent_tags/

*Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins (e.g. Fluent Forms) or.*

Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins (e.g. Fluent Forms) or with the content itself (e.g. mathematical equations).

From Bricks 1.4 onwards, the default Bricks logic is to keep the nonexistent tags (they won't be replaced by an empty string anymore). It is possible to switch off the default Bricks behavior and tell Bricks to replace the nonexistent dynamic data tags with an empty string.

To replace nonexistent tags add the following PHP snippet to your `functions.php` file:

```php
add_filter( 'bricks/dynamic_data/replace_nonexistent_tags', '__return_true', 10, 1 );
```

> **Note**
>
> Note: Bricks 1.3.5 introduced the possibility to toggle this behavior, but by default Bricks was replacing the tags. Bricks 1.4 changed the default action.

---

# Filter: bricks/element/render

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-render/

*Bricks 1.5 introduces the new bricks/element/render filter. This filter enables you to implement your own conditional display logic programmatically.*

Bricks 1.5 introduces the new `bricks/element/render` filter. This filter enables you to implement your own conditional display logic programmatically.

This is ideal for restricting premium content to certain users, etc.

If the condition inside this filter is not met (i.e. it returns `false`), then the element won't be rendered on the frontend.

```php
add_filter( 'bricks/element/render', function( $render, $element ) {
  // Conditional display logic goes here:
  // $render = true to render the element
  // $render = false to skip the element render

  return $render;
}, 10, 2 );
```

> **Note**
>
> Bricks introduced [Element Conditions](https://academy.bricksbuilder.io/builder/features/element-conditions/) in 1.5.4. Use this PHP filter for a more complicated scenario.

## Example 1: Output a specific element if the visitor is logged-in {#example-1}

![](https://academy.bricksbuilder.io/assets/Screenshot-2022-07-01-at-15.28.15.png)

<figcaption>

The 6-character element ID is the last part of the default HTML ID (after the dash).

</figcaption>

In the following example, we check if the element has a specific element ID, and if so, we allow the element to be rendered based on the logged-in/out condition.

```php
add_filter( 'bricks/element/render', function( $render, $element ) {
  // Render element ID "mlttpx" if user is logged in
  if ( $element->id === 'mlttpx' ) {
    return is_user_logged_in();
  }

  return $render;
}, 10, 2 );
```

## Example 2: Don't output elements with a specific custom CSS class for users with a subscriber role {#example-2}

The following example will render an element if it contains the custom CSS class `hide-for-subscribers`, if the user is logged in and is not a subscriber.

You may select different [users' capabilities](https://wordpress.org/support/article/roles-and-capabilities/) according to your needs.

```php
add_filter( 'bricks/element/render', function( $render, $element ) {
  // Get the element CSS classes
  $classes = ! empty( $element->attributes['_root']['class'] ) ? $element->attributes['_root']['class'] : false;

  // Check if the element has the special class "hide-for-subscribers"
  if ( $classes && in_array( 'hide-for-subscribers', $classes ) ) {
    return current_user_can( 'edit_posts' );
  }

  return $render;
}, 10, 2 );
```

## Example 3: Output elements for a specific post category {#example-3}

The following example will render a specific element based on the HTML ID on a single post page with a specific category:

```php
add_filter( 'bricks/element/render', function( $render, $element ) {
  // Check if this is a single post page
  if ( ! is_single() ) {
    return $render;
  }

  // Get the element custom HTML ID
  $html_id = isset( $element->settings['_cssId'] ) ? $element->settings['_cssId'] : false;

  // Check if the element has the HTML ID "project-award"
  if ( $html_id && $html_id === 'project-award' ) {
    return has_category( 'projects' );
  }

  return $render;
}, 10, 2 );
```

## Example 4: Output elements having a class of "logged-in" to logged-in users and elements having a class of "logged-out" to non logged-in visitors

The following example renders elements that have a class of `logged-in` only to users that are logged in and elements that have a class of `logged-out` only to users that are logged out:

```php
add_filter( 'bricks/element/render', function( $render, $element ) {
  // Get the element CSS classes
  $classes = ! empty( $element->attributes['_root']['class'] ) ? $element->attributes['_root']['class'] : false;

  // Check if the element has the special class "logged-in"
  if ( $classes && in_array( 'logged-in', $classes ) ) {
  return is_user_logged_in();
  }

  // Check if the element has the special class "logged-out"
  if ( $classes && in_array( 'logged-out', $classes ) ) {
  return ! is_user_logged_in();
  }

  return $render;
}, 10, 2 );
```

## Example 5: Output an element having a specific HTML ID based on value of a custom field

The following example renders an element that has the specified HTML ID based on the value of a specific custom field of the current post when viewing a singular page:

```php
// Render an element with "project-award" HTML ID if the specified condition is true.
// Condition: The value of a custom field "dont_output_project_award" is false.
add_filter( 'bricks/element/render', function( $render, $element ) {
  // Check if this is a singular page
  if ( ! is_singular() ) {
    return $render;
  }

  // Get the element custom HTML ID
  $html_id = isset( $element->settings['_cssId'] ) ? $element->settings['_cssId'] : false;

  // Check if the element has the HTML ID "project-award"
  if ( $html_id && $html_id === 'project-award' ) {
    return ! get_post_meta( $element->post_id, 'dont_output_project_award', true );
  }

  return $render;
}, 10, 2 );
```

The examples above are really just to illustrate a few simple use cases. Anything that you can check with PHP is possible to include in your own conditional display logic using this new `bricks/element/render` filter.

## Example 6: Output an element in ACF Repeater if the sub field is not empty

Scenario:

ACF Repeater: FAQs

Sub fields: Question, Answer, Button Text and Button URL

Requirement: When Query Loop's query type is set to this ACF Repeater, output a Button (a child element of the repeating element) only in the rows that have a value set for the Button Text sub field.

```php
// Output one or more instances of the specified element (inside a query loop of ACF Repeater type) when the condition is true.
// Condition: The specified sub field inside the specified ACF Repeater field is not empty.
add_filter( 'bricks/element/render', function( $render, $element ) {
  if ( $element->id === 'huciku' && class_exists( 'ACF' ) ) {
    if ( have_rows( 'faqs' ) ) {
      // Loop through rows.
      while( have_rows( 'faqs' ) ) : the_row();
        return get_sub_field( 'button_text' );
      // End loop.
      endwhile;
    }
  }

  return $render;
}, 10, 2 );
```

where `huciku` is the element ID of the Button.

Note: This will be applied as `brxe-huciku` class in the output in this case, not a ID.

Also, replace `faqs` and `button_text` strings as applicable.

---

# Filter: bricks/element/render_attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-render_attributes/

*Starting with Bricks 1.3.7 you may manipulate the HTML attributes of a given element using the following filter:*

Starting with Bricks 1.3.7 you may manipulate the HTML** **attributes of a given element using the following filter:

```php
add_filter( 'bricks/element/render_attributes', function( $attributes, $key, $element ) {
    if ( isset( $element->settings['my_setting'] )
       && $element->settings['my_setting'] == 'xpto' ) {
        $attributes[ $key ]['data-xpto'] = 'my data';
    }

    return $attributes;
}, 10, 3 );
```

The filter callback receives 3 arguments:

- `$attributes` - an associative array of the element attributes, grouped by the $key identifier
- `$key` - the HTML element identifier to render attributes for
- `$element` - the Bricks element object (since Bricks 1.5)

Since Bricks 1.4, if you need to get access to the `$is_frontend` value (whether the element is rendering in the frontend or in the builder), please use the global function `bricks_is_frontend()`.

Since Bricks 1.5, the `$settings` and `$name` arguments are deprecated. You may use the callback 3rd argument to get those: `$element->settings` and `$element->name`.

---

# Filter: bricks/element/settings

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-settings/

*Bricks 1.5 adds the possibility to change the element settings before it is rendered.*

Bricks 1.5 adds the possibility to change the element settings before it is rendered.

This allows you to change a text element content programmatically, or add styles based on a custom conditional logic, like so:

```php
add_filter( 'bricks/element/settings', function( $settings, $element ) {
    // Add "[online]" text to all the headings elements if the visitor is logged in
    if ( $element->name === 'heading' && is_user_logged_in() ) {
        $settings['text'] .= ' [online]';
    }

    return $settings;
}, 10, 2 );
```

In case you need to programmatically add an element conditional display logic, check the filter [`bricks/element/render`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-render/).

##### Example: Dynamically set WooCommerce Product Filter (Price) max price from all products

![](https://academy.bricksbuilder.io/assets/bricks-products-filter-max-price-from-all-products.png)

```php
add_filter('bricks/element/settings', function( $settings, $element ) {
  // Change the zyjhwa to your element ID
  if( $element->id !== 'zyjhwa' || ! isset( $settings['filters'] ) ) {
    return $settings;
  }

  // Get all products
  $products = wc_get_products(array(
    'status' => 'publish',
    'limit' => -1, // Retrieve all products
  ));

  $highest_price = max(array_map(function ($product) {
    return $product->get_price();
  }, $products));

  foreach( $settings['filters'] as $key => $filter ) {
    if( ! isset( $filter['otherFilter'] ) || $filter['otherFilter'] !== 'price' ) {
      continue;
    }

    $settings['filters'][$key]['sliderMax'] = $highest_price;
  }

  return $settings;
}, 10, 2);
```

---

# Filter: bricks/elements/{element_name}/control_groups

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-control_groups/

*Since Bricks 1.4 it is possible to add custom control groups to a specific element like so:*

Since Bricks 1.4 it is possible to add custom control groups to a specific element like so:

```php
add_filter( 'bricks/elements/heading/control_groups', function( $control_groups ) {
    $control_groups['custom_controls'] = [
        'tab'      => 'content', // or 'style'
        'title'    => esc_html__( 'Custom controls', 'my_plugin' ),
    ];

    return $control_groups;
} );
```

Note: the above example adds a new control group with the title "**Custom controls**" to the **heading** element, using the filter `bricks/elements/**heading**/control_groups`. To learn about other Bricks controls, visit the [Controls section](https://academy.bricksbuilder.io/developer/controls/).

---

# Filter: bricks/elements/&#123;element_name&#125;/controls

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-controls/

*Since Bricks 1.3.2 it is possible to add custom controls to any element like so:*

Since Bricks 1.3.2 it is possible to add custom controls to any element like so:

```php
add_filter( 'bricks/elements/posts/controls', function( $controls ) {
    $controls['ignoreStickyPosts'] = [
        'tab'      => 'content',
        'group'    => 'query',
        'label'    => esc_html__( 'Ignore Sticky Posts', 'my_plugin' ),
        'type'     => 'checkbox'
    ];

    return $controls;
} );
```

Note: the above example adds a new checkbox to the **posts** element, using the filter `bricks/elements/**posts**/controls`. To learn about other Bricks controls, visit the [Controls section](https://academy.bricksbuilder.io/developer/controls/).

You might also be interested in the filter [`bricks/posts/query_vars`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-query_vars/) to manipulate the posts element query.

---

# Filter: bricks/filter_element/populated_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-filter_element-populated_options/

*The bricks/filterelement/populatedoptions PHP filter allows you to modify the populated options of Filter - Select, Filter - Radio, and Filter - Checkbox.*

The` bricks/filter_element/populated_options` PHP filter allows you to modify the populated options of **Filter - Select**, **Filter - Radio**, and **Filter - Checkbox** elements **before** they are rendered into HTML. `(@since 2.0.2)`

This is useful if you want to:

- Add/remove certain options
- Reorder options (based on complicated custom requirement)
- Change display text or values

### Example:

The following example removes the "biography" option from a filter element with the ID `uzehuy`:

```php
/**
 * $options is an array of options that are populated by the element
 * 'value' is the value of the option
 * 'text' is the display text of the option
 * 'is_all' exists and is true if the option is the "All" option
 * 'is_placeholder' exist and is true if the option is a placeholder option
 */
add_filter( 'bricks/filter_element/populated_options', function( $options, $element ) {
  if ( $element->id === 'uzehuy' ) {
    // Remove the options that value is 'biography'
    $options = array_filter( $options, function( $option ) {
      return $option['value'] !== 'biography';
    } );
  }

  return $options;
}, 10, 2 );
```

---

# Filter: bricks/footer/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-footer-attributes/

*Programmatically add HTML attributes to the footer tag.*

Programmatically add HTML attributes to the `footer` tag.

```php
add_filter( 'bricks/footer/attributes', function( $attributes ) {
  // Add 'data-is-footer' HTML attribute to footer with value 'y'
  $attributes['data-is-footer'] = 'y';

  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/)
- [/developer/hooks/filters/filter-bricks-content-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes/)

---

# Filter: bricks/form/action/{form_action}

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-action-form_action/

*The bricks/form/action/{formaction} filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a form. It allows developers to.*

The `bricks/form/action/{form_action}` filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a form. It allows developers to define custom logic for handling such actions dynamically.

Bricks provides several reserved actions out of the box, including:

- **email**
- **redirect**
- **mailchimp**
- **sendgrid**
- **login**
- **registration**
- **lost-password**
- **reset-password**
- **custom**

If the user's selected action is not in this list, the `bricks/form/action/{form_action}` filter is triggered.

## Example usage

Here’s how you can handle a custom action called `slack-notification`:

```php
// Handle the Slack notification action
add_action(
    'bricks/form/action/slack-notification',
    function ( $form ) {
        $settings = $form->get_settings();
        $fields   = $form->get_fields();

        // Implement Slack notification logic
    }
);
```

## Parameters:

- **`$form` (\Bricks\Integrations\Form\Init)**: The current form instance, providing access to settings and submitted fields.

---

# Filter: bricks/form/create_post/meta_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-create_post-meta_value/

*This filter is used within the Create post form action in Bricks.*

This filter is used within the [Create post](https://academy.bricksbuilder.io/builder/features/create-update-posts-on-the-frontend/) form action in Bricks.

It allows developers to alter the meta values of new posts created from form submissions before they are saved to the database.

**Functionality:**

This filter activates during the execution of the 'Create Post' action. It provides an opportunity to modify the meta values based on custom logic or specific project requirements. This can include data formatting, validation, files handling, or applying conditional transformations to the meta values.

**Example Usage:**

```php
add_filter(
	'bricks/form/create_post/meta_value',
	function( $meta_value, $meta_key, $form_settings, $form_fields ) {
		if ( $meta_key === 'my_meta_key' ) {
			// Custom logic for 'my_meta_key'
			$meta_value = transform_meta_value( $meta_value );
		}
		// Additional custom logic can be implemented here
		return $meta_value;
	},
	10,
	4
);
```

In this example, the filter modifies the value of the meta key 'my_meta_key' using a custom function `transform_meta_value`.

**Parameters:**

- `$meta_value` (mixed): The original value of the meta field.
- `$meta_key` (string): The key of the meta field being modified.
- `$form_settings` (array): The settings of the form from which the post is created.
- `$form_fields` (array): The form fields data.

**Return:**

- (mixed): The modified value of the meta field, which will be saved with the post.

---

# Filter: bricks/form/update_post/meta_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-update_post-meta_value/

*This filter is part of the Update post form action in Bricks.*

This filter is part of the [**Update post**](https://academy.bricksbuilder.io/builder/features/create-update-posts-on-the-frontend/) form action in Bricks.

It enables developers to customize the meta values of existing posts being updated through form submissions.

**Functionality:**

The `bricks/form/update_post/meta_value` filter is triggered within the 'Update post' action when a post is being updated from a form submission. It allows for altering the meta values based on custom logic or project-specific needs. This includes formatting data, validating content, handling file uploads, or applying conditional transformations to the meta values.

**Example Usage:**

```php
add_filter(
	'bricks/form/update_post/meta_value',
	function( $meta_value, $meta_key, $post_id, $form_fields ) {
		if ( $meta_key === 'specific_meta_key' ) {
			// Custom logic for 'specific_meta_key'
			$meta_value = modify_meta_value( $meta_value );
		}
		// Implement additional custom logic here
		return $meta_value;
	},
	10,
	4
);
```

In this example, the filter modifies the value of a specific meta key ('specific_meta_key') using a custom function `modify_meta_value`.

**Parameters:**

- `$meta_value` (mixed): The original value of the meta field.
- `$meta_key` (string): The key of the meta field being modified.
- `$post_id` (int): The ID of the post being updated.
- `$form_fields` (array): The form fields data.

**Return:**

- (mixed): The modified value of the meta field, which will be updated in the post's meta data.

---

# Filter: bricks/frontend/render_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-frontend-render_data/

*The filter allows you to modify the rendered content for different areas like header, content, and footer before it's displayed on the frontend.*

The filter allows you to modify the rendered content for different areas like header, content, and footer before it's displayed on the frontend.

```php
add_filter( 'bricks/frontend/render_data', function( $content, $post, $area ) {
  // Do something

  return $content;
}, 10, 3 );
```

The filter callback receives three parameters:

- `$content`: The HTML content that's about to be returned. It's a string type.
- `$post`: The post object for which the content is being generated. It's an instance of the WP_Post class.
- `$area`: A string defining the area of the page currently being rendered (e.g., 'header', 'content', 'footer'). Available since version 1.5.4.

## Example: Add a unique ID to each heading

The following example demonstrates how to add a unique ID attribute to each heading in the generated content.

```php
add_filter('bricks/frontend/render_data', function($content, $post, $area) {
  // Iterate over each heading tag
  $content = preg_replace_callback(
    '/(<h[1-6](.*?))>(.*?)(<\/h[1-6]>)/i',
    function($matches) {
      // Add 'id' attribute if it doesn't exist
      if (strpos($matches[2], 'id=') === false) {
        // Use heading's content as the ID
        $matches[0] = $matches[1] . ' id="' . sanitize_title($matches[3])
        . '">' . $matches[3] . $matches[4];
      }

      // Return the (potentially) modified heading tag
      return $matches[0];
    },
    $content // Content to modify
  );

  // Return modified content
  return $content;
}, 10, 3);
```

In this example, a callback function is defined within the add_filter function call targeting the `bricks/frontend/render_data` filter. This callback function modifies every heading tag present in the content to include a unique ID attribute. This can be useful for navigation purposes, such as creating a table of contents.

---

# Filter: bricks/frontend/render_element

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-frontend-render_element/

*The bricks/frontend/renderelement filter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful hook can be used for a.*

The `bricks/frontend/render_element` filter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful hook can be used for a variety of customization tasks, such as adding comments, modifying content, or dynamically adjusting HTML. (@since 2.0)

```php
add_filter( 'bricks/frontend/render_element', function( $html, $element ) {
    // Do not modify the HTML in the builder
    if (
        bricks_is_builder_main() ||
        bricks_is_builder_iframe() ||
        bricks_is_builder_call()
    ) {
        return $html;
    }

    // Add comments before and after an element with a specific ID
    if ( $element->id === 'regxve' ) {
        $html = '<!-- Start of the element -->' . $html . '<!-- End of the element -->';
    }

    // Modify the content of a Basic Text element
    if ( $element->id === 'wtktgp' ) {
        // Replace "|" with ">>" in the HTML
        $html = str_replace( '|', '>>', $html );
    }

    return $html;
}, 10, 2 );

```

---

# Filter: bricks/get_element_data/maybe_from_post_id

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-get_element_data-maybe_from_post_id/

*Provide an alternate post ID for Bricks element-data lookups when custom elements reference content stored in another post or template.*

The `bricks/get_element_data/maybe_from_post_id` filter, available `@since 1.11`, allows you to specify an additional post ID from which to retrieve element data. This can be useful when dealing with custom elements that reference templates, posts, or external data sources, where the target element is not found within the standard element set. (Especially when dealing with Code element + Signed signature)

### When to Use

This filter is useful when working with custom elements that reference data from other templates or posts. For example, if you have a custom element that stores additional Bricks content in another post or template, and there is a code element with a signed signature located there, Bricks may not render the code element on the frontend because it doesn't know where to retrieve the signature. This filter allows you to specify the correct post or template to ensure that all elements are properly rendered.

```php
add_filter( 'bricks/get_element_data/maybe_from_post_id', function( $id, $element_data ) {
  // Check if the element is my custom element and has custom_template_id set on the control
  if ( isset( $element_data['name'] ) && $element_data['name'] === 'my-custom-element' && ! empty( $element_data['settings']['custom_template_id'] ) ) {
    $id = $element_data['settings']['custom_template_id'];
  }

  return $id;
}, 10, 2 );

```

---

# Filter: bricks/builder/i18n

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-i18n/

*Place and customize the following filter to add translatable string to the builder.*

Place and customize the following filter to add translatable string to the builder.

```php
add_filter( 'bricks/builder/i18n', function( $i18n ) {
  // Example: Provide translatable string for element category 'custom'
  $i18n['custom'] = esc_html__( 'Custom', 'bricks' );

  return $i18n;
} );
```

---

# Filter: bricks/is_layout_element

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-is_layout_element/

*Allows to define your custom elements as a layout element, so they are recognised like the section, container, block, div elements and use the same controls.*

Allows to define your custom elements as a layout element, so they are recognised like the section, container, block, div elements and use the same controls like query loop, flex controls, shape divider, etc.

```php
add_filter( 'bricks/is_layout_element', function( $layout_element_names ) {
    // Mark your custom element "custom_box" as a layout element
    $layout_element_names[] = 'custom_box';

    return $layout_element_names;
} );
```

---

# Filter: bricks/header/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/

*Programmatically add HTML attributes to the header tag.*

Programmatically add HTML attributes to the `header` tag.

```php
add_filter( 'bricks/header/attributes', function( $attributes ) {
  // Add custom class to header
  if ( isset( $attributes['class'] ) && is_array( $attributes['class'] ) ) {
    $attributes['class'][] = 'my-header-class';
  } else {
    $attributes['class'] = ['my-header-class'];
  }

  // Add 'data-is-header' HTML attribute to header with value 'y'
  $attributes['data-is-header'] = 'y';

  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-content-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes/)
- [/developer/hooks/filters/filter-bricks-footer-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-footer-attributes/)

---

# Filter: bricks/link_css_selectors

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-link_css_selectors/

*Use this filter in your child theme to overwrite/extend the CSS selectors the \"Theme Styles > Link\" settings are applied to like this (since Bricks 1.10 also.*

Use this filter in your child theme to overwrite/extend the CSS selectors the "Theme Styles > Link" settings are applied to like this (since Bricks 1.10 also available in the builder):

```php
add_filter( 'bricks/link_css_selectors', function( $link_css_selectors ) {
    // Add CSS link styles to .my-custom-element a
    $link_css_selectors[] = '.my-custom-element a';

    // OR return new list of CSS link selectors
    // $link_css_selectors = ['.link-wrapper a', '.link-wrapper-2 a'];

    return $link_css_selectors; // Array of selectors link styles are applied to
} );
```

> **Note**
>
> If the theme styles link styles do not apply to your custom selectors, force the regeneration of the theme styles by changing and saving the link color, the padding, or the text decoration, for example. Your new selectors will then be available.

---

# Filter: bricks/maintenance/should_apply

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-maintenance-should_apply/

*Override whether Bricks maintenance mode or coming-soon mode should be applied for the current request.*

Use this filter `(@since 2.0)` to override whether maintenance mode should be enforced for the current request.

By default, Bricks checks if the user is in the admin area or builder, if the current page is the login page, if the user can bypass maintenance, or if the current post is in the excluded list.

This filter runs *after* all of those checks have passed, giving you a final opportunity to apply custom logic before showing the maintenance or coming soon page.

## Parameters:

- `$apply_maintenance` (bool): Whether maintenance mode should apply. Defaults to `true` after all core checks pass.
- `$mode` (string): The current maintenance mode. Either `'maintenance'` or `'coming_soon'`.

## Return:

- `(bool)`: `true` to apply maintenance mode, `false` to bypass it.

## Example Usage:

In the following example, anyone with the correct `preview_key` in the URL (e.g. `https://domain.com?preview_key=letmein123`) will bypass maintenance mode. This is especially useful for sharing a live preview with clients or collaborators without requiring login access.

```php
add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key = 'letmein123';

    // Bypass maintenance mode if a valid preview key is present in the URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        return false;
    }

    // Keep default behavior for all other cases
    return $apply_maintenance;
}, 10, 2 );
```

### Improved version with cookie persistence:

You can improve this behavior further by **persisting the preview access across page loads** using a cookie. Otherwise, the user would only bypass maintenance on the first page they visit (where the key is present in the URL), and get blocked again when navigating elsewhere.

```php
add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key   = 'letmein123';
    $cookie_name = 'bricks_preview_key';

    // Check preview key in URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        // Set a cookie for 1 hour
        setcookie( $cookie_name, $valid_key, time() + HOUR_IN_SECONDS, COOKIEPATH, COOKIE_DOMAIN );
        return false;
    }

    // Check cookie on subsequent requests
    if ( isset( $_COOKIE[ $cookie_name ] ) && $_COOKIE[ $cookie_name ] === $valid_key ) {
        return false;
    }

    return $apply_maintenance;
}, 10, 2 );
```

---

# Filter: bricks/nav_menu/menu

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-nav_menu-menu/

*The bricks/navmenu/menu filter allows you to modify the navigation menu dynamically in Bricks Builder based on your conditions.*

The `bricks/nav_menu/menu` filter allows you to modify the navigation menu dynamically in Bricks Builder based on your conditions.

In the following example, we'll demonstrate how to change the navigation menu if the user is logged in.

This can be useful for displaying different menus to guests and logged-in users without using multiple Nab Menu elements and Bricks conditions.

**Example: **Use "My Account Menu" on the "Nav Menu" element (id: `kybsde`) if the user is logged in.

![](https://academy.bricksbuilder.io/assets/nav_menu-filter.png)

You can retrieve the menu ID via the URL parameter after selecting it.

![](https://academy.bricksbuilder.io/assets/nav_menu-menu-id.png)

```php
add_filter( 'bricks/nav_menu/menu', function( $menu, $post_id, $element ) {
  // Only target this nav menu element
  if( $element['id'] !== 'kdkdge' ) {
    return $menu;
  }

  // If logged-in, use the menu ID 4
  if( is_user_logged_in() ) {
    $menu = 4;
  }

  return $menu;
}, 10, 3 );
```

---

# Filter: bricks/password_protection/cookie_expires

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/

*Adjust the expiration time for the password cookie used by the password protection template. By default, when a password is set in the template settings, the.*

Adjust the expiration time for the password cookie used by [the password protection template](https://academy.bricksbuilder.io/builder/features/password-protection/). By default, when a password is set in the template settings, the cookie expires after **10 days**. This filter allows you to customize how long the cookie remains valid.

## Example Usage:

```php
add_filter( 'bricks/password_protection/cookie_expires', function( $expire ) {
    // Set cookie expiration to 1 hour (3600 seconds)
    return time() + 3600;
} );
```

In this example, the password cookie will expire after 1 hour, requiring users to re-enter the password if they revisit the page after that time.

**Parameters:**

- `$expire` (int): The default expiration timestamp for the password cookie, which is set to **10 days**.

**Return:**

- (int): The Unix timestamp for when the cookie should expire.

---

# Filter: bricks/password_protection/is_active

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-is_active/

*Use this filter to add custom rules that determine whether a password protection template should be active. By default, the template’s visibility is controlled.*

Use this filter to add custom rules that determine whether a [password protection template](https://academy.bricksbuilder.io/builder/features/password-protection/) should be active. By default, the template’s visibility is controlled by settings such as logged-in status, valid password cookies, and scheduling through the password protection template settings in the builder. This filter allows you to extend those checks, adding more dynamic criteria once the default settings have been applied.

## Example Usage:

```php
add_filter( 'bricks/password_protection/is_active', function( $is_active, $template_id, $settings ) {
    // Bypass password protection for users with the 'manage_options' capability
    if ( current_user_can( 'manage_options' ) ) {
        return false;
    }

    // Maintain default logic for other cases
    return $is_active;
}, 10, 3 );
```

In this example, any user with the `manage_options` capability (typically administrators) will bypass the password protection, while other users will follow the default settings.

**Parameters:**

- `$is_active` (bool): The initial status of whether the password protection is active.
- `$template_id` (int): The ID of the password protection template.
- `$settings` (array): The template settings.

**Return:**

- (bool): `true` to keep the template active, `false` to disable it.

---

# Filter: bricks/placeholder_image

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-placeholder_image/

*The bricks/placeholderimage filter allows you to override the default placeholder image used in Bricks. This can be useful when you want to display a custom.*

The `bricks/placeholder_image` filter allows you to override the default placeholder image used in Bricks. This can be useful when you want to display a custom placeholder for elements when performing template import or pasting elements from another website. `(@since 2.0)`

## Parameters

- `$image` *(string)* – The default placeholder image path or URL.
- `$is_svg` *(bool)* – Whether the placeholder should be an SVG. Leave as is.
- `$format` *(string)* – Can be `'url'` or `'path'` depending on the context Bricks needs it for. Leave as is.

```php
add_filter( 'bricks/placeholder_image', function( $image, $is_svg, $format ) {
  // Custom placeholder images (SVG and non-SVG file required)
  // SVG file: /uploads/2025/04/my-placeholder.svg
  // Non-SVG file: /uploads/2025/04/my-placeholder-img.png
  $relative_path = $is_svg ? '2025/04/my-placeholder.svg' : '2025/04/my-placeholder-img.png';
  $upload_dir    = wp_get_upload_dir();

  if ( $format === 'path' ) {
    // Return absolute path to the image
    $image = $upload_dir['basedir'] . '/' . $relative_path;
  } else {
    // Return full URL to the image
    $image = $upload_dir['baseurl'] . '/' . $relative_path;
  }

  return $image;
}, 10, 3 );
```

---

# Filter: bricks/posts/merge_query

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-merge_query/

*Since Bricks 1.3.7 you'll be able to decide if a certain element query should be merged with the WordPress main query, in the archive or search templates, using.*

Since Bricks 1.3.7 you'll be able to decide if a certain element query should be merged with the WordPress main query, in the archive or search templates, using the following filter:

```php
add_filter( 'bricks/posts/merge_query', function( $merge, $element_id ) {
  if ( $element_id === 'wghgco' ) {
    return false;
  }

  return $merge;
}, 10, 2 );
```

The filter callback receives two arguments:

- `$merge` is a boolean variable indicating whether the query should be merged or not (default: true)
- `$element_id` is a string containing the element ID

This is triggered for all the Bricks elements containing one internal WP_Query query like the Posts and the Carousel element, or any other element where the Query Loop is enabled (Container, Slider, Accordion).

> **Note**
>
> Starting from Bricks 1.7, you can achieve the same result by utilizing the "Disable Query Merge" option in the [Query Loop](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#posts-query), without the need for a PHP filter. Use this filter for more advanced situations.

## How to find the element ID? {#find-element-id}

Each element in Bricks has a unique ID. You may find the element ID when editing the element and looking into the Global CSS classes input. By default, it shows the element HTML ID (e.g. `#bricks-element-wghgco`). For the purpose of this filter, we only need the last portion of the string, the six-character long element ID (e.g. `wghgco`).

![](https://academy.bricksbuilder.io/assets/Screenshot-2021-12-29-at-09.19.37.png)

---

# Filter: bricks/posts/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-query_vars/

*Since Bricks 1.3.2 you may manipulate the posts, products, or Query Loop elements query vars before the query is performed like so:*

Since Bricks 1.3.2 you may manipulate the **posts**, **products,** or **Query Loop** elements query vars before the query is performed like so:

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    // Use an ACF custom field to restrict the query to a set of posts
    if ( $element_id == 'fhmnfx' && function_exists('get_field') ) {
        $query_vars['post__in'] = get_field('my_posts_acf_field');
    }

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_Query](https://developer.wordpress.org/reference/classes/wp_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID (`@since 1.3.6`)
- `$element_name` is a string containing the element name (`@since 1.11.1`)

> **Note**
>
> If you intend to modify the $query_vars for the WooCommerce product query in Bricks, consider increasing the priority argument to a higher value, such as 20 or 30. Failure to do so could result in your filter being potentially overridden by other code that hooks into this filter.

#### Example: Loop images from Metabox.io Advanced Image Field of current post {#metabox-advanced-image-loop}

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {

    // Only target yeamho element_id
    if ( $element_id !== 'yeamho') return $query_vars;

    // Get Metabox advanced images field values. 'mg_projet_galerie_images' is the field id
    $gallery_images = (array) rwmb_meta( 'mg_projet_galerie_images', ['size' => 'full'] );

    // Get the Images Ids only
    $gallery_images_ids = array_keys($gallery_images);

    // If no gallery images, set empty string array
    $gallery_images_ids = count( $gallery_images_ids ) > 0 ? $gallery_images_ids : [''];

    // Set the images ids as post__in parameters
    $query_vars['post__in'] = $gallery_images_ids;

    return $query_vars;
}, 10, 4 );
```

#### Example: Use current taxonomy's ACF gallery images IDs for a Media query loop (Nestable Slider) {#acf-term-gallery-field}

If you want to build a dynamic Slider in term archive template, you can set the query loop on the Slide like below image, and use the code snippet below to retrieve the images IDs from the gallery field for each term, then assign them to the `post__in` parameter.

![](https://academy.bricksbuilder.io/assets/media-query-loop-in-term-archive-01.png)

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
  // Only target udcvuw element_id
  if ( $element_id == 'udcvuw' && function_exists('get_field') ) {
    // Set to 0, ensure no results by default
    $query_vars['post__in'] = [0];
    $current_term = get_queried_object();

    // Check if the current page is a term archive
    if( is_a( $current_term, 'WP_Term' ) ) {
      // Get the images associated with the current term, region_-_banniere is the field name
      $images = get_field('region_-_banniere', 'region_'. $current_term->term_id );

      // Check if images exist and if there's more than 0 images
      if( is_array( $images ) && count( $images ) > 0 ) {
        // Get the IDs of the images (if this field return format is array)
        $images_ids = wp_list_pluck( $images, 'ID' );
        // Set the query to include only posts with these image IDs
        $query_vars['post__in'] = $images_ids;
      }
    }
  }
  return $query_vars;
}, 10, 4 );

```

#### Example: Apply orderby argument with 2 different fields {#orderby-with-multiple-fields}

Imagine you got a Performance post type with a start date field and a start time field. As you will not create the Performance post by actual sequence, you wish to order the Performance posts by start date (ascending) and start time (descending).

Since 1.11.1, you can achieve this in Query Loop user interface. Check [this](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#enhanced-ordering-options) out.

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {

    // Only target 3b03dd element_id
    if( $element_id !== '3b03dd') return $query_vars;

    // Set meta_query
    $query_vars['meta_query'] = [
        'relation' => 'AND',
        'performance_start_date' => array(
            'key' => 'performance_start_date',
            'compare' => 'EXISTS',
        ),
        'performance_start_time' => array(
            'key' => 'performance_start_time',
            'compare' => 'EXISTS',
        ),
    ];

    // Set orderby
    $query_vars['orderby'] = [
        'performance_start_date' => 'ASC',
        'performance_start_time' => 'DESC'
    ];

    return $query_vars;
}, 10, 4 );
```

#### Example: Get WooCommerce Related Products {#woocommerce-related-products-query}

Create a query loop with the following settings

![](https://academy.bricksbuilder.io/assets/woo-related-products-query.png)

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
	if( $element_id !== 'azuxwi' ) return $query_vars;

	$product_id = get_the_ID();
	$product = wc_get_product( $product_id );

	if( ! is_a( $product, 'WC_Product' ) ) return $query_vars;
	// Exclude the upsell products
	$upsell_ids = $product->get_upsell_ids();

	if( count( $upsell_ids ) > 0 ) {
		if( isset( $query_vars['post__not_in'] ) ) {
			$query_vars['post__not_in'] = array_merge( $query_vars['post__not_in'], $upsell_ids );
		} else {
			$query_vars['post__not_in'] = $upsell_ids;
		}
	}

	return $query_vars;
}, 10, 4);
```

#### Example: Get WooCommerce Upsell Products {#woocommerce-upsell-products-query}

Create a query loop with the following settings:

![](https://academy.bricksbuilder.io/assets/query_var_product_upsell.png)

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
	// Change the Id
	if( $element_id !== 'shctqn') return $query_vars;

	$product_id = get_the_ID();
	$product = wc_get_product( $product_id );

	if( ! is_a( $product, 'WC_Product' ) ) return $query_vars;

	$upsell_ids = $product->get_upsell_ids();
	$query_vars['post__in'] =  ( count( $upsell_ids ) > 0 )? $upsell_ids : [0] ;
        // in case your have product variation set as upsell
        $query_vars['post_type'] = ['product', 'product_variation'];

	return $query_vars;
}, 10, 4 );
```

#### Different ways to target the query other than $element_id {#different-ways-to-target-bricks-query-in-php}

Sometimes you might want to target a group of queries instead of a specific element by using the `$element_id`

##### Use WordPress conditional tag function

```php
// Target any query in an archive page
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {

  if( ! is_archive() ) return $query_vars;

  // Perform your logic here

  return $query_vars;
}, 10, 4 );
```

##### Check if CSS class exists on the query element

```php

// Target any query if 'my-custom-class' set on the query element in STYLE > CSS > CSS Classes
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {

  $css_class = isset( $settings['_cssClasses'] ) ? $settings['_cssClasses'] : '';

  if( $css_class === '' || strpos( $css_class, 'my-custom-class' ) === false ) {
    return $query_vars;
  }

  // Perform your logic here

  return $query_vars;
}, 10, 4 );

// Target any query if 'my-custom-class' global class set on the query element
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {

  $global_css_classes = isset( $settings['_cssGlobalClasses'] ) ? \Bricks\Element::get_element_global_classes( $settings['_cssGlobalClasses'] ) : [];

  if( empty( $global_css_classes ) || ! in_array( 'my-custom-class', $global_css_classes ) ) {
    return $query_vars;
  }

  // Perform your logic here

  return $query_vars;
}, 10, 4 );
```

---

# Filter: bricks/query/force_run

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-force_run/

*Bricks has enhanced query performance in 1.9.1. Now, each unique query is executed only once per page load, and subsequently, the query results are reused on.*

Bricks has enhanced query performance in 1.9.1. Now, each unique query is executed only once per page load, and subsequently, the query results are reused on the same page. Consequently, certain queries-related PHP filters will no longer be triggered multiple times.

The following filters may be impacted:

- `bricks/posts/merge_query`
- `bricks/posts/query_vars`
- `bricks/terms/query_vars`
- `bricks/users/query_vars`
- `bricks/query/run`
- `bricks/query/result`
- `bricks/query/result_count`
- `bricks/query/result_max_num_pages`

Nevertheless, developers can utilize this filter to disable this setting for certain queries under specific circumstances.

```php
// Return boolean (default: false)
add_filter( 'bricks/query/force_run', function( $force_run, $query ) {
  // Get element ID
  $element_id  = $query::get_query_element_id();
  // Get element settings
  $settings = $query->settings;

  if ( isset( $settings['usingFacetWP'] ) ) {
    $force_run = true;
  }

  return $force_run;
}, 10, 2 );
```

Since 1.9.2, you can define `$query_vars['bricks_force_run'] = true` to achieve the same result as well. This will be handy if you are using the Bricks Query Editor or PHP filters like `bricks/posts/query_vars`  etc.

![](https://academy.bricksbuilder.io/assets/bricks-query-force-run-query-vars.png)

---

# Filter: bricks/query/init_loop_index

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-init_loop_index/

*Filter the initial Bricks loop index so paginated, infinite-scroll, or custom queries keep their loop-based output aligned.*

The `bricks/query/init_loop_index` filter, available `@since 1.11`, allows you to modify the initial loop index when using various query types in Bricks Builder. This filter is especially useful in cases such as infinite scroll or paginated queries, where setting the correct loop index is crucial for displaying content seamlessly across multiple pages especially when using dynamic backgound images or colors. Without this hook, the generated dynamic CSS might be applied on the incorrect element when performing infinite scroll or paginate actions.

### When to Use

This filter is particularly useful when creating a custom query type using the [bricks/setup/control_options](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-nav_menu-menu/) hook. You can implement your own logic for handling pagination and adjust the initial loop index accordingly.

```php
add_filter( 'bricks/query/init_loop_index', function ( $initial_index, $object_type, $query ) {
  // Check if the object type is 'my_custom_query'
  if ( $object_type !== 'my_custom_query' ) {
    return $initial_index;
  }

  // Add your custom logic to modify the initial loop index
  // Example: Calculate based on custom logic
  // $initial_index = custom_logic_to_calculate_index();

  return $initial_index;
}, 10, 3 );

```

---

# Filter: bricks/query/loop_object

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object/

*The Bricks Query Loop supports 3 types of queries by default (Posts, Terms, and Users). But it can be extended to support any other query. While iterating.*

The Bricks [Query Loop](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) supports 3 types of queries by default (Posts, Terms, and Users). But it can be extended to support [any other query](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-run/). While iterating through the query results, the iteration object could be manipulated using the `bricks/query/loop_object` like so:

```php
add_filter( 'bricks/query/loop_object', function( $loop_object, $loop_key, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $loop_object;
    }

    // Perform some logic, for example:
    // global $post;
    // $post = get_post( $loop_object );
    // setup_postdata( $post );

    return $loop_object;
}, 10, 3 );
```

The filter callback receives two arguments:

- `$loop_object` is the current loop iteration value (from the results array)
- `$loop_key` is the current loop iteration key (from the results array)
- `$query_obj` is an instance of the `\Bricks\Query` class object

Related hooks:

- To add a query type to the Query control use [`bricks/setup/control_options`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/)
- To perform the custom query type and output the results use [`bricks/query/run`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-run/)

---

# Filter: bricks/query/loop_object_id

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object_id/

*Bricks will use \\Bricks\\Query::getloopobjectid() to retrieve the looping iteration's object ID.*

Bricks will use `\Bricks\Query::get_loop_object_id()` to retrieve the looping iteration's object ID.

This static function is used in many places. Especially when trying to parse dynamic data.  By default, Bricks uses the looping ID if the looping object is a WP_Post, WP_Term, or WP_User object. This filter allows you to change the ID conditionally.

```php
// Change the object_id if the current looping query type is myCustomQueryType
add_filter( 'bricks/query/loop_object_id', function( $object_id, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );
    if ( $query_object_type !== 'myCustomQueryType' ) {
	return $object_id;
    }

    // Set my loop_object_id
    $new_id = my_custom_function_to_transform_the_id( $object_id );
    return $new_id;
}, 10, 3 );
```

### Related hooks:

- [bricks/setup/control_options](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/): To add a custom query type to the Query control
- [bricks/query/loop_object](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object/): To manage the object on every loop iteration

---

# Filter: bricks/query/loop_object_type

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object_type/

*Bricks will use \\Bricks\\Query::getloopobjecttype() to retrieve the looping iteration's object type. This static function is used in many places. It plays an.*

Bricks will use `\Bricks\Query::get_loop_object_type()` to retrieve the looping iteration's object type. This static function is used in many places. It plays an important role in many conditions. The possible return object_type should be 'post', 'term', or 'user' only.

```php
// This is the example when Bricks set the object_type in woo cart query, so inside each iteration, it will be treat as a post/product object_type
add_filter( 'bricks/query/loop_object_type', function( $object_type, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );

    if ( $query_object_type !== 'wooCart' ) {
	return $object_type;
    }

    return 'post';
}, 10, 3 );
```

---

# Filter: bricks/query/no_results_content

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-no_results_content/

*You can programmatically change the query loop \"no results content\" using this filter.*

You can programmatically change the query loop "no results content" using this filter.

```php
add_filter( 'bricks/query/no_results_content', function( $content, $settings, $element_id ) {

  // Check if the query element id is the one you want
  if( $element_id !== 'srixvr' ) return $content;

  // Use a bricks section template as the no results content
  $content = do_shortcode('[bricks_template id="3981"]');

  return $content;
}, 10, 3 );
```

---

# Filter: bricks/query/result

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/

*Available since 1.8, this filter lets you customize the query results and implement additional logic. Like modifying the post, term, or user object type. Which.*

Available since 1.8, this filter lets you customize the query results and implement additional logic. Like modifying the post, term, or user object type. Which was previously not editable through the [`bricks/query/run`](https://academy.bricksbuilder.io/article/filter-bricks-query-run/) filter.

```php
// Use this filter to rearrange it by post title (PHP way instead of query orderby)
add_filter( 'bricks/query/result', function( $result, $query_obj ){
  // Return: Element ID is not "djvsvi", nor is it a post query
  if ( $query_obj->element_id !== 'djvsvi' || $query_obj->object_type !== 'post' ) {
    return $result;
  }

  // Sort by post title (descending)
  // Result is WP_Query object with posts
  if ( $result->have_posts() ) {
    $posts = $result->posts;

    usort( $posts, function( $a, $b ) {
      return strcmp( $b->post_title, $a->post_title );
    });

    $result->posts = $posts;
  }

  return $result;
}, 10, 2 );
```

---

# Filter: bricks/query/result_count

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_count/

*Filter the result count Bricks reports for a query object before pagination or related UI uses that total.*

This filter allows you to modify the query result count (@since 1.8).

```php
add_filter( 'bricks/query/result_count', function( $result_count, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $result_count;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $new_count = 123;
  return $new_count;
}, 10, 2 );
```

---

# Filter: bricks/query/result_max_num_pages

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_max_num_pages/

*Filter the maximum number of pages Bricks reports for a query object, including the value used by Pagination.*

This filter allows you to modify the query result maximum number of pages (@since 1.9.1). This value is used for the Pagination element as well.

```php
add_filter( 'bricks/query/result_max_num_pages', function( $max_num_pages, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $max_num_pages;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $max_num_pages = 3;
  return $max_num_pages;
}, 10, 2 );
```

---

# Filter: bricks/query/run

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-run/

*The Bricks Query Loop supports 3 types of queries by default (Posts, Terms and Users). But it can be extended to support any other query. To return a custom.*

The Bricks [Query Loop](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) supports 3 types of queries by default (Posts, Terms and Users). But it can be extended to support any other query. To return a custom query result, Bricks can be extended using the WP filter `bricks/query/run` like so:

```php
add_filter( 'bricks/query/run', function( $results, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $results;
    }

    // Perform the query
    // Assign the results to $results (array)

    return $results;
}, 10, 2 );
```

The filter callback receives two arguments:

- `$results` is the results array (empty by default). The loop will iterate through this array.
- `$query_obj` is an instance of the `\Bricks\Query` class object

Note: This hook should be used to add different types of query results. If you want to alter the posts, terms, or users query, use the following hooks:

- **Posts**: [`bricks/posts/query_vars`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-posts-query_vars/)
- **Terms**: [bricks/terms/query_vars](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars/)
- **Users**: [bricks/users/query_vars](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-users-query_vars/)

Related hooks:

- To add a query type to the Query control use [`bricks/setup/control_options`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/)
- To manage the object on every loop iteration use [`bricks/query/loop_object`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-loop_object/)

---

# Filter: bricks/registered_post_types_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-registered_post_types_args/

*Available since version 1.6, this filter allows you to customise the post type args that are used to query the post type as shown in the Bricks settings & the.*

Available since version 1.6, this filter allows you to customise the post type args that are used to query the post type as shown in the Bricks settings & the builder (e.g. Query control post types, etc.)

```php
add_filter( 'bricks/registered_post_types_args', function( $args ) {
  // Default: Return only public post types
  // $args['public'] = true;

  // Custom: Return all registered post types
  unset( $args['public'] );

  // Available arguments: https://developer.wordpress.org/reference/functions/get_post_types/#comment-2184
  return $args;
} );
```

---

# Filter: bricks/related_posts/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-related_posts-query_vars/

*Since Bricks 1.3.5 you may manipulate the related posts element query vars before the query is performed like so:*

Since Bricks 1.3.5 you may manipulate the **related posts** element query vars before the query is performed like so:

```php
add_filter( 'bricks/related_posts/query_vars', function( $query_vars, $settings, $element_id ) {
    $query_vars['post_type'] = [ 'post', 'project' ];

    return $query_vars;
}, 10, 3 );
```

The filter callback receives two arguments:

- `$query_vars` is an associative array used to feed the [WP_Query](https://developer.wordpress.org/reference/classes/wp_query/) class
- `$settings` is an associative array containing the element settings set in the builder
- `$element_id` is a string containing the element ID

---

# Filter: bricks/render_query_loop_trail

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-render_query_loop_trail/

*Control whether Bricks renders the query loop trail node that frontend JavaScript uses to read query settings.*

The `bricks/render_query_loop_trail` (@since 1.11.1) filter controls the output of the query loop trail node in Bricks. This node is automatically added to each query loop and records the loop's settings, which are then accessed by frontend JavaScript to manage various query-related tasks. Once these settings are read by Bricks, the node is removed from the DOM.

For some third-party plugins, this node may not be needed—especially if they use custom AJAX endpoints to update query results independently of Bricks. Using this filter, you can control whether or not the query loop trail node is rendered.

```php
// Return true = render the query loop trail node
// Return false = skip the query loop trail node
add_filter( 'bricks/render_query_loop_trail', function( $render, $element, $query ) {
  // Do not render query loop trail node if my-custom-param parameter exists
  if ( isset( $_GET['my-custom-param'] ) ) {
    $render = false;
  }

  return $render;
}, 10, 3 );
```

In this example, if the `my-custom-param` parameter is detected in the URL, the query loop trail node will not be rendered. This can be useful for third-party plugins with custom AJAX endpoints that handle query configurations independently.

---

# Filter: bricks/screen_conditions/scores

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-screen_conditions-scores/

*Bricks selects the template & theme style for a specific page according to the conditions you've defined.*

Bricks selects the template & theme style for a specific page according to the conditions you've defined.

Internally this is done via a scoring system from 0 to 10. 0 is the least specific. 10 being the most specific (e.g. specific post ID).

For each template/theme style condition that could apply to a certain context, the template/theme style earns a specific score. After analyzing all templates/theme styles, Bricks chooses the one with the highest score.

If you need to add new template conditions using the filter [`builder/settings/template/controls_data`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-builder-settings-type-controls_data/) or `bricks/theme_styles/controls` for theme styles, you then need to hook into the scoring logic to score the templates/theme styles based on the custom conditions.

This is where the `bricks/screen_conditions/scores` filter comes in handy, like so:

```php
add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  // Run custom logic to score the template/theme style $condition
  // $scores[] = 5;

  return $scores;
}, 10, 4 );
```

**Example 1: Add the score for a specific author role in an author archive template**

After adding the control using the [`builder/settings/template/controls_data`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-builder-settings-type-controls_data/) (check example 1), we now need to hook in `bricks/screen_conditions/scores` to score the template based on the condition, like so:

```php
add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  if ( is_author() && $condition['main'] === 'archiveType' && isset( $condition['archiveType'] ) && in_array( 'author', $condition['archiveType'] ) && isset( $condition['archiveAuthorRoles'] ) ) {
    $user = get_queried_object();

    if ( ! empty( $user->roles ) && is_array( $user->roles ) ) {
      foreach ( $user->roles as $role_name ) {
        if ( in_array( $role_name, $condition['archiveAuthorRoles'] ) ) {
          $scores[] = 9;
        }
      }
    }
  }

  return $scores;
}, 10, 4 );
```

---

# Filter: bricks/search_form/home_url

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-search_form-home_url/

*The bricks/searchform/homeurl filter allows developers to customize the action URL of the search form within the Bricks theme. This filter provides the.*

The `bricks/search_form/home_url` filter allows developers to customize the action URL of the search form within the Bricks theme. This filter provides the flexibility to redirect search queries to a different URL than the default WordPress home URL.

By using this filter, developers can integrate custom search solutions or direct the search form submissions to a specific page, enhancing the search functionality tailored to specific needs.

### Example Usage:

```php
<code>add_filter( 'bricks/search_form/home_url', function( $home_url ) {</code><code>    // Custom logic to determine the action URL</code><code>    $custom_action_url = 'https://example.com/custom-search-page/'; </code>
<code>    return $custom_action_url;</code><code>});</code>
```

In this simple example, the search form action URL is changed to a custom page. This is particularly useful for websites with specialized search requirements or for integrating with external search platforms.

### Parameters:

- `$home_url` (string): The default URL to which the search form points, typically the home URL.

### Return:

- (string): The modified URL for the search form action.

---

# Filter: bricks/element/set_root_attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-set_root_attributes/

*Bricks 1.4 with its improved & slimmer DOM structure now requires to add the element ID, root classes, and other element root HTML attributes directly inside.*

Bricks 1.4 with its improved & slimmer DOM structure now requires to add the element ID, root classes, and other element root HTML attributes directly inside the `render()` function. You can programmatically manipulate the returns element root attributes like so:

```php
add_filter( 'bricks/element/set_root_attributes', function( $attributes, $element ) {
    // Add CSS class 'heading-bg' to every heading element
    if ( $element->name === 'heading' ) {
        $attributes['class'][] = 'heading-bg';
    }

    return $attributes;
}, 10, 2 );
```

The filter callback receives 2 arguments:

- `$attributes` – an associative array of the element root attributes, grouped by the attribute name (e.g. "class", "data-animation", ...)
- `$element` - the Bricks element [object](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/)

**NOTE**: This filter doesn't work in builder & already possible with *[bricks/element/render_attributes](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-render_attributes/)*
