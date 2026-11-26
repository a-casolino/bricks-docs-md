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

# Filter: bricks/query/result

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result/

*Modify fetched Bricks query results, including sorting posts or slicing an array returned by an ACF loop.*

Available since Bricks 1.8, `bricks/query/result` lets you modify fetched query results before the loop renders them. The result type depends on the query: a native post query returns a `WP_Query` object, while an ACF loop can return an array. Use [`bricks/query/run`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-run/) when adding a custom query type.

## Sort post results

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

## Slice an ACF array

For an ACF Relationship loop that returns an array, use a result filter scoped to the loop element to skip or limit items. Replace `abc123` with the loop element's raw Bricks ID, without the `brxe-` prefix or a `#`.

This example skips the first item and returns up to three of the remaining items:

```php
add_filter( 'bricks/query/result', function( $result, $query ) {
    if ( $query->element_id !== 'abc123' || ! is_array( $result ) ) {
        return $result;
    }

    return array_slice( $result, 1, 3 );
}, 10, 2 );
```

With four items in the ACF array, the loop renders the second, third, and fourth items in their existing editorial order. The saved ACF entries remain unchanged. To keep the first item and display up to three items, use `array_slice( $result, 0, 3 )` instead.

Slicing here does not automatically recalculate the query's total count, maximum number of pages, or summary positions. If the loop has a summary or pagination, keep that metadata consistent with the intended behavior using [`bricks/query/result_count`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_count/), [`bricks/query/result_max_num_pages`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-result_max_num_pages/), [`bricks/query/result_start`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/), and [`bricks/query/result_end`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/). A fixed slice does not fetch another page.

For native query limits and offsets, use the [Query Loop controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/). The `result_start` and `result_end` filters change summary metadata only; they do not slice the results.

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

Section templates assigned to action hooks use a separate condition evaluator. Since Bricks 2.5, use [`bricks/section_template/run_on_hook`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-section_template-run_on_hook/) to change their injection decisions.

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

---

# Filter: bricks/terms/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars/

*Bricks terms query variables can be manipulated before the query runs like so:*

Bricks terms query variables can be manipulated before the query runs like so:

