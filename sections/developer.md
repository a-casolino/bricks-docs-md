# Bricks Builder Documentation: Developer

<!-- content-sha256: 127818d8a8e04cf83e7e69496af0a0dc23f9aa4b836ced45eebaefde31388214 -->
<!-- content last changed: 2026-10-13 20:16 UTC -->

Unofficial Markdown export of the Bricks Builder Academy (https://academy.bricksbuilder.io/), refreshed daily. Content © Bricks. 333 pages.

## Table of contents

- [Developer](#developer)
    - [Create Your Own Dynamic Data Tag](#developer-dynamic-data-create-your-own-dynamic-data-tag)
    - [Create Your Own Elements](#developer-elements-create-your-own-elements)
    - [Function: bricks_render_dynamic_data](#developer-functions-function-bricks-render-dynamic-data)
    - [Align Items Control (Flexbox)](#developer-controls-align-items-control)
    - [Audio Control](#developer-controls-audio-control)
    - [Apply Control](#developer-controls-apply-control)
    - [Border Control](#developer-controls-border-control)
    - [Background Control](#developer-controls-background-control)
    - [Nestable Elements (API)](#developer-elements-nestable-elements)
    - [Box Shadow Control](#developer-controls-box-shadow-control)
    - [Checkbox Control](#developer-controls-checkbox-control)
    - [Code Control](#developer-controls-code-control)
    - [Datepicker Control](#developer-controls-datepicker-control)
    - [Direction Control (Flexbox)](#developer-controls-direction-control)
    - [Color Control](#developer-controls-color-control)
    - [Element Controls](#developer-controls-element-controls)
    - [Editor Control](#developer-controls-editor-control)
    - [Dimensions Control](#developer-controls-dimensions-control)
    - [Gradient Control](#developer-controls-gradient-control)
    - [Icon Control](#developer-controls-icon-control)
    - [Filters Control](#developer-controls-filters-control)
    - [Image Control](#developer-controls-image-control)
  - [Controls](#developer-controls)
    - [Info Control](#developer-controls-info-control)
    - [Image Gallery Control](#developer-controls-image-gallery-control)
    - [Justify Content Control (Flexbox)](#developer-controls-justify-content-control)
    - [Link Control](#developer-controls-link-control)
    - [Number Control](#developer-controls-number-control)
    - [Query Control](#developer-controls-query-control)
    - [Repeater Control](#developer-controls-repeater-control)
    - [Select Control](#developer-controls-select-control)
    - [Slider Control](#developer-controls-slider-control)
    - [Text Align Control](#developer-controls-text-align-control)
    - [Text Control](#developer-controls-text-control)
    - [SVG Control](#developer-controls-svg-control)
    - [Text Decoration Control](#developer-controls-text-decoration-control)
    - [Text Shadow Control](#developer-controls-text-shadow-control)
    - [Text Transform Control](#developer-controls-text-transform-control)
    - [Textarea Control](#developer-controls-textarea-control)
    - [Typography Control](#developer-controls-typography-control)
    - [Asset Loading Optimization](#developer-guides-asset-loading)
    - [Best Practices](#developer-guides-best-practices)
    - [Bricks CLI](#developer-guides-bricks-cli)
    - [Child Theme](#developer-guides-child-theme)
    - [Converter](#developer-guides-converter)
    - [Bricks CSS: Compatibility guidelines](#developer-guides-bricks-css-compatibility-guidelines)
    - [Custom JavaScript events in Bricks](#developer-guides-custom-javascript-events-in-bricks)
  - [Hooks](#developer-hooks)
      - [Action: bricks/generate_css_file](#developer-hooks-actions-action-bricks-generate-css-file)
      - [Action: bricks/query/after_loop](#developer-hooks-actions-action-bricks-query-after-loop)
      - [Action: bricks/query/before_loop](#developer-hooks-actions-action-bricks-query-before-loop)
      - [Action: bricks_after_footer](#developer-hooks-actions-bricks-after-footer)
      - [Action: bricks_after_header](#developer-hooks-actions-bricks-after-header)
      - [Action: bricks_after_site_wrapper](#developer-hooks-actions-bricks-after-site-wrapper)
      - [Action: bricks/archive_product/after](#developer-hooks-actions-bricks-archive-product-after)
      - [Action: bricks_before_footer](#developer-hooks-actions-bricks-before-footer)
      - [Action: bricks/archive_product/before](#developer-hooks-actions-bricks-archive-product-before)
      - [Action: bricks_before_header](#developer-hooks-actions-bricks-before-header)
      - [Action: bricks_before_site_wrapper](#developer-hooks-actions-bricks-before-site-wrapper)
      - [Action: bricks_body](#developer-hooks-actions-bricks-body)
      - [Action: bricks/builder/switch_locale](#developer-hooks-actions-bricks-builder-switch-locale)
      - [Action: bricks/database/get_all_templates_by_type/after_query](#developer-hooks-actions-bricks-database-get-all-templates-by-type-after-query)
      - [Action: bricks/dynamic_data/after_do_action](#developer-hooks-actions-bricks-dynamic-data-after-do-action)
      - [Action: bricks/dynamic_data/before_do_action](#developer-hooks-actions-bricks-dynamic-data-before-do-action)
      - [Action: bricks/dynamic_data/tag_value_parsed](#developer-hooks-actions-bricks-dynamic-data-tag-value-parsed)
      - [Action: bricks/dynamic_data/tags_registered](#developer-hooks-actions-bricks-dynamic-data-tags-registered)
      - [Action: bricks_execute_filter_index_job](#developer-hooks-actions-bricks-execute-filter-index-job)
      - [Action: bricks/filter_element/before_set_data_source_from_custom_field](#developer-hooks-actions-bricks-filter-element-before-set-data-source-from-custom-field)
      - [Action: bricks/form/custom_action](#developer-hooks-actions-bricks-form-custom-action)
      - [Action: bricks/frontend/after_render_data](#developer-hooks-actions-bricks-frontend-after-render-data)
      - [Action: bricks/frontend/before_render_data](#developer-hooks-actions-bricks-frontend-before-render-data)
      - [Action: bricks/get_templates/query_after](#developer-hooks-actions-bricks-get-templates-query-after)
      - [Action: bricks_indexer](#developer-hooks-actions-bricks-indexer)
      - [Action: bricks/load_elements/after](#developer-hooks-actions-bricks-load-elements-after)
      - [Action: bricks/load_elements/before](#developer-hooks-actions-bricks-load-elements-before)
      - [Action: bricks_meta_tags](#developer-hooks-actions-bricks-meta-tags)
      - [Action: bricks/query/query_api_response](#developer-hooks-actions-bricks-query-query-api-response)
      - [Action: bricks/query_filters/index_post/before](#developer-hooks-actions-bricks-query-filters-index-post-before)
      - [Action: bricks/query_filters/index_user/before](#developer-hooks-actions-bricks-query-filters-index-user-before)
      - [Action: bricks/render_popup_content/start](#developer-hooks-actions-bricks-render-popup-content-start)
      - [Action: bricks/render_query_page/start](#developer-hooks-actions-bricks-render-query-page-start)
      - [Action: bricks/render_query_result/start](#developer-hooks-actions-bricks-render-query-result-start)
      - [Action: bricks_sendgrid_double_opt_in_handler](#developer-hooks-actions-bricks-sendgrid-double-opt-in-handler)
    - [Action Hooks](#developer-hooks-actions)
      - [Action: render_footer](#developer-hooks-actions-render-footer)
      - [Action: render_header](#developer-hooks-actions-render-header)
      - [Filter: bricks/acf/filter_field_groups](#developer-hooks-filters-bricks-acf-filter-field-groups)
      - [Filter: bricks/acf/google_map/address_parts](#developer-hooks-filters-bricks-acf-google-map-address-parts)
      - [Filter: bricks/acf/google_map/show_as_address](#developer-hooks-filters-bricks-acf-google-map-show-as-address)
      - [Filter: bricks/acf/google_map/text_output](#developer-hooks-filters-bricks-acf-google-map-text-output)
      - [Filter: bricks/acf/taxonomy/show_as_link](#developer-hooks-filters-bricks-acf-taxonomy-show-as-link)
      - [Filter: bricks/active_templates](#developer-hooks-filters-bricks-active-templates)
      - [Filter: bricks/ajax/get_pages_args](#developer-hooks-filters-bricks-ajax-get-pages-args)
      - [Filter: bricks/allowed_html_tags](#developer-hooks-filters-bricks-allowed-html-tags)
      - [Filter: bricks/api/get_templates_data](#developer-hooks-filters-bricks-api-get-templates-data)
      - [Filter: bricks/breadcrumbs/home_label](#developer-hooks-filters-bricks-breadcrumbs-home-label)
      - [Filter: bricks/breadcrumbs/items](#developer-hooks-filters-bricks-breadcrumbs-items)
      - [Filter: bricks/breadcrumbs/separator](#developer-hooks-filters-bricks-breadcrumbs-separator)
      - [Filter: bricks/builder/current_page_type](#developer-hooks-filters-bricks-builder-current-page-type)
      - [Filter: bricks/builder/data_post_id](#developer-hooks-filters-bricks-builder-data-post-id)
      - [Filter: bricks/builder/dynamic_wrapper](#developer-hooks-filters-bricks-builder-dynamic-wrapper)
      - [Filter: bricks/builder/first_element_category](#developer-hooks-filters-bricks-builder-first-element-category)
      - [Filter: bricks/builder/post_title](#developer-hooks-filters-bricks-builder-post-title)
      - [Filter: bricks/builder/state_group_definitions](#developer-hooks-filters-bricks-builder-state-group-definitions)
      - [Filter: bricks/builder/supported_post_types](#developer-hooks-filters-bricks-builder-supported-post-types)
      - [Filter: bricks/builder/term_name](#developer-hooks-filters-bricks-builder-term-name)
      - [Filter: bricks/cmb2/checkbox_value](#developer-hooks-filters-bricks-cmb2-checkbox-value)
      - [Filter: bricks/code/echo_everywhere](#developer-hooks-filters-bricks-code-echo-everywhere)
      - [Filter: bricks/combined_search/post_ids](#developer-hooks-filters-bricks-combined-search-post-ids)
      - [Filter: bricks/combined_search/term_ids](#developer-hooks-filters-bricks-combined-search-term-ids)
      - [Filter: bricks/combined_search/user_ids](#developer-hooks-filters-bricks-combined-search-user-ids)
      - [Filter: bricks/comments/author_tag](#developer-hooks-filters-bricks-comments-author-tag)
      - [Filter: bricks/conditions/groups](#developer-hooks-filters-bricks-conditions-groups)
      - [Filter: bricks/conditions/options](#developer-hooks-filters-bricks-conditions-options)
      - [Filter: bricks/conditions/result](#developer-hooks-filters-bricks-conditions-result)
      - [Filter: bricks/content_analysis/full_post_content_id](#developer-hooks-filters-bricks-content-analysis-full-post-content-id)
      - [Filter: bricks/custom_fonts/mime_types](#developer-hooks-filters-bricks-custom-fonts-mime-types)
      - [Filter: bricks/database/bricks_get_all_templates_by_type_args](#developer-hooks-filters-bricks-database-bricks-get-all-templates-by-type-args)
      - [Filter: bricks/database/content_type](#developer-hooks-filters-bricks-database-content-type)
      - [Filter: bricks/database/get_all_templates_cache_key](#developer-hooks-filters-bricks-database-get-all-templates-cache-key)
      - [Filter: bricks/dynamic_data/allowed_keys](#developer-hooks-filters-bricks-dynamic-data-allowed-keys)
      - [Filter: bricks/dynamic_data/author_value](#developer-hooks-filters-bricks-dynamic-data-author-value)
      - [Filter: bricks/dynamic_data/do_action_context](#developer-hooks-filters-bricks-dynamic-data-do-action-context)
      - [Filter: bricks/dynamic_data/format_value](#developer-hooks-filters-bricks-dynamic-data-format-value)
      - [Filter: bricks/dynamic_data/meta_value/{meta_key}](#developer-hooks-filters-bricks-dynamic-data-meta-value-meta-key)
      - [Filter: bricks/dynamic_data/register_hook](#developer-hooks-filters-bricks-dynamic-data-register-hook)
      - [Filter: bricks/dynamic_data/register_providers](#developer-hooks-filters-bricks-dynamic-data-register-providers)
      - [Filter: bricks/dynamic_data/render_content](#developer-hooks-filters-bricks-dynamic-data-render-content)
      - [Filter: bricks/dynamic_data/render_tag](#developer-hooks-filters-bricks-dynamic-data-render-tag)
      - [Filter: bricks/dynamic_data/text_separator](#developer-hooks-filters-bricks-dynamic-data-text-separator)
      - [Filter: bricks/dynamic_data/user_value](#developer-hooks-filters-bricks-dynamic-data-user-value)
      - [Filter: bricks/dynamic_tags_list](#developer-hooks-filters-bricks-dynamic-tags-list)
      - [Filter: bricks/element/builder_setup_query](#developer-hooks-filters-bricks-element-builder-setup-query)
      - [Filter: bricks/element/form/datepicker_options](#developer-hooks-filters-bricks-element-form-datepicker-options)
      - [Filter: bricks/element/form/honeypot/result](#developer-hooks-filters-bricks-element-form-honeypot-result)
      - [Filter: bricks/element/maybe_set_aria_current_page](#developer-hooks-filters-bricks-element-maybe-set-aria-current-page)
      - [Filter: bricks/elements/{element_name}/scripts](#developer-hooks-filters-bricks-elements-element-name-scripts)
      - [Filter: bricks/elements/nav_menu/menus](#developer-hooks-filters-bricks-elements-nav-menu-menus)
      - [Filter: bricks/export_template_args](#developer-hooks-filters-bricks-export-template-args)
      - [Filter: bricks/elements/nav_menu/name](#developer-hooks-filters-bricks-elements-nav-menu-name)
      - [Filter: bricks/filter-element/datepicker_options](#developer-hooks-filters-bricks-filter-element-datepicker-options)
      - [Filter: bricks/filter/taxonomy_args](#developer-hooks-filters-bricks-filter-taxonomy-args)
      - [Filter: bricks/filter_element/controls](#developer-hooks-filters-bricks-filter-element-controls)
      - [Filter: bricks/filter_element/count_source_wcField](#developer-hooks-filters-bricks-filter-element-count-source-wcfield)
      - [Filter: bricks/filter_element/count_source_{filter_source}](#developer-hooks-filters-bricks-filter-element-count-source-filter-source)
      - [Filter: bricks/filter_element/data_source_{filter_source}](#developer-hooks-filters-bricks-filter-element-data-source-filter-source)
      - [Filter: bricks/filter_element/data_source_wcField](#developer-hooks-filters-bricks-filter-element-data-source-wcfield)
      - [Filter: bricks/filter_element/datepicker_date_format](#developer-hooks-filters-bricks-filter-element-datepicker-date-format)
      - [Filter: bricks/filter_element/datepicker_db_date_format](#developer-hooks-filters-bricks-filter-element-datepicker-db-date-format)
      - [Filter: bricks/filter_element/filtered_source](#developer-hooks-filters-bricks-filter-element-filtered-source)
      - [Filter: bricks/fix_filter_element_db](#developer-hooks-filters-bricks-fix-filter-element-db)
      - [Filter: bricks/form/file_directory](#developer-hooks-filters-bricks-form-file-directory)
      - [Filter: bricks/form/recaptcha_score_threshold](#developer-hooks-filters-bricks-form-recaptcha-score-threshold)
      - [Filter: bricks/form/response](#developer-hooks-filters-bricks-form-response)
      - [Filter: bricks/form/save-submission/form_data](#developer-hooks-filters-bricks-form-save-submission-form-data)
      - [Filter: bricks/form/submission-table/file_url](#developer-hooks-filters-bricks-form-submission-table-file-url)
      - [Filter: bricks/form/tinymce_settings](#developer-hooks-filters-bricks-form-tinymce-settings)
      - [Filter: bricks/form/validate](#developer-hooks-filters-bricks-form-validate)
      - [Filter: bricks/frontend/disable_opengraph](#developer-hooks-filters-bricks-frontend-disable-opengraph)
      - [Filter: bricks/frontend/disable_seo](#developer-hooks-filters-bricks-frontend-disable-seo)
      - [Filter: bricks/get_builder_edit_link](#developer-hooks-filters-bricks-get-builder-edit-link)
      - [Filter: bricks/frontend/render_loop](#developer-hooks-filters-bricks-frontend-render-loop)
      - [Filter: bricks/get_remote_templates_data](#developer-hooks-filters-bricks-get-remote-templates-data)
      - [Filter: bricks/get_template_authors](#developer-hooks-filters-bricks-get-template-authors)
      - [Filter: bricks/get_template_bundles](#developer-hooks-filters-bricks-get-template-bundles)
      - [Filter: bricks/get_template_tags](#developer-hooks-filters-bricks-get-template-tags)
      - [Filter: bricks/get_templates/query_vars](#developer-hooks-filters-bricks-get-templates-query-vars)
      - [Filter: bricks/get_templates](#developer-hooks-filters-bricks-get-templates)
      - [Filter: bricks/get_templates_query/cache_key](#developer-hooks-filters-bricks-get-templates-query-cache-key)
      - [Filter: bricks/get_terms_options/enable_limit](#developer-hooks-filters-bricks-get-terms-options-enable-limit)
      - [Filter: bricks/get_terms_options/excluded_taxonomies](#developer-hooks-filters-bricks-get-terms-options-excluded-taxonomies)
      - [Filter: bricks/get_the_title](#developer-hooks-filters-bricks-get-the-title)
      - [Filter: bricks/handle_no_results_children_elements](#developer-hooks-filters-bricks-handle-no-results-children-elements)
      - [Filter: bricks/helpers/get_posts_args](#developer-hooks-filters-bricks-helpers-get-posts-args)
      - [Filter: bricks/media_browser/health/file_status](#developer-hooks-filters-bricks-media-browser-health-file-status)
      - [Filter: bricks/metabox/checkbox_value](#developer-hooks-filters-bricks-metabox-checkbox-value)
      - [Filter: bricks/metabox/show_as_map](#developer-hooks-filters-bricks-metabox-show-as-map)
      - [Filter: bricks/metabox/taxonomy/show_as_link](#developer-hooks-filters-bricks-metabox-taxonomy-show-as-link)
      - [Filter: bricks/{object_type}s/query_vars](#developer-hooks-filters-bricks-object-types-query-vars)
      - [Filter: bricks/paginate_links_args](#developer-hooks-filters-bricks-paginate-links-args)
      - [Filter: bricks/pagination/current_page](#developer-hooks-filters-bricks-pagination-current-page)
      - [Filter: bricks/pagination/custom_logic](#developer-hooks-filters-bricks-pagination-custom-logic)
      - [Filter: bricks/pagination/total_pages](#developer-hooks-filters-bricks-pagination-total-pages)
      - [Filter: bricks/polylang/builder_ajax_params](#developer-hooks-filters-bricks-polylang-builder-ajax-params)
      - [Filter: bricks/polylang/exclude_controls_from_translation](#developer-hooks-filters-bricks-polylang-exclude-controls-from-translation)
      - [Filter: bricks/popup/attributes](#developer-hooks-filters-bricks-popup-attributes)
      - [Filter: bricks/query/archive_query_arguments](#developer-hooks-filters-bricks-query-archive-query-arguments)
      - [Filter: bricks/query/archive_query_supported_object_types](#developer-hooks-filters-bricks-query-archive-query-supported-object-types)
      - [Filter: bricks/query/cache_key](#developer-hooks-filters-bricks-query-cache-key)
      - [Filter: bricks/query/fake_result](#developer-hooks-filters-bricks-query-fake-result)
      - [Filter: bricks/query/force_is_looping](#developer-hooks-filters-bricks-query-force-is-looping)
      - [Filter: bricks/query/force_loop_index](#developer-hooks-filters-bricks-query-force-loop-index)
      - [Filter: bricks/query/result_end](#developer-hooks-filters-bricks-query-result-end)
      - [Filter: bricks/query/prepare_query_vars_from_settings](#developer-hooks-filters-bricks-query-prepare-query-vars-from-settings)
      - [Filter: bricks/query/result_start](#developer-hooks-filters-bricks-query-result-start)
      - [Filter: bricks/query/run_fake](#developer-hooks-filters-bricks-query-run-fake)
      - [Filter: bricks/query/supress_render_content](#developer-hooks-filters-bricks-query-supress-render-content)
      - [Filter: bricks/query_api/body](#developer-hooks-filters-bricks-query-api-body)
      - [Filter: bricks/query_api/headers](#developer-hooks-filters-bricks-query-api-headers)
      - [Filter: bricks/query_api/request_args](#developer-hooks-filters-bricks-query-api-request-args)
      - [Filter: bricks/query_api/total_pages](#developer-hooks-filters-bricks-query-api-total-pages)
      - [Filter: bricks/query_filters/custom_field_index_rows](#developer-hooks-filters-bricks-query-filters-custom-field-index-rows)
      - [Filter: bricks/query_filters/custom_field_meta_query](#developer-hooks-filters-bricks-query-filters-custom-field-meta-query)
      - [Filter: bricks/query_filters/datepicker_custom_field_meta_query](#developer-hooks-filters-bricks-query-filters-datepicker-custom-field-meta-query)
      - [Filter: bricks/query_filters/element_data](#developer-hooks-filters-bricks-query-filters-element-data)
      - [Filter: bricks/query_filters/filter_query_vars](#developer-hooks-filters-bricks-query-filters-filter-query-vars)
      - [Filter: bricks/query_filters/get_filter_object_ids](#developer-hooks-filters-bricks-query-filters-get-filter-object-ids)
      - [Filter: bricks/query_filters/index_args](#developer-hooks-filters-bricks-query-filters-index-args)
      - [Filter: bricks/query_filters/index_post/meta_exists](#developer-hooks-filters-bricks-query-filters-index-post-meta-exists)
      - [Filter: bricks/query_filters/index_post/{source}](#developer-hooks-filters-bricks-query-filters-index-post-source)
      - [Filter: bricks/query_filters/index_post/wcField](#developer-hooks-filters-bricks-query-filters-index-post-wcfield)
      - [Filter: bricks/query_filters/index_user/meta_exists](#developer-hooks-filters-bricks-query-filters-index-user-meta-exists)
      - [Filter: bricks/query_filters/range_custom_field_meta_query](#developer-hooks-filters-bricks-query-filters-range-custom-field-meta-query)
      - [Filter: bricks/query_filters/sort_query_vars](#developer-hooks-filters-bricks-query-filters-sort-query-vars)
      - [Filter: bricks/query_filters_cf_integration/register_providers](#developer-hooks-filters-bricks-query-filters-cf-integration-register-providers)
      - [Filter: bricks/query_filters_indexer/post/{filter_source}](#developer-hooks-filters-bricks-query-filters-indexer-post-filter-source)
      - [Filter: bricks/query_filters_indexer/post/wcField](#developer-hooks-filters-bricks-query-filters-indexer-post-wcfield)
      - [Filter: bricks/query_filters_indexer/validate_job_settings](#developer-hooks-filters-bricks-query-filters-indexer-validate-job-settings)
      - [Filter: bricks/remote_get](#developer-hooks-filters-bricks-remote-get)
      - [Filter: bricks/remote_post](#developer-hooks-filters-bricks-remote-post)
      - [Filter: bricks/render_footer](#developer-hooks-filters-bricks-render-footer)
      - [Filter: bricks/render_header](#developer-hooks-filters-bricks-render-header)
      - [Filter: bricks/render_with_bricks](#developer-hooks-filters-bricks-render-with-bricks)
      - [Filter: bricks/resolve_attachment_id](#developer-hooks-filters-bricks-resolve-attachment-id)
      - [Filter: bricks/rtl_languages](#developer-hooks-filters-bricks-rtl-languages)
      - [Filter: bricks/security_check_before_save/new_elements](#developer-hooks-filters-bricks-security-check-before-save-new-elements)
      - [Filter: bricks/support_masonry_element](#developer-hooks-filters-bricks-support-masonry-element)
      - [Filter: bricks/svg/allowed_attributes](#developer-hooks-filters-bricks-svg-allowed-attributes)
      - [Filter: bricks/svg/allowed_tags](#developer-hooks-filters-bricks-svg-allowed-tags)
      - [Filter: bricks/svg/bypass_sanitization](#developer-hooks-filters-bricks-svg-bypass-sanitization)
      - [Filter: bricks/template_preview/supported_content_types](#developer-hooks-filters-bricks-template-preview-supported-content-types)
      - [Filter: bricks/theme_style_name](#developer-hooks-filters-bricks-theme-style-name)
      - [Filter: bricks/theme_styles/control_groups](#developer-hooks-filters-bricks-theme-styles-control-groups)
      - [Filter: bricks/theme_styles/controls](#developer-hooks-filters-bricks-theme-styles-controls)
      - [Filter: bricks/theme_styles](#developer-hooks-filters-bricks-theme-styles)
      - [Filter: bricks/user_activation_email/content](#developer-hooks-filters-bricks-user-activation-email-content)
      - [Filter: bricks/user_activation_email/from_name](#developer-hooks-filters-bricks-user-activation-email-from-name)
      - [Filter: bricks/user_activation_email/subject](#developer-hooks-filters-bricks-user-activation-email-subject)
      - [Filter: bricks/webhook/timeout](#developer-hooks-filters-bricks-webhook-timeout)
      - [Filter: bricks/woo_setup_wizard/register_presets](#developer-hooks-filters-bricks-woo-setup-wizard-register-presets)
      - [Filter: bricks/woocommerce/ajax_render_post_id](#developer-hooks-filters-bricks-woocommerce-ajax-render-post-id)
      - [Filter: bricks/woocommerce/cart_proceed_label](#developer-hooks-filters-bricks-woocommerce-cart-proceed-label)
      - [Filter: bricks/woocommerce/dynamic_fragments/fragments](#developer-hooks-filters-bricks-woocommerce-dynamic-fragments-fragments)
      - [Filter: bricks/woocommerce/dynamic_fragments/html](#developer-hooks-filters-bricks-woocommerce-dynamic-fragments-html)
      - [Filter: bricks/woocommerce/dynamic_fragments/targets](#developer-hooks-filters-bricks-woocommerce-dynamic-fragments-targets)
      - [Filter: bricks/woocommerce/predefined_elements/generated_payload](#developer-hooks-filters-bricks-woocommerce-predefined-elements-generated-payload)
      - [Filter: bricks/woocommerce/predefined_elements/local_presets](#developer-hooks-filters-bricks-woocommerce-predefined-elements-local-presets)
      - [Filter: bricks/woocommerce/predefined_elements/remote_payload](#developer-hooks-filters-bricks-woocommerce-predefined-elements-remote-payload)
      - [Filter: bricks/woocommerce/predefined_elements/remote_url](#developer-hooks-filters-bricks-woocommerce-predefined-elements-remote-url)
      - [Filter: bricks/woocommerce/products_filters/options](#developer-hooks-filters-bricks-woocommerce-products-filters-options)
      - [Filter: bricks/woocommerce/products_orderby_options](#developer-hooks-filters-bricks-woocommerce-products-orderby-options)
      - [Filter: bricks/wpml/exclude_controls_from_translation](#developer-hooks-filters-bricks-wpml-exclude-controls-from-translation)
      - [Filter: bricks/wpml/translatable_control_types](#developer-hooks-filters-bricks-wpml-translatable-control-types)
      - [Filter: bricks_query_max_items_in_builder](#developer-hooks-filters-bricks-query-max-items-in-builder)
      - [Filter: bricks/active_templates](#developer-hooks-filters-filter-bricks-active-templates)
      - [Filter: bricks/allowed_html_tags](#developer-hooks-filters-filter-bricks-allowed-html-tags)
      - [Filter: bricks/assets/generate_css_from_element](#developer-hooks-filters-filter-bricks-assets-generate-css-from-element)
      - [Filter: bricks//assets/load_webfonts](#developer-hooks-filters-filter-bricks-assets-load-webfonts)
      - [Filter: bricks/auth/custom_login_redirect](#developer-hooks-filters-filter-bricks-auth-custom-login-redirect)
      - [Filter: bricks/auth/custom_lost_password_redirect](#developer-hooks-filters-filter-bricks-auth-custom-lost-password-redirect)
      - [Filter: bricks/auth/custom_redirect_url](#developer-hooks-filters-filter-bricks-auth-custom-redirect-url)
      - [Filter: bricks/auth/custom_registration_redirect](#developer-hooks-filters-filter-bricks-auth-custom-registration-redirect)
      - [Filter: bricks/auth/custom_reset_password_redirect](#developer-hooks-filters-filter-bricks-auth-custom-reset-password-redirect)
      - [Filter: bricks/body/attributes](#developer-hooks-filters-filter-bricks-body-attributes)
      - [Filter: bricks/builder/codemirror_config](#developer-hooks-filters-filter-bricks-builder-codemirror-config)
      - [Filter: bricks/builder/elements](#developer-hooks-filters-filter-bricks-builder-elements)
      - [Filter: bricks/builder/image_size_options](#developer-hooks-filters-filter-bricks-builder-image-size-options)
      - [Filter: bricks/builder/map_styles](#developer-hooks-filters-filter-bricks-builder-mapstyles)
      - [Filter: bricks/code/allow_execution](#developer-hooks-filters-filter-bricks-code-allow-execution)
      - [Filter: bricks/code/disable_execution](#developer-hooks-filters-filter-bricks-code-disable-execution)
      - [Filter: bricks/code/disallow_keywords](#developer-hooks-filters-filter-bricks-code-disallow-keywords)
      - [Filter: bricks/code/echo_function_names](#developer-hooks-filters-filter-bricks-code-echo-function-names)
      - [Filter: bricks/comments/timestamp](#developer-hooks-filters-filter-bricks-comments-timestamp)
      - [Filter: bricks/content/attributes](#developer-hooks-filters-filter-bricks-content-attributes)
      - [Filter: bricks/content/html_after_begin](#developer-hooks-filters-filter-bricks-content-html-after-begin)
      - [Filter: bricks/content/html_before_end](#developer-hooks-filters-filter-bricks-content-html-before-end)
      - [Filter: bricks/content/tag](#developer-hooks-filters-filter-bricks-content-tag)
      - [Filter: bricks/default_page_title](#developer-hooks-filters-filter-bricks-default-page-title)
      - [Filter: bricks/dynamic_data/exclude_tags](#developer-hooks-filters-filter-bricks-dynamic-data-exclude-tags)
      - [Filter: bricks/dynamic_data/post_terms_links](#developer-hooks-filters-filter-bricks-dynamic-data-post-terms-links)
      - [Filter: bricks/dynamic_data/post_terms_separator](#developer-hooks-filters-filter-bricks-dynamic-data-post-terms-separator)
      - [Filter: bricks/dynamic_data/read_more](#developer-hooks-filters-filter-bricks-dynamic-data-read-more)
      - [Filter: bricks/element/render](#developer-hooks-filters-filter-bricks-element-render)
      - [Filter: bricks/dynamic_data/replace_nonexistent_tags](#developer-hooks-filters-filter-bricks-dynamic-data-replace-nonexistent-tags)
      - [Filter: bricks/element/render_attributes](#developer-hooks-filters-filter-bricks-element-render-attributes)
      - [Filter: bricks/element/settings](#developer-hooks-filters-filter-bricks-element-settings)
      - [Filter: bricks/elements/{element_name}/control_groups](#developer-hooks-filters-filter-bricks-elements-element-name-control-groups)
      - [Filter: bricks/elements/&#123;element_name&#125;/controls](#developer-hooks-filters-filter-bricks-elements-element-name-controls)
      - [Filter: bricks/filter_element/populated_options](#developer-hooks-filters-filter-bricks-filter-element-populated-options)
      - [Filter: bricks/footer/attributes](#developer-hooks-filters-filter-bricks-footer-attributes)
      - [Filter: bricks/form/action/{form_action}](#developer-hooks-filters-filter-bricks-form-action-form-action)
      - [Filter: bricks/form/create_post/meta_value](#developer-hooks-filters-filter-bricks-form-create-post-meta-value)
      - [Filter: bricks/frontend/render_data](#developer-hooks-filters-filter-bricks-frontend-render-data)
      - [Filter: bricks/form/update_post/meta_value](#developer-hooks-filters-filter-bricks-form-update-post-meta-value)
      - [Filter: bricks/frontend/render_element](#developer-hooks-filters-filter-bricks-frontend-render-element)
      - [Filter: bricks/get_element_data/maybe_from_post_id](#developer-hooks-filters-filter-bricks-get-element-data-maybe-from-post-id)
      - [Filter: bricks/header/attributes](#developer-hooks-filters-filter-bricks-header-attributes)
      - [Filter: bricks/builder/i18n](#developer-hooks-filters-filter-bricks-i18n)
      - [Filter: bricks/is_layout_element](#developer-hooks-filters-filter-bricks-is-layout-element)
      - [Filter: bricks/link_css_selectors](#developer-hooks-filters-filter-bricks-link-css-selectors)
      - [Filter: bricks/maintenance/should_apply](#developer-hooks-filters-filter-bricks-maintenance-should-apply)
      - [Filter: bricks/nav_menu/menu](#developer-hooks-filters-filter-bricks-nav-menu-menu)
      - [Filter: bricks/password_protection/cookie_expires](#developer-hooks-filters-filter-bricks-password-protection-cookie-expires)
      - [Filter: bricks/password_protection/is_active](#developer-hooks-filters-filter-bricks-password-protection-is-active)
      - [Filter: bricks/placeholder_image](#developer-hooks-filters-filter-bricks-placeholder-image)
      - [Filter: bricks/posts/merge_query](#developer-hooks-filters-filter-bricks-posts-merge-query)
      - [Filter: bricks/posts/query_vars](#developer-hooks-filters-filter-bricks-posts-query-vars)
      - [Filter: bricks/query/force_run](#developer-hooks-filters-filter-bricks-query-force-run)
      - [Filter: bricks/query/init_loop_index](#developer-hooks-filters-filter-bricks-query-init-loop-index)
      - [Filter: bricks/query/loop_object](#developer-hooks-filters-filter-bricks-query-loop-object)
      - [Filter: bricks/query/loop_object_id](#developer-hooks-filters-filter-bricks-query-loop-object-id)
      - [Filter: bricks/query/loop_object_type](#developer-hooks-filters-filter-bricks-query-loop-object-type)
      - [Filter: bricks/query/no_results_content](#developer-hooks-filters-filter-bricks-query-no-results-content)
      - [Filter: bricks/query/result](#developer-hooks-filters-filter-bricks-query-result)
      - [Filter: bricks/query/result_count](#developer-hooks-filters-filter-bricks-query-result-count)
      - [Filter: bricks/query/result_max_num_pages](#developer-hooks-filters-filter-bricks-query-result-max-num-pages)
      - [Filter: bricks/query/run](#developer-hooks-filters-filter-bricks-query-run)
      - [Filter: bricks/registered_post_types_args](#developer-hooks-filters-filter-bricks-registered-post-types-args)
      - [Filter: bricks/related_posts/query_vars](#developer-hooks-filters-filter-bricks-related-posts-query-vars)
      - [Filter: bricks/render_query_loop_trail](#developer-hooks-filters-filter-bricks-render-query-loop-trail)
      - [Filter: bricks/screen_conditions/scores](#developer-hooks-filters-filter-bricks-screen-conditions-scores)
      - [Filter: bricks/search_form/home_url](#developer-hooks-filters-filter-bricks-search-form-home-url)
      - [Filter: bricks/element/set_root_attributes](#developer-hooks-filters-filter-bricks-set-root-attributes)
      - [Filter: bricks/setup/control_options](#developer-hooks-filters-filter-bricks-setup-control-options)
      - [Filter: bricks/terms/query_vars](#developer-hooks-filters-filter-bricks-terms-query-vars)
      - [Filter: bricks/use_duplicate_content](#developer-hooks-filters-filter-bricks-use-duplicate-content)
      - [Filter: bricks/users/query_vars](#developer-hooks-filters-filter-bricks-users-query-vars)
      - [Filter: builder/settings/{type}/controls_data](#developer-hooks-filters-filter-builder-settings-type-controls-data)
      - [Filter: bricks/builder/color_palette](#developer-hooks-filters-filter-color-palette)
      - [Filter: bricks/builder/save_messages](#developer-hooks-filters-filter-save-messages)
      - [Filter: bricks/builder/standard_fonts](#developer-hooks-filters-filter-standard-fonts)
    - [Filter Hooks](#developer-hooks-filters)

---

<a id="developer"></a>

# Developer

Source: https://academy.bricksbuilder.io/developer/

*Extend Bricks with developer guides, custom elements, controls, hooks, functions, dynamic data tags, and schema references.*

The Developer section covers the extension points and data structures behind Bricks so you can build custom elements, hook into builder behavior, register controls, and generate valid Bricks data outside the UI.

## Explore the developer docs

- [Guides](https://academy.bricksbuilder.io/developer/guides/best-practices/) for conventions, tooling, and development workflows
- [Custom Elements](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/) for building and registering your own elements
- [Controls](https://academy.bricksbuilder.io/developer/controls/) for the control reference used in custom element settings
- [Hooks](https://academy.bricksbuilder.io/developer/hooks/) for action hooks and filter hooks across Bricks
- [Functions](https://academy.bricksbuilder.io/developer/functions/function-bricks_render_dynamic_data/) for documented helper functions
- [Dynamic Data](https://academy.bricksbuilder.io/developer/dynamic-data/create-your-own-dynamic-data-tag/) for custom data tags
- [Schema](https://academy.bricksbuilder.io/developer/schema/) for the underlying Bricks data model

---

<a id="developer-dynamic-data-create-your-own-dynamic-data-tag"></a>

# Create Your Own Dynamic Data Tag

Source: https://academy.bricksbuilder.io/developer/dynamic-data/create-your-own-dynamic-data-tag/

*Create custom dynamic data tags in Bricks so your own values can be inserted into text, media, links, and other supported contexts.*

This article is intended for developers who wish to create a custom dynamic data tag within the builder.

The desired outcome should resemble the following example:

![](https://academy.bricksbuilder.io/assets/bricks-custom-dynamic-tag.png)

<figcaption>

A custom dynamic tag labeled "My Dynamic Data"

</figcaption>

## Step 1: Register a tag through filter: bricks/dynamic_tags_list

Use the `bricks/dynamic_tags_list` filter to render your custom dynamic data tag in the builder.

```php
add_filter( 'bricks/dynamic_tags_list', 'add_my_tag_to_builder' );
function add_my_tag_to_builder( $tags ) {
  // Ensure your tag is unique (best to prefix it)
  $tags[] = [
    'name'  => '{my_dd_tag}',
    'label' => 'My Dynamic Data',
    'group' => 'My Dynamic Data Group',
  ];

  return $tags;
}
```

## Step 2: Hook on several filters

#### 1) bricks/dynamic_data/render_tag

This will be used when `\Bricks\Integrations\Dynamic_Data\Providers::render_tag()` is called to parse a specific tag.

```php
add_filter( 'bricks/dynamic_data/render_tag', 'get_my_tag_value', 20, 3 );
function get_my_tag_value( $tag, $post, $context = 'text' ) {
  if( ! is_string( $tag ) ) {
    return $tag;
  }
  // $tag is the tag name without the outer curly braces
  $clean_tag = str_replace( [ '{', '}' ], '', $tag );

  // Only look for dynamic tag my_dd_tag
  if ( $clean_tag !== 'my_dd_tag' ) {
    return $tag;
  }

  // Do your custom logic here, you should define run_my_dd_tag_logic() function
  $value = run_my_dd_tag_logic();

  return $value;
}

function run_my_dd_tag_logic() {
  // Do your custom logic here
  $my_value = 'My dynamic data value:';

  return $my_value;
}
```

If you intend to accept an argument such as "`my_dd_tag:arg1`", you may need to adjust the logic accordingly. Here is a basic example using PHP logic. For more complex scenarios, you can adapt the logic as needed:

```php
add_filter( 'bricks/dynamic_data/render_tag', 'get_my_tag_value', 20, 3 );
function get_my_tag_value( $tag, $post, $context = 'text' ) {
  if( ! is_string( $tag ) ) {
    return $tag;
  }

  // $tag is the tag name without the outer curly braces
  $clean_tag = str_replace( [ '{', '}' ], '', $tag );

  // Only look for dynamic tag starts with my_dd_tag:
  if ( strpos( $clean_tag, 'my_dd_tag:' ) !== 0 ) {
    return $tag;
  }

  // Get argument
  $argument = str_replace( 'my_dd_tag:', '', $clean_tag );

  // Do your custom logic here, you should define run_my_dd_tag_logic() function
  $value = run_my_dd_tag_logic( $argument );

  return $value;
}

function run_my_dd_tag_logic($argument) {
  // Do your custom logic here
  $my_value = 'My dynamic data value: ' . $argument ;

  return $my_value;
}
```

#### 2) bricks/dynamic_data/render_content and bricks/frontend/render_data

These will be used when `\Bricks\Integrations\Dynamic_Data\Providers::render_content()` is invoked to parse strings that may contain various dynamic tags within the content. One of the functions that perform this action is `bricks_render_dynamic_data()`.

> **Note**
>
> It is crucial to exercise extra caution while working on this aspect, as any mishandling may disrupt the dynamic tag functionality across the entire website.

```php
add_filter( 'bricks/dynamic_data/render_content', 'render_my_tag', 20, 3 );
add_filter( 'bricks/frontend/render_data', 'render_my_tag', 20, 2 );
function render_my_tag( $content, $post, $context = 'text' ) {

  // $content might consists of HTML and other dynamic tags
  // Only look for dynamic tag {my_dd_tag}
  if ( strpos( $content, '{my_dd_tag}' ) === false ) {
    return $content;
  }

  // Do your custom logic here, you should define run_my_dd_tag_logic() function
  $my_value = run_my_dd_tag_logic();

  // Replace the tag with the value you want to display
  $content = str_replace( '{my_dd_tag}', $my_value, $content );

  return $content;
}

```

If your dynamic tag accepts an argument, consider the following example:

```php
add_filter( 'bricks/dynamic_data/render_content', 'render_my_tag', 20, 3 );
add_filter( 'bricks/frontend/render_data', 'render_my_tag', 20, 2 );
function render_my_tag( $content, $post, $context = 'text' ) {

  // $content is the content of the element, including other dynamic tags, HTML, etc.
  // Only look for content starts with {my_dd_tag:
  if ( strpos( $content, '{my_dd_tag:' ) === false ) {
    return $content;
  }

  // Regex to match my_dd_tag: tag
  preg_match_all( '/{(my_dd_tag:[^}]+)}/', $content, $matches );

  // Nothing grouped in the regex, return the original content
  if ( empty( $matches[0] ) ) {
    return $content;
  }

  foreach ( $matches[1] as $key => $match ) {
    $tag = $matches[0][ $key ];

    // Get the dynamic data value, $match is the tag name without the curly brackets
    // Can reuse the get_my_tag_value function created earlier
    $value   = get_my_tag_value( $match, $post, $context );

    // Replace the tag with the transformed value
    $content = str_replace( $tag, $value, $content );
  }

  return $content;
}
```

> **Note**
>
> Note: If your dynamic tag is used in an image context, return an array whose first item is an attachment ID or image URL. Use an attachment ID when Bricks needs image size and srcset metadata. Please refer to the example in our forum threads: [Dynamic data not rendered correctly on image element](https://forum.bricksbuilder.io/t/dynamic-data-not-rendered-correctly-on-image-element/22641/2?u=itchycode)

---

<a id="developer-elements-create-your-own-elements"></a>

# Create Your Own Elements

Source: https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/

*Create custom Bricks elements by extending the element API, registering controls, and rendering frontend output.*

The Bricks [child theme](https://academy.bricksbuilder.io/developer/guides/child-theme/), which you can download from your [Bricks account](https://my.bricksbuilder.io/) includes a simple custom element for demonstration purposes. The article below explains in more detail how to create your own elements programmatically.

Creating your own elements with Bricks follows a pattern similar to how you create WordPress widgets. You start by extending the `Bricks\Element` class and populate the required properties and methods for your element.

First, create a new file `element-test.php` in the root folder of your Bricks child theme.

## Blank element class {#builder}

```php
<?php
// element-test.php
if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = '';
  public $name         = '';
  public $icon         = '';
  public $css_selector = '';
  public $scripts      = [];
  public $nestable     = false; // true || @since 1.5

  // Methods: Builder-specific
  public function get_label() {}
  public function get_keywords() {}
  public function set_control_groups() {}
  public function set_controls() {}

  // Methods: Frontend-specific
  public function enqueue_scripts() {}
  public function render() {}
}
```

Let's walk through the element builder properties and methods:

| **$category** required | Category name (all lowercase, no spaces). Use any of the predefined element categories (e.g. `general`, `media`, etc.) or assign your own category name.<br /><br />When setting your own category make sure to provide a translatable category string for the builder using the filter: [bricks/builder/i18n](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-i18n/) |
| --- | --- |
| **$name** required | Unique element identifier (all lowercase, no spaces). To avoid any conflicts with other elements please prefix your element name, e.g.: `prefix-element-test`. |
| **$icon** | Icon font CSS class. Bricks includes the following icon fonts. Use any icon font CSS class to represent your element in the builder panel:  [Fontawesome 6](https://fontawesome.com/icons?d=gallery&m=free) (i.e. "fas fa-anchor") [Ionicons 4](https://ionicons.com/v4/cheatsheet.html) (i.e. "ion-md-alarm") [Themify Icons](https://themify.me/themify-icons) (i.e. "ti-bolt-alt") |
| **$css_selector** | By default all CSS control settings are applied to the element wrapper:  `.bricks-element-wrapper`. If you want the default CSS selector to target a child HTML element, set this selector here. |
| **$nestable** | Omit for plain elements. Set to `true` to create a [nestable element](https://academy.bricksbuilder.io/developer/elements/nestable-elements/). |
| **$scripts** | An array of JavaScript scripts that run when an element is rendered on the frontend or updated in the builder. The Counter element, for example, uses a script named "bricksCounter" (defined in *frontend.min.js*).<br /><br />To load this script we use: `public $scripts = ['bricksCounter'];`<br /><br />Please prefix all your scripts. E.g.: `prefixElementTest` |
| **get_label()** required | Return localised element label. |
| **get_keywords()** | Array of strings that when matched during the element search display the element in the search results. |
| **set_control_groups()** | By default, all element controls show ungrouped in the builder panel under the "Content" tab. Define custom control groups for your element controls by setting the following properties for each control group: **title** — Localized control group title. **tab** — Set to either "content" or "style". |
| **set_controls()** required | Define element controls. For an overview of all available controls and their settings visit: [Element Controls](https://academy.bricksbuilder.io/developer/controls/element-controls/) |
| **enqueue_scripts()** | Load element-specific scripts and styles. Those are loaded only on pages where this element is used. Results in better performance. Example: `wp_enqueue_script( 'prefix-element-test', get_template_directory_uri() . '/js/custom.js', ['jquery'], '1.0', true );` |
| **render()** required | Renders element HTML. Define HTML attributes via `$this->set_attribute()` and output them via `$this->render_attribute()` |
| **`set_attribute( $key, $attribute, $value )`** | Helper function to set HTML attributes for any HTML tag. `$key` serves as the unique identifier for this HTML tag. `$attribute` is the HTML attribute name. `$value` is a string or array which holds the attribute value(s). |
| **`render_attributes( $key )`** | Helper function to render HTML attributes defined via `$this->set_attribute()`. `$key` serves as the unique identifier for this HTML tag. |
| **`render_dynamic_data_tag( $tag, $context, $args )`** | Helper function to render dynamic data tags inside the render function using `$this->render_dynamic_data_tag(...)`. An example of a `$tag` is the `{post_title}`. Using this helper function sets the correct post Id depending on the environment where the element is being rendered. |
| **`render_dynamic_data( $content )`** | Helper function to render content (string) that could contain dynamic data tags. Use this helper function inside the render function calling `$this->render_dynamic_data(...)`. Using this helper function sets the correct post Id depending on the environment where the element is being rendered. |

Let's populate our element properties and methods with some data:

```php
<?php
// element-test.php

if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = 'general'; // Use predefined element category 'general'
  public $name         = 'prefix-test'; // Make sure to prefix your elements
  public $icon         = 'ti-bolt-alt'; // Themify icon font class
  public $css_selector = '.prefix-test-wrapper'; // Default CSS selector
  public $scripts      = ['prefixElementTest']; // Script(s) run when element is rendered on frontend or updated in builder

  // Return localised element label
  public function get_label() {
    return esc_html__( 'Test element', 'bricks' );
  }

  // Set builder control groups
  public function set_control_groups() {
    $this->control_groups['text'] = [ // Unique group identifier (lowercase, no spaces)
      'title' => esc_html__( 'Text', 'bricks' ), // Localized control group title
      'tab' => 'content', // Set to either "content" or "style"
    ];

    $this->control_groups['settings'] = [
      'title' => esc_html__( 'Settings', 'bricks' ),
      'tab' => 'content',
    ];
  }

  // Set builder controls
  public function set_controls() {
    $this->controls['content'] = [ // Unique control identifier (lowercase, no spaces)
      'tab' => 'content', // Control tab: content/style
      'group' => 'text', // Show under control group
      'label' => esc_html__( 'Content', 'bricks' ), // Control label
      'type' => 'text', // Control type
      'default' => esc_html__( 'Content goes here ..', 'bricks' ), // Default setting
    ];

    $this->controls['type'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];
  }

  // Enqueue element styles and scripts
  public function enqueue_scripts() {
    wp_enqueue_script( 'prefix-test-script' );
  }

  // Render element HTML
  public function render() {
    // Set element attributes
    $root_classes[] = 'prefix-test-wrapper';

    if ( ! empty( $this->settings['type'] ) ) {
      $root_classes[] = "color-{$this->settings['type']}";
    }

    // Add 'class' attribute to element root tag
    $this->set_attribute( '_root', 'class', $root_classes );

    // Render element HTML
    // '_root' attribute is required (contains element ID, class, etc.)
    echo "<div {$this->render_attributes( '_root' )}>"; // Element root attributes
      if ( ! empty( $this->settings['content'] ) ) {
        echo "<div>{$this->settings['content']}</div>";
      }
    echo '</div>';
  }
}
```

You can browse the documented Bricks controls at: [/developer/controls/](https://academy.bricksbuilder.io/developer/controls/)

> **Note**
>
> All element settings are stored in `$this->settings`. To view of element settings you can print them on the screen like so: `var_dump( $this->settings );` in the `render()` function.

## Load and register your element {#register}

After creating your custom element you need to load and register your element. Open up `functions.php` of your Bricks child theme and copy & paste the following code:

```php
/**
 * Register custom elements
 */
add_action( 'init', function() {
  $element_files = [
    __DIR__ . '/element-test.php',
  ];

  foreach ( $element_files as $file ) {
    \Bricks\Elements::register_element( $file );
  }
}, 11 );
```

The `register_element` method accepts 3 arguments:

- `$file` (required): The full path to the custom element PHP file in the server
- `$name` (optional): A string containing the name of the custom element (e.g.: `prefix-element-test`)
- `$element_class` (optional): A string containing the class name of the element (e.g.: `Prefix_Element_Test`) which should derive from the Bricks element class (`\Bricks\Element`)

> **Note**
>
> **Note:** Using the `$name` and `$element_class` arguments will improve the loading performance.

---

<a id="developer-functions-function-bricks-render-dynamic-data"></a>

# Function: bricks_render_dynamic_data

Source: https://academy.bricksbuilder.io/developer/functions/function-bricks_render_dynamic_data/

*Use the bricks_render_dynamic_data() helper to resolve dynamic tags inside a content string in your own custom code.*

This helper function will render the dynamic data tags inside of a content string (@since 1.5.5).

```php
echo bricks_render_dynamic_data( $content, $post_id, $context );
```

### Parameters:

- `$content` - a string containing dynamic data tags (required)
- `$post_id` - the post id if needed (default: current post id)
- `$context` - the context where the data is used after rendered: *text*, *link*, *image*, *media* (default: *text*)

### Return:

The string after replacing the dynamic data tags with their content.

Example:

```php
echo bricks_render_dynamic_data('My Post Title: {post_title}');
```

---

<a id="developer-controls-align-items-control"></a>

# Align Items Control (Flexbox)

Source: https://academy.bricksbuilder.io/developer/controls/align-items-control/

*Reference for the Bricks Align Items Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements.*

Use the align-items control to allow users to set the `align-items` CSS property (alignment along the [cross-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)) of your CSS flexbox layout.

There is also a [`justify-content`](https://academy.bricksbuilder.io/developer/controls/justify-content-control/) control to allow users to set the alignment along the main axis of your CSS flexbox layout:

```php
public function set_controls() {
  $this->controls['alignItems'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Align items', 'bricks' ),
    'type'  => 'align-items',
    'css'   => [
      [
        'property' => 'align-items',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}
```

---

<a id="developer-controls-audio-control"></a>

# Audio Control

Source: https://academy.bricksbuilder.io/developer/controls/audio-control/

*Reference for the Bricks Audio control, including its options, CSS mapping, and usage in custom elements.*

The audio control lets you select an audio file from the media library. It also gives you various options to show/hide artist and title, choose between a light/dark theme, autoplay the audio file, etc. It has no custom control parameters.

```php
class Prefix_Element_Audio extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['file'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Audio file', 'bricks' ),
      'type' => 'audio',
    ];
  }

  // Render element HTML
  public function render() {
    $settings = $this->settings;

    if ( isset( $settings['file']['url'] ) ) {
      echo wp_audio_shortcode( [
        'src'      => $settings['file']['url'],
        'loop'     => isset( $settings['loop'] ) ? $settings['loop'] : false,
        'autoplay' => isset( $settings['autoplay'] ) ? $settings['autoplay'] : false,
        'preload'  => isset( $settings['preload'] ) ? $settings['preload'] : 'none',
      ] );
    }
  }
}
```

### Resources

[https://codex.wordpress.org/Function_Reference/wp_audio_shortcode](https://codex.wordpress.org/Function_Reference/wp_audio_shortcode)

---

<a id="developer-controls-apply-control"></a>

# Apply Control

Source: https://academy.bricksbuilder.io/developer/controls/apply-control/

*Reference for the Bricks Apply control, including its options, CSS mapping, and usage in custom elements.*

The `apply` control saves your settings. You can set the `reload` control property to **true** in order to trigger a builder reload after the "Apply" button has been clicked. We use it in the builder for settings like the template "Populate Content" or the "SEO" page settings.

```php
$this->controls['apply'] = [
  'group' => 'template-preview',
  'type' => 'apply',
  'reload' => true,
  'label' => esc_html__( 'Apply preview', 'bricks' ),
];
```

---

<a id="developer-controls-border-control"></a>

# Border Control

Source: https://academy.bricksbuilder.io/developer/controls/border-control/

*Reference for the Bricks Border control, including its options, CSS mapping, and usage in custom elements.*

The border control lets you set the following border properties:

- Border width (top/right/bottom/left)
- Background style (top/right/bottom/left)
- Background color (none/solid/double/dotted/dashed)
- Border radius (top/right/bottom/left)

The example below illustrates how to apply a border via the `css` parameter and how to set border defaults.

```php
class Builder_Element_Prefix_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['titleBorder'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title border', 'bricks' ),
      'type' => 'border',
      'css' => [
        [
          'property' => 'border',
          'selector' => '.prefix-test-title',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'width' => [
          'top' => 1,
          'right' => 0,
          'bottom' => 0,
          'left' => 0,
        ],
        'style' => 'solid',
        'color' => [
          'hex' => '#ffff00',
        ],
        'radius' => [
          'top' => 1,
          'right' => 1,
          'bottom' => 1,
          'left' => 1,
        ],
      ],

    ];
  }
}
```

---

<a id="developer-controls-background-control"></a>

# Background Control

Source: https://academy.bricksbuilder.io/developer/controls/background-control/

*Reference for the Bricks Background control, including its options, CSS mapping, and usage in custom elements.*

The background control lets you set the following background properties:

- Background color
- Background image
- Background video (requires `bricksBackgroundVideoInit` script. See code example below)

There are various settings for the background image and video. You can exclude color/image/video settings via the `exclude` parameter.

As the background control serves most likely as a CSS setting the following example shows you how to set the `css` parameter to apply it to the elements' `.prefix-test-wrapper` HTML.

Adding a background video requires you to load the `bricksBackgroundVideoInit` script and use the `BricksFrontend::get_element_background_video_wrapper()` method to render it.

> **Note**
>
> When you just want to set a background color better use the [color control](https://academy.bricksbuilder.io/developer/controls/color-control/). The background control is handier when using a background image or video on top of the color.

```php
class Prefix_Element_Background extends \Bricks\Element {
  // Required for background video
  public $scripts = ['bricksBackgroundVideoInit'];

  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBackground'] = [ // Setting key
      'tab' => 'content',
      'label' => esc_html__( 'Background', 'bricks' ),
      'type' => 'background',
      'css' => [
        [
          'property' => 'background',
          'selector' => '.prefix-background-wrapper',
        ],
      ],
      'exclude' => [
        // 'color',
        // 'image',
        // 'parallax',
        // 'attachment',
        // 'position',
        // 'positionX',
        // 'positionY',
        // 'repeat',
        // 'size',
        // 'custom',
        // 'videoUrl',
        // 'videoScale',
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'color' => [
          'rgb' => 'rgba(255, 255, 255, .5)',
          'hex' => '#ffffff',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-background-wrapper">';

    // Background video
    echo BricksFrontend::get_element_background_video_wrapper(
      ['settings' => $settings],
      'exampleBackground' // Setting key
    );

    echo get_bloginfo( 'name' );

    echo '</div>';
  }
}
```

---

<a id="developer-elements-nestable-elements"></a>

# Nestable Elements (API)

Source: https://academy.bricksbuilder.io/developer/elements/nestable-elements/

*Understand the Bricks API for nestable elements, including how parents, children, and allowed structures are defined.*

Bricks 1.5 introduces **Nestable Elements**. Plus an API that allows you to programmatically define your own custom elements that can contain other elements. In exactly the structure you want.

Prior to Bricks 1.5 every element in Bricks was "flat". Meaning even though an element contained a deep HTML structure (like the Slider, etc.) you couldn't click on an inner part of this element to edit it directly (e.g. contents of slide 3), or change the inner structure of it to your liking via Drag & Drop, as you could do inside a layout element.

Making it often impossible to properly customise more complex elements like the Icon Box, Pricing Table, List, etc.

Complex elements such as the Accordion, Slider, and Tabs weren't properly customisable at all.

## Full Access & Control Over Individual Element Structure

Starting at version 1.5, Bricks provides three nestable elements:

- Accordion (Nestable)
- Slider (Nestable)
- Tabs (Nestable)

Those elements were notoriously hard to properly customise due to their complex structure, and the limits of their "flat" element structure.

Now that you can populate every slide with the elements you want, purpose-specific slider-like elements such as the "Carousel" & "Team Members" are not really needed.

![](https://academy.bricksbuilder.io/assets/bricks-1.5-nestable-accordion-1024x398.jpg)

<figcaption>

Accordion - Nestable

</figcaption>

> **Note**
>
> Nestable elements are going to exist alongside their flat origin elements for the foreseeable future until we have collected enough feedback & fixed any major bugs in order to fully make the switch to nestable elements.

> **Note**
>
> Certain interactive nestable elements that are heavily JavaScript-driven (such as the Accordion, Slider, and Tabs) might prevent the Drag & drop from working 100% on the canvas. If you encounter this behavior you can always add & order elements by using the Structure panel too.

> **Note**
>
> **Nestable tabs**: If you need to change the `display` property of the tab "pane", please do so by adding another "Block" element inside the panel and setting the `display` setting there. The pane itself uses `display: none` in order to hide all non-active panes. If you change the display setting there, all tab panes will always be visible.

So you can start playing around with those new nestable elements, and slowly transition away from the old plain elements.

Over time we'll convert more and more `flat` elements into nestable elements, so that you'll be able to properly customize most elements in Bricks once their nestable equivalent becomes available.

## Nestable Elements API {#api}

The rest of this article shows how to programmatically create your own nestable elements.

A good starting point to learn about the new nestable elements syntax is to inspect the Bricks source code of the following nestable element files:

- accordion-nested.php
- slider-nested.php
- tabs-nested.php

### Define Your Custom Element As "nestable"

First make sure to set the [`$nestable`](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/#builder) property of your custom element class to `true`.

This is required so Bricks knows to render this custom element using the nestable render function in the builder, and to enable drag & drop inside the builder for this custom element.

### Nestable Element Template

You can define the structure of your custom element via the `get_nestable_children` function. It expects to return an array of element definitions.

This is best illustrated by having a look at the Nestable Slider elements' `get_nestable_children` function:

```php
public function get_nestable_children() {
  return [
      [
        'name'     => 'block',
        'label'    => esc_html__( 'Slide', 'bricks' ) . ' {item_index}',
        'settings' => [
          '_hidden' => [
            '_cssClasses' => 'hidden-class', // CSS class not visible in builder UI
          ],
        ],
        'children' => [
            [
              'name'     => 'heading',
              'settings' => [
                'text' => esc_html__( 'Slide', 'bricks' ) . ' {item_index}',
              ],
            ],
            [
              'name'     => 'button',
              'settings' => [
                'text'  => esc_html__( 'I am a button', 'bricks' ),
                'size'  => 'lg',
                'style' => 'primary',
              ],
            ],
          ],
      ],
  ];
}
```

The code above adds a "Slide" block inside the nestable slider, which then contains a "Heading" & "Button" element.

The `children` property, if set, accepts an array of further nested elements. Specify the `settings` array to populate individual elements inside your nestable element as needed.

### Nestable Render Function (PHP) {#php}

The only new function you need to add to your PHP `render()` function is called `render_children` and it requires the element instance `$this` to be passed as the first parameter:

```php
public function render() {
  $output = "<div {$this->render_attributes( '_root' )}>";

  // Render children elements (= individual items)
  $output .= Frontend::render_children( $this );

  $output .= '</div>';

  echo $output;
}
```

### Nestable Render Function (Vue x-template) {#x-template}

To render elements inside your nestable element in your custom x-template, simply add the `` component plus `element` props as shown in the following code snippet:

```php
public function render_builder() {
  <script type="text/x-template" id="tmpl-bricks-element-custom-nestable">
    <component :is="tag">
      <h2>Title before nestable children</h2>
      <bricks-element-children :element="element"/>
      <p>Text node after nestable children</p>
    </component>
  </script>
}
```

### Nestable Element Items (in panel)

If your nestable element structure is based on items on the same level (such as our Accordion above), then you can add a Repeater (see builder panel in screenshot above) by adding a `repeater` control with the `items` property set to `children`:

```php
public function set_controls() {
  // Array of nestable element.children (@since 1.5)
  $this->controls['_children'] = [
    'type'          => 'repeater',
    'titleProperty' => 'label',
    'items'         => 'children',
  ];
];
```

> **Note**
>
> If you are start using and/or experimenting with the new Nestable Elements API for your custom elements, [we'd love to hear your feedback](https://bricksbuilder.io/contact/). Does this API miss any features, did you encounter any bugs?

---

<a id="developer-controls-box-shadow-control"></a>

# Box Shadow Control

Source: https://academy.bricksbuilder.io/developer/controls/box-shadow-control/

*Reference for the Bricks Box Shadow control, including its options, CSS mapping, and usage in custom elements.*

The box-shadow control is a CSS control and you can set the following properties:

- Offset X
- Offset Y
- Spread
- Blur
- Color
- Inset

```php
class Prefix_Element_Box_Shadow extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBoxShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'BoxShadow', 'bricks' ),
      'type' => 'box-shadow',
      'css' => [
        [
          'property' => 'box-shadow',
          'selector' => '.prefix-box-shadow-wrapper',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'values' => [
          'offsetX' => 0,
          'offsetY' => 0,
          'blur' => 2,
          'spread' => 0,
        ],
        'color' => [
          'rgb' => 'rgba(0, 0, 0, .1)',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-box-shadow-wrapper">';
    echo get_bloginfo( 'name' );
    echo '</div>';
  }
}
```

### Resources

[https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)

---

<a id="developer-controls-checkbox-control"></a>

# Checkbox Control

Source: https://academy.bricksbuilder.io/developer/controls/checkbox-control/

*Reference for the Bricks Checkbox control, including its options, CSS mapping, and usage in custom elements.*

The checkbox control is a simple on/off switch. If enabled it outputs a boolean value of `true`. Disabled it returns `false`. You can use it to conditionally show/hide other content settings as we illustrate in the following code example:

```php
class Prefix_Element_Checkbox extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleCheckbox'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Show site title', 'bricks' ),
      'type' => 'checkbox',
      'inline' => true,
      'small' => true,
      'default' => true, // Default: false
    ];
  }

  // Render element HTML
  public function render() {
    // Show site title if setting checkbox 'exampleCheckbox' is checked
    if ( isset( $this->settings['exampleCheckbox'] ) ) {
      echo get_bloginfo( 'name' );
    }
  }
}
```

---

<a id="developer-controls-code-control"></a>

# Code Control

Source: https://academy.bricksbuilder.io/developer/controls/code-control/

*Reference for the Bricks Code control, including its options, CSS mapping, and usage in custom elements.*

The code control embeds a code editor utilizing the amazing CodeMirror library. Users for which you've enabled "**Code Execution**" in the Bricks settings, will be able to execute PHP, HTML, CSS, and JavaScript.

```php
class Prefix_Element_Code extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleHtml'] = [
      'tab' => 'content',
      'label' => esc_html__( 'HTML', 'bricks' ),
      'type' => 'code',
      'mode' => 'php',
      'default' => '<h4>Example H4 HTML title</h4>',
    ];
  }

  // Render element HTML
  public function render() {
    echo isset( $this->settings['exampleHtml'] ) ? $this->settings['exampleHtml'] : esc_html__( 'No HTML provided.', 'bricks' );
  }
}
```

> **Note**
>
> You don't need to define your own element CSS and JS controls. Those are already available when editing the element under the Style tab "CSS" control group.

---

<a id="developer-controls-datepicker-control"></a>

# Datepicker Control

Source: https://academy.bricksbuilder.io/developer/controls/datepicker-control/

*Reference for the Bricks Datepicker control, including its options, CSS mapping, and usage in custom elements.*

The datepicker control provides a great interface for selecting a specific date and time and outputting it in the [format of your choice](http://hilios.github.io/jQuery.countdown/documentation.html#directives).

The Datepicker control leverages the Flatpickr library to offer a robust date selection interface. Since Bricks 1.9.8 an `options` property has been added which allows for further customization.

## Properties:

### Property: options (since 1.9.8)

- **Type:** array (associative)
- **Description:** Enables customization of the datepicker by passing an associative array of options defined in the Flatpickr library.
- **Default values:**
  - **enableTime:** Defaults to `true` unless explicitly set through a passed property.
  - **altInput:** Defaults to `true` unless specified otherwise through a passed property.

**Example usage:**

```php
$this->controls['date'] = [
  'tab' => 'content',
  'label' => esc_html__('Date', 'bricks'),
  'type' => 'datepicker',
  'options' => [
    'enableTime' => true,  // Enables time selection.
    'time_24hr' => true,   // Displays time picker in 24-hour mode.
    'noCalendar' => true   // Hides the calendar day selection.
  ]
];
```

In this example, the `options` array is configured to create a time picker that operates in 24-hour format without showing a calendar for day selection. The `enableTime` option is set to true to ensure time can be selected, `time_24hr` is enabled for 24-hour time format, and `noCalendar` is set to true to hide the calendar component. Adjust the `options` array as needed to customize the datepicker to meet different requirements.

For a full list of customizable options available in Flatpickr, please refer to the [Flatpickr Options documentation](https://flatpickr.js.org/options/).

### Property: enableTime

- **Type:** boolean
- **Description:** Determines whether time selection is enabled. Overridden if any settings are passed in the `options` property.
- **Default:** true

### Property: altInput

- **Type:** boolean
- **Description:** Enables an alternative, more user-friendly input style. Overridden if any settings are passed in the `options` property.
- **Default:** true

## Example: Countdown element

```php
// Example: Countdown element
class Prefix_Element_Countdown extends \Bricks\Element {
  public $category = 'general';
  public $name     = 'countdown';
  public $icon     = 'ti-timer';
  public $scripts  = ['bricksCountdown'];

  public function get_label() {
    return esc_html__( 'Countdown', 'bricks' );
  }

  public function set_controls() {
    $this->controls['date'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Date', 'bricks' ),
      'type' => 'datepicker',
      'options' => ['enableTime' => true, 'altInput' => true],
      'default' => '2019-01-01 12:00',
    ];

    $this->controls['format'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Format', 'bricks' ),
      'type' => 'text',
      'default' => '%D days %H hours %M minutes %S seconds.',
      'description' => sprintf(
        '%s <a target="_blank" href="http://hilios.github.io/jQuery.countdown/documentation.html#directives">%s</a>.',
        esc_html__( 'For formatting options see', 'bricks' ),
        esc_html__( 'directives', 'bricks' )
      ),
    ];
  }

  public function render() {
    $this->set_attribute( 'wrapper', 'class', 'countdown-wrapper' );

    $countdown_options = [
      'date' => isset( $this->settings['date'] ) ? $this->settings['date'] : '',
      'format' => isset( $this->settings['format'] ) ? $this->settings['format'] : '',
    ];

    $this->set_attribute( 'wrapper', 'data-bricks-countdown-options', wp_json_encode( $countdown_options ) );

    // Render
    if ( ! isset( $this->settings['date'] ) || ! isset( $this->settings['format'] ) ) {
      return $this->render_element_placeholder( [
        'icon-class' => 'ti-timer',
        'text'       => esc_html__( 'No date/format set.', 'bricks' ),
      ] );
    } else {
      echo '<div ' . $this->render_attributes( 'wrapper' ) . '></div>';
    }
  }
}
```

---

<a id="developer-controls-direction-control"></a>

# Direction Control (Flexbox)

Source: https://academy.bricksbuilder.io/developer/controls/direction-control/

*Reference for the Bricks Direction Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements.*

Use the direction control to allow users to set the `flex-direction` CSS property of your CSS flexbox layout.

```php
public function set_controls() {
  $this->controls['direction'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Direction', 'bricks' ),
    'type'  => 'direction',
    'css'   => [
      [
        'property' => 'flex-direction',
        'selector' => '.flexbox-wrapper',
        // 'id'       => '', // Leave 'id' empty to apply to .flexbox-wrapper directly (@since 1.5.6)
      ],
    ],
  ];
}
```

---

<a id="developer-controls-color-control"></a>

# Color Control

Source: https://academy.bricksbuilder.io/developer/controls/color-control/

*Reference for the Bricks Color control, including its options, CSS mapping, and usage in custom elements.*

The color control is a custom-built color picker that you won't find anywhere else.

It lets you pick and adjust colors in `hex`, `rgba` and `hsl` format. It also includes a global color palette to save any color for later reuse anywhere else on your site.

Define your own default color palette with the `bricks/builder/color_palette` filter.

You can set the CSS `property` to `color` or `background-color` as illustrated in the example below.

```php
class Prefix_Element_Color extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Text color applied to '.prefix-element-test-title'
    $this->controls['exampleColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.prefix-element-test-title',
        ]
      ],
      'default' => [
        'hex' => '#3ce77b',
        'rgb' => 'rgba(60, 231, 123, 0.9)',
      ],
    ];

    // Background color applied to '.prefix-element-test-content'
    $this->controls['exampleBackgroundColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Background color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'background-color',
          'selector' => '.prefix-element-test-content',
        ]
      ],
      'default' => [
        'hex' => '#1ebea5',
        'rgb' => 'rgba(30, 190, 165, 0.8)',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-test-title">' . get_bloginfo( 'name' ) . '</h5>';
    echo '<p class="prefix-element-test-content">Just some bogus text ..</p>';
  }
}

```

### Color palette filter

Add the following PHP code into the funcions.php file of your [chil](https://docs.bricksbuilder.io/article/71-child-theme)[d theme](https://academy.bricksbuilder.io/developer/guides/child-theme/) to add your own colors to the default color palette (option #1) or replace all default colors with your own choice of colors (option #2).

```php
// functions.php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add individual color
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

> **Note**
>
> If you have saved any custom colors with the builder you need to reset your global settings in order for your new default colors to take effect.

---

<a id="developer-controls-element-controls"></a>

# Element Controls

Source: https://academy.bricksbuilder.io/developer/controls/element-controls/

*Reference for the Bricks Element Controls control, including its options, CSS mapping, and usage in custom elements.*

Element controls allow the user to change the content and appearance of an element. You can define the controls of an element with the set_controls() method in your [element PHP class](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/).

Example element class with control parameters for control `testColor`:

```php
class Prefix_Element_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['testColor'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Text color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'small' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.content',
          'important' => true, // Optional
        ],
      ],
      'default' => [
        'rgb' => 'rgba(158, 158, 158, .8)',
        'hex' => '#9e9e9e',
      ],
      'pasteStyles' => false,
      'description' => esc_html__( 'Define the content color.', 'bricks' ),
      'required' => ['showText', '!=', ''],
    ];
  }
}
```

The following control parameters are available for all control types. To dive deeper into the arguments of a specific control type select the control from the list at the bottom.

### Universal control arguments

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| tab | string | content | Tab under which to show the control. Accepts: `content` or `style`. |
| group | string |  | Group under which to show the control. By default a control shows ungrouped under the `content` tab. |
| label | string |  | Localized control label. E.g.: `esc_html__( 'Color', 'bricks' ),` |
| type | string |  | Set the control type (see the list below for a list of all available control types). |
| inline | bool | false | Set to true to show control label and input on the same line. |
| small | bool | false | Set to true to show a control input of 60px width. By default inline label and input have equal widths of 50%. |
| css | array |  | Array with CSS rule definitions. Each CSS rule is a separate array and requires a `property` and `selector` parameter. |
| default | string/array |  | Default control value. Either a string or an array (depending on the control type, see control list below for specific control default) |
| pasteStyles | bool | true | Set to true excludes setting from being pasted via the builders' custom right click "Paste Styles". Recommended for all controls that output HTML content instead of CSS. |
| description | string |  | Optional description for controls that need additional explanation or link to a resource. |
| required | array |  | Show control in relation to the setting of another control.<br /><br />Parameter #1: control ID<br /><br />Parameter #2: comparison operator: `=`, `!=`, `>`, `<`, `>=`, `<=`<br /><br />Example: `'required' => ['layout', '=', ['list', 'grid']],`<br /><br />Required condition: Show this control if setting value of control `layout` equals `=` either `list` or `grid`. |

### Controls Types

| Control Type | Output (Content/CSS) |
| --- | --- |
| [apply](https://academy.bricksbuilder.io/developer/controls/apply-control/) | None |
| [align-items](https://academy.bricksbuilder.io/developer/controls/align-items-control/) | CSS |
| [audio](https://academy.bricksbuilder.io/developer/controls/audio-control/) | Content |
| [background](https://academy.bricksbuilder.io/developer/controls/background-control/) | CSS |
| [border](https://academy.bricksbuilder.io/developer/controls/border-control/) | CSS |
| [box-shadow](https://academy.bricksbuilder.io/developer/controls/box-shadow-control/) | CSS |
| [checkbox](https://academy.bricksbuilder.io/developer/controls/checkbox-control/) | Conditional |
| [code](https://academy.bricksbuilder.io/developer/controls/code-control/) | Content |
| [color](https://academy.bricksbuilder.io/developer/controls/color-control/) | CSS |
| [datepicker](https://academy.bricksbuilder.io/developer/controls/datepicker-control/) | Content |
| [dimensions](https://academy.bricksbuilder.io/developer/controls/dimensions-control/) | CSS |
| [direction](https://academy.bricksbuilder.io/developer/controls/direction-control/) | CSS |
| [editor](https://academy.bricksbuilder.io/developer/controls/editor-control/) | Content |
| [filters](https://academy.bricksbuilder.io/developer/controls/filters-control/) | CSS |
| [gradient](https://academy.bricksbuilder.io/developer/controls/gradient-control/) | CSS |
| [icon](https://academy.bricksbuilder.io/developer/controls/icon-control/) | Content |
| [image](https://academy.bricksbuilder.io/developer/controls/image-control/) | Content/CSS |
| [image-gallery](https://academy.bricksbuilder.io/developer/controls/image-gallery-control/) | Content |
| [info](https://academy.bricksbuilder.io/developer/controls/info-control/) | Builder panel only |
| [justify-content](https://academy.bricksbuilder.io/developer/controls/justify-content-control/) | CSS |
| [link](https://academy.bricksbuilder.io/developer/controls/link-control/) | Content |
| [number](https://academy.bricksbuilder.io/developer/controls/number-control/) | Content/CSS |
| [posts](https://academy.bricksbuilder.io/builder/elements/wordpress/posts/) | Content |
| [repeater](https://academy.bricksbuilder.io/developer/controls/repeater-control/) | Content |
| [select](https://academy.bricksbuilder.io/developer/controls/select-control/) | Content/CSS |
| [slider](https://academy.bricksbuilder.io/developer/controls/slider-control/) | Content |
| [svg](https://academy.bricksbuilder.io/developer/controls/svg-control/) | Content |
| [text](https://academy.bricksbuilder.io/developer/controls/text-control/) | Content |
| [textarea](https://academy.bricksbuilder.io/developer/controls/textarea-control/) | Content |
| [text-align](https://academy.bricksbuilder.io/developer/controls/text-align-control/) | CSS |
| [text-decoration](https://academy.bricksbuilder.io/developer/controls/text-decoration-control/) | CSS |
| [text-shadow](https://academy.bricksbuilder.io/developer/controls/text-shadow-control/) | CSS |
| [text-transform](https://academy.bricksbuilder.io/developer/controls/text-transform-control/) | CSS |
| [typography](https://academy.bricksbuilder.io/developer/controls/typography-control/) | CSS |

---

<a id="developer-controls-editor-control"></a>

# Editor Control

Source: https://academy.bricksbuilder.io/developer/controls/editor-control/

*Reference for the Bricks Editor control, including its options, CSS mapping, and usage in custom elements.*

The editor control provides the default WordPress editor. To directly edit content in the builder preview set the `inlineEditing` properties. See the code example below:

```php
class Prefix_Element_Editor extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleEditor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text editor', 'bricks' ),
      'type' => 'editor',
      'inlineEditing' => [
        'selector' => '.text-editor', // Mount inline editor to this CSS selector
        'toolbar' => true, // Enable/disable inline editing toolbar
      ],
      'default' => esc_html__( 'Here goes the content ..', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleEditor'] ) ) {
      echo '<div class="text-editor">' . $this->settings['exampleEditor'] . '</div>';
    }
  }
}
```

---

<a id="developer-controls-dimensions-control"></a>

# Dimensions Control

Source: https://academy.bricksbuilder.io/developer/controls/dimensions-control/

*Reference for the Bricks Dimensions control, including its options, CSS mapping, and usage in custom elements.*

The dimensions control is perfect for adding multi-directional CSS properties such as margin and padding (top/right/bottom/left). You can set the directions to anything you want via the `directions` property.

```php
class Prefix_Element_Dimensions extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleDimensions'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title padding', 'bricks' ),
      'type' => 'dimensions',
      'css' => [
        [
          'property' => 'padding',
          'selector' => '.prefix-element-dimensions-title',
        ]
      ],
      'default' => [
        'top' => '30px',
        'right' => 0,
        'bottom' => '10em',
        'left' => 0,
      ],
      // 'unitless' => false, // false by default
      // Custom directions
      // 'directions' => [
        // 'offsetX' => esc_html__( 'Offset X', 'bricks' ),
        // 'offsetY' => esc_html__( 'Offset Y', 'bricks' ),
        // 'spread'  => esc_html__( 'Spread', 'bricks' ),
        // 'blur'    => esc_html__( 'Offset Y', 'bricks' ),
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-dimensions-title">' . get_bloginfo( 'name' ) . '</h5>';
  }
}
```

---

<a id="developer-controls-gradient-control"></a>

# Gradient Control

Source: https://academy.bricksbuilder.io/developer/controls/gradient-control/

*Reference for the Bricks Gradient control, including its options, CSS mapping, and usage in custom elements.*

The gradient control lets you define an unlimited number of gradients that you can apply to text, background, and as an overlay.

You can set the CSS selector in the control, adjust the angle between 0 and 360°, and set a color stop for each color.

```php
class Prefix_Element_Gradient extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleGradient'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Gradient', 'bricks' ),
      'type' => 'gradient',
      'css' => [
        [
          'property' => 'background-image',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo get_bloginfo( 'name' );
  }
}
```

> **Note**
>
> All sections, rows, columns, and elements already have a **CSS Gradient** control under the Style tab Gradient / Overlay group.

---

<a id="developer-controls-icon-control"></a>

# Icon Control

Source: https://academy.bricksbuilder.io/developer/controls/icon-control/

*Reference for the Bricks Icon control, including its options, CSS mapping, and usage in custom elements.*

The icon control lets you select and output icons from the following icon font libraries:

- [Fontawesome 6](https://fontawesome.com/icons?d=gallery&m=free)
- [Ionicons 4](https://ionic.io/ionicons/v4/cheatsheet.html)
- [Themify](https://themify.me/themify-icons)

The user can also select individually uploaded SVG files if you've enabled "**SVG Uploads**" under `Bricks > Settings` in your WordPress dashboard, and custom icon sets since Bricks 2.0.

```php
class Prefix_Element_Icon extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleIcon'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Icon', 'bricks' ),
      'type' => 'icon',
      'default' => [
        'library' => 'themify', // fontawesome/ionicons/themify
        'icon' => 'ti-star',    // Example: Themify icon class
      ],
      'css' => [
        [
          'selector' => '.icon-svg', // Use to target SVG file
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    // Set icon 'class' attribute
    if ( isset( $this->settings['exampleIcon'] ) ) {
      Helpers::render_control_icon( $settings['exampleIcon'], ['test-class', 'test-class-2'] );
    }
  }
}
```

---

<a id="developer-controls-filters-control"></a>

# Filters Control

Source: https://academy.bricksbuilder.io/developer/controls/filters-control/

*Reference for the Bricks Filters control, including its options, CSS mapping, and usage in custom elements.*

The filters control offers the following [CSS filters](https://developer.mozilla.org/en-US/docs/Web/CSS/filter): `blur`, `brightness`, `contrast`, `hue`, `invert`, `opacity`, `saturation`, `sepia`.

```php
class Prefix_Element_Filters extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleFilters'] = [
      'tab' => 'content',
      'label' => esc_html__( 'CSS filters', 'bricks' ),
      'type' => 'filters',
      'inline' => true,
      'css' => [
        [
          'property' => 'filter',
          'selector' => '.css-filter',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="css-filter">' . echo get_bloginfo( 'name' ); . '</div>';
  }
}
```

> **Note**
>
> All sections, rows, columns, and elements already have a **CSS Filters** control under the Style tab CSS group.

---

<a id="developer-controls-image-control"></a>

# Image Control

Source: https://academy.bricksbuilder.io/developer/controls/image-control/

*Reference for the Bricks Image control, including its options, CSS mapping, and usage in custom elements.*

The image control lets you select a single image from your media library. Once an image has been selected you can choose the image size.

You can either use the returned image `id` and `size` to render an image on your page or as a `background-image` via the CSS control property. See the code example below.

> **Note**
>
> **TIP:** Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.

```php
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImage'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image', 'bricks' ),
      'type' => 'image',
      // Use the selected image as a background image
      // 'css' => [
      //   [
      //     'property' => 'background-image',
      //     'selector' => '.bricks-video-overlay-image',
      //   ],
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    // Dump 'exampleImage' settings on the screen
    // var_dump( $this->settings['exampleImage'] );

    if ( isset( $this->settings['exampleImage'] ) ) {
      // Render <img> tag by prodiving image 'id' and 'size'
      //
      echo wp_get_attachment_image(
        $this->settings['exampleImage']['id'],
        $this->settings['exampleImage']['size'],
        false,
        [] // Image attributes
      );
    } else {
      esc_html_e( 'No image selected.', 'bricks' );
    }
  }
}
```

---

<a id="developer-controls"></a>

# Controls

Source: https://academy.bricksbuilder.io/developer/controls/

*Reference the Bricks controls used in custom elements and builder extensions, from layout and typography controls to media, code, query, and repeater controls.*

Bricks controls define how users edit custom element settings inside the builder. This section helps you understand the available control types, the data they store, and when to use each one.

## Common control groups

- [Element Controls](https://academy.bricksbuilder.io/developer/controls/element-controls/) for the overall structure of element settings
- [Content Controls](https://academy.bricksbuilder.io/developer/controls/text-control/) for text, textarea, editor, select, and checkbox inputs
- [Styling Controls](https://academy.bricksbuilder.io/developer/controls/color-control/) for visual styling fields such as color, typography, border, and shadow
- [Media Controls](https://academy.bricksbuilder.io/developer/controls/image-control/) for images, galleries, icons, SVG, and audio
- [Advanced Controls](https://academy.bricksbuilder.io/developer/controls/query-control/) for query, repeater, code, filters, and apply workflows

---

<a id="developer-controls-info-control"></a>

# Info Control

Source: https://academy.bricksbuilder.io/developer/controls/info-control/

*Reference for the Bricks Info control, including its options, CSS mapping, and usage in custom elements.*

The info control does not affect the HTML or CSS on the frontend. It serves as a builder-only helper controls to provide additional information.

Example below: the **Alert** element displays an info control when the *Type* is set to *Custom*.

```php
class Prefix_Element_Info extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['type'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
        'custom' => esc_html__( 'Custom', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];

    $this->controls['typeInfo'] = [
      'tab' => 'content',
      'content' => esc_html__( 'Customize alert in STYLE tab.', 'bricks' ),
      'type' => 'info',
      'required' => ['type', '=', 'custom'], // Show info control if 'type' = 'custom'
    ];
  }
}
```

---

<a id="developer-controls-image-gallery-control"></a>

# Image Gallery Control

Source: https://academy.bricksbuilder.io/developer/controls/image-gallery-control/

*Reference for the Bricks Image Gallery control, including its options, CSS mapping, and usage in custom elements.*

The image gallery control lets you select multiple images from your media library. Once images have been selected you can choose the image size.

Your selected images are stored in an array, which you have to loop through (see code example below). Use the `id` and `size`  of each image to render it on your page.

> **Note**
>
> **Tip #1:** Hold down the *SHIFT* key in order to select multiple image in your media library.

> **Note**
>
> **Tip #2:** Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.

```php
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImageGallery'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image gallery', 'bricks' ),
      'type' => 'image-gallery',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleImageGallery'] ) ) {
      foreach( $this->settings['exampleImageGallery'] as $index => $image ) {
        echo wp_get_attachment_image(
          $image['id'],
          $image['size'],
          false,
          ['class' => 'css-filter']
        );
      }
    } else {
      esc_html_e( 'No image(s) selected.', 'bricks' );
    }
  }
}
```

---

<a id="developer-controls-justify-content-control"></a>

# Justify Content Control (Flexbox)

Source: https://academy.bricksbuilder.io/developer/controls/justify-content-control/

*Reference for the Bricks Justify Content Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements.*

Use the justify-content control to allow users to set the `justify-content` CSS property (alignment along the [main-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)) of your CSS flexbox layout.

There is also a [`align-items`](https://academy.bricksbuilder.io/developer/controls/align-items-control/) control to allow users to set the alignment along the cross axis of your CSS flexbox layout:

```php
public function set_controls() {
  $this->controls['justifyContent'] = [
    'tab'   => 'content',
    'label' => esc_html__( 'Justify content', 'bricks' ),
    'type'  => 'justify-content',
    'css'   => [
      [
        'property' => 'justify-content',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}
```

---

<a id="developer-controls-link-control"></a>

# Link Control

Source: https://academy.bricksbuilder.io/developer/controls/link-control/

*Reference for the Bricks Link control, including its options, CSS mapping, and usage in custom elements.*

The link control give you the choice of different link types:

- Internal post/page
- External URL
- Popup (image, video)

```php
class Prefix_Element_Link extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleLink'] = [
      'tab'         => 'content',
      'label'       => esc_html__( 'Link', 'bricks' ),
      'type'        => 'link',
      'pasteStyles' => false,
      'placeholder' => esc_html__( 'http://yoursite.com', 'bricks' ),
      // 'exclude'     => [
      //  'rel',
      //  'newTab',
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleLink'] ) ) {
      // Set link attributes by passing attribute key and link settings
      $this->set_link_attributes( 'a', $this->settings['exampleLink'] );

      echo '<a ' . $this->render_attributes( 'a' ) . '>' . get_bloginfo( 'name' ) . '</a>';
    } else {
      esc_html_e( 'No link provided.', 'bricks' );
    }
  }
}
```

---

<a id="developer-controls-number-control"></a>

# Number Control

Source: https://academy.bricksbuilder.io/developer/controls/number-control/

*Reference for the Bricks Number control, including its options, CSS mapping, and usage in custom elements.*

The number control represents a simple number input field. It has the following custom properties:

- units (optional: boolean or array)
- unit (string: `px`, `em`, `rem` etc.)
- min (number)
- step (Default: 1) (Custom: '0.1' etc.)

Use it to render a number to the page or set the `css` control property to target a specific CSS style.

```php
class Prefix_Element_Number extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleNumber'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Number', 'bricks' ),
      'type' => 'number',
      'min' => 0,
      'step' => '0.1', // Default: 1
      'inline' => true,
      'default' => 123,
    ];

    $this->controls['examplePadding'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Padding in px', 'bricks' ),
      'type' => 'number',
      'unit' => 'px',
      'inline' => true,
      'css' => [
        [
          'property' => 'padding',
        ],
      ],
      'default' => 33,
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleNumber'] ) ) {
      echo esc_html__( 'Number: ', 'bricks' ) . $this->settings['exampleNumber'];
    } else {
      esc_html_e( 'No number provided.', 'bricks' );
    }
  }
}
```

---

<a id="developer-controls-query-control"></a>

# Query Control

Source: https://academy.bricksbuilder.io/developer/controls/query-control/

*Reference for the Bricks Query control, including its options, CSS mapping, and usage in custom elements.*

The query control lets you set query arguments to retrieve items of any post type. Use the returned value to set up a custom `WP_Query` to render the matching posts in any way you want.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleQueryArgs'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Posts', 'bricks' ),
      'type' => 'query',
      // Default required for query to populate
      'default' => [
        'post_type' => 'post',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $query_args = $this->settings['exampleQueryArgs'];
    $posts_query = new WP_Query( $query_args );

    // Standard WordPress loop
    if ( $posts_query->have_posts() ) :
      while ( $posts_query->have_posts() ) : $posts_query->the_post();
        // Render post title and thumbnail
        the_title( '<h5>', '</h5>' );
        the_post_thumbnail( 'thumbnail' );
      endwhile;

      wp_reset_postdata();
    else :
     esc_html_e( 'No posts matched your criteria.', 'bricks' );
    endif;
  }
}
```

### Resources

- [https://codex.wordpress.org/Class_Reference/WP_Query#Parameters](https://codex.wordpress.org/Class_Reference/WP_Query#Parameters)

---

<a id="developer-controls-repeater-control"></a>

# Repeater Control

Source: https://academy.bricksbuilder.io/developer/controls/repeater-control/

*Reference for the Bricks Repeater control, including its options, CSS mapping, and usage in custom elements.*

The repeater control lets you create repeatable fields. Fields can be cloned, deleted, and sorted via Drag & Drop. Use the `fields` argument to set up the field controls.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleRepeater'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Repeater', 'bricks' ),
      'type' => 'repeater',
      'titleProperty' => 'title', // Default 'title'
      'default' => [
        [
          'title' => 'Design',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Code',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Launch',
          'description' => 'Here goes the description for repeater item.',
        ],
      ],
      'placeholder' => esc_html__( 'Title placeholder', 'bricks' ),
      'fields' => [
        'title' => [
          'label' => esc_html__( 'Title', 'bricks' ),
          'type' => 'text',
        ],
        'description' => [
          'label' => esc_html__( 'Description', 'bricks' ),
          'type' => 'textarea',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $items = $this->settings['exampleRepeater'];

    if ( count( $items ) ) {
      foreach ( $items as $item ) {
        echo '<h4>' . $item['title'] . '</h4>';
        echo '<p>' . $item['description'] . '</p>';
      }
    } else {
      esc_html_e( 'No items defined.', 'bricks' );
    }
  }
}
```

---

<a id="developer-controls-select-control"></a>

# Select Control

Source: https://academy.bricksbuilder.io/developer/controls/select-control/

*Reference for the Bricks Select control, including its options, CSS mapping, and usage in custom elements.*

The select control lets you select an option from a dropdown. It can be used to render content or CSS styling. Use the options array to populate the dropdown with your own options. The option key should be all lowercase, with no spaces.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Example content
    $this->controls['exampleSelectTitleTag'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title tag', 'bricks' ),
      'type' => 'select',
      'options' => [
        'h1' => 'H1',
        'h2' => 'H2',
        'h3' => 'H3',
        'h4' => 'H4',
        'h5' => 'H5',
        'h6' => 'H6',
      ],
      'inline' => true,
      'placeholder' => esc_html__( 'Select tag', 'bricks' ),
      'multiple' => true,
      'searchable' => true,
      'clearable' => true,
      'default' => 'h3',
    ];

    // Example CSS
    $this->controls['exampleSelectTextAlign'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text align', 'bricks' ),
      'type' => 'select',
      'options' => [
        'right' => esc_html__( 'Right', 'bricks' ),
        'center' => esc_html__( 'Center', 'bricks' ),
        'left' => esc_html__( 'Left', 'bricks' ),
      ],
      'inline' => true,
      'css' => [
        [
          'property' => 'text-align',
          'selector' => '.prefix-title',
        ],
      ],
      'placeholder' => esc_html__( 'Select', 'bricks' ),
      'default' => 'center', // Option key
    ];
  }

  // Render element HTML
  public function render() {
    $title_tag = isset( $this->settings['exampleSelectTitleTag'] ) ? $this->settings['exampleSelectTitleTag'] : 'h5';
    echo '<' . $title_tag . ' class="prefix-title">' . get_bloginfo( 'name' ) . '</' . $title_tag . '>';
  }
}
```

---

<a id="developer-controls-slider-control"></a>

# Slider Control

Source: https://academy.bricksbuilder.io/developer/controls/slider-control/

*Reference for the Bricks Slider control, including its options, CSS mapping, and usage in custom elements.*

The slider control shows a draggable range input field. Default units are `px`, `em` and `rem`. You can set the following control parameters:

- units (array with custom units and `min`, `max`, `step` attributes)
- unitless (set to `false` for plain number)

```php
class Prefix_Element_Slider extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSliderFontSize'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Font size', 'bricks' ),
      'type' => 'slider',
      'css' => [
        [
          'property' => 'font-size',
        ],
      ],
      'units' => [
        'px' => [
          'min' => 1,
          'max' => 50,
          'step' => 1,
        ],
        'em' => [
          'min' => 1,
          'max' => 20,
          'step' => 0.1,
        ],
      ],
      'default' => '30px',
      'description' => esc_html__( 'Slider adjusts font size via CSS.', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3>' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range)

---

<a id="developer-controls-text-align-control"></a>

# Text Align Control

Source: https://academy.bricksbuilder.io/developer/controls/text-align-control/

*Reference for the Bricks Text Align control, including its options, CSS mapping, and usage in custom elements.*

Use the **text-align** control to allow users to set the text-align CSS property like so:

```php
public function set_controls() {
  $this->controls['textAlign'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text align', 'bricks' ),
    'type' => 'text-align',
    'css' => [
      [
        'property' => 'text-align',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

---

<a id="developer-controls-text-control"></a>

# Text Control

Source: https://academy.bricksbuilder.io/developer/controls/text-control/

*Reference for the Bricks Text control, including its options, CSS mapping, and usage in custom elements.*

The text control displays a text input field. You can set the following parameters:

- `spellcheck`: true/false. (Default: false)
- `trigger`: 'keyup'/'enter'. (Default: keyup)
- `inlineEditing`: Set to true to enable

```php
class Prefix_Element_Text extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleText'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text', 'bricks' ),
      'type' => 'text',
      'spellcheck' => true, // Default: false
      // 'trigger' => 'enter', // Default: 'enter'
      'inlineEditing' => true,
      'default' => 'Here goes your text ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleText'] ) ) {
      echo $this->settings['exampleText'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg)
- [https://css-tricks.com/using-svg/](https://css-tricks.com/using-svg/)

---

<a id="developer-controls-svg-control"></a>

# SVG Control

Source: https://academy.bricksbuilder.io/developer/controls/svg-control/

*Reference for the Bricks SVG control, including its options, CSS mapping, and usage in custom elements.*

The SVG control lets you select an SVG (Scalable Vector Graphic) file from the media library. The selected SVG returns an array with the following keys:

- `id` (media library item ID)
- `filename`
- `url`

We recommend rendering the SVG inline as shown in the code example below. This way you can easily customize it via CSS.

```php
class Prefix_Element_Svg extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSvg'] = [
      'tab' => 'content',
      'type' => 'svg',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleSvg']['url'] ) ) {
      echo file_get_contents( esc_url( $this->settings['exampleSvg']['url'] ) );
    } else {
      esc_html_e( 'No SVG selected.', 'bricks' );
    }
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg)
- [https://css-tricks.com/using-svg/](https://css-tricks.com/using-svg/)

---

<a id="developer-controls-text-decoration-control"></a>

# Text Decoration Control

Source: https://academy.bricksbuilder.io/developer/controls/text-decoration-control/

*Reference for the Bricks Text Decoration control, including its options, CSS mapping, and usage in custom elements.*

Use the **text-decoration** control to allow users to set the text-decoration CSS property like so:

```php
public function set_controls() {
  $this->controls['textDecoration'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text decoration', 'bricks' ),
    'type' => 'text-decoration',
    'css' => [
      [
        'property' => 'text-decoration',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

---

<a id="developer-controls-text-shadow-control"></a>

# Text Shadow Control

Source: https://academy.bricksbuilder.io/developer/controls/text-shadow-control/

*Reference for the Bricks Text Shadow control, including its options, CSS mapping, and usage in custom elements.*

The text-shadow control displays a popup that lets you set the CSS text-shadow of a specified HTML text element.

```php
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text Shadow', 'bricks' ),
      'type' => 'text-shadow',
      'css' => [
        [
          'property' => 'text-shadow',
          'selector' => '.prefix-text',
        ],
      ],
      'inline' => true,
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-text">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

### Resources

[https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow)

---

<a id="developer-controls-text-transform-control"></a>

# Text Transform Control

Source: https://academy.bricksbuilder.io/developer/controls/text-transform-control/

*Reference for the Bricks Text Transform control, including its options, CSS mapping, and usage in custom elements.*

Use the **text-transform** control to allow users to set the text-transform CSS property like so:

```php
public function set_controls() {
  $this->controls['textTransform'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text transform', 'bricks' ),
    'type' => 'text-transform',
    'css' => [
      [
        'property' => 'text-transform',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

---

<a id="developer-controls-textarea-control"></a>

# Textarea Control

Source: https://academy.bricksbuilder.io/developer/controls/textarea-control/

*Reference for the Bricks Textarea control, including its options, CSS mapping, and usage in custom elements.*

The textarea control displays a textarea input field. You can set the following parameters:

- `rows` (number. Default: 5)
- `readonly` (true/false. Default: false)
- `spellcheck` (true/false. Default: false)
- `inlineEditing` (true to enable)

```php
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextarea'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Textarea', 'bricks' ),
      'type' => 'textarea',
      // 'readonly' => true, // Default: false
      'rows' => 10, // Default: 5
      'spellcheck' => true, // Default: false
      'inlineEditing' => true,
      'default' => 'Here goes your content ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleTextarea'] ) ) {
      echo $this->settings['exampleTextarea'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

---

<a id="developer-controls-typography-control"></a>

# Typography Control

Source: https://academy.bricksbuilder.io/developer/controls/typography-control/

*Reference for the Bricks Typography control, including its options, CSS mapping, and usage in custom elements.*

The typography control provides the following CSS properties:

- color
- font-size
- text-align
- text-transform
- font-family
- font-weight
- font-style
- line-height
- letter-spacing
- text-shadow
- text-decoration

Use the `exclude` parameter to hide specific typography properties. Set `popup` to false to show control inline.

```php
class Prefix_Element_Typography extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTypography'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Typography', 'bricks' ),
      'type' => 'typography',
      'css' => [
        [
          'property' => 'typography',
          'selector' => '.prefix-typography',
        ],
      ],
      'inline' => true,
      // 'exclude' => [
      //   'font-family',
      //   'font-weight',
      //   'text-align',
      //   'text-transform',
      //   'font-size',
      //   'line-height',
      //   'letter-spacing',
      //   'color',
      //   'text-shadow',
      // ],
      // 'popup' => false, // Default: true
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-typography">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

---

<a id="developer-guides-asset-loading"></a>

# Asset Loading Optimization

Source: https://academy.bricksbuilder.io/developer/guides/asset-loading/

*Optimize asset loading in Bricks extensions so scripts and styles are only loaded where they are actually needed.*

"Performance" being one of Bricks' three pillars, Bricks only loads many frontend assets when they are needed on the current page.

https://www.youtube.com/watch?v=O_B19LBtnwM&t=45s

Bricks always enqueues the main frontend stylesheet through the `bricks-frontend` handle and the main frontend script through the `bricks-scripts` handle. Additional libraries such as sliders, lightboxes, maps, animations, icon fonts, and date pickers are registered and loaded only when needed.

By default, Bricks uses the cascade-layer frontend stylesheet (`frontend-layer.min.css`). If cascade layers are disabled, Bricks falls back to `frontend.min.css`. When the CSS loading method is set to "External Files", Bricks uses the lighter frontend stylesheet (`frontend-light-layer.min.css`, or `frontend-light.min.css` when cascade layers are disabled) and loads the generated CSS files for the current page.

## How To Reduce Asset Loading Even Further through "External Files" {#external-files}

By default, generated styles such as page settings, template settings, element styles, global custom CSS, theme styles, color palettes, global class CSS, and other Bricks data are output inline.

To further optimize & minimize the loaded styles you can set the "CSS Loading Method" under "Bricks - Settings - Performance" to "**External Files**".

To regenerate all CSS files in one go, click **Regenerate CSS files** under **Bricks > Settings > Performance > CSS loading method**. This action is available after setting CSS loading method to **External Files**.

**Please click the "Regenerate CSS files" button once you've changed the CSS loading method to "External Files", so Bricks can create the required directory and CSS files.**

This generates minified CSS files for your Bricks data within the `wp-content/uploads/bricks/css` directory (or whatever you've set as your WordPress "uploads" directory) and serves them as needed according to the requested page.

> **Note**
>
> If the "External Files" CSS loading method does conflict for some reason with your server or plugin caching solution or outputs incorrect or missing styles, please revert to the default "**Inline Styles**" CSS loading method, and report the issue to us via [email](https://bricksbuilder.io/contact/), so we can address it. Thank you!

![](https://academy.bricksbuilder.io/assets/bricks-builder-css-loading-method-external-files-1024x835.png)

<figcaption>

CSS Loading Method: "External Files"

</figcaption>

## How To Enqueue Individual Styles & Scripts {#enqueue}

If you are working with a third-party Bricks plugin or if for some reason a certain style/script is not being loaded as needed, you can always load/enqueue those individually to your own needs by following the instructions below.

What follows is a list of Bricks style & script names which you can enqueue on any of your pages as needed through your child theme's functions.php by hooking into the `wp_enqueue_scripts` WordPress action or inside the `enqueue_scripts` function in case your [custom Bricks element](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/) depends on any of those styles and/or scripts.

```php
add_action( 'wp_enqueue_scripts', function() {
  // isotopeJS (e.g. metro & masonry layouts)
  wp_enqueue_script( 'bricks-isotope' );
  wp_enqueue_style( 'bricks-isotope' );

  // Icon font files
  wp_enqueue_style( 'bricks-font-awesome-6' );
  wp_enqueue_style( 'bricks-font-awesome-6-brands' );
  wp_enqueue_style( 'bricks-ionicons' );
  wp_enqueue_style( 'bricks-themify-icons' );

  // Animations
  wp_enqueue_style( 'bricks-animate' );

  // Tooltips
  wp_enqueue_style( 'bricks-tooltips' );

  // Datepicker
  wp_enqueue_script( 'bricks-flatpickr' );
  wp_enqueue_style( 'bricks-flatpickr' );

  // swiperJS (e.g. slider, carousel)
  wp_enqueue_script( 'bricks-swiper' );
  wp_enqueue_style( 'bricks-swiper' );

  // splideJS (e.g. nestable slider, carousel)
  wp_enqueue_script( 'bricks-splide' );
  wp_enqueue_style( 'bricks-splide' );

  // Lightbox
  wp_enqueue_script( 'bricks-photoswipe' );
  wp_enqueue_script( 'bricks-photoswipe-lightbox' );
  wp_enqueue_script( 'bricks-photoswipe-caption' );
  wp_enqueue_style( 'bricks-photoswipe' );

  // Leaflet map
  wp_enqueue_script( 'bricks-leaflet' );
  wp_enqueue_style( 'bricks-leaflet' );

  // Code prettifier
  wp_enqueue_script( 'bricks-prettify' );
  wp_enqueue_style( 'bricks-prettify' );

  // Choices.js
  wp_enqueue_script( 'bricks-choices-lib' );
  wp_enqueue_script( 'bricks-choices-js' );
  wp_enqueue_style( 'bricks-choices' );
}, 11 );
```

---

<a id="developer-guides-best-practices"></a>

# Best Practices

Source: https://academy.bricksbuilder.io/developer/guides/best-practices/

*Follow Bricks development best practices for permalinks, image handling, child-theme usage, and safer long-term customization.*

Please keep the points below in mind when working with Bricks:

| **Permalink Settings** | We recommend **Post name** permalinks for cleaner URLs. Go to **Settings > Permalinks**, select **Post name**, and click **Save Changes**. Bricks builds builder URLs from the page permalink, so other WordPress permalink structures can work as long as WordPress resolves them correctly. |
| --- | --- |
| **Min. Image Dimensions** | Upload images with a minimum width of 600 pixels. Ideally 1600 pixels in width or more.<br /><br />If you already have images in your media library and start working with Bricks make sure to [Regenerate Thumbnails](https://wordpress.org/plugins/regenerate-thumbnails/) so all Bricks-specific image sizes are generated properly. |
| **Never Edit Theme Code Directly** | **Do not edit any of the Bricks theme core files directly!**<br /><br />As all your changes will be lost/overwritten when updating the theme. Use the [Bricks child theme](https://academy.bricksbuilder.io/developer/guides/child-theme/) or a code snippet plugin to extend Bricks with your custom code. |

---

<a id="developer-guides-bricks-cli"></a>

# Bricks CLI

Source: https://academy.bricksbuilder.io/developer/guides/bricks-cli/

*Use Bricks CLI commands through WP-CLI to run builder-related maintenance tasks from the command line.*

Bricks 1.8.1+ integrates with the [WP-CLI](https://wp-cli.org/) (WordPress Command Line Interface). Allowing you to perform specific tasks from your server's command line interface instead of the GUI (Graphical User Interface).

### Regenerates CSS Files

Requires the Bricks "CSS loading method" to be set to "external files".

`wp bricks regenerate_assets`

---

<a id="developer-guides-child-theme"></a>

# Child Theme

Source: https://academy.bricksbuilder.io/developer/guides/child-theme/

*Set up a Bricks child theme for custom PHP, assets, templates, and safer update-friendly development.*

> **Note**
>
> Please do not edit any of the Bricks theme core files directly, as updating the theme will cause all your changes to be lost.

Instead, use the Bricks child theme to make modifications and overwrite files. You can download the Bricks child theme directly from your [Bricks account](https://my.bricksbuilder.io/).

Upload this child theme ZIP file (bricks-child.zip) like any other WordPress theme. Go to **Appearance → Themes** and activate **Bricks Child Theme**. You can add your own styles to **style.css**.

## How To Enqueue Scripts (JS) & Styles (CSS)

In order to load your files only on the front end & the canvas and not in the builder panel (as your custom CSS might affect the builder), you have to check against `bricks_is_builder_main()` like this:

```php
add_action( 'wp_enqueue_scripts', function() {
  // Code & check below enqueues your files on the canvas & frontend, not the builder panel. Otherwise custom CSS might affect builder)
  if ( ! bricks_is_builder_main() ) {
    wp_enqueue_style( 'bricks-child', get_stylesheet_uri(), ['bricks-frontend'], filemtime( get_stylesheet_directory() . '/style.css' ) );
  }
} );
```

You can learn more about how a Child Theme works by visiting the official WordPress Codex: [https://developer.wordpress.org/themes/advanced-topics/child-themes/](https://developer.wordpress.org/themes/advanced-topics/child-themes/)

The `functions.php` file of a child theme, unlike `style.css`, does not override the `functions.php` file of the parent theme. Instead, it is loaded in addition to the parent theme's `functions.php`, right before the parent file.

---

<a id="developer-guides-converter"></a>

# Converter

Source: https://academy.bricksbuilder.io/developer/guides/converter/

*Use the Bricks converter workflow to transform source markup or data into Bricks-compatible structures more safely.*

Bricks offers multiple so-called "Converter" options for legacy data migrations.

The Converter is a built-in tool that scans your database for outdated Bricks data and automatically updates it to the latest valid syntax of the installed version.

> **Note**
>
> The converter performs changes to the Bricks data in your database. So please perform a full-site backup before running the converter.

In current Bricks versions, the database Converter row is hidden from the normal Settings screen. Treat it as a legacy/support workflow, not a routine maintenance step.

When the legacy Converter is run, the process can take a minute or two depending on your server and the size of your Bricks data. Please do not close or refresh the page until you see the green "THE END" success message:

![](https://academy.bricksbuilder.io/assets/bricks-1.4-converter-results-1024x324.png)

<figcaption>

Converter results: Updated Page Settings & Global Custom CSS

</figcaption>

## What is being converted?

With the improved DOM structure and element ID & class names, Bricks replaced the old `bricks-element-` element ID and class prefix with `brxe-`. Structural wrapper IDs such as `#bricks-header`, `#bricks-content`, and `#bricks-footer` are converted to `#brx-header`, `#brx-content`, and `#brx-footer`.

Depending on the selected conversion action, the Converter can update these areas of Bricks data:

- Bricks global settings
- Bricks theme styles
- Bricks global classes
- Bricks page settings
- Bricks page data
- Global elements, including conversion to components
- Bricks templates
- Legacy Container structures
- Entry animations
- Element positioning data

The Converter is not limited to custom CSS/JS. Only run the specific conversion requested for the legacy data you need to migrate.

---

<a id="developer-guides-bricks-css-compatibility-guidelines"></a>

# Bricks CSS: Compatibility guidelines

Source: https://academy.bricksbuilder.io/developer/guides/bricks-css-compatibility-guidelines/

*Follow Bricks CSS compatibility guidelines so custom CSS keeps working across builder output, theme updates, and integrations.*

Bricks aims to use CSS features that are broadly supported in modern browsers and avoid fallbacks that add weight for uncommon older browsers. We use [Baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) as a practical reference when evaluating CSS support in Bricks output.

## What is Baseline?

Baseline is a compatibility model that tracks when web platform features become widely interoperable across all major browsers. It defines two key stages:

- **Newly Available**: Feature works across all major browsers (desktop and mobile).
- **Widely Available**: Reached ~30 months after “Newly Available”; safe to use in production for most users globally (~95% support).

Baseline considers support in the following browsers:

- Apple Safari (iOS)
- Apple Safari (macOS)
- Google Chrome (Android)
- Google Chrome (desktop)
- Microsoft Edge (desktop)
- Mozilla Firefox (Android)
- Mozilla Firefox (desktop)

## Which CSS features does Bricks use?

Bricks output already includes modern CSS such as the [`:where` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:where) and [@layer CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer). Both are listed by MDN as **Widely Available**, which is the kind of broad support we look for before relying on a CSS feature in Bricks output.

![](https://academy.bricksbuilder.io/assets/mdn-baseline.png)

## What happens on much older or less common browsers?

We aim to strike the right balance: adopting modern standards when they’re stable and broadly supported, while avoiding unnecessary technical debt or regressions for the majority of users. Adding fallbacks for edge-case devices below the Baseline threshold would compromise code quality and performance for everyone else.

## Does this affect user-added CSS?

No. This only applies to the CSS generated by Bricks.

You can continue writing your own CSS however you like, including fallbacks or feature checks for legacy devices. Bricks just won't include those fallbacks automatically in its own output.

---

<a id="developer-guides-custom-javascript-events-in-bricks"></a>

# Custom JavaScript events in Bricks

Source: https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks/

*Work with Bricks custom JavaScript events so scripts can respond to builder and frontend interactions more reliably.*

Bricks dispatches custom JavaScript events for several frontend actions. Use these events when your own scripts need to respond to Bricks forms, popups, query filters, AJAX updates, tabs, accordions, or other interactive elements.

## Form element events

- [bricks/form/submit](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-submit) Emitted before an AJAX call for form submission is made.
- [bricks/form/success](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-success) Emitted after a successful form submission AJAX call is returned.
- [bricks/form/error](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-error) Emitted after an error in the form submission AJAX call is returned.

## Tabs / Tabs (Nestable) element events

- [bricks/tabs/changed](#bricks-tabs-changed-code): Emitted after click on a tab title (`@since 1.9.8`)

<span id="bricks-tabs-changed-code"></span>

```php
// Listen for the 'bricks/tabs/changed' event
document.addEventListener('bricks/tabs/changed', (event) => {
  // Extract information from the event detail
  const { elementId, activeIndex, activeTitle, activePane } = event.detail;

  // Only target elementID lwxvfh
  if( elementId !== 'lwxvfh' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Tabs Changed - Element ID: ${elementId}, Active Index: ${activeIndex}, Active Title: ${activeTitle}, Active Pane: ${activePane}`);

  // Your custom logic here
  // For example, update the UI based on the tab change
});
```

## Accordion / Accordion (Nestable) element events

- [bricks/accordion/open](#bricks-accordion-open-code): Emitted after an accordion item is opened/expanded via click action (`@since 1.9.8`)
- [bricks/accordion/close](#bricks-accordion-close-code): Emitted after an accordion item is closed/collapsed via click action (`@since 1.9.8`)

<span id="bricks-accordion-open-code"></span>

```php
// Listen for the 'bricks/accordion/open' event
document.addEventListener('bricks/accordion/open', (event) => {
  // Extract information from the event detail
  const { elementId, openItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Accordion Opened - Element ID: ${elementId}, Open Item ID: ${openItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being opened
});

```

<span id="bricks-accordion-close-code"></span>

```php
// Listen for the 'bricks/accordion/close' event
document.addEventListener('bricks/accordion/close', (event) => {
  // Extract information from the event detail
  const { elementId, closeItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Accordion Closed - Element ID: ${elementId}, Closed Item ID: ${closeItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being closed
});
```

## Animation events

- [bricks/animation/end/\{animationId\}](https://academy.bricksbuilder.io/builder/features/interactions/#bricks-animation-end-code): Emitted when a specified animation (identified by `{animationId}`) completes its playback.

## Popup events

- [bricks/popup/open](https://academy.bricksbuilder.io/builder/features/popup-builder/#bricks-popup-open-close-code) Emitted after popup opened.
- [bricks/popup/close](https://academy.bricksbuilder.io/builder/features/popup-builder/#bricks-popup-open-close-code) Emitted after popup closed.
- [bricks/ajax/popup/start](https://academy.bricksbuilder.io/builder/features/popup-builder/#ajax-events) Emitted before making an AJAX popup call.
- [bricks/ajax/popup/end](https://academy.bricksbuilder.io/builder/features/popup-builder/#ajax-events) Emitted after completing an AJAX popup call.
- [bricks/ajax/popup/loaded](https://academy.bricksbuilder.io/builder/features/popup-builder/#ajax-events) Emitted after adding AJAX popup content to the DOM.

### AJAX popup open event sequence

1. bricks/ajax/popup/start
2. bricks/ajax/popup/end
3. bricks/ajax/popup/loaded
4. bricks/popup/open

## Bricks AJAX events

> **Note**
>
> Bricks AJAX = Infinite Scroll, Load More, AJAX Pagination, or Query Filter.

- [bricks/ajax/start](#bricks-ajax-start-code): Emitted before a Bricks AJAX call is made.
- [bricks/ajax/end](#bricks-ajax-end-code): Emitted after completing a Bricks AJAX call.
- [bricks/ajax/pagination/completed](#bricks-ajax-pagination-completed-code): Emitted after an AJAX pagination call is completed.
- [bricks/ajax/load_page/completed](#bricks-ajax-load_page-completed-code): Emitted after an Infinite scroll AJAX call is completed.
- [bricks/ajax/query_result/completed](#bricks-ajax-query_result-completed-code): Emitted after a Query filter AJAX call is completed.
- [bricks/ajax/nodes_added](#bricks-ajax-nodes_added-code): Emitted after Bricks adds new AJAX result nodes to the DOM. The event detail contains the `queryId`. (`@since 1.11.1`)
- [bricks/ajax/query_result/displayed](#bricks-ajax-query_result-displayed-code): Emitted after adding all filtered results to the DOM.
- [bricks/filter/submit/start](#bricks-filter-submit-start-code): Emitted when a Filter - Submit element starts an AJAX filter submission. The event detail contains the `queryId` and `filterId`. (`@since 2.4`)
- [bricks/filter/submit/end](#bricks-filter-submit-end-code): Emitted when a Filter - Submit AJAX filter submission finishes. The event detail contains the `queryId` and `filterId`. (`@since 2.4`)

### Infinite scroll event sequence

1. bricks/ajax/start
2. bricks/ajax/nodes_added
3. bricks/ajax/end
4. bricks/ajax/load_page/completed

### AJAX pagination event sequence

1. bricks/ajax/start
2. bricks/ajax/nodes_added
3. bricks/ajax/end
4. bricks/ajax/pagination/completed

> **Note**
>
> The `bricks/ajax/pagination/completed` event is only emitted for standalone AJAX pagination. If the Pagination element targets a query that uses Bricks Query Filters, this event is not emitted. In this case, listen for the Query Filter events instead.

### AJAX query filter event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/query_result/completed
4. bricks/ajax/nodes_added
5. bricks/ajax/query_result/displayed

### Filter submit event sequence

The `bricks/filter/submit/start` and `bricks/filter/submit/end` events are specific to the Filter - Submit element. They run only for AJAX filter submissions that refresh the current page results. They are not emitted when the Submit element redirects to another URL.

1. bricks/filter/submit/start
2. bricks/ajax/start
3. bricks/ajax/end
4. bricks/ajax/query_result/completed
5. bricks/ajax/nodes_added
6. bricks/ajax/query_result/displayed
7. bricks/filter/submit/end

Use these events when your script should react only to a deliberate submit action, not to every query filter AJAX request.

<span id="bricks-ajax-start-code"></span>

```php
document.addEventListener('bricks/ajax/start', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request start
});
```

<span id="bricks-ajax-end-code"></span>

```php
document.addEventListener('bricks/ajax/end', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request end
});
```

<span id="bricks-ajax-pagination-completed-code"></span>

```php
document.addEventListener('bricks/ajax/pagination/completed', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, handle the completed pagination for the specific queryId
});
```

<span id="bricks-ajax-load_page-completed-code"></span>

```php
document.addEventListener('bricks/ajax/load_page/completed', (event) => {
  // Extract information from the event detail
  const { queryTrailElement, queryId } = event.detail;

  // Your custom logic here
  // For example, handle the completed AJAX page load for the specific queryId and queryTrailElement
});
```

<span id="bricks-ajax-query_result-completed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/completed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```

<span id="bricks-ajax-nodes_added-code"></span>

```php
document.addEventListener('bricks/ajax/nodes_added', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, initialize scripts that need the new AJAX result nodes to exist first
});
```

<span id="bricks-ajax-query_result-displayed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/displayed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```

<span id="bricks-filter-submit-start-code"></span>

```php
document.addEventListener('bricks/filter/submit/start', (event) => {
  const { queryId, filterId } = event.detail;

  // Only react to the Filter - Submit element with Bricks ID xnueeh
  if (filterId !== 'xnueeh') {
    return;
  }

  // Your custom logic here
});
```

<span id="bricks-filter-submit-end-code"></span>

```php
document.addEventListener('bricks/filter/submit/end', (event) => {
  const { queryId, filterId } = event.detail;

  // Only react to the target query with Bricks ID kpmnav
  if (queryId !== 'kpmnav') {
    return;
  }

  // Your custom logic here
});
```

## Mega menu events

- [bricks/megamenu/repositioned](#bricks-megamenu-repositioned-code): Emitted after a mega menu submenu is repositioned on the frontend. The event detail contains the `menuItem` and `submenu`. (`@since 2.0`)

<span id="bricks-megamenu-repositioned-code"></span>

```php
document.addEventListener('bricks/megamenu/repositioned', (event) => {
  const { menuItem, submenu } = event.detail;

  // Your custom logic here
  // For example, update third-party scripts inside the repositioned submenu
});
```

---

<a id="developer-hooks"></a>

# Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/

*Browse documented Bricks hooks, including action hooks and filter hooks for builder behavior, rendering, queries, authentication, and integrations.*

These are all documented Bricks hooks:

---

<a id="developer-hooks-actions-action-bricks-generate-css-file"></a>

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

<a id="developer-hooks-actions-action-bricks-query-after-loop"></a>

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

<a id="developer-hooks-actions-action-bricks-query-before-loop"></a>

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

<a id="developer-hooks-actions-bricks-after-footer"></a>

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

<a id="developer-hooks-actions-bricks-after-header"></a>

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

<a id="developer-hooks-actions-bricks-after-site-wrapper"></a>

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

<a id="developer-hooks-actions-bricks-archive-product-after"></a>

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

<a id="developer-hooks-actions-bricks-before-footer"></a>

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

<a id="developer-hooks-actions-bricks-archive-product-before"></a>

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

<a id="developer-hooks-actions-bricks-before-header"></a>

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

<a id="developer-hooks-actions-bricks-before-site-wrapper"></a>

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

<a id="developer-hooks-actions-bricks-body"></a>

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

<a id="developer-hooks-actions-bricks-builder-switch-locale"></a>

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

<a id="developer-hooks-actions-bricks-database-get-all-templates-by-type-after-query"></a>

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

<a id="developer-hooks-actions-bricks-dynamic-data-after-do-action"></a>

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

<a id="developer-hooks-actions-bricks-dynamic-data-before-do-action"></a>

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

<a id="developer-hooks-actions-bricks-dynamic-data-tag-value-parsed"></a>

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

<a id="developer-hooks-actions-bricks-dynamic-data-tags-registered"></a>

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

<a id="developer-hooks-actions-bricks-execute-filter-index-job"></a>

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

<a id="developer-hooks-actions-bricks-filter-element-before-set-data-source-from-custom-field"></a>

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

<a id="developer-hooks-actions-bricks-form-custom-action"></a>

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

<a id="developer-hooks-actions-bricks-frontend-after-render-data"></a>

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

<a id="developer-hooks-actions-bricks-frontend-before-render-data"></a>

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

<a id="developer-hooks-actions-bricks-get-templates-query-after"></a>

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

<a id="developer-hooks-actions-bricks-indexer"></a>

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

<a id="developer-hooks-actions-bricks-load-elements-after"></a>

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

<a id="developer-hooks-actions-bricks-load-elements-before"></a>

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

<a id="developer-hooks-actions-bricks-meta-tags"></a>

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

<a id="developer-hooks-actions-bricks-query-query-api-response"></a>

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

<a id="developer-hooks-actions-bricks-query-filters-index-post-before"></a>

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

<a id="developer-hooks-actions-bricks-query-filters-index-user-before"></a>

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

<a id="developer-hooks-actions-bricks-render-popup-content-start"></a>

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

<a id="developer-hooks-actions-bricks-render-query-page-start"></a>

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

<a id="developer-hooks-actions-bricks-render-query-result-start"></a>

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

<a id="developer-hooks-actions-bricks-sendgrid-double-opt-in-handler"></a>

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

<a id="developer-hooks-actions"></a>

# Action Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/actions/

*Documented Bricks action hooks for running custom code at specific points in the builder and frontend lifecycle.*

These are all documented Bricks action hooks:

---

<a id="developer-hooks-actions-render-footer"></a>

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

<a id="developer-hooks-actions-render-header"></a>

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

<a id="developer-hooks-filters-bricks-acf-filter-field-groups"></a>

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

<a id="developer-hooks-filters-bricks-acf-google-map-address-parts"></a>

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

<a id="developer-hooks-filters-bricks-acf-google-map-show-as-address"></a>

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

<a id="developer-hooks-filters-bricks-acf-google-map-text-output"></a>

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

<a id="developer-hooks-filters-bricks-acf-taxonomy-show-as-link"></a>

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

<a id="developer-hooks-filters-bricks-active-templates"></a>

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

<a id="developer-hooks-filters-bricks-ajax-get-pages-args"></a>

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

<a id="developer-hooks-filters-bricks-allowed-html-tags"></a>

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

<a id="developer-hooks-filters-bricks-api-get-templates-data"></a>

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

<a id="developer-hooks-filters-bricks-breadcrumbs-home-label"></a>

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

<a id="developer-hooks-filters-bricks-breadcrumbs-items"></a>

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

<a id="developer-hooks-filters-bricks-breadcrumbs-separator"></a>

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

<a id="developer-hooks-filters-bricks-builder-current-page-type"></a>

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

<a id="developer-hooks-filters-bricks-builder-data-post-id"></a>

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

<a id="developer-hooks-filters-bricks-builder-dynamic-wrapper"></a>

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

<a id="developer-hooks-filters-bricks-builder-first-element-category"></a>

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

<a id="developer-hooks-filters-bricks-builder-post-title"></a>

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

<a id="developer-hooks-filters-bricks-builder-state-group-definitions"></a>

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

<a id="developer-hooks-filters-bricks-builder-supported-post-types"></a>

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

<a id="developer-hooks-filters-bricks-builder-term-name"></a>

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

<a id="developer-hooks-filters-bricks-cmb2-checkbox-value"></a>

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

<a id="developer-hooks-filters-bricks-code-echo-everywhere"></a>

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

<a id="developer-hooks-filters-bricks-combined-search-post-ids"></a>

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

<a id="developer-hooks-filters-bricks-combined-search-term-ids"></a>

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

<a id="developer-hooks-filters-bricks-combined-search-user-ids"></a>

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

<a id="developer-hooks-filters-bricks-comments-author-tag"></a>

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

<a id="developer-hooks-filters-bricks-conditions-groups"></a>

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

<a id="developer-hooks-filters-bricks-conditions-options"></a>

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

<a id="developer-hooks-filters-bricks-conditions-result"></a>

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

<a id="developer-hooks-filters-bricks-content-analysis-full-post-content-id"></a>

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

<a id="developer-hooks-filters-bricks-custom-fonts-mime-types"></a>

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

<a id="developer-hooks-filters-bricks-database-bricks-get-all-templates-by-type-args"></a>

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

<a id="developer-hooks-filters-bricks-database-content-type"></a>

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

<a id="developer-hooks-filters-bricks-database-get-all-templates-cache-key"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-allowed-keys"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-author-value"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-do-action-context"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-format-value"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-meta-value-meta-key"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-register-hook"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-register-providers"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-render-content"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-render-tag"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-text-separator"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-data-user-value"></a>

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

<a id="developer-hooks-filters-bricks-dynamic-tags-list"></a>

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

<a id="developer-hooks-filters-bricks-element-builder-setup-query"></a>

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

<a id="developer-hooks-filters-bricks-element-form-datepicker-options"></a>

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

<a id="developer-hooks-filters-bricks-element-form-honeypot-result"></a>

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

<a id="developer-hooks-filters-bricks-element-maybe-set-aria-current-page"></a>

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

<a id="developer-hooks-filters-bricks-elements-element-name-scripts"></a>

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

<a id="developer-hooks-filters-bricks-elements-nav-menu-menus"></a>

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

<a id="developer-hooks-filters-bricks-export-template-args"></a>

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

<a id="developer-hooks-filters-bricks-elements-nav-menu-name"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-datepicker-options"></a>

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

<a id="developer-hooks-filters-bricks-filter-taxonomy-args"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-controls"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-count-source-wcfield"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-count-source-filter-source"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-data-source-filter-source"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-data-source-wcfield"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-datepicker-date-format"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-datepicker-db-date-format"></a>

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

<a id="developer-hooks-filters-bricks-filter-element-filtered-source"></a>

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

<a id="developer-hooks-filters-bricks-fix-filter-element-db"></a>

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

<a id="developer-hooks-filters-bricks-form-file-directory"></a>

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

<a id="developer-hooks-filters-bricks-form-recaptcha-score-threshold"></a>

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

<a id="developer-hooks-filters-bricks-form-response"></a>

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

<a id="developer-hooks-filters-bricks-form-save-submission-form-data"></a>

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

<a id="developer-hooks-filters-bricks-form-submission-table-file-url"></a>

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

<a id="developer-hooks-filters-bricks-form-tinymce-settings"></a>

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

<a id="developer-hooks-filters-bricks-form-validate"></a>

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

<a id="developer-hooks-filters-bricks-frontend-disable-opengraph"></a>

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

<a id="developer-hooks-filters-bricks-frontend-disable-seo"></a>

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

<a id="developer-hooks-filters-bricks-get-builder-edit-link"></a>

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

<a id="developer-hooks-filters-bricks-frontend-render-loop"></a>

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

<a id="developer-hooks-filters-bricks-get-remote-templates-data"></a>

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

<a id="developer-hooks-filters-bricks-get-template-authors"></a>

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

<a id="developer-hooks-filters-bricks-get-template-bundles"></a>

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

<a id="developer-hooks-filters-bricks-get-template-tags"></a>

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

<a id="developer-hooks-filters-bricks-get-templates-query-vars"></a>

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

<a id="developer-hooks-filters-bricks-get-templates"></a>

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

<a id="developer-hooks-filters-bricks-get-templates-query-cache-key"></a>

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

<a id="developer-hooks-filters-bricks-get-terms-options-enable-limit"></a>

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

<a id="developer-hooks-filters-bricks-get-terms-options-excluded-taxonomies"></a>

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

<a id="developer-hooks-filters-bricks-get-the-title"></a>

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

<a id="developer-hooks-filters-bricks-handle-no-results-children-elements"></a>

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

<a id="developer-hooks-filters-bricks-helpers-get-posts-args"></a>

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

<a id="developer-hooks-filters-bricks-media-browser-health-file-status"></a>

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

<a id="developer-hooks-filters-bricks-metabox-checkbox-value"></a>

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

<a id="developer-hooks-filters-bricks-metabox-show-as-map"></a>

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

<a id="developer-hooks-filters-bricks-metabox-taxonomy-show-as-link"></a>

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

<a id="developer-hooks-filters-bricks-object-types-query-vars"></a>

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

<a id="developer-hooks-filters-bricks-paginate-links-args"></a>

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

<a id="developer-hooks-filters-bricks-pagination-current-page"></a>

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

<a id="developer-hooks-filters-bricks-pagination-custom-logic"></a>

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

<a id="developer-hooks-filters-bricks-pagination-total-pages"></a>

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

<a id="developer-hooks-filters-bricks-polylang-builder-ajax-params"></a>

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

<a id="developer-hooks-filters-bricks-polylang-exclude-controls-from-translation"></a>

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

<a id="developer-hooks-filters-bricks-popup-attributes"></a>

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

<a id="developer-hooks-filters-bricks-query-archive-query-arguments"></a>

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

<a id="developer-hooks-filters-bricks-query-archive-query-supported-object-types"></a>

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

<a id="developer-hooks-filters-bricks-query-cache-key"></a>

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

<a id="developer-hooks-filters-bricks-query-fake-result"></a>

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

<a id="developer-hooks-filters-bricks-query-force-is-looping"></a>

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

<a id="developer-hooks-filters-bricks-query-force-loop-index"></a>

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

<a id="developer-hooks-filters-bricks-query-result-end"></a>

# Filter: bricks/query/result_end

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/

*Filters the ending index used when slicing the query results. This allows you to control which portion of the results is displayed, useful for custom pagination.*

Filters the ending index used when slicing the query results. This allows you to control which portion of the results is displayed, useful for custom pagination or limit logic.

## Parameters

- `$end` (*int*): The ending index for the result slice.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/result_end', function( $end, $query ) {
    // Example: Limit results to 5 for a specific query ID
    if ( $query->id === 'my_limited_query' ) {
        return 5;
    }

    return $end;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-query-prepare-query-vars-from-settings"></a>

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

<a id="developer-hooks-filters-bricks-query-result-start"></a>

# Filter: bricks/query/result_start

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/

*Filters the starting index used when slicing the query results. This allows you to control where the displayed results begin, useful for custom offsets or.*

Filters the starting index used when slicing the query results. This allows you to control where the displayed results begin, useful for custom offsets or pagination.

## Parameters

- `$start` (*int*): The starting index for the result slice.
- `$query` (*object*): The Bricks Query instance.

## Example usage

```php
add_filter( 'bricks/query/result_start', function( $start, $query ) {
    // Example: Offset results by 1 for a specific query ID
    if ( $query->id === 'my_offset_query' ) {
        return $start + 1;
    }

    return $start;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-query-run-fake"></a>

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

<a id="developer-hooks-filters-bricks-query-supress-render-content"></a>

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

<a id="developer-hooks-filters-bricks-query-api-body"></a>

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

<a id="developer-hooks-filters-bricks-query-api-headers"></a>

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

<a id="developer-hooks-filters-bricks-query-api-request-args"></a>

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

<a id="developer-hooks-filters-bricks-query-api-total-pages"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-custom-field-index-rows"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-custom-field-meta-query"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-datepicker-custom-field-meta-query"></a>

# Filter: bricks/query_filters/datepicker_custom_field_meta_query

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-datepicker_custom_field_meta_query/

*Filters the metaquery generated for a datepicker filter targeting a custom field. This allows you to customize how date comparisons are handled (e.g., date.*

Filters the `meta_query` generated for a datepicker filter targeting a custom field. This allows you to customize how date comparisons are handled (e.g., date formats, range logic) for specific fields.

## Parameters

- `$meta_query` (*array*): The generated `meta_query` array (e.g., `['key' => '...', 'value' => '...', 'type' => 'DATE']`).
- `$filter` (*array*): The active filter data, including settings and parsed dates.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/query_filters/datepicker_custom_field_meta_query', function( $meta_query, $filter, $provider, $query_id ) {
    // Example: Change type to 'NUMERIC' for timestamp fields stored as numbers
    if ( $filter['settings']['fieldName'] === 'my_timestamp_field' ) {
        if ( isset( $meta_query['type'] ) ) {
            $meta_query['type'] = 'NUMERIC';
        } elseif ( isset( $meta_query[0] ) ) {
            // Handle range query (array of arrays)
            foreach ( $meta_query as $key => $clause ) {
                if ( is_int( $key ) ) {
                    $meta_query[ $key ]['type'] = 'NUMERIC';
                }
            }
        }
    }

    return $meta_query;
}, 10, 4 );
```

---

<a id="developer-hooks-filters-bricks-query-filters-element-data"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-filter-query-vars"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-get-filter-object-ids"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-index-args"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-index-post-meta-exists"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-index-post-source"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-index-post-wcfield"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-index-user-meta-exists"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-range-custom-field-meta-query"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-sort-query-vars"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-cf-integration-register-providers"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-indexer-post-filter-source"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-indexer-post-wcfield"></a>

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

<a id="developer-hooks-filters-bricks-query-filters-indexer-validate-job-settings"></a>

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

<a id="developer-hooks-filters-bricks-remote-get"></a>

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

<a id="developer-hooks-filters-bricks-remote-post"></a>

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

<a id="developer-hooks-filters-bricks-render-footer"></a>

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

<a id="developer-hooks-filters-bricks-render-header"></a>

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

<a id="developer-hooks-filters-bricks-render-with-bricks"></a>

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

<a id="developer-hooks-filters-bricks-resolve-attachment-id"></a>

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

<a id="developer-hooks-filters-bricks-rtl-languages"></a>

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

<a id="developer-hooks-filters-bricks-security-check-before-save-new-elements"></a>

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

<a id="developer-hooks-filters-bricks-support-masonry-element"></a>

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

---

<a id="developer-hooks-filters-bricks-svg-allowed-attributes"></a>

# Filter: bricks/svg/allowed_attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-allowed_attributes/

*Filters the list of allowed SVG attributes during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain.*

Filters the list of allowed SVG attributes during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain malicious attributes.

## Parameters

- `$attributes` (*array*): Array of allowed SVG attributes.

## Example usage

```php
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    // Example: Allow 'data-custom' attribute
    $attributes[] = 'data-custom';

    return $attributes;
} );
```

---

<a id="developer-hooks-filters-bricks-svg-allowed-tags"></a>

# Filter: bricks/svg/allowed_tags

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-allowed_tags/

*Filters the list of allowed SVG tags during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain.*

Filters the list of allowed SVG tags during sanitization. This is used by the Bricks SVG sanitizer to ensure that uploaded or rendered SVGs do not contain malicious tags.

## Parameters

- `$tags` (*array*): Array of allowed SVG tags.

## Example usage

```php
add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    // Example: Allow 'foreignObject' tag (use with caution!)
    $tags[] = 'foreignObject';

    return $tags;
} );
```

---

<a id="developer-hooks-filters-bricks-svg-bypass-sanitization"></a>

# Filter: bricks/svg/bypass_sanitization

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-svg-bypass_sanitization/

*Determines whether to bypass the SVG sanitization process when uploading SVG files. This can be useful if you need to upload SVGs with complex features (like.*

Determines whether to bypass the SVG sanitization process when uploading SVG files. This can be useful if you need to upload SVGs with complex features (like animations or scripts) that the sanitizer would normally strip out, but it comes with security risks.

## Parameters

- `$bypass` (*bool*): Whether to bypass sanitization. Default is `false`.
- `$file` (*array*): Array containing file information (e.g., `tmp_name`, `type`).

## Example usage

```php
add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
    // Example: Bypass sanitization for trusted users only
    if ( current_user_can( 'administrator' ) ) {
        return true;
    }

    return $bypass;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-template-preview-supported-content-types"></a>

# Filter: bricks/template_preview/supported_content_types

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-template_preview-supported_content_types/

*Filters the list of content types available for selection in the \"Populate Content\" (Template Preview) setting. This allows you to add custom preview contexts.*

Filters the list of content types available for selection in the "Populate Content" (Template Preview) setting. This allows you to add custom preview contexts.

## Parameters

- `$types` (*array*): Associative array where keys are the content type IDs and values are their labels.

## Example usage

```php
add_filter( 'bricks/template_preview/supported_content_types', function( $types ) {
    // Example: Add a custom preview type
    $types['my_custom_preview'] = esc_html__( 'My Custom Preview', 'my-plugin' );

    return $types;
} );
```

---

<a id="developer-hooks-filters-bricks-theme-style-name"></a>

# Filter: bricks/theme_style_name

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_style_name/

*Filters the name of the Theme Style used when generating the CSS file name. This allows you to sanitize or modify the name before it is used in the file system.*

Filters the name of the Theme Style used when generating the CSS file name. This allows you to sanitize or modify the name before it is used in the file system.

## Parameters

- `$name` (*string*): The theme style name.
- `$theme_style` (*array*): The theme style data array.

## Example usage

```php
add_filter( 'bricks/theme_style_name', function( $name, $theme_style ) {
    // Example: Prefix theme style file names
    return 'custom-prefix-' . $name;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-theme-styles-control-groups"></a>

# Filter: bricks/theme_styles/control_groups

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles-control_groups/

*Filters the control groups available in the Theme Styles settings panel. This allows you to add new sections or tabs to organize custom Theme Style controls.*

Filters the control groups available in the Theme Styles settings panel. This allows you to add new sections or tabs to organize custom Theme Style controls.

## Parameters

- `$control_groups` (*array*): Associative array of control groups.

## Example usage

```php
add_filter( 'bricks/theme_styles/control_groups', function( $control_groups ) {
    // Add a new control group for 'My Plugin'
    $control_groups['my_plugin'] = [
        'title' => esc_html__( 'My Plugin Settings', 'my-plugin' ),
        'tab'   => 'content', // or 'style'
    ];

    return $control_groups;
} );
```

---

<a id="developer-hooks-filters-bricks-theme-styles-controls"></a>

# Filter: bricks/theme_styles/controls

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles-controls/

*Filters the individual controls available within the Theme Styles settings. This allows you to add custom fields to existing Theme Style groups or to your own.*

Filters the individual controls available within the Theme Styles settings. This allows you to add custom fields to existing Theme Style groups or to your own custom groups.

## Parameters

- `$controls` (*array*): Associative array of controls.

## Example usage

```php
add_filter( 'bricks/theme_styles/controls', function( $controls ) {
    // Add a custom color control to the 'colors' group
    $controls['myCustomColor'] = [
        'group' => 'colors', // Target existing group
        'label' => esc_html__( 'My Custom Color', 'my-plugin' ),
        'type'  => 'color',
    ];

    return $controls;
} );
```

---

<a id="developer-hooks-filters-bricks-theme-styles"></a>

# Filter: bricks/theme_styles

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-theme_styles/

*Filters the array of Theme Styles loaded from the database. This allows you to modify, add, or remove Theme Styles programmatically.*

Filters the array of Theme Styles loaded from the database. This allows you to modify, add, or remove Theme Styles programmatically.

## Parameters

- `$styles` (*array*): Associative array of Theme Styles, where the key is the style name and the value is an array of style data.

## Example usage

```php
add_filter( 'bricks/theme_styles', function( $styles ) {
    // Example: Add a default property to all theme styles
    foreach ( $styles as $key => $style ) {
        if ( ! isset( $styles[ $key ]['settings']['typography'] ) ) {
            $styles[ $key ]['settings']['typography'] = [ 'font-size' => '16px' ];
        }
    }

    return $styles;
} );
```

---

<a id="developer-hooks-filters-bricks-user-activation-email-content"></a>

# Filter: bricks/user_activation_email/content

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-content/

*Filters the content for Bricks user activation emails.*

Filters the content for Bricks user activation emails.

## Parameters

- `$content` (string): The email content.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/content', function( $content, $user_id ) {
    return $content;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-user-activation-email-from-name"></a>

# Filter: bricks/user_activation_email/from_name

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-from_name/

*Filters the sender name for Bricks user activation emails.*

Filters the sender name for Bricks user activation emails.

## Parameters

- `$from_name` (string): The email sender name.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/from_name', function( $from_name, $user_id ) {
    return get_bloginfo( 'name' );
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-user-activation-email-subject"></a>

# Filter: bricks/user_activation_email/subject

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-subject/

*Filters the subject for Bricks user activation emails.*

Filters the subject for Bricks user activation emails.

## Parameters

- `$subject` (string): The email subject.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/subject', function( $subject, $user_id ) {
    return '[Site access] Activate your account';
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-webhook-timeout"></a>

# Filter: bricks/webhook/timeout

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-webhook-timeout/

*Allows you to modify the timeout duration (in seconds) for webhook requests triggered by the Form element.*

Allows you to modify the timeout duration (in seconds) for webhook requests triggered by the Form element.

## Parameters

- `$timeout` (int): The timeout duration in seconds. Default is `15`.

## Example usage

```php
add_filter( 'bricks/webhook/timeout', function( $timeout ) {
    // Increase timeout to 30 seconds
    return 30;
} );
```

---

<a id="developer-hooks-filters-bricks-woo-setup-wizard-register-presets"></a>

# Filter: bricks/woo_setup_wizard/register_presets

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woo_setup_wizard-register_presets/

*Filters Woo setup wizard presets.*

Filters Woo setup wizard presets before Bricks registers them. Use it to add or override one-click setup JSON presets.

## Parameters

- `$presets` (array): Preset data grouped by area and preset ID.

## Example usage

```php
add_filter( 'bricks/woo_setup_wizard/register_presets', function( $presets ) {
    $presets['checkout']['my-preset'] = [
        'label' => 'My checkout preset',
    ];

    return $presets;
} );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-ajax-render-post-id"></a>

# Filter: bricks/woocommerce/ajax_render_post_id

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-ajax_render_post_id/

*Filters the post ID used for WooCommerce AJAX rendering.*

Filters the post ID Bricks uses as context for WooCommerce AJAX rendering.

## Parameters

- `$post_id` (int): The post ID Bricks resolved for the WooCommerce page.
- `$wc_page` (string): The WooCommerce page context being rendered.

## Example usage

```php
add_filter( 'bricks/woocommerce/ajax_render_post_id', function( $post_id, $wc_page ) {
    return $post_id;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-cart-proceed-label"></a>

# Filter: bricks/woocommerce/cart_proceed_label

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-cart_proceed_label/

*Allows you to modify the text of the \"Proceed to checkout\" button in the WooCommerce Cart element.*

Allows you to modify the text of the "Proceed to checkout" button in the WooCommerce Cart element.

## Parameters

- `$label` (string): The button text. Default is "Proceed to checkout".

## Example usage

```php
add_filter( 'bricks/woocommerce/cart_proceed_label', function( $label ) {
    return 'Go to Checkout';
} );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-dynamic-fragments-fragments"></a>

# Filter: bricks/woocommerce/dynamic_fragments/fragments

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-fragments/

*Filters WooCommerce dynamic fragments before the AJAX response is sent.*

Filters WooCommerce dynamic fragments before Bricks returns the AJAX response.

## Parameters

- `$fragments` (array): Selector-keyed fragment HTML.
- `$targets` (array): Mounted fragment targets from the current page.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/fragments', function( $fragments, $targets ) {
    return $fragments;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-dynamic-fragments-html"></a>

# Filter: bricks/woocommerce/dynamic_fragments/html

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-html/

*Filters rendered HTML for a WooCommerce dynamic fragment.*

Filters rendered HTML for a single WooCommerce dynamic fragment.

## Parameters

- `$html` (string): Rendered fragment HTML.
- `$target` (array): The fragment target being rendered.
- `$render_data` (array): Bricks render data used for the fragment.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/html', function( $html, $target, $render_data ) {
    return $html;
}, 10, 3 );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-dynamic-fragments-targets"></a>

# Filter: bricks/woocommerce/dynamic_fragments/targets

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-dynamic_fragments-targets/

*Filters WooCommerce dynamic fragment targets before rendering.*

Filters WooCommerce dynamic fragment targets before Bricks renders the fragments.

## Parameters

- `$targets` (array): Mounted fragment targets from the current page.

## Example usage

```php
add_filter( 'bricks/woocommerce/dynamic_fragments/targets', function( $targets ) {
    return $targets;
} );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-predefined-elements-generated-payload"></a>

# Filter: bricks/woocommerce/predefined_elements/generated_payload

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-generated_payload/

*Filters a generated WooCommerce predefined element payload.*

Filters a generated WooCommerce predefined element payload before Bricks returns it.

## Parameters

- `$response` (array): The generated payload response.
- `$preset` (string): The preset ID being generated.
- `$context` (array): Generation context for the preset.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/generated_payload', function( $response, $preset, $context ) {
    return $response;
}, 10, 3 );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-predefined-elements-local-presets"></a>

# Filter: bricks/woocommerce/predefined_elements/local_presets

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-local_presets/

*Filters local WooCommerce predefined element presets.*

Filters local WooCommerce predefined element presets after Bricks loads JSON presets.

## Parameters

- `$presets` (array): Local preset payloads.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/local_presets', function( $presets ) {
    return $presets;
} );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-predefined-elements-remote-payload"></a>

# Filter: bricks/woocommerce/predefined_elements/remote_payload

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-remote_payload/

*Filters the remote WooCommerce predefined elements payload.*

Filters the remote WooCommerce predefined elements payload after Bricks decodes the response and before it validates/caches the payload.

## Parameters

- `$remote_payload` (array|mixed): Decoded remote payload data.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/remote_payload', function( $remote_payload ) {
    return $remote_payload;
} );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-predefined-elements-remote-url"></a>

# Filter: bricks/woocommerce/predefined_elements/remote_url

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-predefined_elements-remote_url/

*Filters the remote URL for WooCommerce predefined element presets.*

Filters the remote URL Bricks uses to fetch WooCommerce predefined element presets. Return an empty string to keep remote fetching disabled.

When a URL is returned, Bricks appends `schemaVersion`, `site`, and `time` query arguments before making the request.

## Parameters

- `$remote_url` (string): The remote preset endpoint URL.

## Example usage

```php
add_filter( 'bricks/woocommerce/predefined_elements/remote_url', function( $remote_url ) {
    return 'https://example.com/bricks-woo-presets.json';
} );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-products-filters-options"></a>

# Filter: bricks/woocommerce/products_filters/options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_filters-options/

*Allows you to modify the options available in the WooCommerce Products Filter element.*

Allows you to modify the options available in the WooCommerce Products Filter element.

## Parameters

- `$options` (array): An array of options, where each option is an associative array with `id` and `name`.
- `$settings` (array): The element settings.

## Example usage

```php
add_filter( 'bricks/woocommerce/products_filters/options', function( $options, $settings ) {
    // Add a custom "All" option to the beginning
    array_unshift( $options, [
        'id'   => 'all',
        'name' => 'All Products',
    ] );

    return $options;
}, 10, 2 );
```

---

<a id="developer-hooks-filters-bricks-woocommerce-products-orderby-options"></a>

# Filter: bricks/woocommerce/products_orderby_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-products_orderby_options/

*Filters WooCommerce product order-by options used by Bricks.*

Filters WooCommerce product order-by options used by Bricks controls.

## Parameters

- `$options` (array): Order-by option keys and labels.

## Example usage

```php
add_filter( 'bricks/woocommerce/products_orderby_options', function( $options ) {
    $options['title'] = esc_html__( 'Sort by title', 'my-plugin' );

    return $options;
} );
```

---

<a id="developer-hooks-filters-bricks-wpml-exclude-controls-from-translation"></a>

# Filter: bricks/wpml/exclude_controls_from_translation

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-wpml-exclude_controls_from_translation/

*Filters Bricks control keys excluded from WPML translation.*

Filters Bricks control keys excluded from WPML translation. Return the control keys that should not be translated for the current element/control context.

## Parameters

- `$excluded_keys` (array): Control keys excluded from translation.
- `$element` (array): The Bricks element data.
- `$control` (array): The control definition.
- `$key` (string): The current control key or repeater field key.

## Example usage

```php
add_filter( 'bricks/wpml/exclude_controls_from_translation', function( $excluded_keys, $element, $control, $key ) {
    $excluded_keys[] = 'my_untranslated_control';

    return $excluded_keys;
}, 10, 4 );
```

---

<a id="developer-hooks-filters-bricks-wpml-translatable-control-types"></a>

# Filter: bricks/wpml/translatable_control_types

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-wpml-translatable_control_types/

*Add Bricks control types, including selected code fields, to WPML translation jobs.*

The `bricks/wpml/translatable_control_types` filter controls which Bricks control types WPML includes in its translation jobs.

Bricks includes `text`, `textarea`, `editor`, `repeater`, and `link` controls by default. The `code` type is excluded because automatic or manual translation can change executable PHP, JavaScript, HTML, or CSS. Add it only for fields whose complete value needs to differ between languages.

The filter applies to element controls and Page Settings. Page Settings use a synthetic element with the name `page-settings`, which lets a callback target page-level custom code without exposing every code control on the site.

## Parameters

- `$types` (array): Control types currently exposed to WPML.
- `$element` (array): The current Bricks element. For Page Settings, its `name` is `page-settings` and its `id` is `pageSettings`.
- `$control` (array|null): The current control definition.
- `$key` (string): The current control key or repeater field key.

## Translate the PHP and HTML field of Code elements

This example exposes only the `code` field of the Code element. Its CSS and JavaScript fields remain excluded.

```php
add_filter( 'bricks/wpml/translatable_control_types', function( $types, $element, $control, $key ) {
    if ( ( $element['name'] ?? '' ) === 'code' && $key === 'code' ) {
        $types[] = 'code';
    }

    return array_unique( $types );
}, 10, 4 );
```

## Translate a Page Settings custom-code field

The following callback exposes only **Page Settings → Custom code → Header scripts**. Other page-level CSS and script fields continue to use the source-language value.

```php
add_filter( 'bricks/wpml/translatable_control_types', function( $types, $element, $control, $key ) {
    $is_page_settings = ( $element['name'] ?? '' ) === 'page-settings';

    if ( $is_page_settings && $key === 'customScriptsHeader' ) {
        $types[] = 'code';
    }

    return array_unique( $types );
}, 10, 4 );
```

Available page-level custom-code keys are:

- `customCss`
- `customScriptsHeader`
- `customScriptsBodyHeader`
- `customScriptsBodyFooter`

After adding the filter, update the source page and send its translation to WPML again. The opted-in code field then appears in the WPML translation job. Review the translated value before publishing, especially when automatic translation is enabled, because a changed quote, variable, selector, or function name can break the code.

---

<a id="developer-hooks-filters-bricks-query-max-items-in-builder"></a>

# Filter: bricks_query_max_items_in_builder

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks_query_max_items_in_builder/

*Filters builder query results for custom object types when Bricks applies the builder max-results limit.*

Filters dynamic query results in the builder when Bricks applies the builder query max-results limit.

Bricks handles built-in `post`, `term`, `user`, and supported provider object types internally. This filter runs for custom query object types that Bricks does not know how to trim itself.

## Parameters

- `$result` (mixed): The current query result.
- `$query_instance` (Bricks\Query): The Bricks query instance.
- `$builder_query_max_results` (int): The maximum number of results Bricks allows in the builder.

## Example usage

```php
add_filter( 'bricks_query_max_items_in_builder', function( $result, $query_instance, $builder_query_max_results ) {
    if ( is_array( $result ) ) {
        return array_slice( $result, 0, $builder_query_max_results );
    }

    return $result;
}, 10, 3 );
```

---

<a id="developer-hooks-filters-filter-bricks-active-templates"></a>

# Filter: bricks/active_templates

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-active_templates/

*Filter the active Bricks templates applied to the current request so you can add, remove, or swap templates programmatically.*

Modify the templates applied on a page programmatically (`@since 1.8.4`)

This is an alternative to setting an active template via the [bricks/screen_conditions/scores](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-screen_conditions-scores/) filter.

> **Note**
>
> Please note that this filter is executed after `bricks/screen_conditions/scores`

## Example: Do not use the Single template if the post has been edited with Bricks {#exclude-default-template-if-post-edit-by-bricks}

In this example, we want to exclude the single post from utilizing a template if it contains Bricks data (Edit with Bricks).

```php
add_filter( 'bricks/active_templates', 'set_my_active_templates', 10, 3 );
function set_my_active_templates( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'post'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'post' ) {
    return $active_templates;
  }

  /**
   * $active_templates is an array with different important keys
   *
   * $active_templates['header'] is the header template ID, set it to 0 if do not want to use any template
   * $active_templates['content'] is the content template ID, set it to current post ID if do not want to use any template
   * $active_templates['footer'] is the footer template ID, set it to 0 if do not want to use any template
   *
   * $active_templates['search'] is the search template ID, will only be used if $content_type is 'search'
   * $active_templates['archive'] is the archive template ID, will only be used if $content_type is 'archive'
   * $active_templates['error] is the error template ID, will only be used if $content_type is 'error'
  */

  // Check if the current post has Bricks data, return value is an array
  $bricks_data = \Bricks\Database::get_data( $post_id, 'content' );

  if ( count( $bricks_data ) > 0 ) {
    // Has Bricks data: Don't use any template, set the $active_templates['content'] to current post ID
    $active_templates['content'] = $post_id;

    // To disable header & footer (e.g. landing page) set $active_templates['header'] & $active_templates['footer'] to 0
    $active_templates['header'] = 0;
    $active_templates['footer'] = 0;
  }

  return $active_templates;
}
```

## Example: Change a single template based on a custom field {#single-template-via-custom-field}

There is a scenario like having multiple single templates for a custom post type. Using this filter, you can decide which template to apply based on a custom field.

```php
add_filter( 'bricks/active_templates', 'set_active_templates_by_custom_field', 10, 3 );

function set_active_templates_by_custom_field( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'project'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'project' ) {
    return $active_templates;
  }

  // Get the custom field value from Metabox
  $value = absint( rwmb_meta( 'use_template_id' ) );

  // Value not empty: Set $active_templates['content'] to the value
  if ( $value > 0 ) {
    $active_templates['content'] = $value;
    // If single template, the page settings will be used, so no need to set header and footer
  }

  return $active_templates;
}
```

## Example: Disable active template in the builder {#disable-active-template-in-builder}

Since Bricks 1.12, templates applied to a page are now also displayed in the Builder. Previously, only the *Post Content* element was visible, making it difficult to style surrounding elements. If you prefer the old behavior and want to disable the applied template *only inside the builder*, you can use this filter:

```php
add_filter( 'bricks/active_templates', 'disable_template_in_builder', 10, 3 );

function disable_template_in_builder( $active_templates, $post_id, $content_type ) {
  // Only run my logic in the Builder
  if ( bricks_is_builder() ) {
    $active_templates['content'] = 0;
  }

  return $active_templates;
}
```

### Explanation:

- This function runs only when Bricks is in **Builder mode** (`bricks_is_builder()`).
- It prevents the active single template from applying inside the Builder by setting `$active_templates['content'] = 0`.
- The frontend remains unaffected; the template is still used when viewing the post/page normally.
- This effectively disables the new **outer Post Content elements visibility** introduced in **Bricks 1.12**, restoring the previous Builder behavior.

---

<a id="developer-hooks-filters-filter-bricks-allowed-html-tags"></a>

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

<a id="developer-hooks-filters-filter-bricks-assets-generate-css-from-element"></a>

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

<a id="developer-hooks-filters-filter-bricks-assets-load-webfonts"></a>

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

<a id="developer-hooks-filters-filter-bricks-auth-custom-login-redirect"></a>

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

<a id="developer-hooks-filters-filter-bricks-auth-custom-lost-password-redirect"></a>

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

<a id="developer-hooks-filters-filter-bricks-auth-custom-redirect-url"></a>

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

<a id="developer-hooks-filters-filter-bricks-auth-custom-registration-redirect"></a>

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

<a id="developer-hooks-filters-filter-bricks-auth-custom-reset-password-redirect"></a>

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

<a id="developer-hooks-filters-filter-bricks-body-attributes"></a>

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

<a id="developer-hooks-filters-filter-bricks-builder-codemirror-config"></a>

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

<a id="developer-hooks-filters-filter-bricks-builder-elements"></a>

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

<a id="developer-hooks-filters-filter-bricks-builder-image-size-options"></a>

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

<a id="developer-hooks-filters-filter-bricks-builder-mapstyles"></a>

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

<a id="developer-hooks-filters-filter-bricks-code-allow-execution"></a>

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

<a id="developer-hooks-filters-filter-bricks-code-disable-execution"></a>

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

<a id="developer-hooks-filters-filter-bricks-code-disallow-keywords"></a>

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

<a id="developer-hooks-filters-filter-bricks-code-echo-function-names"></a>

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

<a id="developer-hooks-filters-filter-bricks-comments-timestamp"></a>

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

<a id="developer-hooks-filters-filter-bricks-content-attributes"></a>

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

<a id="developer-hooks-filters-filter-bricks-content-html-after-begin"></a>

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

<a id="developer-hooks-filters-filter-bricks-content-html-before-end"></a>

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

<a id="developer-hooks-filters-filter-bricks-content-tag"></a>

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

<a id="developer-hooks-filters-filter-bricks-default-page-title"></a>

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

<a id="developer-hooks-filters-filter-bricks-dynamic-data-exclude-tags"></a>

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

<a id="developer-hooks-filters-filter-bricks-dynamic-data-post-terms-links"></a>

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

<a id="developer-hooks-filters-filter-bricks-dynamic-data-post-terms-separator"></a>

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

<a id="developer-hooks-filters-filter-bricks-dynamic-data-read-more"></a>

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

<a id="developer-hooks-filters-filter-bricks-element-render"></a>

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

<a id="developer-hooks-filters-filter-bricks-dynamic-data-replace-nonexistent-tags"></a>

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

<a id="developer-hooks-filters-filter-bricks-element-render-attributes"></a>

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

<a id="developer-hooks-filters-filter-bricks-element-settings"></a>

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

<a id="developer-hooks-filters-filter-bricks-elements-element-name-control-groups"></a>

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

<a id="developer-hooks-filters-filter-bricks-elements-element-name-controls"></a>

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

<a id="developer-hooks-filters-filter-bricks-filter-element-populated-options"></a>

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

<a id="developer-hooks-filters-filter-bricks-footer-attributes"></a>

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

<a id="developer-hooks-filters-filter-bricks-form-action-form-action"></a>

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

<a id="developer-hooks-filters-filter-bricks-form-create-post-meta-value"></a>

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

<a id="developer-hooks-filters-filter-bricks-frontend-render-data"></a>

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

<a id="developer-hooks-filters-filter-bricks-form-update-post-meta-value"></a>

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

<a id="developer-hooks-filters-filter-bricks-frontend-render-element"></a>

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

<a id="developer-hooks-filters-filter-bricks-get-element-data-maybe-from-post-id"></a>

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

<a id="developer-hooks-filters-filter-bricks-header-attributes"></a>

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

<a id="developer-hooks-filters-filter-bricks-i18n"></a>

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

<a id="developer-hooks-filters-filter-bricks-is-layout-element"></a>

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

<a id="developer-hooks-filters-filter-bricks-link-css-selectors"></a>

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

<a id="developer-hooks-filters-filter-bricks-maintenance-should-apply"></a>

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

<a id="developer-hooks-filters-filter-bricks-nav-menu-menu"></a>

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

<a id="developer-hooks-filters-filter-bricks-password-protection-cookie-expires"></a>

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

<a id="developer-hooks-filters-filter-bricks-password-protection-is-active"></a>

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

<a id="developer-hooks-filters-filter-bricks-placeholder-image"></a>

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

<a id="developer-hooks-filters-filter-bricks-posts-merge-query"></a>

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

<a id="developer-hooks-filters-filter-bricks-posts-query-vars"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-force-run"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-init-loop-index"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-loop-object"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-loop-object-id"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-loop-object-type"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-no-results-content"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-result"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-result-count"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-result-max-num-pages"></a>

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

<a id="developer-hooks-filters-filter-bricks-query-run"></a>

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

<a id="developer-hooks-filters-filter-bricks-registered-post-types-args"></a>

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

<a id="developer-hooks-filters-filter-bricks-related-posts-query-vars"></a>

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

<a id="developer-hooks-filters-filter-bricks-render-query-loop-trail"></a>

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

<a id="developer-hooks-filters-filter-bricks-screen-conditions-scores"></a>

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

<a id="developer-hooks-filters-filter-bricks-search-form-home-url"></a>

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

<a id="developer-hooks-filters-filter-bricks-set-root-attributes"></a>

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

<a id="developer-hooks-filters-filter-bricks-setup-control-options"></a>

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

<a id="developer-hooks-filters-filter-bricks-terms-query-vars"></a>

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

<a id="developer-hooks-filters-filter-bricks-use-duplicate-content"></a>

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

<a id="developer-hooks-filters-filter-bricks-users-query-vars"></a>

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

<a id="developer-hooks-filters-filter-builder-settings-type-controls-data"></a>

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

<a id="developer-hooks-filters-filter-color-palette"></a>

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

<a id="developer-hooks-filters-filter-save-messages"></a>

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

<a id="developer-hooks-filters-filter-standard-fonts"></a>

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

---

<a id="developer-hooks-filters"></a>

# Filter Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/filters/

*Documented Bricks filter hooks for builder settings, rendering, queries, authentication, code execution, and frontend behavior.*

These are all documented Bricks filter hooks:
