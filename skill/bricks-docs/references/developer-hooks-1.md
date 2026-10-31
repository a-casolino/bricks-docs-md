# Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/

*Browse documented Bricks hooks, including action hooks and filter hooks for builder behavior, rendering, queries, authentication, and integrations.*

These are all documented Bricks hooks:

---

# Action: bricks/generate_css_file

Source: https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-generate_css_file/

*If your CSS loading method is set to External files, this hook will be triggered when a CSS file is generated in Bricks. Developers can use this hook to trigger.*

If your CSS loading method is set to **External files**, this hook will be triggered when a CSS file is generated in Bricks. Developers can use this hook to trigger other actions related to CSS file generation. It's useful for instructing a cache plugin to clear the cache when a CSS file is generated. (`@since 1.9.5`)

```php
/**
  * $type : 'global-color-palettes' | 'global-elements' | 'theme-styles' | 'global-custom-css' | 'post'
  * $file_name : The generated CSS file name
*/
add_action( 'bricks/generate_css_file', function( $type, $file_name ) {
  error_log( 'Generated CSS file: ' . $type . ' - ' . $file_name );
}, 10, 2 );
```

**Parameters:**

- `$type` (string): Possible strings `global-color-palettes` `global-elements` `theme-styles` `global-custom-css` `post`
- `$file_name` (string): The generated CSS file name

---

# Action: bricks/query/after_loop

Source: https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-query-after_loop/

*If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data after the loop.*

If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data after the loop runs. (`@since 1.7.2`)

```php
// Perform certain action after the loop of query element oklvcq
add_action( 'bricks/query/after_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );
```

---

# Action: bricks/query/before_loop

Source: https://academy.bricksbuilder.io/developer/hooks/actions/action-bricks-query-before_loop/

*If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data before the loop.*

If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data before the loop runs. (`@since 1.7.2`)

```php
// Perform certain action before the loop of query element oklvcq
add_action( 'bricks/query/before_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );
```

---

# Action: bricks_after_footer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_footer/

*Runs after Bricks renders the footer and before the site wrapper closes.*

Runs after Bricks renders the footer and before the site wrapper closes. Use it when custom output needs to appear immediately after the footer template.

## Example usage

```php
add_action( 'bricks_after_footer', function() {
    echo '<div class="after-footer-note">Footer add-on output</div>';
} );
```

---

# Action: bricks_after_header

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_header/

*Runs after Bricks renders the header template.*

Runs after Bricks renders the header template. Use it for output or setup that should happen directly after the site header.

## Example usage

```php
add_action( 'bricks_after_header', function() {
    echo '<div class="after-header-banner">Announcement</div>';
} );
```

---

# Action: bricks/archive_product/after

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-archive_product-after/

*Runs after the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives.*

Runs after the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives rendered by Bricks.

## Parameters

- `$bricks_data` (*array*): The Bricks data for the template being rendered.
- `$post_id` (*int*): The ID of the post/archive being rendered.

## Example usage

```php
add_action( 'bricks/archive_product/after', function( $bricks_data, $post_id ) {
    // Output custom content after the product archive
    echo '<div class="custom-archive-footer">End of product list</div>';
} );
```

---

# Action: bricks/archive_product/before

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-archive_product-before/

*Runs before the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives.*

Runs before the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives rendered by Bricks.

## Parameters

- `$bricks_data` (_array_): The Bricks data for the template being rendered.
- `$post_id` (_int_): The ID of the post/archive being rendered.

## Example usage

```php
add_action( 'bricks/archive_product/before', function( $bricks_data, $post_id ) {
    // Output custom content before the product archive
    echo '<div class="custom-archive-header">Welcome to our shop</div>';
} );
```

---

# Action: bricks_before_footer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_footer/

*Runs before Bricks renders the footer template.*

Runs before Bricks renders the footer template. Use it to output markup or run logic immediately before footer rendering.

## Example usage

```php
add_action( 'bricks_before_footer', function() {
    echo '<div class="before-footer-cta">Need help?</div>';
} );
```

---

# Action: bricks_after_site_wrapper

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_site_wrapper/

*Runs in footer.php after the footer render action and before wp_footer(). Bricks uses it to close the builder wrapper.*

Runs in `footer.php` after `bricks_after_footer` and before `wp_footer()`.

In the builder, Bricks uses this hook to close the `.brx-body` wrapper. On the frontend, Bricks also uses this position for one page navigation output when that page setting is enabled.

## Example usage

```php
add_action( 'bricks_after_site_wrapper', function() {
    echo '</div><!-- .before-site-wrapper -->';
} );
```

---

# Action: bricks_before_site_wrapper

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_site_wrapper/

*Runs in header.php before the header render action. Bricks uses it to open the builder wrapper.*

Runs in `header.php` after `bricks_body` and before `bricks_before_header`.

In the builder, Bricks uses this hook to open the `.brx-body` wrapper around the builder frame. On the frontend, it is a general position before the header render flow.

## Example usage

```php
add_action( 'bricks_before_site_wrapper', function() {
    echo '<div class="before-site-wrapper">';
} );
```

---

# Action: bricks_body

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-body/

*Runs after the document head closes. Bricks uses it to print the opening body tag and body-start output.*

Runs in `header.php` after the document head closes and before the site-wrapper and header hooks.

Bricks attaches its opening `<body>` tag callback to this hook at priority `1`. Default-priority callbacks run after the opening body tag and after Bricks has printed body-start scripts and skip links.

## Example usage

```php
add_action( 'bricks_body', function() {
    echo '<div id="body-integration-root"></div>';
} );
```

---

# Action: bricks/builder/switch_locale

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-builder-switch_locale/

*Runs when Bricks switches the builder locale.*

Runs when Bricks switches the builder locale. Use it to synchronize integration state when the builder language changes.

## Parameters

- `$locale` (string): The locale Bricks is switching the builder to.

## Example usage

```php
add_action( 'bricks/builder/switch_locale', function( $locale ) {
    // Switch integration language context to match the builder.
}, 10, 1 );
```

---

# Action: bricks_before_header

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_header/

*Runs before Bricks renders the header template.*

Runs before Bricks renders the header template. Use it to output markup or run logic immediately before header rendering.

## Example usage

```php
add_action( 'bricks_before_header', function() {
    echo '<div class="top-strip">Free shipping this week</div>';
} );
```

---

# Action: bricks/database/get_all_templates_by_type/after_query

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-database-get_all_templates_by_type-after_query/

*Runs after Bricks queries templates by type.*

Runs after Bricks performs the uncached `get_posts()` query for all published Bricks templates. Use it to restore integration query context after Bricks has fetched template IDs.

This action does not run when Bricks returns templates from object cache or the in-memory `Database::$all_templates` cache.

## Parameters

- `$template_ids` (array): Template IDs returned by the query.
- `$args` (array): The query arguments used to fetch templates.

## Example usage

```php
add_action( 'bricks/database/get_all_templates_by_type/after_query', function( $template_ids, $args ) {
    // Restore custom query or language context here.
}, 10, 2 );
```

---

# Action: bricks/dynamic_data/after_do_action

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-after_do_action/

*Runs after the dynamic data {doaction:myhook} tag is processed. This allows you to execute code after a specific doaction tag has been rendered.*

Runs after the dynamic data `{do_action:my_hook}` tag is processed. This allows you to execute code after a specific `do_action` tag has been rendered.

## Parameters

- `$action` (*string*): The action name specified in the tag (e.g. `my_hook` in `{do_action:my_hook}`).
- `$filters` (*array*): Array of filters applied to the tag.
- `$context` (*string*): The context in which the tag is being rendered (e.g., 'text').
- `$post` (*WP_Post|null*): The current post object, or null.
- `$value` (*string*): The rendered output of the action (captured via output buffering).

## Example usage

```php
add_action( 'bricks/dynamic_data/after_do_action', function( $action, $filters, $context, $post, $value ) {
    if ( $action === 'my_custom_hook' ) {
        // Code to run after 'my_custom_hook' is processed via dynamic data
        error_log( 'Finished processing my_custom_hook' );
    }
}, 10, 5 );
```

---

# Action: bricks/dynamic_data/before_do_action

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-before_do_action/

*Runs before the dynamic data {doaction:myhook} tag is processed. This allows you to execute code before a specific doaction tag is rendered.*

Runs before the dynamic data `{do_action:my_hook}` tag is processed. This allows you to execute code before a specific `do_action` tag is rendered.

## Parameters

- `$action` (_string_): The action name specified in the tag (e.g. `my_hook` in `{do_action:my_hook}`).
- `$filters` (_array_): Array of filters applied to the tag.
- `$context` (_string_): The context in which the tag is being rendered (e.g., 'text').
- `$post` (_WP_Post|null_): The current post object, or null.

## Example usage

```php
add_action( 'bricks/dynamic_data/before_do_action', function( $action, $filters, $context, $post ) {
    if ( $action === 'my_custom_hook' ) {
        // Code to run before 'my_custom_hook' is processed via dynamic data
        error_log( 'Starting processing my_custom_hook' );
    }
}, 10, 4 );
```

---

# Action: bricks/dynamic_data/tag_value_parsed

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tag_value_parsed/

*Runs after Bricks parses a dynamic data tag value.*

Runs after Bricks parses a dynamic data tag value. This action is for observing or reacting to the parsed value; it does not change the returned value.

## Parameters

- `$value` (mixed): The parsed dynamic data value.
- `$tag` (string): The parsed tag name.
- `$original_tag` (string): The original dynamic data tag before parsing.
- `$args` (array): Parsed tag arguments.
- `$post` (WP_Post|int|null): The post context used while parsing.
- `$context` (string): The render context, such as text, link, or image.
- `$provider` (string|null): The provider that resolved the tag, when available.

## Example usage

```php
add_action( 'bricks/dynamic_data/tag_value_parsed', function( $value, $tag, $original_tag, $args, $post, $context, $provider ) {
    // Log or inspect parsed dynamic data values.
}, 10, 7 );
```

---

# Action: bricks_execute_filter_index_job

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-execute_filter_index_job/

*Runs before a query filter index job is executed.*

