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

---

# Filter: bricks/frontend/disable_seo

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_seo/

*Determines whether Bricks should generate and output SEO meta tags (e.g., description, keywords, robots) and modify the document title. Use this to disable.*

Determines whether Bricks should generate and output SEO meta tags (e.g., description, keywords, robots) and modify the document title. Use this to disable Bricks' built-in SEO features if you are using a dedicated SEO plugin.

## Parameters

- `$disable` (*bool*): Whether to disable SEO tags.

## Example usage

```php
add_filter( 'bricks/frontend/disable_seo', function( $disable ) {
    // Example: Always disable Bricks SEO features
    return true;
} );
```

---

# Filter: bricks/frontend/render_loop

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-render_loop/

*Filters the HTML output of a query loop iteration. This allows you to modify the content of each item rendered within a loop.*

Filters the HTML output of a query loop iteration. This allows you to modify the content of each item rendered within a loop.

## Parameters

- `$output` (*string*): The rendered HTML of the loop item.
- `$element` (*array*): The element data array.
- `$container` (*object*): The container element instance managing the loop.

## Example usage

```php
add_filter( 'bricks/frontend/render_loop', function( $output, $element, $container ) {
    // Example: Wrap each loop item in a custom div
    return '<div class="my-custom-loop-wrapper">' . $output . '</div>';
}, 10, 3 );
```

---

# Filter: bricks/get_builder_edit_link

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_builder_edit_link/

*Filters the \"Edit with Bricks\" URL generated for a post. This allows you to append custom query parameters or modify the link structure.*

Filters the "Edit with Bricks" URL generated for a post. This allows you to append custom query parameters or modify the link structure.

## Parameters

- `$url` (*string*): The "Edit with Bricks" URL.
- `$post_id` (*int*): The ID of the post.

## Example usage

```php
add_filter( 'bricks/get_builder_edit_link', function( $url, $post_id ) {
    // Example: Append a custom parameter to the builder URL
    return add_query_arg( 'my_param', 'value', $url );
}, 10, 2 );
```

---

# Filter: bricks/get_template_tags

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_tags/

*Filters the list of template tags displayed in the Bricks template manager. Template tags are a custom taxonomy used to organize templates.*

Filters the list of template tags displayed in the Bricks template manager. Template tags are a custom taxonomy used to organize templates.

## Parameters

- `$tags` (*array*): Associative array of template tags, where the key is the term slug and the value is the term name.

## Example usage

```php
add_filter( 'bricks/get_template_tags', function( $tags ) {
    // Example: Remove the 'dark' tag from the list
    if ( isset( $tags['dark'] ) ) {
        unset( $tags['dark'] );
    }

    return $tags;
} );
```

---

# Filter: bricks/get_template_authors

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_authors/

*Filters the list of authors displayed in the Bricks template manager. This allows you to customize which authors are selectable when filtering templates.*

Filters the list of authors displayed in the Bricks template manager. This allows you to customize which authors are selectable when filtering templates.

## Parameters

- `$authors` (*array*): Array of author display names.

## Example usage

```php
add_filter( 'bricks/get_template_authors', function( $authors ) {
    // Example: Remove 'admin' from the authors list
    if ( ( $key = array_search( 'admin', $authors ) ) !== false ) {
        unset( $authors[ $key ] );
    }

    return $authors;
} );
```

---

# Filter: bricks/get_template_bundles

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_bundles/

*Filters the list of template bundles displayed in the Bricks template manager. Template bundles are a custom taxonomy used to categorize templates.*

Filters the list of template bundles displayed in the Bricks template manager. Template bundles are a custom taxonomy used to categorize templates.

## Parameters

- `$bundles` (*array*): Associative array of template bundles, where the key is the term slug and the value is the term name.

## Example usage

```php
add_filter( 'bricks/get_template_bundles', function( $bundles ) {
    // Example: Rename a specific bundle
    if ( isset( $bundles['my-bundle'] ) ) {
        $bundles['my-bundle'] = 'My Renamed Bundle';
    }

    return $bundles;
} );
```

---

# Filter: bricks/get_remote_templates_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_remote_templates_data/

*Filters the data retrieved from a remote template source (e.g., the Bricks Community Templates or a custom remote library). This allows you to modify, add, or.*

Filters the data retrieved from a remote template source (e.g., the Bricks Community Templates or a custom remote library). This allows you to modify, add, or remove templates before they are displayed in the template manager.

## Parameters

- `$remote_templates` (*array*): The decoded JSON response from the remote source, containing template data.

## Example usage

```php
add_filter( 'bricks/get_remote_templates_data', function( $remote_templates ) {
    // Example: Remove templates with a specific tag
    if ( ! empty( $remote_templates['templates'] ) ) {
        foreach ( $remote_templates['templates'] as $key => $template ) {
            if ( isset( $template['tags'] ) && in_array( 'deprecated', $template['tags'] ) ) {
                unset( $remote_templates['templates'][ $key ] );
            }
        }
    }

    return $remote_templates;
} );
```

---

# Filter: bricks/get_templates/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates-query_vars/

*Filters the query arguments used by Templates::gettemplatesquery() to retrieve Bricks templates. This allows you to customize which templates are fetched, for.*

Filters the query arguments used by `Templates::get_templates_query()` to retrieve Bricks templates. This allows you to customize which templates are fetched, for example, to support multilingual plugins or custom filtering.

## Parameters

- `$query_vars` (*array*): Array of arguments passed to `WP_Query`.

## Example usage

```php
add_filter( 'bricks/get_templates/query_vars', function( $query_vars ) {
    // Example: Exclude templates with a specific meta key
    $query_vars['meta_query'][] = [
        'key'     => 'my_exclude_key',
        'compare' => 'NOT EXISTS',
    ];

    return $query_vars;
} );
```

---

# Filter: bricks/get_templates

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates/

*Filters the list of templates returned by the Templates::gettemplates() method. This allows you to modify the templates array before it is returned to the.*

Filters the list of templates returned by the `Templates::get_templates()` method. This allows you to modify the templates array before it is returned to the builder or other parts of the application.

## Parameters

- `$templates` (*array*): Array of template data.
- `$custom_args` (*array*): The arguments used to query the templates.

## Example usage

```php
add_filter( 'bricks/get_templates', function( $templates, $custom_args ) {
    // Example: Add a custom property to all templates
    foreach ( $templates as $key => $template ) {
        $templates[ $key ]['my_custom_property'] = 'value';
    }

    return $templates;
}, 10, 2 );
```

---

# Filter: bricks/get_templates_query/cache_key

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates_query-cache_key/

*Filters the cache key used by Templates::gettemplatesquery() to store and retrieve template queries. Use this to create unique cache entries when modifying the.*

Filters the cache key used by `Templates::get_templates_query()` to store and retrieve template queries. Use this to create unique cache entries when modifying the template query arguments based on custom context (e.g., user role, language).

## Parameters

- `$cache_key` (*string*): The unique cache key string.

## Example usage

```php
add_filter( 'bricks/get_templates_query/cache_key', function( $cache_key ) {
    // Example: Append current user role to cache key
    $user = wp_get_current_user();
    $role = ( array ) $user->roles;
    
    return $cache_key . '_' . implode( '-', $role );
} );
```

---

# Filter: bricks/get_terms_options/enable_limit

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_terms_options-enable_limit/

*Enables a limit on the number of taxonomies queried when fetching terms for builder controls. This is useful for sites with a very large number of taxonomies to.*

Enables a limit on the number of taxonomies queried when fetching terms for builder controls. This is useful for sites with a very large number of taxonomies to prevent memory exhaustion.

## Parameters

- `$enable_limit` (*bool*): Whether to limit the number of queried taxonomies. Default is `false`.

## Example usage

```php
add_filter( 'bricks/get_terms_options/enable_limit', function( $enable_limit ) {
    // Enable the limit to improve performance on sites with many taxonomies
    return true;
} );
```

---

# Filter: bricks/get_terms_options/excluded_taxonomies

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_terms_options-excluded_taxonomies/

*Filters the list of taxonomies excluded from term selection controls in the builder. This allows you to hide specific taxonomies (e.g., internal taxonomies).*

Filters the list of taxonomies excluded from term selection controls in the builder. This allows you to hide specific taxonomies (e.g., internal taxonomies) from the UI.

## Parameters

- `$excluded_taxonomies` (*array*): Array of taxonomy slugs to exclude. Defaults include `nav_menu`, `link_category`, `post_format`.

## Example usage

```php
add_filter( 'bricks/get_terms_options/excluded_taxonomies', function( $excluded_taxonomies ) {
    // Example: Exclude 'my_internal_taxonomy'
    $excluded_taxonomies[] = 'my_internal_taxonomy';

    return $excluded_taxonomies;
} );
```

---

# Filter: bricks/get_the_title

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_the_title/

*Filters the page title returned by Helpers::getthetitle(). This function determines the appropriate title based on the context (single post, archive, search.*

Filters the page title returned by `Helpers::get_the_title()`. This function determines the appropriate title based on the context (single post, archive, search results, etc.).

## Parameters

- `$title` (*string*): The generated page title.
- `$post_id` (*int*): The ID of the current post or template.

## Example usage

```php
add_filter( 'bricks/get_the_title', function( $title, $post_id ) {
    // Example: Add a prefix to the title for search results
    if ( is_search() ) {
        return 'Searching: ' . $title;
    }

    return $title;
}, 10, 2 );
```

---

# Filter: bricks/global_history/keep_days

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_days/

*Set the age window that protects all recent global data history entries from automatic cleanup.*

Since Bricks 2.5, `bricks/global_history/keep_days` changes the age window used when cleaning up [Global Data Revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/).

## Parameter and return value

- `$days` (*int*): The number of days of recent history to keep. Default: `90`.
- Return the desired number of days. Bricks casts it to an integer and uses a minimum of `1`. Returning `0` or `false` does not delete all history or disable cleanup.

## Example usage

Protect all history recorded within the last 30 days:

```php
add_filter( 'bricks/global_history/keep_days', function( $days ) {
    return 30;
} );
```

Add the filter in a plugin or child theme that loads during WP-Cron requests.

## How it combines with the entry count

The age window is not a maximum age for every stored entry. Bricks also protects each item's latest entries through [`bricks/global_history/keep_latest`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_latest/), which defaults to 20.

Cleanup removes an entry only when it is older than the configured age window and outside that latest-entry count. With the example above and the default count, an item retains all entries from the last 30 days plus its latest 20 entries, even when some of those 20 are older.

The filter is read during scheduled daily cleanup. Changing it does not remove entries immediately. Cleanup depends on WP-Cron running, and increasing the period cannot recover entries already pruned.

This filter does not control page revisions or draft undo points. For finished drafts and version undo points, see [`bricks/drafts/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-drafts-keep_days/).

---

# Filter: bricks/global_history/keep_latest

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_latest/

*Set the minimum number of recent history entries kept for each shared Bricks item during cleanup.*

Since Bricks 2.5, `bricks/global_history/keep_latest` changes how many of an item's latest [Global Data Revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/) entries are protected from automatic cleanup.

## Parameter and return value

- `$latest` (*int*): The number of latest entries to keep per resource/item pair. Default: `20`.
- Return the desired count. Bricks casts it to an integer and uses a minimum of `1`. Returning `0` or `false` does not disable retention or request unlimited history.

## Example usage

Keep at least the latest 40 entries for each recorded item:

```php
add_filter( 'bricks/global_history/keep_latest', function( $latest ) {
    return 40;
} );
```

Add the filter in a plugin or child theme that loads during WP-Cron requests.

## How it combines with the age limit

Bricks also keeps every entry within the period set by [`bricks/global_history/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_days/), which defaults to 90 days. Cleanup deletes an entry only when it is both outside the protected latest count and older than that period.

With the example above, an item can keep more than 40 entries if they are recent. It can also keep 40 entries older than 90 days when those are its latest entries. The count is a minimum retained per item, not a storage cap.

The filter is read during the scheduled daily cleanup. Changing it does not prune records immediately or recover records already removed. WP-Cron must run for scheduled cleanup to take place.

---

# Filter: bricks/handle_no_results_children_elements

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-handle_no_results_children_elements/

*Determines whether Bricks should run logic to handle children elements displayed when a query loop returns no results (e.g., ensuring scripts/styles are.*

Determines whether Bricks should run logic to handle children elements displayed when a query loop returns no results (e.g., ensuring scripts/styles are enqueued for "No results" content).

## Parameters

- `$run` (*bool*): Whether to handle "No results" children logic. Defaults to `true` if Query Filters are enabled.

## Example usage

```php
add_filter( 'bricks/handle_no_results_children_elements', function( $run ) {
    // Example: Always enable this logic, even if native Query Filters are disabled
    return true;
} );
```

---

# Filter: bricks/helpers/get_posts_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-helpers-get_posts_args/

*The bricks/helpers/getpostsargs filter allows you to modify the query arguments used when Bricks retrieves posts in the builder via AJAX.*

The `bricks/helpers/get_posts_args` filter allows you to modify the query arguments used when Bricks retrieves posts in the **builder via AJAX**.

This includes scenarios such as:

- Searching posts or pages in the link-type control
- Searching posts, pages, or custom post types in the populate content dropdown

This hook gives you full control over the underlying `WP_Query` arguments before the query is executed.

> **Note**
>
> This filter affects multiple builder features globally. Incorrect modifications may break expected behavior in post selection controls.

## Parameters

- `$query_args` (*array*): Array of arguments passed to `get_posts()`.

## Example: Exclude media from builder search

When WordPress queries with `post_type` set to `any`, the results may include attachments. This example excludes media items unless the caller explicitly requests the `attachment` post type.

```php
add_filter( 'bricks/helpers/get_posts_args', function( $query_args ) {
    // If no post type is provided, treat it as "any" for safety.
    $post_type_arg = $query_args['post_type'] ?? 'any';

    // Detect whether the caller explicitly requested the attachment post type.
    $has_attachment = false;

    if ( is_array( $post_type_arg ) ) {
        $has_attachment = in_array( 'attachment', $post_type_arg, true );
    } else {
        $has_attachment = ( $post_type_arg === 'attachment' );
    }

    // If attachment was explicitly requested, do nothing.
    if ( $has_attachment ) {
        return $query_args;
    }

    // Get all public post types once. We only use this when expanding "any".
    $public_post_types = array_values(
        array_diff(
            get_post_types( [ 'public' => true ], 'names' ),
            [ 'attachment' ]
        )
    );

    // CASE 1: post_type = 'any'
    if ( $post_type_arg === 'any' ) {
        $query_args['post_type'] = $public_post_types;
    }

    // CASE 2: post_type is an array
    elseif ( is_array( $post_type_arg ) ) {
        $normalized_post_types = array_diff( $post_type_arg, [ 'attachment' ] );

        // Defensive handling: if "any" exists in the array, replace it with
        // all public post types except attachment.
        if ( in_array( 'any', $normalized_post_types, true ) ) {
            $normalized_post_types = array_diff( $normalized_post_types, [ 'any' ] );
            $normalized_post_types = array_merge( $normalized_post_types, $public_post_types );
        }

        $query_args['post_type'] = array_values( array_unique( $normalized_post_types ) );
    }

    return $query_args;
} );
```

---

# Filter: bricks/metabox/checkbox_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-checkbox_value/

*Filters the output value of a Meta Box checkbox field when rendered via Bricks dynamic data. By default, Bricks converts truthy values to \"Yes\" and falsy values.*

Filters the output value of a Meta Box checkbox field when rendered via Bricks dynamic data. By default, Bricks converts truthy values to "Yes" and falsy values to "No".

## Parameters

- `$value` (*string*): The processed value (e.g., "Yes" or "No").
- `$original_value` (*mixed*): The raw value from the database.
- `$field` (*array*): The Meta Box field settings array.
- `$post` (*WP_Post*): The current post object.

## Example usage

```php
add_filter( 'bricks/metabox/checkbox_value', function( $value, $original_value, $field, $post ) {
    // Example: Return "Active" or "Inactive"
    return $original_value ? 'Active' : 'Inactive';
}, 10, 4 );
```

---

# Filter: bricks/media_browser/health/file_status

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-media-browser-health-file-status/

*Report the file status of offloaded attachments to Bricks Media Health without treating a missing local copy as a broken file.*

Bricks 2.4 uses `bricks/media_browser/health/file_status` to let media integrations override the original attachment's file status in Media Health.

By default, Bricks checks the attached file on the local filesystem. An offload integration can return a status based on its own storage records when the local copy has been removed.

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `$state` | string | Status detected by Bricks before this filter runs. |
| `$attachment_id` | int | WordPress attachment ID. |
| `$file` | string or false | Attached file path returned by `get_attached_file()`. |
| `$url` | string or false | Attachment URL returned by `wp_get_attachment_url()`. |

Register the callback with four accepted arguments. Return one of these strings:

| Return value | Meaning | Broken-file check |
| --- | --- | --- |
| `exists` | The original file is available. | Does not flag the original as broken. |
| `missing` | The original file is absent. | Flags it as broken. |
| `unreadable` | The original file cannot be read. | Flags it as broken. |
| `empty` | The original file has no content. | Flags it as broken. |
| `unknown` | The integration cannot determine availability. | Does not flag the original as broken. |

The broken-file check must be enabled for those issues to be reported. Bricks sanitizes the returned value and treats unsupported values as `unknown`. An `unknown` result is not confirmation that the file is healthy.

## Example: use a provider's stored status

Add the filter in your integration plugin. This example assumes your own offload process records a verified status in an attachment meta field named `_my_offload_file_state`. Replace that field and lookup with your provider's actual status source. Bricks does not create or refresh this metadata.

```php
add_filter( 'bricks/media_browser/health/file_status', function( $state, $attachment_id, $file, $url ) {
    $provider_state = get_post_meta( $attachment_id, '_my_offload_file_state', true );

    // Leave attachments outside this integration unchanged.
    if ( $provider_state === '' ) {
        return $state;
    }

    $allowed = [ 'exists', 'missing', 'unreadable', 'empty', 'unknown' ];

    return in_array( $provider_state, $allowed, true ) ? $provider_state : 'unknown';
}, 10, 4 );
```

Only return `exists` when the provider has confirmed that the remote original is available. An attachment URL alone does not prove the file exists. Keep stored results current when files are uploaded, removed, or moved; avoid a separate remote request for every attachment during a scan.

## Scope and repair limits

The filter changes classification of the original file. It does not download offloaded media, supply a remote file size, or make local repair actions work on remote files.

Image-size checks can still inspect local derivative files. Operations such as image regeneration and optimization require a readable local source within the uploads directory. Restore a local copy through your offload integration before attempting repairs that require it.

---

# Filter: bricks/metabox/show_as_map

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-show_as_map/

*Determines whether a Meta Box map field should be rendered as a map (using rwmbmeta()) or as raw latitude/longitude coordinates when used in dynamic data.*

Determines whether a Meta Box map field should be rendered as a map (using `rwmb_meta()`) or as raw latitude/longitude coordinates when used in dynamic data.

## Parameters

- `$show_as_map` (*bool*): Whether to render as a map. Default is `false` (renders coordinates).
- `$field` (*array*): The Meta Box field settings array.
- `$post` (*WP_Post*): The current post object.

## Example usage

```php
add_filter( 'bricks/metabox/show_as_map', function( $show_as_map, $field, $post ) {
    // Example: Render as map for a specific field ID
    if ( $field['id'] === 'my_map_field' ) {
        return true;
    }

    return $show_as_map;
}, 10, 3 );
```

---

# Filter: bricks/metabox/taxonomy/show_as_link

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-metabox-taxonomy-show_as_link/

*Determines whether Meta Box taxonomy fields retrieved via dynamic data should be rendered as links to the term archives.*

Determines whether Meta Box taxonomy fields retrieved via dynamic data should be rendered as links to the term archives.

## Parameters

- `$show_as_link` (*bool*): Whether to render as links. Default is `true`.
- `$value` (*mixed*): The raw value of the taxonomy field.
- `$field` (*array*): The Meta Box field settings array.

## Example usage

```php
add_filter( 'bricks/metabox/taxonomy/show_as_link', function( $show_as_link, $value, $field ) {
    // Disable links for a specific taxonomy field
    if ( $field['id'] === 'my_taxonomy_field' ) {
        return false;
    }

    return $show_as_link;
}, 10, 3 );
```

---

# Filter: bricks/{object_type}s/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-object_types-query_vars/

*Allows you to modify the query variables for a specific object type query loop. This is a dynamic filter where {$objecttype} is replaced by the type of object.*

Allows you to modify the query variables for a specific object type query loop. This is a dynamic filter where `{$object_type}` is replaced by the type of object being queried (e.g., `post`, `term`, `user`).

Common variations:
- `bricks/posts/query_vars`
- `bricks/terms/query_vars`
- `bricks/users/query_vars`

## Parameters

- `$query_vars` (array): The query variables/arguments.
- `$settings` (array): The element settings.
- `$element_id` (string): The element ID.
- `$element_name` (string): The element name (available since Bricks 1.11.1).

## Example usage

```php
add_filter( 'bricks/posts/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    // Only apply to a specific element ID
    if ( $element_id !== 'brxe-abcdef' ) {
        return $query_vars;
    }

    // Modify query variables
    $query_vars['posts_per_page'] = 12;

    return $query_vars;
}, 10, 4 );
```

---

# Filter: bricks/paginate_links_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-paginate_links_args/

*Filters the arguments passed to the WordPress paginatelinks() function when generating pagination output. This allows you to customize the pagination structure,.*

Filters the arguments passed to the WordPress `paginate_links()` function when generating pagination output. This allows you to customize the pagination structure, text labels, and other settings.

## Parameters

- `$args` (*array*): Array of arguments for `paginate_links()`.

## Example usage

```php
add_filter( 'bricks/paginate_links_args', function( $args ) {
    // Example: Change the "Previous" and "Next" text
    $args['prev_text'] = 'Previous';
    $args['next_text'] = 'Next';

    // Example: Change the number of adjacent page links shown
    $args['mid_size'] = 3;

    return $args;
} );
```

---

# Filter: bricks/pagination/custom_logic

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-custom_logic/

*Enable custom pagination logic in Bricks when your query type needs custom current-page and total-page handling.*

The `bricks/pagination/custom_logic` filter allows you to implement custom pagination logic in Bricks Builder based on specific query settings. `@since 2.2`

In this example, we'll demonstrate how to apply custom pagination logic to a custom loop.

Next, you will need to use the following 2 filters to amend the current page and total page arguments when generating HTML for the pagination:

- `bricks/pagination/current_page`
- `bricks/pagination/total_pages`

```php
// Return true if want to use custom logic, default is false
add_filter( 'bricks/pagination/custom_logic', function( $custom_logic, $query_settings, $element ) {
  $query_object_type = $query_settings['query']['objectType'] ?? false;

  // If not my custom loop, return original value
  if( $query_object_type !== 'my_custom_loop' ) {
    return $custom_logic;
  }

  // You can access the element settings via $element->settings

  return true;
}, 10, 3);

```

---

# Filter: bricks/pagination/total_pages

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-total_pages/

*The bricks/pagination/totalpages filter allows you to modify the total number of pages used in the pagination logic of Bricks Builder. In this example, we'll.*

The `bricks/pagination/total_pages` filter allows you to modify the total number of pages used in the pagination logic of Bricks Builder. In this example, we'll demonstrate how to customize the total pages value based on custom loop results. `@since 2.2`

Related hooks:

- `bricks/pagination/custom_logic`
- `bricks/pagination/current_page`

```php
add_filter( 'bricks/pagination/total_pages', function( $total_page, $query_settings, $element ) {
  $query_object_type = $query_settings['query']['objectType'] ?? false;

  // If not my custom loop, return original value
  if( $query_object_type !== 'my_custom_loop' ) {
    return $total_page;
  }

  // You can access the element settings via $element->settings

  // My result stored in a global variable
  global $my_custom_loop_results;

  if ( ! $my_custom_loop_results ) {
    return $total_page;
  }

  // My predefined items per page
  $post_per_page = 3;

  return ceil( count( $my_custom_loop_results ) / $post_per_page );
}, 10, 3);
```

---

# Filter: bricks/pagination/current_page

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-pagination-current_page/

*The bricks/pagination/currentpage filter allows you to modify the current page number used in the pagination logic of Bricks Builder. In this example, we'll.*

The `bricks/pagination/current_page` filter allows you to modify the current page number used in the pagination logic of Bricks Builder. In this example, we'll demonstrate how to customize the current page value based on query variables for a custom loop. `@since 2.2`

You can use `\Bricks\Helpers::get_ajax_current_page()` helper function to retrieve the Bricks AJAX pagination endpoint current page value inside your custom query logic.

Related hooks:

- `bricks/pagination/custom_logic`
- `bricks/pagination/total_pages`

```php
add_filter( 'bricks/pagination/current_page', function( $current_page, $query_settings, $element ) {
  $query_object_type = $query_settings['query']['objectType'] ?? false;

  // If not my custom loop, return original value
  if( $query_object_type !== 'my_custom_loop' ) {
    return $current_page;
  }

  // You can access the element settings via $element->settings

  // Change current page based on query var
  if ( \Bricks\Helpers::get_ajax_current_page() ) {
    $current_page = \Bricks\Helpers::get_ajax_current_page();
  } elseif ( get_query_var( 'page' ) ) {
    // Check for 'page' on static front page
    $current_page = get_query_var( 'page' );
  } elseif ( get_query_var( 'paged' ) ) {
    $current_page = get_query_var( 'paged' );
  } else {
    $current_page = 1;
  }

  return $current_page;
}, 10, 3);
```

---

# Filter: bricks/polylang/builder_ajax_params

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-polylang-builder_ajax_params/

*Filters the Polylang AJAX parameters injected into builder media requests.*

Filters the Polylang AJAX parameters injected into builder media requests. Use it to add or adjust language-aware parameters for the media library in the builder.

## Parameters

- `$params` (array): Parameters added to media AJAX requests.
- `$post_id` (int): The current builder post ID.

## Example usage

```php
add_filter( 'bricks/polylang/builder_ajax_params', function( $params, $post_id ) {
    $params['lang'] = pll_current_language();

    return $params;
}, 10, 2 );
```

---

# Filter: bricks/polylang/exclude_controls_from_translation

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-polylang-exclude_controls_from_translation/

*Filters Bricks control keys excluded from Polylang translation.*

Filters Bricks control keys excluded from Polylang translation. Return the control keys that should not be translated for the current element/control context.

## Parameters

- `$excluded_keys` (array): Control keys excluded from translation.
- `$element` (array): The Bricks element data.
- `$control` (array): The control definition.
- `$key` (string): The current control key.

## Example usage

```php
add_filter( 'bricks/polylang/exclude_controls_from_translation', function( $excluded_keys, $element, $control, $key ) {
    $excluded_keys[] = 'my_untranslated_control';

    return $excluded_keys;
}, 10, 4 );
```

---

# Filter: bricks/popup/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-popup-attributes/

*Filters the HTML attributes of the popup container. This allows you to add custom classes, data attributes, or other attributes to the popup element.*

Filters the HTML attributes of the popup container. This allows you to add custom classes, data attributes, or other attributes to the popup element.

## Parameters

- `$attributes` (*array*): Array of HTML attributes (e.g., `class`, `data-popup-id`).
- `$popup_id` (*int*): The ID of the popup template.

## Example usage

```php
add_filter( 'bricks/popup/attributes', function( $attributes, $popup_id ) {
    // Example: Add a custom class to a specific popup
    if ( $popup_id === 1234 ) {
        $attributes['class'][] = 'my-custom-popup-class';
        $attributes['data-custom-attr'] = 'value';
    }

    return $attributes;
}, 10, 2 );
```

---

# Filter: bricks/query/archive_query_arguments

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-archive_query_arguments/

*Filters the list of WPQuery arguments that are preserved from the main WordPress query when \"Is main query\" is enabled in a query loop. This ensures that.*

Filters the list of `WP_Query` arguments that are preserved from the main WordPress query when "Is main query" is enabled in a query loop. This ensures that essential archive parameters (like pagination, taxonomy terms) are passed to the Bricks query.

## Parameters

- `$arguments` (*array*): Array of `WP_Query` argument keys (e.g., `post_type`, `posts_per_page`, `tax_query`).

## Example usage

```php
add_filter( 'bricks/query/archive_query_arguments', function( $arguments ) {
    // Example: specific custom query var from the main query
    $arguments[] = 'my_custom_var';

    return $arguments;
} );
```

---

# Filter: bricks/query/archive_query_supported_object_types

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-archive_query_supported_object_types/

*Filters the list of Bricks query object types that support the \"Is main query\" setting (archive loop). By default, only 'post' queries are supported.*

Filters the list of Bricks query object types that support the "Is main query" setting (archive loop). By default, only 'post' queries are supported.

## Parameters

- `$object_types` (*array*): Array of supported query object types (e.g., `['post']`).

## Example usage

```php
add_filter( 'bricks/query/archive_query_supported_object_types', function( $object_types ) {
    // Example: Enable "Is main query" for user loops (if implementing custom archive logic)
    $object_types[] = 'user';

    return $object_types;
} );
```

---

# Filter: bricks/query/cache_key

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-cache_key/

*Filters the cache key used for a Bricks query loop.*

Filters the cache key used for a Bricks query loop. Use it when external context, such as language, should split query cache entries.

## Parameters

- `$cache_key` (string): The generated query cache key.
- `$query` (Bricks\Query): The Bricks query instance.

## Example usage

```php
add_filter( 'bricks/query/cache_key', function( $cache_key, $query ) {
    if ( function_exists( 'pll_current_language' ) ) {
        $cache_key .= '_' . pll_current_language();
    }

    return $cache_key;
}, 10, 2 );
```

---

# Filter: bricks/query/fake_result

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-fake_result/

*Filters the results of a \"fake\" query execution. Fake queries are auxiliary queries run by Bricks (e.g., to count total results for filters without pagination).*

Filters the results of a "fake" query execution. Fake queries are auxiliary queries run by Bricks (e.g., to count total results for filters without pagination) that mirror the main query but with modified parameters (like `posts_per_page = -1`).

## Parameters

- `$results` (*array*): The query results (e.g., array of WP_Post objects or IDs).
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/fake_result', function( $results, $query ) {
    // Example: Manipulate the results for a specific query ID
    if ( $query->id === 'my_filtered_loop' ) {
        // Custom logic to modify results
    }

    return $results;
}, 10, 2 );
```

---

# Filter: bricks/query/force_is_looping

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-force_is_looping/

*Forces Bricks\\Query::islooping() to return true. This is useful in AJAX contexts (like popups) where you need to simulate being inside a query loop to correctly.*

Forces `Bricks\Query::is_looping()` to return `true`. This is useful in AJAX contexts (like popups) where you need to simulate being inside a query loop to correctly render dynamic data that depends on the loop context.

## Parameters

- `$force` (*bool*): Whether to force the is_looping state. Default is `false`.
- `$query_id` (*string*): The ID of the query being checked.
- `$element_id` (*string*): The ID of the element being checked.

## Example usage

```php
add_filter( 'bricks/query/force_is_looping', function( $force, $query_id, $element_id ) {
    // Example: Force looping for a specific element ID
    if ( $element_id === 'my_element_id' ) {
        return true;
    }

    return $force;
}, 10, 3 );
```

---

# Filter: bricks/query/force_loop_index

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-force_loop_index/

*Forces Bricks\\Query::getloopindex() to return a specific value. This is useful for AJAX contexts (like popups) where you need to simulate a specific loop.*

Forces `Bricks\Query::get_loop_index()` to return a specific value. This is useful for AJAX contexts (like popups) where you need to simulate a specific loop iteration to render correct data or styles.

## Parameters

- `$index` (*string|int*): The forced loop index. Default is `''` (empty string), meaning no override.

## Example usage

```php
add_filter( 'bricks/query/force_loop_index', function( $index ) {
    // Example: Force loop index to 0
    return 0;
} );
```

---

# Filter: bricks/query/prepare_query_vars_from_settings

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-prepare_query_vars_from_settings/

*Filters the element settings before they are converted into query variables. This runs early in the query setup process, allowing you to modify the raw query.*

Filters the element settings before they are converted into query variables. This runs early in the query setup process, allowing you to modify the raw query settings of an element.

## Parameters

- `$settings` (*array*): The element settings array. The query settings are typically located in `$settings['query']`.
- `$element_id` (*string*): The ID of the element being queried.

## Example usage

```php
add_filter( 'bricks/query/prepare_query_vars_from_settings', function( $settings, $element_id ) {
    // Example: Force a specific post type for a query element with ID 'my_query_element'
    if ( $element_id === 'my_query_element' ) {
        $settings['query']['post_type'] = 'my_custom_post_type';
    }

    return $settings;
}, 10, 2 );
```

---

# Filter: bricks/query/result_end

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/

*Filters the numeric ending result position reported by Query Results Summary. Changes summary metadata only, without limiting or slicing results.*

The `bricks/query/result_end` filter changes the numeric ending position stored in `$query->end`. [Query Results Summary](https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/) reads this value for its `%end%` placeholder.

This filter changes summary metadata only. It does not change the returned items, skip the first item, limit the rendered cards, change the total count, or fetch another page.

## Parameters

- `$end` (*int*): The current ending result position. Native post, term, and user queries normally calculate one-based positions. The value can be `0` when no range has been populated, including in provider-backed ACF loops.
- `$query` (`Bricks\Query`): The query instance. Use its public `$element_id` property to scope the filter to a specific loop element.

## Example usage

This example sets the ending position reported for a specific loop to `3`. It changes only the summary number; it does not limit the loop to three items.

Replace `abc123` with the loop element's raw Bricks ID, without the `brxe-` prefix or a `#`.

```php
add_filter( 'bricks/query/result_end', function( $end, $query ) {
    if ( $query->element_id === 'abc123' ) {
        // Adjust the summary's ending position only.
        return 3;
    }

    return $end;
}, 10, 2 );
```

For example, if an ACF Relationship loop returns four items, returning `3` here still renders all four in their original order. The total count remains `4`, and no additional page is fetched.

## Change the actual results

Use the [Query Loop controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) for native query limits and offsets, or [`bricks/query/result`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/) to modify fetched results.

For an ACF loop that returns an array, a result filter scoped to the loop element can use `array_slice()` to skip or limit items. This changes the returned array while preserving the saved ACF entries and the editorial order of the retained items. See the [ACF array example](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/#slice-an-acf-array).

---

# Filter: bricks/query/result_start

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/

*Filters the numeric starting result position reported by Query Results Summary. Changes summary metadata only, without offsetting or slicing results.*

The `bricks/query/result_start` filter changes the numeric starting position stored in `$query->start`. [Query Results Summary](https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/) reads this value for its `%start%` placeholder.

This filter changes summary metadata only. It does not change the returned items, skip the first item, limit the rendered cards, change the total count, or fetch another page.

## Parameters

- `$start` (*int*): The current starting result position. Native post, term, and user queries normally calculate one-based positions. The value can be `0` when no range has been populated, including in provider-backed ACF loops.
- `$query` (`Bricks\Query`): The query instance. Use its public `$element_id` property to scope the filter to a specific loop element.

## Example usage

This example adds one to the starting position reported for a specific loop. It changes only the summary number; the first item still renders.

Replace `abc123` with the loop element's raw Bricks ID, without the `brxe-` prefix or a `#`.

```php
add_filter( 'bricks/query/result_start', function( $start, $query ) {
    if ( $query->element_id === 'abc123' ) {
        // Adjust the summary's starting position only.
        return $start + 1;
    }

    return $start;
}, 10, 2 );
```

For example, if `$start` is `1`, the summary reports `2`. All returned items still render in their original order, and `%end%` and `%total%` remain unchanged.

## Change the actual results

Use the [Query Loop controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) for native query limits and offsets, or [`bricks/query/result`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/) to modify fetched results.

For an ACF loop that returns an array, a result filter scoped to the loop element can use `array_slice()` to skip or limit items. This changes the returned array while preserving the saved ACF entries and the editorial order of the retained items. See the [ACF array example](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/#slice-an-acf-array).

---

# Filter: bricks/query/run_fake

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-run_fake/

*Defines the results of a \"fake\" query execution for custom or unsupported query types. This is used when calculating filter counts or other logic that requires.*

Defines the results of a "fake" query execution for custom or unsupported query types. This is used when calculating filter counts or other logic that requires querying all potential results without pagination.

## Parameters

- `$results` (*array*): The query results array (default `[]`).
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/run_fake', function( $results, $query ) {
    // Example: Provide all results for a custom 'my_api' query type
    if ( $query->object_type === 'my_api' ) {
        // Fetch all IDs from your API
        return [ 1, 2, 3, 4, 5 ]; 
    }

    return $results;
}, 10, 2 );
```

---

# Filter: bricks/query/supress_render_content

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-supress_render_content/

*Determines whether to suppress the rendering of the query loop content. This is used by the \"Live Search\" feature to prevent rendering initial results on page.*

Determines whether to suppress the rendering of the query loop content. This is used by the "Live Search" feature to prevent rendering initial results on page load if they are going to be immediately replaced by AJAX results.

## Parameters

- `$suppress` (*bool*): Whether to suppress rendering.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/supress_render_content', function( $suppress, $query ) {
    // Example: Suppress content rendering for a specific query ID on mobile devices
    if ( $query->id === 'heavy_query' && wp_is_mobile() ) {
        return true;
    }

    return $suppress;
}, 10, 2 );
```

---

# Filter: bricks/query_api/body

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-body/

*Filters the body used by a Query API element request.*

Filters the body data used by a Query API element request before Bricks adds it to the HTTP request.

Bricks only builds a body for request methods that support one in the Query API implementation, currently `POST`.

## Parameters

- `$body_data` (string|array|null): The request body data Bricks has built.
- `$element_id` (string): The Query API element ID.
- `$query_api` (object): The Query API integration instance.

## Example usage

```php
add_filter( 'bricks/query_api/body', function( $body_data, $element_id, $query_api ) {
    return $body_data;
}, 10, 3 );
```

---

# Filter: bricks/query_api/headers

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-headers/

*Filters the headers used by a Query API element request.*

Filters the headers used by a Query API element request before Bricks sends it.

## Parameters

- `$headers` (array): HTTP request headers.
- `$element_id` (string): The Query API element ID.
- `$query_api` (object): The Query API integration instance.

## Example usage

```php
add_filter( 'bricks/query_api/headers', function( $headers, $element_id, $query_api ) {
    $headers['X-Client'] = 'my-site';

    return $headers;
}, 10, 3 );
```

---

# Filter: bricks/query_api/request_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-request_args/

*Filters the request arguments used by a Query API element.*

Filters the request arguments used by a Query API element before Bricks sends the request.

## Parameters

- `$args` (array): HTTP request arguments.
- `$element_id` (string): The Query API element ID.
- `$query_api` (object): The Query API integration instance.

## Example usage

```php
add_filter( 'bricks/query_api/request_args', function( $args, $element_id, $query_api ) {
    $args['timeout'] = 20;

    return $args;
}, 10, 3 );
```

---

# Filter: bricks/query_api/total_pages

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_api-total_pages/

*Filters the total number of pages calculated for an external API query loop. This is useful when the API response structure for pagination doesn't match Bricks'.*

Filters the total number of pages calculated for an external API query loop. This is useful when the API response structure for pagination doesn't match Bricks' standard extraction logic.

## Parameters

- `$total_pages` (*int*): The calculated total number of pages.
- `$element_id` (*string*): The ID of the query element.
- `$query_api` (*object*): The `Bricks\Integrations\Query\Query_API` instance.

## Example usage

```php
add_filter( 'bricks/query_api/total_pages', function( $total_pages, $element_id, $query_api ) {
    // Example: Set total pages for a specific API query
    if ( $element_id === 'my_api_loop' ) {
        // Assume you stored the total in a custom property or need a fixed value
        return 10;
    }

    return $total_pages;
}, 10, 3 );
```

---

# Filter: bricks/query_filters/custom_field_index_rows

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-custom_field_index_rows/

*Filters the index rows generated for a custom field in the Query Filters system. This allows providers (like ACF, Meta Box) or custom code to handle how complex.*

Filters the index rows generated for a custom field in the Query Filters system. This allows providers (like ACF, Meta Box) or custom code to handle how complex field data is indexed for filtering.

## Parameters

- `$rows` (*array*): Array of index rows. Each row is an associative array representing a filterable value.
- `$object_id` (*int*): The ID of the object (post, term, user) being indexed.
- `$meta_key` (*string*): The meta key of the custom field.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$object_type` (*string*): The type of object (`post`, `term`, `user`).

## Example usage

```php
add_filter( 'bricks/query_filters/custom_field_index_rows', function( $rows, $object_id, $meta_key, $provider, $object_type ) {
    // Example: Index a custom serialized field
    if ( $meta_key === 'my_serialized_field' ) {
        $value = get_post_meta( $object_id, $meta_key, true );
        // ... parse value ...
        $rows[] = [
            'filter_value' => 'parsed_value',
            'filter_value_display' => 'Display Value',
            // ... other required fields ...
        ];
    }

    return $rows;
}, 10, 5 );
```

---

# Filter: bricks/query_filters/datepicker_custom_field_meta_query

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-datepicker_custom_field_meta_query/

*Filter the custom-field meta query generated by a Datepicker filter, with notes on separate start and end fields.*

Filters the `meta_query` generated for a datepicker filter targeting a custom field. This allows you to customize how date comparisons are handled (e.g., date formats, range logic) for specific fields.

Starting with **Bricks 2.5**, use the built-in [separate start and end field settings](https://academy.bricksbuilder.io/builder/elements/filter/filter-datepicker/#separate-date-fields) for supported WordPress, ACF, Meta Box, and JetEngine fields on posts, terms, or users. Each endpoint is resolved independently. With a separate end field configured, Bricks also applies query-level interval validation and containment checks. Changing the meta query through this hook does not remove those checks or provide an overlap-matching mode.

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => '...', 'type' => 'DATE']`).
- `$filter` (*array*): The active filter data, including `settings` and the selected `value`.
- `$provider` (*string*): The field provider, such as `none` for WordPress metadata, `acf`, `metabox`, or `jetengine`.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

For a Datepicker using the native `event_start` meta key, require the same object's `event_status` field to contain `published`. The existing date conditions remain grouped together. Priority `20` runs after the built-in provider callbacks.