```php
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = 23; // Exclude term id 23

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_Term_Query](https://developer.wordpress.org/reference/classes/wp_term_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID
- `$element_name` is a string containing the element name (`@since 1.11.1`)

## Example 1: Exclude the current term from the query {#exclude-current-term}

Inside a term archive page, to exclude the current term from the query:

```php
// Exclude current term from the terms query loop on term archive pages.
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'uxtkgn' ) {
        return $query_vars;
    }

    $query_vars['exclude'] = get_queried_object_id();

    return $query_vars;
}, 10, 4 );
```

where `uxtkgn` is the Bricks ID of the element on which query loop is enabled.

## Example 2: Get terms assigned to a post {#get-terms-assigned-to-a-post}

In this example, we would like to get only the terms assigned to a specific post ID (the same as the WordPress function [`wp_get_object_terms()`](https://developer.wordpress.org/reference/functions/wp_get_object_terms/) output):

```php
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'mjvhur' ) {
        return $query_vars;
    }

    $query_vars['object_ids'] = get_the_ID();

    return $query_vars;
}, 10, 4 );
```

---

# Filter: bricks/setup/control_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/

*Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:*

Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:

- Template Types (e.g. Header, Footer, Single, Section...)
- Background position, repeat, attachment or size
- Button sizes
- Button or Heading styles
- Border styles
- Font weight and style
- CSS position
- Query types (e.g. Posts, Terms, Users, ..)
- Query order by, compare, operator and value type
- Image Sizes
- Taxonomies
- User roles

To manage any of these options or add new ones, use the WP hook `bricks/setup/control_options` like so:

```php
add_filter( 'bricks/setup/control_options', function( $control_options ) {
    $control_options['templateTypes']['my_template_type'] = esc_html__( 'My Template Type', 'my-plugin' );

    return $control_options;
} );
```

Note: the above example adds a new template type. To learn about other Bricks controls, visit the [Controls section](https://academy.bricksbuilder.io/developer/controls/).

---

# Filter: bricks/use_duplicate_content

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-use_duplicate_content/

*Duplicate content is available for all users with the editpost capability. Use this feature to duplicate any post or page containing Bricks data to ensure.*

Duplicate content is available for all users with the `edit_post` capability. Use this feature to duplicate any post or page containing Bricks data to ensure Bricks IDs are not duplicated. The duplicate option is also available for posts without Bricks data, allowing you to duplicate standard posts without the need for a third-party plugin.

![](https://academy.bricksbuilder.io/assets/bricks-duplicate-content-setting-example.png)

In **Bricks > Settings**, you can configure the duplicate content behavior:

![](https://academy.bricksbuilder.io/assets/bricks-duplicate-content-setting.png)

**Enable**: Duplicate content is available for all posts.
**Disable globally**: Duplicate content is disabled for all posts.
**Disable for WordPress Data**: Duplicate content is disabled for posts that do not use Bricks data.

This `bricks/use_duplicate_content` hook provides an additional layer of customization, enabling you to implement more complex logic based on your specific requirements. `(@since 1.12)`

## Parameters

**`$use`** *(bool)*

- The current decision on whether duplicate content is allowed. Default is based on settings and user capabilities.

**`$post_id`** *(int)*

- The ID of the post being checked.

**`$setting`** *(string)*

- The value in Bricks > Settings. Which can be `enable`, `disabled_all`, or `disable_wp`

## Return Value

This filter expects a boolean value:

- `true` to allow duplicate content for the particular post.
- `false` to disallow duplicate content for the particular post.

## Example Usage

Follow setting logic + ensure the user is admin

```php
add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Only allow if current has user administrative privileges
  $has_admin_cap = current_user_can( 'manage_options' );

  // Fulfilled the condition
  return $use && $has_admin_cap;
}, 10, 3 );
```

Follow setting logic + exclude post type for ACF or MB

```php
add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Check if the post type is 'acf-field-group' or 'mb-post-type
  $post_type = get_post_type( $post_id );
  $exclude_post_types = [ 'acf-field-group', 'mb-post-type' ];

  // Fulfilled the condition
  return $use && ! in_array( $post_type, $exclude_post_types, true );
}, 10, 3 );
```

---

# Filter: bricks/users/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-users-query_vars/

*Bricks users query variables can be manipulated before the query runs like so:*

Bricks users query variables can be manipulated before the query runs like so:

```php
add_filter( 'bricks/users/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = [ 2, 5 ]; // Exclude users id 2 and 5

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_User_Query](https://developer.wordpress.org/reference/classes/wp_user_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID
- `$element_name` is a string containing the element name (`@since 1.11.1`)

---

# Filter: builder/settings/{type}/controls_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-builder-settings-type-controls_data/

*Register custom controls for the Bricks Page Settings or Template Settings panels in the builder.*

This filter allows you to add new controls to the Page Settings or Template Settings panels in the builder.

To manage the **Template Settings** controls use the `builder/settings/template/controls_data` hook like so:

```php
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Do something

  return $data;
} );
```

To manage the **Page Settings** controls use the `builder/settings/page/controls_data` hook like so:

```php
add_filter( 'builder/settings/page/controls_data', function( $data ) {
  // Do something

  return $data;
} );
```

**Example: Add a control to select the user roles in the author archive template type template condition**

```php
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Get all the site user roles
  $all_roles = wp_roles()->roles;

  $roles = [];

  foreach ( $all_roles as $role => $role_data ) {
    $roles[ $role ] = $role_data['name'];
  }

  // Add control to select the user roles for an author archive template type
  $data['controls']['templateConditions']['fields']['archiveAuthorRoles'] = [
    'type'        => 'select',
    'label'       => esc_html__( 'Author roles', 'bricks' ),
    'options'     => $roles,
    'multiple'    => true,
    'placeholder' => esc_html__( 'Select role', 'bricks' ),
    'description' => esc_html__( 'Leave empty to apply template to all roles.', 'bricks' ),
    'required'    => [ 'archiveType', '=', 'author' ],
  ];

  return $data;
} );
```

---

# Filter: bricks/builder/color_palette

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-color-palette/

*Place and customize the following filter to display a different default color palette for the color control.*

Place and customize the following filter to display a different default color palette for the color control.

```php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add an individual color
    $colors[] = [
      'hex' => '#3ce77b',
      'rgb' => 'rgba(60, 231, 123, 0.56)',
    ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```

---

# Filter: bricks/builder/save_messages

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages/

*Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks.*

Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks.

```php
add_filter( 'bricks/builder/save_messages', function( $messages ) {
  // Option #1: Append individual save message to existing message collection
    $messages[] = 'Yasss';

  // Option #2: Replace all existing builder save messages
    $messages = [
      'Done',
      'Cool',
      'High five!',
    ];

  return $messages;
} );
```

---

# Filter Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/filters/

*Documented Bricks filter hooks for builder settings, rendering, queries, authentication, code execution, and frontend behavior.*

These are all documented Bricks filter hooks:

---

# Filter: bricks/builder/standard_fonts

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-standard-fonts/

*Place and customize the following filter to display a different set of web-safe fonts in the typography control.*

Place and customize the following filter to display a different set of web-safe fonts in the typography control.

```php
add_filter( 'bricks/builder/standard_fonts', function( $standard_fonts ) {
  // Option #1: Add individual standard font
  $standard_fonts[] = 'Verdana';

  // Option #2: Replace all standard fonts
  $standard_fonts = [
    'Georgia',
    'Times New Roman',
    'Verdana',
  ];

  return $standard_fonts;
} );
```