Runs before a query filter index job is executed. Bricks uses this point so integrations can prepare context, such as switching language, before indexing starts.

## Parameters

- `$job` (array): The index job data that is about to be processed.

## Example usage

```php
add_action( 'bricks_execute_filter_index_job', function( $job ) {
    // Prepare integration context before this index job runs.
}, 10, 1 );
```

---

# Action: bricks/form/custom_action

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-form-custom_action/

*Runs when a form with a \"Custom\" action is submitted. This allows you to execute custom PHP logic to handle the form submission.*

Runs when a form with a "Custom" action is submitted. This allows you to execute custom PHP logic to handle the form submission.

## Parameters

- `$form` (*Bricks\Form*): The form instance.

## Example usage

```php
add_action( 'bricks/form/custom_action', function( $form ) {
    // Get form fields
    $fields = $form->get_fields();
    
    // Get form settings
    $settings = $form->get_settings();
    
    // Get submitted data
    $form_data = $fields['formId'] ?? []; // Or retrieve specific field values
    
    // Perform custom logic, e.g., send to external API
    $name = isset( $fields['form-field-name'] ) ? $fields['form-field-name'] : '';
    
    if ( $name === 'Specific Name' ) {
        // Do something
        $form->set_result( [
            'type' => 'success', // or 'danger', 'info', 'warning'
            'message' => esc_html__( 'Custom action executed successfully.', 'bricks' ),
        ] );
    }
} );
```

---

# Action: bricks/dynamic_data/tags_registered

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-dynamic_data-tags_registered/

*Runs after all core dynamic data tags have been registered. This is the recommended hook for registering custom dynamic data providers or adding logic that.*

Runs after all core dynamic data tags have been registered. This is the recommended hook for registering custom dynamic data providers or adding logic that depends on registered tags.

## Parameters

None.

## Example usage

```php
add_action( 'bricks/dynamic_data/tags_registered', function() {
    // Register custom dynamic data tags or providers here
    // Example: Bricks\Integrations\Dynamic_Data\Providers::register( 'my_custom_provider', $provider_instance );
} );
```

---

# Action: bricks/filter_element/before_set_data_source_from_custom_field

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-filter_element-before_set_data_source_from_custom_field/

*Runs before setting the data source for a filter element that uses a custom field. This hook allows you to modify the filter element instance before the custom.*

Runs before setting the data source for a filter element that uses a custom field. This hook allows you to modify the filter element instance before the custom field data is processed.

## Parameters

- `$filter_element` (*Bricks\Filter_Element*): The filter element instance.

## Example usage

```php
add_action( 'bricks/filter_element/before_set_data_source_from_custom_field', function( $filter_element ) {
    // You can access $filter_element properties here, for example:
    // $settings = $filter_element->settings;
    
    // Example: modify settings before processing
    // $filter_element->settings['customFieldKey'] = 'modified_key';
} );
```

---

# Action: bricks/frontend/after_render_data

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-frontend-after_render_data/

*Runs after the Bricks\\Frontend::renderdata method has finished generating the HTML for a set of elements. This action is undocumented in the official docs but.*

Runs after the `Bricks\Frontend::render_data` method has finished generating the HTML for a set of elements. This action is undocumented in the official docs but useful for re-adding plugin actions/filters that were removed in `bricks/frontend/before_render_data` or performing cleanup.

## Parameters

- `$elements` (_array_): The array of elements that were rendered.
- `$area` (_string_): The area being rendered (e.g., 'content', 'header', 'footer').

## Example usage

```php
add_action( 'bricks/frontend/after_render_data', function( $elements, $area ) {
    // Restore actions/filters removed in before_render_data
    // add_filter( 'the_content', 'my_plugin_content_filter' );

    // Example: Log render completion
    // error_log( "Finished rendering area: $area" );
} );
```

---

# Action: bricks/frontend/before_render_data

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-frontend-before_render_data/

*Runs before the Bricks\\Frontend::renderdata method starts generating the HTML for a set of elements. This action is undocumented in the official docs but useful.*

Runs before the `Bricks\Frontend::render_data` method starts generating the HTML for a set of elements. This action is undocumented in the official docs but useful for removing plugin actions/filters that might interfere with Bricks rendering.

## Parameters

- `$elements` (*array*): The array of elements to be rendered.
- `$area` (*string*): The area being rendered (e.g., 'content', 'header', 'footer').

## Example usage

```php
add_action( 'bricks/frontend/before_render_data', function( $elements, $area ) {
    // Remove actions/filters that interfere with Bricks rendering
    // remove_filter( 'the_content', 'my_plugin_content_filter' );
    
    // Example: Log render start
    // error_log( "Starting rendering area: $area" );
} );
```

---

# Action: bricks/get_templates/query_after

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-get_templates-query_after/

*Runs after Bricks queries templates.*

Runs after Bricks performs the uncached `WP_Query` inside `Templates::get_templates_query()`. Use it to restore integration context after the internal template query has run.

This action does not run when Bricks returns the template query from object cache.

## Parameters

- `$query` (WP_Query): The template query object.
- `$merged_args` (array): The query arguments after Bricks merges custom and default values.

## Example usage

```php
add_action( 'bricks/get_templates/query_after', function( $query, $merged_args ) {
    // Restore custom query context after template lookup.
}, 10, 2 );
```

---

# Action: bricks_meta_tags

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-meta_tags/

*Runs in the document head before wp_head().*

Runs in the document head before `wp_head()`. Use it to output meta tags that should be controlled through the Bricks header template flow.

## Example usage

```php
add_action( 'bricks_meta_tags', function() {
    echo '<meta name="theme-color" content="#111111">';
} );
```

---

# Action: bricks/load_elements/after

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-after/

*Runs after Bricks loads element classes.*

Runs after Bricks loads element classes. Use it to restore integration state after element labels, controls, or classes are initialized.

## Example usage

```php
add_action( 'bricks/load_elements/after', function() {
    // Restore state after Bricks loads element classes.
} );
```

---

# Action: bricks/load_elements/before

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-before/

*Runs before Bricks loads element classes.*

Runs before Bricks loads element classes. Use it to prepare integration state before element labels, controls, or classes are initialized.

## Example usage

```php
add_action( 'bricks/load_elements/before', function() {
    // Prepare state before Bricks loads element classes.
} );
```

---

# Action: bricks_indexer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-indexer/

*Triggers the Bricks query filter indexer job runner.*

Triggers the Bricks query filter indexer job runner. Bricks schedules this action with WP-Cron every five minutes and also triggers it from the background indexing AJAX endpoint.

The core indexer callback bails when the indexer is already running, then continues pending jobs until the queue is empty or server resource limits are reached.

## Example usage

```php
add_action( 'my_plugin_run_bricks_indexer', function() {
    do_action( 'bricks_indexer' );
} );
```

---

# Action: bricks/query/query_api_response

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query-query_api_response/

*Runs after a Query API request is performed. This action allows you to inspect or process the response from the API query.*

Runs after a Query API request is performed. This action allows you to inspect or process the response from the API query.

## Parameters

- `$response` (*array|WP_Error*): The response from the API request.
- `$element_id` (*string*): The element ID associated with the query.

## Example usage

```php
add_action( 'bricks/query/query_api_response', function( $response, $element_id ) {
    if ( is_wp_error( $response ) ) {
        error_log( 'Query API Error for element ' . $element_id . ': ' . $response->get_error_message() );
        return;
    }
    
    // Process successful response
    // $data = $response;
    // Do something with $data
}, 10, 2 );
```

---

# Action: bricks/query_filters/index_post/before

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query_filters-index_post-before/

*Runs before a post is indexed for Query Filters. This action is triggered during the indexing process for a specific post.*

Runs before a post is indexed for Query Filters. This action is triggered during the indexing process for a specific post.

## Parameters

- `$post_id` (*int*): The ID of the post being indexed.

## Example usage

```php
add_action( 'bricks/query_filters/index_post/before', function( $post_id ) {
    // Perform actions before indexing a post, e.g., logging or checking conditions
    // error_log( "Starting indexing for post ID: $post_id" );
    
    // Maybe register custom dynamic data providers if needed for indexing
} );
```

---

# Action: bricks/render_popup_content/start

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_popup_content-start/

*Runs at the start of the AJAX popup content rendering process (loadpopupcontent endpoint). This action allows you to execute custom logic before the popup.*

Runs at the start of the AJAX popup content rendering process (`load_popup_content` endpoint). This action allows you to execute custom logic before the popup content is generated and returned.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., postId, popupId, etc.).

## Example usage

```php
add_action( 'bricks/render_popup_content/start', function( $request_data ) {
    // Access request data
    // $post_id = $request_data['postId'] ?? 0;
    
    // Example: Switch language for multilingual plugins (Polylang/WPML integration uses this)
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```

---

# Action: bricks/render_query_page/start

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_query_page-start/

*Runs at the start of the AJAX query page rendering process (loadquerypage endpoint - used for infinite scroll/pagination). This action allows you to execute.*

Runs at the start of the AJAX query page rendering process (`load_query_page` endpoint - used for infinite scroll/pagination). This action allows you to execute custom logic before the query page content is generated.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., queryElementId, postId, page, queryVars, etc.).

## Example usage

```php
add_action( 'bricks/render_query_page/start', function( $request_data ) {
    // Access request data
    // $page = $request_data['page'] ?? 1;
    
    // Example: Switch language for multilingual plugins
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```

---

# Action: bricks/query_filters/index_user/before

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query_filters-index_user-before/

*Runs before a user is indexed for Query Filters. This action is triggered during the indexing process for a specific user.*

Runs before a user is indexed for Query Filters. This action is triggered during the indexing process for a specific user.

## Parameters

- `$user_id` (*int*): The ID of the user being indexed.

## Example usage

```php
add_action( 'bricks/query_filters/index_user/before', function( $user_id ) {
    // Perform actions before indexing a user
    // error_log( "Starting indexing for user ID: $user_id" );
    
    // Maybe register custom dynamic data providers if needed for indexing
} );
```

---

# Action: bricks/render_query_result/start

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-render_query_result-start/

*Runs at the start of the AJAX query result rendering process (queryresult endpoint - used for filters, live search, etc.). This action allows you to execute.*