Add the filter to your child theme's `functions.php` file or a custom plugin.

```php
add_filter( 'bricks/query_filters/datepicker_custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    if ( ! in_array( $provider, [ '', 'none' ], true ) ||
        ( $filter['settings']['customFieldKey'] ?? '' ) !== 'event_start' ) {
        return $meta_query;
    }

    return [
        'relation' => 'AND',
        $meta_query,
        [
            'key'     => 'event_status',
            'value'   => 'published',
            'compare' => '=',
        ],
    ];
}, 20, 4 );
```

---

# Filter: bricks/query_filters/custom_field_meta_query

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-custom_field_meta_query/

*Filters the metaquery generated for a custom field filter in the Query Filters system. This allows you to customize how the filtering logic is applied to the.*

Filters the `meta_query` generated for a custom field filter in the Query Filters system. This allows you to customize how the filtering logic is applied to the main query.

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => '...', 'compare' => '...']`).
- `$filter` (*array*): The active filter data, including settings and selected values.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/query_filters/custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    // Example: Change comparison to 'LIKE' for a specific field
    if ( $filter['settings']['fieldName'] === 'my_text_field' ) {
        $meta_query['compare'] = 'LIKE';
    }

    return $meta_query;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/default_value

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-default_value/

*Supply or disable initial query-filter selections using the original page, product, or archive context.*

Available in **Bricks 2.5**, `bricks/query_filters/default_value` filters the initial selection before the target query runs. Use it when a default depends on PHP logic, such as choosing one material from the current product's terms.

For defaults that only need a fixed value or dynamic data tag, use the builder's [Default value controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values).

## Parameters

- `$value` (*mixed*): The configured default after dynamic data has resolved, or `null` when no default is configured. Numeric and date ranges receive a two-item endpoint array. Geolocation receives an associative coordinate array when its default-location toggle is enabled.
- `$context` (*array*): The filter identity, resolved settings, and original page context.

| Context key | Value |
| --- | --- |
| `filter_id` | Physical filter element ID. |
| `definition_id` | Linked global filter ID, or an empty string for an independent filter. |
| `query_id` | Rendered target query ID, including an instance suffix where applicable. |
| `filter_type` | Element name, such as `filter-radio` or `filter-geolocation`. |
| `filter_action` | `filter`, `sort`, or `per_page`. |
| `settings` | Effective element settings, including shared global-filter settings. |
| `post_id` | Original page, product, or preview post ID. Zero for archive contexts. |
| `queried_object` | Original WordPress queried object, or the builder preview object. |

## Return values

Return `$value` to keep the configured default or `null` to disable it. The hook can supply a default even when no builder default is configured.

| Filter | Return format |
| --- | --- |
| Radio, single Select, Search, sort, or results per page | A scalar value. Choice values must match a configured option, such as `cotton`, `title_ASC`, or `20`. |
| Checkbox or multiple Select | An array of exact option values, such as `['cotton', 'wool']`. |
| Range | Two numeric endpoints, such as `[20, 100]`. Use `''` for an endpoint that should use the original range boundary. |
| Single Datepicker | A date string in `YYYY-MM-DD` format. |
| Datepicker range | Two dates in `YYYY-MM-DD` format, with both endpoints present. |
| Geolocation | An array with `lat` and `lng`, plus optional `label`, `radius`, and `unit` (`km` or `mi`). Omitted radius and unit use the filter settings. |

Returned values undergo the same validation as builder defaults. Return resolved values rather than dynamic data expressions. Invalid or unavailable choices, invalid coordinates, and invalid range endpoints are ignored and produce builder-preview warnings. Geolocation still requires at least one enabled visitor search method, and its origin is normalized to `default`.

## Example: Select one material from the current product

This example selects the product's material with the lowest term ID. It applies only to a Radio or single Select filter using the `pa_material` taxonomy on a single product page.

```php
add_filter( 'bricks/query_filters/default_value', function( $value, $context ) {
    $settings = $context['settings'];

    if ( ! in_array( $context['filter_type'], [ 'filter-radio', 'filter-select' ], true ) ||
        $context['filter_action'] !== 'filter' ||
        ( $settings['filterSource'] ?? '' ) !== 'taxonomy' ||
        ( $settings['filterTaxonomy'] ?? '' ) !== 'pa_material' ||
        ( ! empty( $settings['choicesJs'] ) && ! empty( $settings['enableMultiple'] ) ) ||
        ! $context['post_id'] ||
        get_post_type( $context['post_id'] ) !== 'product' ) {
        return $value;
    }

    $slugs = wp_get_post_terms( $context['post_id'], 'pa_material', [
        'fields'  => 'slugs',
        'orderby' => 'term_id',
        'order'   => 'ASC',
    ] );

    return is_wp_error( $slugs ) || ! $slugs ? null : $slugs[0];
}, 10, 2 );
```

`post_id` refers to the original product even when the filter lives in a template. For an independent filter, check `filter_id` to limit the callback to one element. For linked desktop and mobile copies, check `definition_id` to address the shared filter.

## Initialization and state

The hook runs once per rendered query/filter group during initialization, including groups without a configured default. Linked elements targeting the same query share one evaluation. Reusing a definition on another query creates a separate evaluation. Resolved defaults are request-local and do not overwrite the saved settings or expressions.

A recognized filter URL restores the complete selection across URL-enabled queries on the page. Omitted filters remain clear, and an explicit empty parameter also suppresses defaults. Queries with URL parameters disabled still apply defaults.

Defaults apply before the first query, including Submit-based filters. Reset clears defaults while respecting exclusions. AJAX updates, pagination, Load more, and history restoration do not reapply them. A fresh visit or reload without filter parameters applies defaults again. See [default state behavior](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-state).

---

# Filter: bricks/query_filters/element_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-element_data/

*Filters the data for a filter element before it is saved to the internal index table (bricksfilterelements). This allows plugins to attach extra metadata (like.*

Filters the data for a filter element before it is saved to the internal index table (`bricks_filter_elements`). This allows plugins to attach extra metadata (like language) to the filter configuration.

## Parameters

- `$element_data` (*array*): The data array to be saved (e.g., `filter_id`, `settings`, `post_id`, `language`).
- `$element` (*array*): The raw element data from the builder.
- `$post_id` (*int*): The ID of the post/template containing the element.

## Example usage

```php
add_filter( 'bricks/query_filters/element_data', function( $element_data, $element, $post_id ) {
    // Example: Add a custom property to the saved data
    $element_data['my_custom_prop'] = 'value';

    return $element_data;
}, 10, 3 );
```

---

# Filter: bricks/query_filters/filter_query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-filter_query_vars/

*Filters the query variables generated by an active filter element before they are applied to the query loop. This allows you to customize how specific filters.*

Filters the query variables generated by an active filter element before they are applied to the query loop. This allows you to customize how specific filters affect the query.

## Parameters

- `$query_vars` (*array*): The `WP_Query` arguments generated by this filter.
- `$filter` (*array*): The active filter data (settings, selected values).
- `$query_id` (*string*): The ID of the query loop being filtered.
- `$filter_index` (*int*): The index of this filter in the active filters list.

## Example usage

```php
add_filter( 'bricks/query_filters/filter_query_vars', function( $query_vars, $filter, $query_id, $filter_index ) {
    // Example: Add extra query args for a specific filter
    if ( $filter['settings']['fieldName'] === 'my_special_filter' ) {
        $query_vars['post_status'] = 'publish';
    }

    return $query_vars;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/get_filter_object_ids

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-get_filter_object_ids/

*Filters the object IDs used to build query filter counts.*

Filters the object IDs used to build query filter counts. Use it when an integration needs to supply or alter the base object IDs for a query/filter source.

## Parameters

- `$all_object_ids` (array): The object IDs Bricks has collected.
- `$query_id` (string): The query element ID.
- `$query_type` (string): The query type being processed.
- `$source` (string): The filter source.

## Example usage

```php
add_filter( 'bricks/query_filters/get_filter_object_ids', function( $all_object_ids, $query_id, $query_type, $source ) {
    return $all_object_ids;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/index_args

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_args/

*Filters the query arguments used by the Query Filters indexer to find objects (posts, terms, users) that need to be indexed.*

Filters the query arguments used by the Query Filters indexer to find objects (posts, terms, users) that need to be indexed.

## Parameters

- `$args` (*array*): The query arguments (for `WP_Query`, `WP_Term_Query`, or `WP_User_Query`).
- `$filter_source` (*string*): The source of the filter data (e.g., `wpField`, `customField`).
- `$filter_settings` (*array*): The settings of the filter element being indexed.
- `$query_type` (*string*): The type of query being run (`wp_query`, `wp_term_query`, `wp_user_query`).

## Example usage

```php
add_filter( 'bricks/query_filters/index_args', function( $args, $filter_source, $filter_settings, $query_type ) {
    // Example: Include 'private' posts when indexing
    if ( $query_type === 'wp_query' ) {
        $args['post_status'] = [ 'publish', 'private' ];
    }

    return $args;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/index_post/meta_exists

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_post-meta_exists/

*Determines if a custom field (meta key) exists for a specific post during the indexing process. This is used when a third-party provider (like ACF or Meta Box).*

Determines if a custom field (meta key) exists for a specific post during the indexing process. This is used when a third-party provider (like ACF or Meta Box) is selected, to avoid indexing empty or non-existent fields.

## Parameters

- `$exists` (*bool*): Whether the meta key exists. Default is `false`.
- `$post_id` (*int*): The ID of the post being checked.
- `$meta_key` (*string*): The meta key of the custom field.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).

## Example usage

```php
add_filter( 'bricks/query_filters/index_post/meta_exists', function( $exists, $post_id, $meta_key, $provider ) {
    // Example: Custom check for a serialized meta field
    if ( $meta_key === 'my_serialized_data' ) {
        $data = get_post_meta( $post_id, $meta_key, true );
        return ! empty( $data );
    }

    return $exists;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/index_post/wcField

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_post-wcfield/

*A specialized hook for indexing WooCommerce product fields (like price, stock status, rating) when a product is saved. This allows the Query Filters index to.*

A specialized hook for indexing WooCommerce product fields (like price, stock status, rating) when a product is saved. This allows the Query Filters index to stay updated with WooCommerce product data.

## Parameters

- `$rows` (*array*): Array of index rows to be inserted.
- `$post_id` (*int*): The ID of the product (post) being indexed.
- `$elements` (*array*): Array of filter elements targeting this product.

## Example usage

```php
add_filter( 'bricks/query_filters/index_post/wcField', function( $rows, $post_id, $elements ) {
    // This filter is typically used internally by Bricks to handle WooCommerce fields.
    // However, you could hook into it to index custom WooCommerce product data.
    
    // Example: Index a custom product property
    $product = wc_get_product( $post_id );
    if ( $product ) {
        // ... generate index rows ...
    }

    return $rows;
}, 10, 3 );
```

---

# Filter: bricks/query_filters/index_post/{source}

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_post-source/

*Filters index rows generated for a post when the filter source is unknown or provided by an integration.*

Filters the index rows generated for a post when the filter source is unknown or handled by a third-party provider. The `{$source}` portion of the hook name corresponds to the filter source (e.g., `wcField` or a custom source).

## Parameters

- `$rows` (*array*): Array of index rows to be inserted into the database. Default is `[]`.
- `$post_id` (*int*): The ID of the post being indexed.
- `$elements` (*array*): Array of filter elements targeting this post.

Each row must include `filter_id`, `object_id`, `object_type`, `filter_value`, `filter_value_display`, `filter_value_id`, and `filter_value_parent`.

## Example usage

```php
add_filter( 'bricks/query_filters/index_post/my_custom_source', function( $rows, $post_id, $elements ) {
    foreach ( $elements as $element ) {
        // Calculate filter value for this post
        $value = get_post_meta( $post_id, 'my_custom_field', true );

        if ( $value ) {
            $rows[] = [
                'filter_id'            => $element['filter_id'],
                'object_id'            => $post_id,
                'object_type'          => 'post',
                'filter_value'         => $value,
                'filter_value_display' => $value,
                'filter_value_id'      => 0,
                'filter_value_parent'  => 0,
            ];
        }
    }

    return $rows;
}, 10, 3 );
```

---

# Filter: bricks/query_filters/index_user/meta_exists

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_user-meta_exists/

*Determines if a custom field (meta key) exists for a specific user during the indexing process. This is used when a third-party provider (like ACF or Meta Box).*

Determines if a custom field (meta key) exists for a specific user during the indexing process. This is used when a third-party provider (like ACF or Meta Box) is selected, to avoid indexing empty or non-existent fields for users.

## Parameters

- `$exists` (*bool*): Whether the meta key exists. Default is `false`.
- `$user_id` (*int*): The ID of the user being checked.
- `$meta_key` (*string*): The meta key of the custom field.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).

## Example usage

```php
add_filter( 'bricks/query_filters/index_user/meta_exists', function( $exists, $user_id, $meta_key, $provider ) {
    // Example: Custom check for a serialized meta field on a user
    if ( $meta_key === 'user_custom_data' ) {
        $data = get_user_meta( $user_id, $meta_key, true );
        return ! empty( $data );
    }

    return $exists;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/range_custom_field_meta_query

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-range_custom_field_meta_query/

*Filters the metaquery generated for a range filter (slider) targeting a custom field. This allows you to customize how the range comparison is performed (e.g.,.*

Filters the `meta_query` generated for a range filter (slider) targeting a custom field. This allows you to customize how the range comparison is performed (e.g., handling decimal values, changing the data type).

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => [min, max], 'compare' => 'BETWEEN', 'type' => 'NUMERIC']`).
- `$filter` (*array*): The active filter data, including settings and selected min/max values.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/query_filters/range_custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    // Example: Change type to 'DECIMAL' for precise price filtering
    if ( $filter['settings']['fieldName'] === 'product_price' ) {
        $meta_query['type'] = 'DECIMAL(10,2)';
    }

    return $meta_query;
}, 10, 4 );
```

---

# Filter: bricks/query_filters/sort_query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-sort_query_vars/

*Filters the query variables generated by an active \"Sort\" filter element. This allows you to implement custom sorting logic (e.g., sorting by a custom meta key.*

Filters the query variables generated by an active "Sort" filter element. This allows you to implement custom sorting logic (e.g., sorting by a custom meta key or a calculated value).

## Parameters

- `$query_vars` (*array*): The `WP_Query` arguments generated by the sort filter (e.g., `['orderby' => '...', 'order' => '...']`).
- `$filter` (*array*): The active filter data, including selected sort option.
- `$query_id` (*string*): The ID of the query loop being sorted.
- `$filter_index` (*int*): The index of this filter in the active filters list.

## Example usage

```php
add_filter( 'bricks/query_filters/sort_query_vars', function( $query_vars, $filter, $query_id, $filter_index ) {
    // Example: Custom sort by 'popularity'
    if ( $filter['value'] === 'popularity' ) {
        $query_vars['orderby'] = 'meta_value_num';
        $query_vars['meta_key'] = 'post_views_count';
        $query_vars['order'] = 'DESC';
    }

    return $query_vars;
}, 10, 4 );
```

---

# Filter: bricks/query_filters_cf_integration/register_providers

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_cf_integration-register_providers/

*Filters custom field providers used by query filter integrations.*

Filters custom field providers used by query filter integrations before Bricks registers their provider classes.

Bricks maps each provider key to a class named `Bricks\Integrations\Query_Filters\Field_{Provider}` using `ucfirst( $provider )`. The default provider keys are `acf` and `metabox`.

## Parameters

- `$providers` (array): Provider keys registered for query filter custom field integration.

## Example usage

```php
add_filter( 'bricks/query_filters_cf_integration/register_providers', function( $providers ) {
    $providers[] = 'myprovider';

    return $providers;
} );
```

---

# Filter: bricks/query_filters_indexer/post/{filter_source}

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_indexer-post-filter_source/

*Filters index rows generated by the Query Filters Indexer for an unknown or integration-provided filter source.*

Filters the index rows generated for a post by the Query Filters Indexer when processing a specific filter job. The `{$filter_source}` portion of the hook name corresponds to the filter source (e.g., `wcField` or a custom source).

## Parameters

- `$rows` (*array*): Array of index rows to be inserted. Default is `[]`.
- `$post` (*WP_Post|int*): The post object or ID being indexed.
- `$filter_id` (*string*): The ID of the filter element.
- `$filter_settings` (*array*): The settings of the filter element.

Each row must include `filter_id`, `object_id`, `object_type`, `filter_value`, `filter_value_display`, `filter_value_id`, and `filter_value_parent`.

## Example usage

```php
add_filter( 'bricks/query_filters_indexer/post/my_custom_source', function( $rows, $post, $filter_id, $filter_settings ) {
    // Generate index rows for custom logic
    $value = get_post_meta( $post->ID, 'my_custom_field', true );

    if ( $value ) {
        $rows[] = [
            'filter_id'            => $filter_id,
            'object_id'            => $post->ID,
            'object_type'          => 'post',
            'filter_value'         => $value,
            'filter_value_display' => $value,
            'filter_value_id'      => 0,
            'filter_value_parent'  => 0,
        ];
    }

    return $rows;
}, 10, 4 );
```

---

# Filter: bricks/query_filters_indexer/post/wcField

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_indexer-post-wcfield/

*A specialized hook for the Query Filters Indexer to generate index rows for WooCommerce product fields (like price, stock status, rating) when processing a.*

A specialized hook for the Query Filters Indexer to generate index rows for WooCommerce product fields (like price, stock status, rating) when processing a filter job.

## Parameters

- `$rows` (*array*): Array of index rows to be inserted. Default is `[]`.
- `$post` (*WP_Post|int*): The product object or ID being indexed.
- `$filter_id` (*string*): The ID of the filter element.
- `$filter_settings` (*array*): The settings of the filter element.

## Example usage

```php
add_filter( 'bricks/query_filters_indexer/post/wcField', function( $rows, $post, $filter_id, $filter_settings ) {
    // This filter is typically used internally by Bricks to handle WooCommerce fields.
    // However, you could hook into it to index custom WooCommerce product data via the 'wcField' source.
    
    // Check if indexing a specific custom WC field
    if ( isset( $filter_settings['sourceFieldType'] ) && $filter_settings['sourceFieldType'] === 'my_custom_wc_field' ) {
        // ... generate and return rows ...
    }

    return $rows;
}, 10, 4 );
```

---

# Filter: bricks/query_filters_indexer/validate_job_settings

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters_indexer-validate_job_settings/

*Validates the settings of a filter job before the Query Filters Indexer processes it. This is used for unknown or custom filter sources to ensure they have the.*

Validates the settings of a filter job before the Query Filters Indexer processes it. This is used for unknown or custom filter sources to ensure they have the necessary configuration.

## Parameters

- `$validate` (*bool*): Whether the settings are valid. Default is `false` for unknown sources.
- `$filter_source` (*string*): The source of the filter data (e.g., `wcField`, `customSource`).
- `$filter_settings` (*array*): The settings of the filter element.

## Example usage

```php
add_filter( 'bricks/query_filters_indexer/validate_job_settings', function( $validate, $filter_source, $filter_settings ) {
    // Validate settings for a custom source
    if ( $filter_source === 'my_custom_source' ) {
        // Check if required 'my_key' setting is present
        return ! empty( $filter_settings['my_key'] );
    }

    return $validate;
}, 10, 3 );
```

---

# Filter: bricks/remote_post

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-remote_post/

*Filters the arguments passed to wpremotepost() when Bricks performs a remote POST request (e.g., verifying license, submitting form data to webhook).*

Filters the arguments passed to `wp_remote_post()` when Bricks performs a remote POST request (e.g., verifying license, submitting form data to webhook).

## Parameters

- `$args` (*array*): Array of arguments for `wp_remote_post()` (e.g., `body`, `timeout`, `sslverify`).
- `$url` (*string*): The URL being requested.

## Example usage

```php
add_filter( 'bricks/remote_post', function( $args, $url ) {
    // Example: Add custom headers to webhook requests
    if ( strpos( $url, 'webhook.example.com' ) !== false ) {
        $args['headers']['X-Custom-Header'] = 'my-value';
    }

    return $args;
}, 10, 2 );
```

---

# Filter: bricks/remote_get

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-remote_get/

*Filters the arguments passed to wpremoteget() when Bricks performs a remote GET request (e.g., fetching templates, community library).*

Filters the arguments passed to `wp_remote_get()` when Bricks performs a remote GET request (e.g., fetching templates, community library).

## Parameters

- `$args` (*array*): Array of arguments for `wp_remote_get()` (e.g., `timeout`, `sslverify`).
- `$url` (*string*): The URL being requested.

## Example usage

```php
add_filter( 'bricks/remote_get', function( $args, $url ) {
    // Example: Increase timeout for specific API requests
    if ( strpos( $url, 'api.example.com' ) !== false ) {
        $args['timeout'] = 60;
    }

    return $args;
}, 10, 2 );
```

---

# Filter: bricks/render_footer

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_footer/

*Filters the rendered HTML of the Bricks footer template. This allows you to wrap the footer in custom markup or modify its output before it is echoed to the.*

Filters the rendered HTML of the Bricks footer template. This allows you to wrap the footer in custom markup or modify its output before it is echoed to the page.

## Parameters

- `$footer_html` (*string*): The rendered HTML of the footer.

## Example usage

```php
add_filter( 'bricks/render_footer', function( $footer_html ) {
    // Example: Wrap the footer in a custom container
    return '<div class="custom-footer-wrapper">' . $footer_html . '</div>';
} );
```

---

# Filter: bricks/render_header

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_header/

*Filters the rendered HTML of the Bricks header template. This allows you to wrap the header in custom markup or modify its output before it is echoed to the.*

Filters the rendered HTML of the Bricks header template. This allows you to wrap the header in custom markup or modify its output before it is echoed to the page.

## Parameters

- `$header_html` (*string*): The rendered HTML of the header.

## Example usage

```php
add_filter( 'bricks/render_header', function( $header_html ) {
    // Example: Add a notification bar before the header
    $notification = '<div class="notification-bar">Welcome!</div>';
    
    return $notification . $header_html;
} );
```

---

# Filter: bricks/render_with_bricks

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-render_with_bricks/

*Determines whether a specific post or page should be rendered using Bricks. If this filter returns false, Bricks will yield control to the default WordPress.*

Determines whether a specific post or page should be rendered using Bricks. If this filter returns `false`, Bricks will yield control to the default WordPress template loader or another builder.

## Parameters

- `$render` (*bool|null*): Whether to render with Bricks. Default is `null` (Bricks decides based on settings).
- `$post_id` (*int*): The ID of the post being checked.

## Example usage

```php
add_filter( 'bricks/render_with_bricks', function( $render, $post_id ) {
    // Example: Disable Bricks rendering for posts with a specific meta value
    if ( get_post_meta( $post_id, 'disable_bricks', true ) ) {
        return false;
    }

    return $render;
}, 10, 2 );
```

---

# Filter: bricks/resolve_attachment_id

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-resolve_attachment_id/

*Filters an attachment ID before Bricks uses it for frontend output.*

Filters an attachment ID before Bricks uses it for frontend output. This is useful for multilingual plugins or media integrations that need to resolve translated attachment IDs.

Bricks casts the filtered value with `absint()`. If the filtered value is empty or invalid, Bricks keeps the original attachment ID so image output does not break.

## Parameters

- `$attachment_id` (int): The attachment post ID Bricks is about to use.

## Example usage

```php
add_filter( 'bricks/resolve_attachment_id', function( $attachment_id ) {
    return $attachment_id;
} );
```

---

# Filter: bricks/rtl_languages

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-rtl_languages/

*Filters the list of language codes that Bricks considers right-to-left (RTL). This affects the layout direction of the builder interface when a specific locale.*

Filters the list of language codes that Bricks considers right-to-left (RTL). This affects the layout direction of the builder interface when a specific locale is active.

## Parameters

- `$languages` (*array*): Array of RTL language codes (e.g., `['ar', 'he', 'fa']`).

## Example usage

```php
add_filter( 'bricks/rtl_languages', function( $languages ) {
    // Add a custom RTL language code
    $languages[] = 'abc';

    return $languages;
} );
```

---

# Filter: bricks/security_check_before_save/new_elements

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-security_check_before_save-new_elements/

*Filters the array of new elements before they are saved to the database, specifically during the security check process (e.g., when validating {echo:} tags)..*

Filters the array of new elements before they are saved to the database, specifically during the security check process (e.g., when validating `{echo:}` tags). This allows you to inspect or modify the element data before it persists.

## Parameters

- `$new_elements` (*array*): Array of new element data structures.
- `$old_elements_indexed` (*array*): Array of existing elements, indexed by their ID, for comparison.

## Example usage

```php
add_filter( 'bricks/security_check_before_save/new_elements', function( $new_elements, $old_elements_indexed ) {
    // Example: Loop through new elements and log changes
    foreach ( $new_elements as $element ) {
        // Custom logic here
    }

    return $new_elements;
}, 10, 2 );
```

---

# Filter: bricks/support_masonry_element

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-support_masonry_element/

*Filters the list of element names that support the Masonry layout option. By default, this includes section, container, block, and div.*

Filters the list of element names that support the Masonry layout option. By default, this includes `section`, `container`, `block`, and `div`.

## Parameters

- `$element_names` (*array*): Array of element names (slugs) that support Masonry.

## Example usage

```php
add_filter( 'bricks/support_masonry_element', function( $element_names ) {
    // Enable Masonry support for a custom element
    $element_names[] = 'my-custom-grid';

    return $element_names;
} );
```