Runs at the start of the AJAX query result rendering process (`query_result` endpoint - used for filters, live search, etc.). This action allows you to execute custom logic before the query result content is generated.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., queryElementId, postId, filters, etc.).

## Example usage

```php
add_action( 'bricks/render_query_result/start', function( $request_data ) {
    // Access request data
    // $filters = $request_data['filters'] ?? [];
    
    // Example: Switch language for multilingual plugins
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```

---

# Action: bricks_sendgrid_double_opt_in_handler

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-sendgrid_double_opt_in_handler/

*Runs before the SendGrid form action adds a new contact.*

Runs before the SendGrid form action adds a new contact. Use it to trigger a custom double opt-in flow with the subscriber data Bricks collected.

## Parameters

- `$new_subscriber_data` (array): Subscriber data prepared for SendGrid, including the email address and optional first or last name.

## Example usage

```php
add_action( 'bricks_sendgrid_double_opt_in_handler', function( $new_subscriber_data ) {
    // Send a custom double opt-in email here.
}, 10, 1 );
```

---

# Action Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/actions/

*Documented Bricks action hooks for running custom code at specific points in the builder and frontend lifecycle.*

These are all documented Bricks action hooks:

---

# Action: render_footer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/render_footer/

*Runs at the footer render position. Bricks attaches its default footer renderer to this action.*

Runs in `footer.php` between `bricks_before_footer` and `bricks_after_footer`.

Bricks attaches its frontend footer renderer to this action by default. Use this hook only when you need to add low-level output at the footer render position. To modify the generated footer HTML, use the `bricks/render_footer` filter instead.

## Example usage

```php
add_action( 'render_footer', function() {
    echo '<div class="after-render-footer"></div>';
}, 20 );
```

---

# Action: render_header

Source: https://academy.bricksbuilder.io/developer/hooks/actions/render_header/

*Runs at the header render position. Bricks attaches its default header renderer to this action.*

Runs in `header.php` between `bricks_before_header` and `bricks_after_header`.

Bricks attaches its frontend header renderer to this action by default. Use this hook only when you need to add low-level output at the header render position. To modify the generated header HTML, use the `bricks/render_header` filter instead.

## Example usage

```php
add_action( 'render_header', function() {
    echo '<div class="after-render-header"></div>';
}, 20 );
```

---

# Filter: bricks/acf/filter_field_groups

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-filter_field_groups/

*Filters the ACF field groups available in the Bricks dynamic data picker. This allows you to exclude specific field groups from appearing in the builder's.*

Filters the ACF field groups available in the Bricks dynamic data picker. This allows you to exclude specific field groups from appearing in the builder's dynamic data dropdown.

## Parameters

- `$groups` (*array*): Array of ACF field groups retrieved via `acf_get_field_groups()`.

## Example usage

```php
add_filter( 'bricks/acf/filter_field_groups', function( $groups ) {
    // Loop through groups and unset the one you want to hide
    foreach ( $groups as $key => $group ) {
        // Example: Hide field group with key 'group_60f1234567890'
        if ( $group['key'] === 'group_60f1234567890' ) {
            unset( $groups[ $key ] );
        }
    }

    return $groups;
} );
```

---

# Filter: bricks/acf/google_map/address_parts

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-address_parts/

*Filters the parts of the address displayed when rendering an ACF Google Map field. You can use this to reorder or remove specific components of the address.*

Filters the parts of the address displayed when rendering an ACF Google Map field. You can use this to reorder or remove specific components of the address.

## Parameters

- `$address_parts` (*array*): Array of address part keys. Defaults: `[ 'street_name', 'street_number', 'city', 'state', 'post_code', 'country' ]`.
- `$value` (*array*): The raw value of the ACF Google Map field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/google_map/address_parts', function( $address_parts, $value, $field ) {
    // Example: Only show city and country, and change order
    return [ 'city', 'country' ];
}, 10, 3 );
```

---

# Filter: bricks/acf/google_map/text_output

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-text_output/

*Filters the final HTML output of the ACF Google Map field dynamic data. This runs after the address parts or coordinates have been formatted.*

Filters the final HTML output of the ACF Google Map field dynamic data. This runs after the address parts or coordinates have been formatted.

## Parameters

- `$output` (*string*): The rendered HTML output string.
- `$value` (*array*): The raw value of the ACF Google Map field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/google_map/text_output', function( $output, $value, $field ) {
    // Example: Strip HTML tags to get plain text
    return wp_strip_all_tags( $output );
}, 10, 3 );
```

---

# Filter: bricks/acf/google_map/show_as_address

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-show_as_address/

*Determines whether the ACF Google Map field dynamic data should be rendered as a formatted address or as latitude/longitude coordinates.*

Determines whether the ACF Google Map field dynamic data should be rendered as a formatted address or as latitude/longitude coordinates.

## Parameters

- `$show_as_address` (*bool*): Whether to render as an address. Defaults to `true` if ACF version >= 5.6.8.
- `$value` (*array*): The raw value of the ACF Google Map field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/google_map/show_as_address', function( $show_as_address, $value, $field ) {
    // Force showing latitude and longitude instead of address
    return false;
}, 10, 3 );
```

---

# Filter: bricks/acf/taxonomy/show_as_link

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-taxonomy-show_as_link/

*Determines whether the ACF Taxonomy field dynamic data output should be rendered as links to the term archives.*

Determines whether the ACF Taxonomy field dynamic data output should be rendered as links to the term archives.

## Parameters

- `$show_as_link` (*bool*): Whether to render as links. Defaults to `true`.
- `$value` (*mixed*): The raw value of the ACF Taxonomy field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/taxonomy/show_as_link', function( $show_as_link, $value, $field ) {
    // Disable links for taxonomy terms
    return false;
}, 10, 3 );
```

---

# Filter: bricks/active_templates

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-active_templates/

*Filters the array of active templates (header, footer, content, popup) that Bricks has determined should be rendered for the current page.*

Filters the array of active templates (header, footer, content, popup) that Bricks has determined should be rendered for the current page.

## Parameters

- `$active_templates` (*array*): Array of active template IDs, keyed by template type (e.g., `header`, `footer`, `content`, `popup`).
- `$post_id` (*int*): The current post ID being rendered.
- `$content_type` (*string*): The type of content being rendered (e.g., `content`, `archive`, `search`, `error`).

## Example usage

```php
add_filter( 'bricks/active_templates', function( $active_templates, $post_id, $content_type ) {
    // Example: Use a specific header template (ID: 1234) for single posts
    if ( is_single() ) {
        $active_templates['header'] = 1234;
    }

    return $active_templates;
}, 10, 3 );
```

---

# Filter: bricks/ajax/get_pages_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-ajax-get_pages_args/

*Filters the query arguments used when searching for pages or posts within the Bricks builder (e.g., in link controls or populate content settings).*

Filters the query arguments used when searching for pages or posts within the Bricks builder (e.g., in link controls or populate content settings).

## Parameters

- `$query_args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/ajax/get_pages_args', function( $query_args ) {
    // Example: Exclude specific post IDs from the search results
    $query_args['post__not_in'] = [ 12, 34, 56 ];

    return $query_args;
} );
```

---

# Filter: bricks/api/get_templates_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-api-get_templates_data/

*Filters the data returned by the Bricks REST API endpoint /get-templates-data/. This endpoint is used to retrieve templates, authors, bundles, tags, and other.*

Filters the data returned by the Bricks REST API endpoint `/get-templates-data/`. This endpoint is used to retrieve templates, authors, bundles, tags, and other assets for the template library.

## Parameters

- `$templates_data` (*array*): Array containing:
    - `templates` (*array*): List of template data.
    - `authors` (*array*): List of template authors.
    - `bundles` (*array*): List of template bundles.
    - `tags` (*array*): List of template tags.
    - `globalVariables` (*array*): Global variables.
    - `colorPalette` (*array*): Color palettes.
    - `timestamp` (*int*): Current timestamp.
    - `date` (*string*): Formatted date.
    - `get` (*array*): URL parameters from the request.

## Example usage

```php
add_filter( 'bricks/api/get_templates_data', function( $templates_data ) {
    // Example: Remove a specific template bundle by name
    if ( ! empty( $templates_data['bundles'] ) ) {
        foreach ( $templates_data['bundles'] as $key => $bundle ) {
            if ( $bundle === 'Deprecated Bundle' ) {
                unset( $templates_data['bundles'][ $key ] );
            }
        }
    }

    return $templates_data;
} );
```

---

# Filter: bricks/breadcrumbs/home_label

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-home_label/

*Filters the label text used for the \"Home\" link in the Breadcrumbs element.*

Filters the label text used for the "Home" link in the Breadcrumbs element.

## Parameters

- `$home_label` (*string*): The home label text (may include HTML if an icon is used).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/home_label', function( $home_label ) {
    return 'Start';
} );
```

---

# Filter: bricks/allowed_html_tags

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-allowed_html_tags/

*Filters the list of allowed HTML tags that can be used when selecting a \"Custom\" HTML tag in element settings. This ensures that custom tags are sanitized.*

Filters the list of allowed HTML tags that can be used when selecting a "Custom" HTML tag in element settings. This ensures that custom tags are sanitized correctly.

## Parameters

- `$allowed_html_tags` (*array*): Array of allowed HTML tag names.

## Example usage

```php
add_filter( 'bricks/allowed_html_tags', function( $allowed_html_tags ) {
    // Add 'marquee' to the list of allowed tags
    $allowed_html_tags[] = 'marquee';

    return $allowed_html_tags;
} );
```

---

# Filter: bricks/breadcrumbs/items

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-items/

*Filters the array of breadcrumb items (HTML strings) before they are rendered in the Breadcrumbs element. This allows you to add, remove, or modify specific.*

Filters the array of breadcrumb items (HTML strings) before they are rendered in the Breadcrumbs element. This allows you to add, remove, or modify specific breadcrumb links.

## Parameters

- `$breadcrumb_items` (*array*): Array of HTML strings, where each string represents a breadcrumb item (e.g., a link or current page span).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/items', function( $breadcrumb_items ) {
    // Example: Add a custom item after the Home link (assuming Home is the first item)
    $custom_item = '<a href="https://academy.bricksbuilder.io/custom-link/">Custom Link</a>';
    array_splice( $breadcrumb_items, 1, 0, $custom_item );

    return $breadcrumb_items;
} );
```

---

# Filter: bricks/breadcrumbs/separator

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-separator/

*Filters the separator HTML displayed between items in the Breadcrumbs element.*

Filters the separator HTML displayed between items in the Breadcrumbs element.

## Parameters

- `$separator` (*string*): The HTML string for the breadcrumb separator (e.g., a span containing text or an icon).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/separator', function( $separator ) {
    // Change separator to a custom character
    return '<span class="bricks-breadcrumbs-separator"> &raquo; </span>';
} );
```

---

# Filter: bricks/builder/current_page_type

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-current_page_type/

*Filters the detected current page type stored in Database::$pagedata['currentpagetype']. This value is used by Bricks to determine the context for dynamic data.*

Filters the detected current page type stored in `Database::$page_data['current_page_type']`. This value is used by Bricks to determine the context for dynamic data and other logic.

## Parameters

- `$page_type` (*string*): The detected page type (e.g., `post`, `archive`, `search`, `author`, `404`, `term`, `user`).

## Example usage

```php
add_filter( 'bricks/builder/current_page_type', function( $page_type ) {
    // Example: Treat a custom endpoint as an archive
    if ( get_query_var( 'my_custom_archive' ) ) {
        return 'archive';
    }

    return $page_type;
} );
```

---

# Filter: bricks/builder/data_post_id

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-data_post_id/

*Filters the post ID used by Bricks to retrieve page data (header, content, footer). This allows you to programmatically change the source of the Bricks data for.*

Filters the post ID used by Bricks to retrieve page data (header, content, footer). This allows you to programmatically change the source of the Bricks data for the current page request.

## Parameters

- `$post_id` (*int*): The current post ID.

## Example usage

```php
add_filter( 'bricks/builder/data_post_id', function( $post_id ) {
    // Example: Use a specific post ID for a custom route
    if ( get_query_var( 'my_custom_route' ) ) {
        return 123; // ID of the post/template to use
    }

    return $post_id;
} );
```

---

# Filter: bricks/builder/dynamic_wrapper

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-dynamic_wrapper/

*Filters the dynamic wrappers available in the Bricks builder. Dynamic wrappers are used to inject content before or after specific hooks in the builder canvas.*

Filters the dynamic wrappers available in the Bricks builder. Dynamic wrappers are used to inject content before or after specific hooks in the builder canvas (e.g., WooCommerce hooks).

## Parameters

- `$dynamic_wrapper` (*array*): Array of dynamic wrappers.

## Example usage

```php
add_filter( 'bricks/builder/dynamic_wrapper', function( $dynamic_wrapper ) {
    // Add a custom dynamic wrapper
    $dynamic_wrapper[] = [
        'name' => 'my_custom_wrapper',
        'title' => esc_html__( 'My Custom Wrapper', 'my-plugin' ),
        'hooks' => [
            'before' => 'my_custom_action_before',
            'after'  => 'my_custom_action_after',
        ],
    ];

    return $dynamic_wrapper;
} );
```

---

# Filter: bricks/builder/first_element_category

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-first_element_category/

*Filters the default expanded element category in the Bricks builder panel. This allows you to prioritize specific element categories based on the post type or.*

Filters the default expanded element category in the Bricks builder panel. This allows you to prioritize specific element categories based on the post type or ID being edited.

## Parameters

- `$category` (*string|bool*): The category name to expand by default (e.g., `layout`, `basic`, `single`). Default is `false`.
- `$post_id` (*int*): The ID of the post being edited.
- `$post_type` (*string*): The post type of the post being edited.

## Example usage

```php
add_filter( 'bricks/builder/first_element_category', function( $category, $post_id, $post_type ) {
    // Example: Expand 'woocommerce' category for product templates
    if ( $post_type === 'product' ) {
        return 'woocommerce';
    }

    return $category;
}, 10, 3 );
```

---

# Filter: bricks/builder/post_title

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-post_title/

*Filters the post title displayed in the Bricks builder interface (e.g., in search results, dropdowns, and lists).*

Filters the post title displayed in the Bricks builder interface (e.g., in search results, dropdowns, and lists).

## Parameters

- `$title` (*string*): The post title.
- `$post_id` (*int*): The ID of the post.

## Example usage

```php
add_filter( 'bricks/builder/post_title', function( $title, $post_id ) {
    // Example: Append the post ID to the title
    return $title . ' (ID: ' . $post_id . ')';
}, 10, 2 );
```

---

# Filter: bricks/builder/state_group_definitions

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-state_group_definitions/

*Filters builder state group definitions used for WooCommerce modular element preview states.*

Filters the builder state group definitions returned by `Woocommerce::get_builder_state_group_definitions()`.

Bricks sends these definitions to the builder as `stateGroupDefinitions`. The default definitions are currently for WooCommerce modular element states such as cart, checkout, and account page preview states.

## Parameters

- `$definitions` (array): State group definitions keyed by element name.

## Example usage

```php
add_filter( 'bricks/builder/state_group_definitions', function( $definitions ) {
    $definitions['my-group'] = [
        'label'  => 'My group',
        'states' => [],
    ];

    return $definitions;
} );
```

---

# Filter: bricks/builder/term_name

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-term_name/

*Filters the term name displayed in the Bricks builder interface (e.g., in taxonomy pickers).*

Filters the term name displayed in the Bricks builder interface (e.g., in taxonomy pickers).

## Parameters

- `$term_name` (*string*): The formatted term name (e.g., `Term Name (Taxonomy Label)`).
- `$term_id` (*int|string*): The ID of the term.
- `$taxonomy` (*string*): The slug of the taxonomy.

## Example usage

```php
add_filter( 'bricks/builder/term_name', function( $term_name, $term_id, $taxonomy ) {
    // Example: Add the term ID to the name
    return $term_name . ' [ID: ' . $term_id . ']';
}, 10, 3 );
```

---

# Filter: bricks/builder/supported_post_types

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-supported_post_types/

*Filters the list of post types that are enabled for editing with Bricks. This checks whether the builder should load for the current post type.*

Filters the list of post types that are enabled for editing with Bricks. This checks whether the builder should load for the current post type.

## Parameters

- `$supported_post_types` (*array*): Array of supported post type slugs (e.g., `['page', 'post', 'my_cpt']`).
- `$current_post_type` (*string*): The post type of the post being accessed.

## Example usage

```php
add_filter( 'bricks/builder/supported_post_types', function( $supported_post_types, $current_post_type ) {
    // Example: Always allow 'my_custom_post_type' to be edited with Bricks
    if ( $current_post_type === 'my_custom_post_type' && ! in_array( 'my_custom_post_type', $supported_post_types ) ) {
        $supported_post_types[] = 'my_custom_post_type';
    }

    return $supported_post_types;
}, 10, 2 );
```

---

# Filter: bricks/code/echo_everywhere

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-code-echo_everywhere/

*Determines whether the {echo:} dynamic data tag should be parsed recursively if it appears within the output of another dynamic data tag. By default, this is.*

Determines whether the `{echo:}` dynamic data tag should be parsed recursively if it appears within the output of another dynamic data tag. By default, this is disabled for security and performance reasons.

## Parameters

- `$echo_everywhere` (*bool*): Whether to allow recursive parsing of `{echo:}` tags. Default is `false`.

## Example usage

```php
add_filter( 'bricks/code/echo_everywhere', function( $echo_everywhere ) {
    // Enable recursive parsing of {echo:} tags
    // WARNING: Use with caution as this may lead to infinite loops or security vulnerabilities
    return true;
} );
```

---

# Filter: bricks/cmb2/checkbox_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-cmb2-checkbox_value/

*Filters the output value of a CMB2 checkbox field when rendered via Bricks dynamic data. By default, Bricks converts 'on' to \"Yes\" and other values to \"No\".*

Filters the output value of a CMB2 checkbox field when rendered via Bricks dynamic data. By default, Bricks converts 'on' to "Yes" and other values to "No".

## Parameters

- `$value` (*string*): The processed value (e.g., "Yes" or "No").
- `$original_value` (*string*): The raw value from the database (e.g., 'on').
- `$field` (*array*): The CMB2 field settings array.
- `$post` (*WP_Post*): The current post object.

## Example usage

```php
add_filter( 'bricks/cmb2/checkbox_value', function( $value, $original_value, $field, $post ) {
    // Example: Return "True" or "False" instead of "Yes" or "No"
    return $original_value === 'on' ? 'True' : 'False';
}, 10, 4 );
```

---

# Filter: bricks/combined_search/post_ids

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-post_ids/

*Filters the list of post IDs returned by the combined search logic (used in AJAX search filters). This allows you to include or exclude posts from the search.*

Filters the list of post IDs returned by the combined search logic (used in AJAX search filters). This allows you to include or exclude posts from the search results after the initial search query has run.

## Parameters

- `$post_ids` (*array*): Array of found post IDs.
- `$search_fields` (*array*): Array of post fields being searched (e.g., `['title', 'content', 'excerpt']`).
- `$meta_fields` (*array*): Array of meta keys being searched.
- `$search_term` (*string*): The search term entered by the user.
- `$filter_id` (*string*): The ID of the filter element initiating the search.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/combined_search/post_ids', function( $post_ids, $search_fields, $meta_fields, $search_term, $filter_id, $query_id ) {
    // Example: Always include a specific sticky post in search results
    $sticky_post_id = 123;
    if ( ! in_array( $sticky_post_id, $post_ids ) ) {
        $post_ids[] = $sticky_post_id;
    }

    return $post_ids;
}, 10, 6 );
```

---

# Filter: bricks/combined_search/term_ids

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-term_ids/

*Filters the list of term IDs returned by the combined search logic (used in AJAX search filters targeting terms). This allows you to include or exclude terms.*

Filters the list of term IDs returned by the combined search logic (used in AJAX search filters targeting terms). This allows you to include or exclude terms from the search results after the initial search query has run.

## Parameters

- `$term_ids` (*array*): Array of found term IDs.
- `$term_fields` (*array*): Array of term fields being searched (e.g., `['name', 'slug']`).
- `$meta_fields` (*array*): Array of meta keys being searched.
- `$search_term` (*string*): The search term entered by the user.
- `$filter_id` (*string*): The ID of the filter element initiating the search.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/combined_search/term_ids', function( $term_ids, $term_fields, $meta_fields, $search_term, $filter_id, $query_id ) {
    // Example: Exclude 'uncategorized' term (ID: 1) from search results
    if ( ( $key = array_search( 1, $term_ids ) ) !== false ) {
        unset( $term_ids[ $key ] );
    }

    return $term_ids;
}, 10, 6 );
```

---

# Filter: bricks/combined_search/user_ids

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-user_ids/

*Filters the list of user IDs returned by the combined search logic (used in AJAX search filters targeting users). This allows you to include or exclude users.*

Filters the list of user IDs returned by the combined search logic (used in AJAX search filters targeting users). This allows you to include or exclude users from the search results after the initial search query has run.

## Parameters

- `$user_ids` (*array*): Array of found user IDs.
- `$user_fields` (*array*): Array of user fields being searched (e.g., `['display_name', 'user_email']`).
- `$meta_fields` (*array*): Array of meta keys being searched.
- `$search_term` (*string*): The search term entered by the user.
- `$filter_id` (*string*): The ID of the filter element initiating the search.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/combined_search/user_ids', function( $user_ids, $user_fields, $meta_fields, $search_term, $filter_id, $query_id ) {
    // Example: Exclude administrator (ID: 1) from search results
    if ( ( $key = array_search( 1, $user_ids ) ) !== false ) {
        unset( $user_ids[ $key ] );
    }

    return $user_ids;
}, 10, 6 );
```

---

# Filter: bricks/comments/author_tag

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-comments-author_tag/

*Filters the HTML tag used to wrap the comment author's name in the comments list.*

Filters the HTML tag used to wrap the comment author's name in the comments list.

## Parameters

- `$tag` (*string*): The HTML tag name. Defaults to `h5`.

## Example usage

```php
add_filter( 'bricks/comments/author_tag', function( $tag ) {
    // Change author name tag to 'span'
    return 'span';
} );
```

---

# Filter: bricks/conditions/options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-options/

*Filters the condition options available in the element conditions interface. This allows you to add custom conditions that users can select to control element.*

Filters the condition options available in the element conditions interface. This allows you to add custom conditions that users can select to control element visibility.

## Parameters

- `$options` (*array*): Array of condition options. Each option defines the condition key, label, group, comparison operators, and value input type.

## Example usage

```php
add_filter( 'bricks/conditions/options', function( $options ) {
    // Add a custom 'Is Weekend' condition
    $options[] = [
        'key'     => 'is_weekend',
        'group'   => 'other', // Or a custom group created via bricks/conditions/groups
        'label'   => esc_html__( 'Is Weekend', 'my-plugin' ),
        'compare' => [
            'type'        => 'select',
            'options'     => [
                '==' => esc_html__( 'is', 'bricks' ),
            ],
        ],
        'value'   => [
            'type'    => 'select',
            'options' => [
                'true'  => esc_html__( 'True', 'bricks' ),
                'false' => esc_html__( 'False', 'bricks' ),
            ],
        ],
    ];

    return $options;
} );
```

---

# Filter: bricks/conditions/groups

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-groups/

*Filters the condition groups available in the element conditions interface. This allows you to add new categories for your custom conditions.*

Filters the condition groups available in the element conditions interface. This allows you to add new categories for your custom conditions.

## Parameters

- `$groups` (*array*): Array of condition groups. Each group has a `name` and `label`.

## Example usage

```php
add_filter( 'bricks/conditions/groups', function( $groups ) {
    // Add a custom condition group
    $groups[] = [
        'name'  => 'my_custom_group',
        'label' => esc_html__( 'My Custom Group', 'my-plugin' ),
    ];

    return $groups;
} );
```

---

# Filter: bricks/content_analysis/full_post_content_id

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-content_analysis-full_post_content_id/

*Filters the post ID Bricks treats as the full-content target during content analysis.*

Filters the post ID Bricks treats as the full-content target during content analysis. Return a post ID to let Bricks remove the More block only for that target post.

## Parameters

- `$post_id` (int): The content analysis target post ID. Defaults to 0.

## Example usage

```php
add_filter( 'bricks/content_analysis/full_post_content_id', function( $post_id ) {
    return defined( 'MY_CONTENT_ANALYSIS_POST_ID' ) ? MY_CONTENT_ANALYSIS_POST_ID : $post_id;
} );
```

---

# Filter: bricks/conditions/result

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-conditions-result/

*Filters the boolean result of a condition check. This filter is used to implement the logic for custom conditions or to override existing condition logic.*

Filters the boolean result of a condition check. This filter is used to implement the logic for custom conditions or to override existing condition logic.

## Parameters

- `$result` (*bool*): The result of the condition evaluation.
- `$condition_key` (*string*): The key of the condition being evaluated (e.g., `user_role`, `my_custom_condition`).
- `$condition` (*array*): The condition settings (contains `compare`, `value`, etc.).

## Example usage

```php
add_filter( 'bricks/conditions/result', function( $result, $condition_key, $condition ) {
    // Logic for custom 'is_weekend' condition
    if ( $condition_key === 'is_weekend' ) {
        $is_weekend = ( date( 'N' ) >= 6 );
        $value      = isset( $condition['value'] ) ? $condition['value'] : 'true';

        // Check if condition value matches current state
        if ( $value === 'true' ) {
            return $is_weekend;
        } else {
            return ! $is_weekend;
        }
    }

    return $result;
}, 10, 3 );
```

---

# Filter: bricks/custom_fonts/mime_types

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-custom_fonts-mime_types/

*Filters the list of allowed MIME types for custom font uploads in the Bricks Custom Fonts manager.*

Filters the list of allowed MIME types for custom font uploads in the Bricks Custom Fonts manager.

## Parameters

- `$mime_types` (*array*): Array of file extensions and their corresponding MIME types (e.g., `['woff2' => 'font/woff2']`).

## Example usage

```php
add_filter( 'bricks/custom_fonts/mime_types', function( $mime_types ) {
    // Add support for OTF fonts
    $mime_types['otf'] = 'font/otf';

    return $mime_types;
} );
```

---

# Filter: bricks/database/bricks_get_all_templates_by_type_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-bricks_get_all_templates_by_type_args/

*Filters the query arguments used to retrieve all Bricks templates. This is primarily used by multilingual plugins (like WPML and Polylang) to ensure only.*

Filters the query arguments used to retrieve all Bricks templates. This is primarily used by multilingual plugins (like WPML and Polylang) to ensure only templates in the current language are fetched.

## Parameters

- `$args` (*array*): Array of arguments passed to `get_posts()`.

## Example usage

```php
add_filter( 'bricks/database/bricks_get_all_templates_by_type_args', function( $args ) {
    // Example: Include private templates
    $args['post_status'] = [ 'publish', 'private' ];

    return $args;
} );
```

---

# Filter: bricks/database/content_type

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-content_type/

*Filters the content type determined by Bricks for the current page request. This affects which template conditions are checked (e.g., whether to look for a.*

Filters the content type determined by Bricks for the current page request. This affects which template conditions are checked (e.g., whether to look for a single template, archive template, or search results template).

## Parameters

- `$content_type` (*string*): The detected content type (e.g., `content`, `archive`, `search`, `error`, `header`, `footer`).
- `$post_id` (*int*): The current post ID.

## Example usage

```php
add_filter( 'bricks/database/content_type', function( $content_type, $post_id ) {
    // Example: Treat a specific page as a search results page
    if ( is_page( 'advanced-search' ) ) {
        return 'search';
    }

    return $content_type;
}, 10, 2 );
```

---

# Filter: bricks/database/get_all_templates_cache_key

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-get_all_templates_cache_key/

*Filters the cache key used to store and retrieve the list of all Bricks templates. This allows plugins to create unique cache entries based on context (e.g.,.*

Filters the cache key used to store and retrieve the list of all Bricks templates. This allows plugins to create unique cache entries based on context (e.g., current language).

## Parameters

- `$cache_key` (*string*): The default cache key (e.g., `all_templates_{timestamp}`).

## Example usage

```php
add_filter( 'bricks/database/get_all_templates_cache_key', function( $cache_key ) {
    // Example: Append current language code to cache key
    if ( defined( 'ICL_LANGUAGE_CODE' ) ) {
        $cache_key .= '_' . ICL_LANGUAGE_CODE;
    }

    return $cache_key;
} );
```

---

# Filter: bricks/dynamic_data/do_action_context

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-do_action_context/

*Filters the action context used by the dynamic data do_action tag.*

Filters the action context used when Bricks resolves a dynamic data `{do_action}` tag. Use it to change the action name, pass arguments, or skip execution.

## Parameters

- `$action_context` (array): Action context with action, args, requested_action, and skip keys.
- `$filters` (array): Dynamic data filters parsed from the tag.
- `$context` (string): The dynamic data render context.
- `$post` (WP_Post|int|null): The current post context.

## Example usage

```php
add_filter( 'bricks/dynamic_data/do_action_context', function( $action_context, $filters, $context, $post ) {
    if ( $action_context['requested_action'] === 'my_public_alias' ) {
        $action_context['action'] = 'my_private_action';
        $action_context['args']   = [ get_the_ID() ];
    }

    return $action_context;
}, 10, 4 );
```

---

# Filter: bricks/dynamic_data/allowed_keys

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-allowed_keys/

*Filter which argument keys Bricks accepts inside dynamic data tags, so you can support custom modifiers and parsing behavior.*

Filters the allowed argument keys (modifiers) that can be parsed in dynamic data tags (e.g., `{post_title:my_key}`). This allows you to introduce custom arguments for your dynamic tags.

## Parameters

- `$allowed_keys` (*array*): Array of allowed argument keys. Defaults include `fallback`, `fallback-image`, `sanitize`, `exclude`, `start-at`, `pad`, `key`, `is-array`, `date`, `from`, `to`.

## Example usage

```php
add_filter( 'bricks/dynamic_data/allowed_keys', function( $allowed_keys ) {
    // Add 'limit' as an allowed argument key
    $allowed_keys[] = 'limit';

    return $allowed_keys;
} );
```

---

# Filter: bricks/dynamic_data/author_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-author_value/

*Filters the value returned by {author...} dynamic data tags (e.g., {authorname}, {authoremail}).*

Filters the value returned by `{author_...}` dynamic data tags (e.g., `{author_name}`, `{author_email}`).

## Parameters

- `$value` (*string*): The value of the author field.
- `$field_type` (*string*): The specific author field being retrieved (e.g., `name`, `email`, `bio`, `website`, `avatar`).
- `$filters` (*array*): Array of modifiers applied to the tag (e.g., `['fallback' => '...']`).

## Example usage

```php
add_filter( 'bricks/dynamic_data/author_value', function( $value, $field_type, $filters ) {
    // Example: Append text to author bio
    if ( $field_type === 'bio' ) {
        return $value . ' [Verified Author]';
    }

    return $value;
}, 10, 3 );
```

---

# Filter: bricks/dynamic_data/register_hook

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_hook/

*Filters the WordPress action hook used to register Bricks dynamic data providers and tags.*

Filters the WordPress action hook used to register Bricks dynamic data providers and tags.

## Parameters

- `$hook` (*string*): The action hook name. Defaults to `init`.

## Example usage

```php
add_filter( 'bricks/dynamic_data/register_hook', function( $hook ) {
    // Register dynamic data on 'wp_loaded' instead of 'init'
    return 'wp_loaded';
} );
```

---

# Filter: bricks/dynamic_data/format_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-format_value/

*Filters the final processed value of any dynamic data tag before it is rendered. This is a powerful filter that runs for every dynamic tag, allowing you to.*

Filters the final processed value of any dynamic data tag before it is rendered. This is a powerful filter that runs for every dynamic tag, allowing you to globally modify outputs based on context or tag name.

## Parameters

- `$value` (*mixed*): The processed value of the dynamic tag.
- `$tag` (*string*): The dynamic data tag (e.g., `post_title`, `my_custom_tag`).
- `$post_id` (*int*): The ID of the post context.
- `$filters` (*array*): Array of modifiers/arguments applied to the tag (e.g., `['fallback' => '...']`).
- `$context` (*string*): The context where the tag is being rendered (e.g., `text`, `link`, `image`, `video`, `object`, `media`).

## Example usage

```php
add_filter( 'bricks/dynamic_data/format_value', function( $value, $tag, $post_id, $filters, $context ) {
    // Example: Add a suffix to the post title when used in text context
    if ( $tag === 'post_title' && $context === 'text' ) {
        return $value . ' | My Site';
    }

    return $value;
}, 10, 5 );
```

---

# Filter: bricks/dynamic_data/meta_value/{meta_key}

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-meta_value-meta_key/

*Filter the value returned for a specific custom-field key when Bricks resolves dynamic data from post meta.*

Filters the value of a specific post meta key when retrieved via dynamic data (e.g., `{cf_my_key}`). The `{$meta_key}` portion of the hook name should be replaced with your actual meta key.

## Parameters

- `$value` (*mixed*): The value of the custom field.
- `$post` (*WP_Post*): The post object.

## Example usage

```php
// Filter the value of the custom field with key 'my_price_field'
add_filter( 'bricks/dynamic_data/meta_value/my_price_field', function( $value, $post ) {
    // Example: Format the price
    return '$' . number_format( (float) $value, 2 );
}, 10, 2 );
```

---

# Filter: bricks/dynamic_data/register_providers

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_providers/

*Filters the dynamic data providers registered by Bricks.*

Filters the dynamic data providers registered by Bricks. Use it to add, remove, or reorder provider keys before Bricks registers them.

## Parameters

- `$providers` (array): Provider keys such as cmb2, wp, woo, acf, pods, metabox, toolset, and jetengine.

## Example usage

```php
add_filter( 'bricks/dynamic_data/register_providers', function( $providers ) {
    $providers[] = 'my_provider';

    return $providers;
} );
```

---

# Filter: bricks/dynamic_data/render_content

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-render_content/

*Filter the content string that Bricks parses for dynamic data tags before those tags are resolved into output values.*

Filters the content passed through Bricks' dynamic data parser. Bricks attaches its own parser callback to this filter, so calling `apply_filters( 'bricks/dynamic_data/render_content', ... )` resolves dynamic tags such as `{post_title}` into their output values.

Use `add_filter()` on this hook when you need to adjust content before or after Bricks resolves dynamic data. Use `apply_filters()` when you need to parse a custom string through the same dynamic data pipeline.

## Parameters

- `$content` (*string*): The content string containing dynamic tags.
- `$post` (*WP_Post*): The post context.
- `$context` (*string*): The context where the content is used (e.g., `text`).

## Example usage

```php
$content = 'Hello {post_title}';
$post_id = 123;
$post    = get_post( $post_id );

// Manually parse dynamic data in a string
$parsed_content = apply_filters( 'bricks/dynamic_data/render_content', $content, $post, 'text' );

// Output: Hello My Post Title
echo $parsed_content;
```

---

# Filter: bricks/dynamic_data/render_tag

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-render_tag/

*Filters the logic to resolve a single dynamic data tag to its value. This filter is called for each individual tag found in the content.*

Filters the logic to resolve a single dynamic data tag to its value. This filter is called for each individual tag found in the content.

## Parameters

- `$tag` (*string*): The dynamic data tag string (without curly braces, e.g., `post_title:fallback`).
- `$post` (*WP_Post*): The post context.
- `$context` (*string*): The context where the tag is being rendered.

## Example usage

```php
add_filter( 'bricks/dynamic_data/render_tag', function( $tag, $post, $context ) {
    // Implement a custom tag '{my_custom_tag}'
    if ( $tag === 'my_custom_tag' ) {
        return 'My Custom Value';
    }

    return $tag; // Return original tag to let other providers handle it
}, 10, 3 );
```

---

# Filter: bricks/dynamic_data/text_separator

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-text_separator/

*Filters the separator used when joining array values in a dynamic data tag (text context). The default separator is a comma and a space (, ).*

Filters the separator used when joining array values in a dynamic data tag (text context). The default separator is a comma and a space (`, `).

## Parameters

- `$sep` (*string*): The separator string.
- `$tag` (*string*): The dynamic data tag.
- `$post_id` (*int*): The ID of the post context.
- `$filters` (*array*): Array of modifiers applied to the tag.

## Example usage

```php
add_filter( 'bricks/dynamic_data/text_separator', function( $sep, $tag, $post_id, $filters ) {
    // Example: Use a line break separator for a specific custom field
    if ( $tag === 'my_repeater_field' ) {
        return '<br>';
    }

    return $sep;
}, 10, 4 );
```

---

# Filter: bricks/dynamic_data/user_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-user_value/

*Filters the value returned by {wpuser...} dynamic data tags (e.g., {wpuseremail}, {wpuserrole}).*

Filters the value returned by `{wp_user_...}` dynamic data tags (e.g., `{wp_user_email}`, `{wp_user_role}`).

## Parameters

- `$value` (*mixed*): The value of the user field.
- `$field_type` (*string*): The specific user field being retrieved (e.g., `email`, `login`, `first_name`, `last_name`, `bio`, `picture`, `role`, `registered_date`).
- `$filters` (*array*): Array of modifiers applied to the tag.

## Example usage

```php
add_filter( 'bricks/dynamic_data/user_value', function( $value, $field_type, $filters ) {
    // Example: Capitalize the user role
    if ( $field_type === 'role' && is_string( $value ) ) {
        return ucfirst( $value );
    }

    return $value;
}, 10, 3 );
```

---

# Filter: bricks/element/builder_setup_query

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-builder_setup_query/

*Filters the query arguments used to set up the preview context in the builder (e.g., when \"Populate Content\" is active).*

Filters the query arguments used to set up the preview context in the builder (e.g., when "Populate Content" is active).

## Parameters

- `$query_args` (*array*): Array of arguments passed to `WP_Query`.
- `$post_id` (*int*): The ID of the template being edited.

## Example usage

```php
add_filter( 'bricks/element/builder_setup_query', function( $query_args, $post_id ) {
    // Example: If editing a specific template, force a specific post for preview
    if ( $post_id === 123 ) {
        $query_args['p'] = 456;
        $query_args['post_type'] = 'post';
    }

    return $query_args;
}, 10, 2 );
```

---

# Filter: bricks/dynamic_tags_list

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_tags_list/

*Filters the list of dynamic data tags available in the builder's dynamic data picker. This allows you to register your custom dynamic tags so they appear in the.*

Filters the list of dynamic data tags available in the builder's dynamic data picker. This allows you to register your custom dynamic tags so they appear in the UI.

## Parameters

- `$tags` (*array*): Array of dynamic data tag definitions.

## Example usage

```php
add_filter( 'bricks/dynamic_tags_list', function( $tags ) {
    $tags[] = [
        'name'  => '{my_custom_tag}',
        'label' => esc_html__( 'My Custom Tag', 'my-plugin' ),
        'group' => 'My Plugin Group',
    ];

    return $tags;
} );
```

---

# Filter: bricks/element/form/datepicker_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-form-datepicker_options/

*Filters the Flatpickr options for the datepicker field in the Form element. This allows you to customize the behavior of the date picker (e.g., disable specific.*

Filters the Flatpickr options for the datepicker field in the Form element. This allows you to customize the behavior of the date picker (e.g., disable specific dates, change the date format, set min/max dates).

## Parameters

- `$datepicker_options` (*array*): Array of Flatpickr options.
- `$element` (*object*): The Form element instance.

## Example usage

```php
add_filter( 'bricks/element/form/datepicker_options', function( $datepicker_options, $element ) {
    // Example: Disable weekends (Saturday and Sunday)
    $datepicker_options['disable'] = [
        function( $date ) {
            // Return true to disable
            return ( $date->format( 'N' ) >= 6 );
        }
    ];

    // Example: Set minDate to today
    $datepicker_options['minDate'] = 'today';

    return $datepicker_options;
}, 10, 2 );
```

---

# Filter: bricks/element/maybe_set_aria_current_page

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-maybe_set_aria_current_page/

*Filters the boolean value that determines whether to add the aria-current=\"page\" attribute to a link element. This is used to indicate that a link points to the.*

Filters the boolean value that determines whether to add the `aria-current="page"` attribute to a link element. This is used to indicate that a link points to the currently active page.

## Parameters

- `$set_aria_current` (*bool*): Whether the link matches the current page.
- `$url` (*string*): The URL of the link being checked.

## Example usage

```php
add_filter( 'bricks/element/maybe_set_aria_current_page', function( $set_aria_current, $url ) {
    // Example: Consider a link active if it matches a specific query parameter
    if ( isset( $_GET['section'] ) && strpos( $url, 'section=' . $_GET['section'] ) !== false ) {
        return true;
    }

    return $set_aria_current;
}, 10, 2 );
```

---

# Filter: bricks/element/form/honeypot/result

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-form-honeypot-result/

*Filters the result returned when a honeypot field is triggered (spam detection). This allows you to customize the error message shown to potential bots (or.*

Filters the result returned when a honeypot field is triggered (spam detection). This allows you to customize the error message shown to potential bots (or users who accidentally filled the hidden field).

## Parameters

- `$result` (*array*): The result array, typically containing `['type' => 'error', 'message' => '...']`.
- `$field_id` (*string*): The ID of the honeypot field that was filled.
- `$form` (*object*): The Form integration object.

## Example usage

```php
add_filter( 'bricks/element/form/honeypot/result', function( $result, $field_id, $form ) {
    // Customize the error message
    $result['message'] = esc_html__( 'Spam detected. Please do not fill out the hidden fields.', 'my-domain' );

    return $result;
}, 10, 3 );
```

---

# Filter: bricks/elements/{element_name}/scripts

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-element_name-scripts/

*Filters the script handles registered for a specific element. Replace {element_name} with the element name.*

Filters the list of script handles to be loaded for a specific element. The `{$element_name}` portion of the hook name should be replaced with the element's name (e.g., `slider`, `accordion`, `my_custom_element`).

## Parameters

- `$scripts` (*array*): Array of script handles registered via `wp_register_script`.

## Example usage

```php
// Filter scripts for the 'slider' element
add_filter( 'bricks/elements/slider/scripts', function( $scripts ) {
    // Add a custom script dependency
    $scripts[] = 'my-custom-slider-script';

    return $scripts;
} );
```

---

# Filter: bricks/elements/nav_menu/menus

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-menus/

*Filters the nav menus shown in the Nav Menu element while in the builder.*

Filters the nav menus shown in the Nav Menu element while in the builder. Return an array of menu objects to override the menus Bricks loads from WordPress.

## Parameters

- `$menus` (array|null): Menus to use in the builder. Return null to let Bricks fall back to wp_get_nav_menus().

## Example usage

```php
add_filter( 'bricks/elements/nav_menu/menus', function( $menus ) {
    return wp_get_nav_menus();
} );
```

---

# Filter: bricks/elements/nav_menu/name

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-name/

*Filters a nav menu label shown in the Nav Menu element.*

Filters a nav menu label shown in the Nav Menu element. Use it to adjust menu names in the builder, for example by appending language or site context.

## Parameters

- `$name` (string): The menu name.
- `$menu` (WP_Term): The nav menu term object.

## Example usage

```php
add_filter( 'bricks/elements/nav_menu/name', function( $name, $menu ) {
    return $name . ' (' . $menu->term_id . ')';
}, 10, 2 );
```

---

# Filter: bricks/export_template_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-export_template_args/

*Filters the URL arguments used for the \"Export Template\" link in the Bricks templates list table.*

Filters the URL arguments used for the "Export Template" link in the Bricks templates list table.

## Parameters

- `$args` (*array*): Array of query arguments for the export URL (e.g., `action`, `nonce`, `templateId`).
- `$post_id` (*int*): The ID of the template being exported.

## Example usage

```php
add_filter( 'bricks/export_template_args', function( $args, $post_id ) {
    // Example: Add a custom parameter to the export URL
    $args['my_param'] = 'value';

    return $args;
}, 10, 2 );
```

---

# Filter: bricks/filter-element/datepicker_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter-element-datepicker_options/

*Filters the Flatpickr options used by the Filter: Datepicker element. This allows you to customize the behavior of the date picker within query filters.*

Filters the Flatpickr options used by the Filter: Datepicker element. This allows you to customize the behavior of the date picker within query filters.

## Parameters

- `$datepicker_options` (*array*): Array of Flatpickr options.
- `$element` (*object*): The Filter: Datepicker element instance.

## Example usage

```php
add_filter( 'bricks/filter-element/datepicker_options', function( $datepicker_options, $element ) {
    // Example: Change the date format
    $datepicker_options['dateFormat'] = 'Y-m-d';

    // Example: Disable specific dates
    $datepicker_options['disable'] = [ '2023-12-25', '2024-01-01' ];

    return $datepicker_options;
}, 10, 2 );
```

---

# Filter: bricks/filter/taxonomy_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter-taxonomy_args/

*Filters the arguments passed to getterms() when generating options for taxonomy-based filter elements (e.g., Checkbox, Radio, Select filters).*

Filters the arguments passed to `get_terms()` when generating options for taxonomy-based filter elements (e.g., Checkbox, Radio, Select filters).

## Parameters

- `$args` (*array*): Array of arguments for `get_terms()`.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter/taxonomy_args', function( $args, $element ) {
    // Example: Exclude specific term IDs from the filter options
    $args['exclude'] = [ 1, 2, 3 ];

    return $args;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/controls

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-controls/

*Filters the controls available for filter elements (e.g., Checkbox, Radio, Select, Range). This allows you to add, remove, or modify settings for these elements.*

Filters the controls available for filter elements (e.g., Checkbox, Radio, Select, Range). This allows you to add, remove, or modify settings for these elements globally.

## Parameters

- `$controls` (*array*): Array of element controls.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/controls', function( $controls, $element ) {
    // Add a custom control to all filter elements
    $controls['my_custom_setting'] = [
        'tab'   => 'content',
        'group' => 'filter',
        'label' => esc_html__( 'My Custom Setting', 'my-plugin' ),
        'type'  => 'checkbox',
    ];

    return $controls;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/count_source_{filter_source}

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-count_source-filter_source/

*Filters indexed count data for a specific custom filter source.*

Filters indexed count data for a specific custom filter source. The `{$filter_source}` portion of the hook name should be replaced with the actual `filterSource` key, such as `wcField` or a custom source.

Built-in `taxonomy`, `wpField`, and `customField` sources are handled before this dynamic filter runs.

## Parameters

- `$count_source` (*array*): Indexed count rows. Each row can include `filter_value`, `filter_value_display`, `filter_value_id`, `filter_value_parent`, and `count`.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/count_source_wcField', function( $count_source, $element ) {
    foreach ( $count_source as &$row ) {
        if ( isset( $row['filter_value'] ) && $row['filter_value'] === 'featured' ) {
            $row['count'] = 999;
        }
    }
    unset( $row );

    return $count_source;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/count_source_wcField

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-count_source_wcfield/

*Filters the count data specifically for WooCommerce field filters (e.g., price, rating). This allows you to customize the counts displayed next to filter.*

Filters the count data specifically for WooCommerce field filters (e.g., price, rating). This allows you to customize the counts displayed next to filter options.

## Parameters

- `$count_source` (*array*): Associative array where keys are filter values and values are their respective counts.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/count_source_wcField', function( $count_source, $element ) {
    // Example: Hide counts for rating filter by setting them to 0 (if logic hides 0 counts)
    // Or manipulate them for specific ratings
    return $count_source;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/data_source_{filter_source}

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-data_source-filter_source/

*Filters the data source (options) for a specific filter source. The {$filtersource} portion of the hook name should be replaced with the actual source name.*

Filters the data source (options) for a specific filter source. The `{$filter_source}` portion of the hook name should be replaced with the actual source name.

Built-in `taxonomy`, `wpField`, and `customField` sources are handled before this dynamic filter runs. Use this hook for custom filter sources that Bricks does not populate internally.

## Parameters

- `$data_source` (*array*): Array of filter options. Each option should be an associative array with keys like `value`, `text`, `class`, etc.
- `$element` (*object*): The filter element instance.

## Example usage

```php
// Populate options for a custom source 'my_source'
add_filter( 'bricks/filter_element/data_source_my_source', function( $data_source, $element ) {
    $data_source[] = [
        'value' => 'option_1',
        'text'  => 'Option 1',
    ];

    $data_source[] = [
        'value' => 'option_2',
        'text'  => 'Option 2',
    ];

    return $data_source;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/data_source_wcField

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-data_source_wcfield/

*Filters the data source (options) specifically for WooCommerce field filters. This allows you to customize the options displayed for WooCommerce filters like.*

Filters the data source (options) specifically for WooCommerce field filters. This allows you to customize the options displayed for WooCommerce filters like product visibility, stock status, etc.

## Parameters

- `$data_source` (*array*): Array of filter options.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/data_source_wcField', function( $data_source, $element ) {
    // Example: Add a custom option to a WooCommerce filter
    // Note: You might need to check $element->settings to target specific WC fields
    if ( isset( $element->settings['sourceFieldType'] ) && $element->settings['sourceFieldType'] === 'stock_status' ) {
         // Modify stock status options
    }

    return $data_source;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/datepicker_date_format

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-datepicker_date_format/

*Filters the PHP date format string used by the Filter: Datepicker element. This determines how dates are parsed and formatted for comparison with the database.*

Filters the PHP date format string used by the Filter: Datepicker element. This determines how dates are parsed and formatted for comparison with the database values.

## Parameters

- `$date_format` (*string*): The PHP date format string (e.g., `Y-m-d`, `d/m/Y`).
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`, `pods`, `jetengine`).
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/datepicker_date_format', function( $date_format, $provider, $element ) {
    // Example: Use a specific format for ACF date fields
    if ( $provider === 'acf' ) {
        return 'Ymd'; // ACF often stores dates as Ymd
    }

    return $date_format;
}, 10, 3 );
```

---

# Filter: bricks/filter_element/filtered_source

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-filtered_source/

*Filters the data retrieved from the index representing the available filter options and their counts based on the current query results.*

Filters the data retrieved from the index representing the available filter options and their counts based on the current query results.

## Parameters

- `$filtered_source` (*array*): Associative array where keys are filter values and values are their respective counts (based on the current filtered query).
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/filtered_source', function( $filtered_source, $element ) {
    // Example: Ensure a specific value is always present with a count of 0 if missing
    if ( ! isset( $filtered_source['some_value'] ) ) {
        $filtered_source['some_value'] = 0;
    }

    return $filtered_source;
}, 10, 2 );
```

---

# Filter: bricks/filter_element/datepicker_db_date_format

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-datepicker_db_date_format/

*Filters the database date format used by a Datepicker filter element.*

Filters the database date format used by a Datepicker filter element. This is intended for custom field providers that store dates in a different format.

## Parameters

- `$db_format` (string): The database date format Bricks will use.
- `$provider` (string): The active custom field provider.
- `$element` (object): The Datepicker filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/datepicker_db_date_format', function( $db_format, $provider, $element ) {
    if ( $provider === 'my_provider' ) {
        return 'Ymd';
    }

    return $db_format;
}, 10, 3 );
```

---

# Filter: bricks/form/file_directory

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-file_directory/

*Filter the directory Bricks uses when uploaded form files are saved into a custom file-storage location.*

This filter allows you to modify the directory where your uploaded form files are stored when the `Save File` setting is "Save in custom directory".

![](https://academy.bricksbuilder.io/assets/bricks-filter-form-file-directory-442x1024.png)

By default, the folder is always located in WordPress "uploads" if you configure it via the `Direction name` in the setting below `Save file`.

You can change the final file storage location by utilizing the `bricks/form/file_directory` filter.

> **Note**
>
> Bricks will automatically create the directory if it doesn't already exist.

```php
add_filter( 'bricks/form/file_directory', function( $directory_path, $form, $input_name ){
  $form_fields   = $form->get_fields();
  $form_id       = $form_fields['formId'];

  // Return: Target form ID is not 'exbedq' OR field name is not 'form-field-vfkfev'
  // if ( $form_id !== 'exbedq' || $input_name !== 'form-field-vfkfev' ) {
    // return $directory_path;
  // }

  // Get uploads directory
  $wp_upload_dir = wp_upload_dir();

  // Store form files under /uploads/form-files
  $directory_path = $wp_upload_dir['basedir'] . '/form-files';

  return $directory_path;
}, 10, 3);
```

---

# Filter: bricks/fix_filter_element_db

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-fix_filter_element_db/

*Allows plugins to intercept and handle the database update process for filter elements on a per-post basis. If the filter returns true, Bricks will skip its.*

Allows plugins to intercept and handle the database update process for filter elements on a per-post basis. If the filter returns `true`, Bricks will skip its default update logic for that post.

## Parameters

- `$handled` (*bool*): Whether the update has been handled. Default is `false`.
- `$post_id` (*int*): The ID of the post being processed.
- `$template_type` (*string*): The template type of the post.

## Example usage

```php
add_filter( 'bricks/fix_filter_element_db', function( $handled, $post_id, $template_type ) {
    // Example: Skip processing for a specific post ID
    if ( $post_id === 1234 ) {
        return true;
    }

    return $handled;
}, 10, 3 );
```

---

# Filter: bricks/form/recaptcha_score_threshold

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-recaptcha_score_threshold/

*Filters the minimum score required for Google reCAPTCHA v3 validation in Bricks forms. Scores range from 0.0 (likely a bot) to 1.0 (likely a human).*

Filters the minimum score required for Google reCAPTCHA v3 validation in Bricks forms. Scores range from 0.0 (likely a bot) to 1.0 (likely a human).

## Parameters

- `$score` (*float*): The minimum score threshold. Default is `0.5`.

## Example usage

```php
add_filter( 'bricks/form/recaptcha_score_threshold', function( $score ) {
    // Increase threshold to 0.8 for stricter validation
    return 0.8;
} );
```

---

# Filter: bricks/form/response

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-response/

*Filters the JSON response sent to the browser after a Bricks form submission. This allows you to customize the success message, redirection URL, or add extra.*

Filters the JSON response sent to the browser after a Bricks form submission. This allows you to customize the success message, redirection URL, or add extra data to the response.

## Parameters

- `$response` (*array*): The response data array (e.g., `['type' => 'success', 'message' => '...', 'redirectUrl' => '...']`).
- `$form` (*object*): The Form integration instance.

## Example usage

```php
add_filter( 'bricks/form/response', function( $response, $form ) {
    // Example: Append a "Thank you" note to the success message
    if ( isset( $response['type'] ) && $response['type'] === 'success' ) {
        $response['message'] .= ' ' . esc_html__( 'Thank you for contacting us!', 'my-domain' );
    }

    return $response;
}, 10, 2 );
```

---

# Filter: bricks/form/save-submission/form_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-save-submission-form_data/

*The bricks/form/save-submission/formdata filter allows you to modify submitted Bricks form data before it is saved to the database and shown in the Form.*

The `bricks/form/save-submission/form_data` filter allows you to modify submitted Bricks form data before it is saved to the database and shown in the Form Submissions admin screen. ([Save submission](https://academy.bricksbuilder.io/builder/features/save-form-submissions/))

This is useful when you want to:

- Remove unwanted fields from stored submissions
- Mask sensitive values (e.g. passwords, tokens, IDs)
- Normalize or reformat values before storage

### Example:

In this example, the form submission should store other registration fields, but the password field is masked before saving.

```php
/**
 * $form_data is an array of Submission data to be saved.
 * $form_id The Bricks Form element ID.
 * $post_id The post/page ID where the form is located
 */
add_filter( 'bricks/form/save-submission/form_data', function( $form_data, $form_id, $post_id ) {
  if ( $form_id !== 'coudkb' ) {
    return $form_data;
  }

  // Array of all data going to be saved for this submission, the array key is the field ID
  // Example, mask the field ID 798ce3 before saving
  if ( isset( $form_data['798ce3']['value'] ) ) {
    $form_data['798ce3']['value'] = '******';
  }
  return $form_data;
}, 10, 3 );
```

**Notes:**

- This filter affects **save submissions only**. It does not change what is sent via email actions or other integrations unless those also use the stored submission data.
- For sensitive fields, consider disabling save submission entirely if you don’t need it, or mask/remove values using this filter.

---

# Filter: bricks/form/submission-table/file_url

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-submission-table-file_url/

*Filters the URL of an uploaded file displayed in the Form Submissions table in the admin area. This is useful if you have customized the upload directory and.*

Filters the URL of an uploaded file displayed in the Form Submissions table in the admin area. This is useful if you have customized the upload directory and the auto-generated URL is incorrect.

## Parameters

- `$file_url` (*string*): The generated URL for the file.
- `$file` (*array*): Array containing file information (e.g., `file` path, `name`, `type`).
- `$field_key` (*string*): The ID of the form field.

## Example usage

```php
add_filter( 'bricks/form/submission-table/file_url', function( $file_url, $file, $field_key ) {
    // Example: Fix URL for files in a custom 'secure-uploads' directory
    if ( strpos( $file['file'], 'secure-uploads' ) !== false ) {
        return site_url( '/secure-uploads/' . basename( $file['file'] ) );
    }

    return $file_url;
}, 10, 3 );
```

---

# Filter: bricks/form/tinymce_settings

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-tinymce_settings/

*Filters the TinyMCE configuration settings for \"Rich Text\" fields in Bricks forms. This allows you to customize the toolbar, menus, and other editor options.*

Filters the TinyMCE configuration settings for "Rich Text" fields in Bricks forms. This allows you to customize the toolbar, menus, and other editor options.

## Parameters

- `$settings` (*array*): Array of TinyMCE settings.

## Example usage

```php
add_filter( 'bricks/form/tinymce_settings', function( $settings ) {
    // Example: Disable the menubar
    $settings['menubar'] = false;

    // Example: Simplify the toolbar
    $settings['toolbar'] = 'bold italic underline | bullist numlist | link unlink';

    return $settings;
} );
```

---

# Filter: bricks/form/validate

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-validate/

*Filters the validation errors for a form submission. This allows you to implement custom validation logic (e.g., checking if an email is from a specific domain,.*

Filters the validation errors for a form submission. This allows you to implement custom validation logic (e.g., checking if an email is from a specific domain, or if a field value meets certain criteria).

## Parameters

- `$errors` (*array*): Array of validation error messages.
- `$form` (*object*): The Form integration instance.

## Example usage

```php
add_filter( 'bricks/form/validate', function( $errors, $form ) {
    $form_id = $form->get_element_id();
    $fields  = $form->get_fields();

    // Example: Only validate a specific form
    if ( $form_id === 'my_form_id' ) {
        // Check if email domain is allowed
        $email_field_id = 'form-field-email';
        if ( isset( $fields[ $email_field_id ] ) ) {
            $email = $fields[ $email_field_id ];
            if ( strpos( $email, '@example.com' ) === false ) {
                $errors[] = esc_html__( 'Please use an @example.com email address.', 'my-domain' );
            }
        }
    }

    return $errors;
}, 10, 2 );
```

---

# Filter: bricks/frontend/disable_opengraph

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_opengraph/

*Determines whether Bricks should generate and output Open Graph meta tags (e.g., og:title, og:image). Use this to disable Bricks' Open Graph implementation if.*

Determines whether Bricks should generate and output Open Graph meta tags (e.g., `og:title`, `og:image`). Use this to disable Bricks' Open Graph implementation if you are using a third-party SEO plugin that already handles this.

## Parameters

- `$disable` (*bool*): Whether to disable Open Graph tags.

## Example usage

```php
add_filter( 'bricks/frontend/disable_opengraph', function( $disable ) {
    // Example: Disable Open Graph tags on 'product' post type
    if ( is_singular( 'product' ) ) {
        return true;
    }

    return $disable;
} );
```
