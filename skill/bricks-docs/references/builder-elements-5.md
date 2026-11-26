# Form

Source: https://academy.bricksbuilder.io/builder/elements/general/form/

*Build forms, validate submissions, and run email, integration, authentication, post, and custom actions with the Form element.*

The Form element lets you build custom forms with the following form field types:

- Email
- Text
- Textarea
- Rich text
- Telephone
- Number
- URL
- Image (Media library)
- Gallery (Media library)
- Checkbox
- Select
- Radio
- Files
- Datepicker
- Password
- Remember me
- HTML
- Hidden

You can define **actions** triggered by form submissions like sending an email notification, redirecting to a certain page, communicating to SendGrid or Mailchimp servers, or user login/registration. If this is not enough, you can also develop your own actions.

The form element also integrates with [Google reCaptcha V3](#spam), [hCaptcha](https://www.hcaptcha.com/), and [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) to protect your sites from fraudulent activities, spam, and abuse. Supports dynamic data, and [form validation](#form-validation) through a new action hook.

https://youtu.be/UoNv7OECMvw

## How the Form element is structured {#structure}

A new Form element starts with three fields: **Name** (Text), **Email** (required), and **Message** (Textarea, required), plus a **Send** button. Labels are hidden by default and only the placeholders show. Enable **Show labels** under **Fields** to display them.

The settings are split into control groups:

- **Fields**: The form fields and their validation settings. Each field shows its unique six-character **ID** at the end of its settings.
- **Submit button**: Text, style, and icon of the submit button.
- **Actions**: What happens after a valid submission, the **Success message**, and optional action conditions.
- **Notices**: When and how success and error messages close.
- One group for each selected action, for example **Email**, **Confirmation email**, or **Save submission**.
- **Spam protection**: reCAPTCHA, hCaptcha, Turnstile, and honeypot information.

An action's control group only appears once the action is selected under **Actions**. A new form has **Email** selected, so the **Email** and **Confirmation email** groups are visible right away.

> **Note**
>
> Form submissions only run on the frontend. Submitting a form inside the builder does nothing, so test your form on the live page.

## Select fields {#select-fields}

The **Select** field is a dropdown for choosing one option. It has no built-in multiple-selection setting. Use a **Checkbox** field when visitors need to choose several options without custom code.

Starting with Bricks 2.5-beta, a Select field rejects submissions containing more than one value. Custom code or plugins that turn a Select field into a multi-select must explicitly allow multiple values for the intended form and field through the `bricks/form/select/allow_multiple` PHP filter. Adding a `multiple` attribute or a `name[]` suffix alone is insufficient.

Bricks checks this before custom form validation and form actions. Normal single selections continue to work.

## Auto-focus field (since 2.5) {#auto-focus-field}

Use **Auto-focus field** to focus a field when the frontend page loads, so visitors can start typing without clicking it first.

1. Select the Form element.
2. Open **Content > Fields** and add the fields you need.
3. In **Auto-focus field**, select the field to focus.
4. Save the page and reload it on the frontend to check the focus.

Leave the setting at **None** to keep the form from requesting initial focus. The dropdown includes **Email**, **Text**, **Textarea**, **Telephone**, **Number**, **URL**, **Select**, and **Password** fields. Honeypots and other field types are excluded.

<div className="screenshot screenshot--control-panel">

![Form Fields settings with Auto-focus field set to Username or email.](https://academy.bricksbuilder.io/assets/form-auto-focus-field.webp)

</div>

Bricks adds the native HTML `autofocus` attribute to the selected field on the frontend. It suppresses the attribute in Builder renders so the form does not take focus from the canvas or settings panel. If you delete the selected field or change it to an unsupported type or a honeypot, it no longer receives autofocus.

For a [login form](#login-registration), select the username or email field. When that field has focus, pressing Enter can submit the form through the browser's normal form behavior. Test this on the frontend with your browser's saved credentials; autofill and Enter behavior can vary between browsers and field types. Autofocus does not change the form's action mapping or validation.

> **Note**
>
> Use autofocus on only one field per page, including pages with multiple forms or repeated form instances. It can scroll the page to the field and open an on-screen keyboard on touch devices. For screen reader users, it can move focus past introductory content. See the [HTML autofocus reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autofocus) before enabling it on a page where the form is not the main task.

## Field descriptions {#field-descriptions}

Since Bricks 2.5, you can add a **Description** to each form field. Use it for instructions that visitors need while filling out the form, such as an accepted file format or an explanation of how you will use their email address.

### Add a description

1. Select the Form element and open **Content > Fields**.
2. Expand the field you want to describe.
3. Enter your instructions in **Description**.
4. Save the page and check the description on the frontend.

For example, add "Include your country code, such as +44." to a Telephone field. The instructions appear below the input and remain visible while the visitor types.

<div className="screenshot screenshot--control-panel">

![Telephone field settings with the label Telephone number and the description Include your country code, such as +44.](https://academy.bricksbuilder.io/assets/form-field-description.webp)

</div>

Descriptions appear after the field control. For Checkbox and Radio fields, one description appears below the whole list of options. The setting is available for all interactive field types, including Rich text, Datepicker, Files, Image, and Gallery. Hidden fields, HTML fields, and honeypots do not support descriptions.

### Style descriptions

Under **Content > Fields**, below the field list, find the **Description** styling section. These settings apply to all field descriptions in that Form element.

Descriptions take up the full width of their field. Bricks does not add description-specific font sizes, colors, or spacing by default, so configure these to suit your form.

### Dynamic data and HTML

The **Description** field supports [dynamic data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/) and HTML, such as links or emphasis. Bricks resolves dynamic data when rendering the field and sanitizes the HTML using WordPress's allowed post-content markup.

If the description is empty, or has no text after dynamic data is resolved and HTML is sanitized, Bricks outputs no description or accessibility association.

### Accessibility

Bricks automatically connects each field to its description using `aria-describedby`, making the instructions available to assistive technology. You do not need to create an ID or add the attribute manually.

For Checkbox and Radio fields, each option is connected to the shared description. Image and Gallery descriptions are connected to the media picker button. Datepicker display inputs and Rich text editors retain the association when initialized on the frontend.

Keep a clear field label as well. The label names the field; the description provides extra instructions. Descriptions do not replace [validation messages](#form-validation) or enforce requirements such as file types or a password length.

## Actions {#actions}

Form actions run after the form has been submitted successfully.

You may set one or multiple actions for your form. Actions run in the sequence they have been selected, except for the "Redirect" action, which always runs at the very end.

For each selected action, a separate control group appears.

The **Success message** setting in the **Actions** group sets the text visitors see after a successful submission. Bricks shows it below the submit button and resets the form fields.

![Bricks Form element - email action settings](https://academy.bricksbuilder.io/assets/form-mail-action.jpg)

<figcaption>

Form element: email action settings

</figcaption>

### Conditional actions (@since 2.4) {#conditional-actions}

Use **Action conditions** to run a selected action only when submitted form data matches your rules. An action without an action rule always runs after a successful submission.

To add a rule:

1. Select every action the form may run under **Actions after successful form submit**.
2. Under **Action conditions**, click **Add action rule**.
3. Choose the **Action** to control. The list only includes actions selected for the current form.
4. Under **Run action if**, choose a form **Field** and a **Compare** operator.
5. Enter a **Value** when the selected operator requires one.
6. Add more conditions if needed, then set **Relation** to **And** or **Or**.

<div className="screenshot screenshot--control-panel">

![](https://academy.bricksbuilder.io/assets/form-action-conditions.webp)

</div>

The available comparison operators are:

| Operator             | The condition matches when                    |
| -------------------- | --------------------------------------------- |
| **is**               | A submitted value exactly matches **Value**.  |
| **is not**           | No submitted value exactly matches **Value**. |
| **contains**         | A submitted value contains **Value**.         |
| **does not contain** | No submitted value contains **Value**.        |
| **is empty**         | The field has no submitted value.             |
| **is not empty**     | The field has a submitted value.              |

For fields that can submit multiple values, such as checkboxes, Bricks checks each submitted value. Use **is empty** or **is not empty** when the presence of a selection matters more than its exact value.

#### Example: Subscribe only after consent

A contact form can always send an enquiry email while subscribing only people who select a marketing consent checkbox:

1. Add a checkbox field for marketing consent. Do not make it required if visitors must be able to submit the enquiry without subscribing.
2. Select both **Email** and **Mailchimp** under **Actions after successful form submit**.
3. Add an action rule and select **Mailchimp** as the action.
4. Under **Run action if**, select the consent checkbox and set **Compare** to **is not empty**.

The **Email** action has no rule, so it runs for every successful submission. **Mailchimp** runs only when the checkbox has a submitted value.

> **Note**
>
> Within one action rule, **And** requires every condition to match, while **Or** requires at least one condition to match. If you add multiple action rules for the same action, every rule must pass.

HTML fields are not available as condition fields because they do not submit values. File-field conditions include newly uploaded files and verified files retained by an **Update post** form. An incomplete rule, such as a missing field or required comparison value, does not run the action.

### Email {#email}

The email form action sends one email on form submission. By default, it is configured to send the email to the site administrator email containing all the form fields content.

You may customize the form email action with the following settings:

- **Subject**: The email subject
- **Send to email address**: Fill in the email recipients. You may choose to send the email to the website administrator or to a custom email address (it accepts multiple email addresses, separated by a comma)
- **BCC email address**: Additional recipients who receive a blind copy.
- **From email address**: The email address that shows as the sender
- **From name**: The name that shows as the sender. It is only used when **From email address** is set.
- **Reply to email address**: In case the recipient replies to the email, this email will be used instead of the "From email address". If empty, Bricks uses the first email address from the submitted form.
- **Email content**: In case you want to personalize the email content message. Leave this field empty to send all submitted fields, followed by the URL of the page the form was sent from.
- **Error message**: The message that will be presented to the site's user if the email fails for some reason.
- **HTML email**: Enabled by default. Disable it to send a plain text email.

### Confirmation email {#confirmation-email}

Let the person who submitted a form know that you have received their email by automatically sending out a custom confirmation email whenever the form is submitted.

The **Confirmation email** group belongs to the **Email** action, so it is only available while **Email** is selected. The confirmation email is only sent when its **Email content** is filled in. By default it goes to the email address entered in the form.

We highly recommend properly setting up SMTP to ensure the best possible email delivery from your website. There are plenty of free WordPress plugins available that let you configure this within a few minutes. A search for "WordPress SMTP" should bring up countless articles & plugins for it.

If the "From name" & "From email address" you have set under the "Confirmation Email" settings inside the Form element aren't used, you have to check if any plugin and/or custom code is overwriting/forcing another name & email address.

### Form dynamic fields {#dynamic-fields}

![](https://academy.bricksbuilder.io/assets/form-fields-ids.jpg)

<figcaption>

Field ID

</figcaption>

In certain scenarios, it could be useful to get some of the submitted form fields' content to populate the email action settings.

To use the submitted data in your form settings, you have copy & paste the unique field ID (which you'll find at the end of every form field) and wrap it in two curly brackets like this: `{{form_field_id}}`

Use those dynamic fields in the "Subject", "Email address", "Email content", "From name", and "From email" settings.

Regular Bricks dynamic data works in these settings as well. For example, a subject like `Enquiry: {post_title}` in a single post template includes the title of the post the form was submitted on.

Use the `{{referrer_url}}` in the above fields to insert the URL of the page where the form was submitted.

To render all submitted fields in the "Email content" use the `{{all_fields}}` placeholder.

### User Login, Registration, Lost Password, and Reset Password {#login-registration}

These four actions allow you to build custom authentication forms without coding.

When selecting one of these actions, you have to map the form fields appropriately:

- **User login**: Map the form fields to "Login", "Password", and optionally the new "Remember me" checkbox.
- **User registration**: Map the form fields to "Email", "Password", "Username", and optionally "First/Last name". If you want to customize the default WordPress emails sent to the admin or new user upon registration, use the following hooks:
  - [`wp_new_user_notification_email`](https://developer.wordpress.org/reference/hooks/wp_new_user_notification_email/): Modify the email sent to the user.
  - [`wp_new_user_notification_email_admin`](https://developer.wordpress.org/reference/hooks/wp_new_user_notification_email_admin/): Modify the email sent to the site admin.
- **Lost password**: Map the form field to "Email" or "Username" to send reset instructions. If you want to customize the email content for password reset instructions, use the [`retrieve_password_message`](https://developer.wordpress.org/reference/hooks/retrieve_password_message/) filter.
- **Reset password**: Map the form field "password".

> **Note**
>
> When using **Lost password** or **Reset password** actions, you **do not need to configure an Email Action**. WordPress automatically handles sending the necessary emails using its default methods.

For detailed instructions on configuring custom authentication pages using the Form element, please visit the [Authentication Pages](https://academy.bricksbuilder.io/builder/features/custom-authentication-pages/) article.

#### Confirm a password

Since Bricks 2.4, a Password field can check that its value matches another Password field in the same form. Use this for registration or password reset forms:

1. Add two **Password** fields, labeled **Password** and **Confirm password**.
2. Copy the field ID shown at the end of the main Password field's settings.
3. Open the Confirm password field and enable **Mark as confirmation password**.
4. Paste the main field's ID into **Main password field ID**, without curly brackets or a `form-field-` prefix.
5. Set **Password mismatch error message** if you want to replace the default "Passwords do not match" message.
6. Map the authentication action's Password setting to the main field.

Bricks checks the values when the form is submitted. A mismatch prevents the form actions from running. Leaving **Main password field ID** empty skips the comparison, so always link the confirmation field to the correct field ID.

Matching and required-field validation are separate. Two empty optional fields pass the comparison. Enable **Required** on both fields when visitors must enter a password.

### Redirect {#redirect}

This form action redirects the user from the form page to a different page on your site. You may set the redirection to the admin area or to a custom URL and set the redirection to happen only after a specific period of time.

The Redirect form action is only triggered after all the other actions run successfully.

Since 1.10, Custom redirect URL field is supporting [Form dynamic field](#dynamic-fields) tag.

### Unlock password protection {#unlock-password-protection}

This form action is used to grant access to content protected by Bricks' password protection feature. You can map the relevant form field to “Password”, but if no field is mapped, the first password field in the form will be used by default.

For more detailed instructions on setting up password protection with forms, please refer to the [Password Protection article](https://academy.bricksbuilder.io/builder/features/password-protection/).

### Webhook (@since 2.0) {#webhook}

The **Webhook** form action, available since version 2.0, sends submitted form data to one or more external URLs.

Typical use cases include:

- Sending leads to CRMs like **Zoho**, **Hubspot**, or **Salesforce**
- Triggering **Zapier** or **Make** scenarios
- Storing form data in **Google Sheets** or external databases
- Notifying internal tools via a **custom API or Slack bot**

A webhook is simply an HTTP request sent when the form is submitted. You can control what data is sent, how it’s formatted, and whether errors should stop the form.

#### Setting: Endpoints

You can set up multiple webhook endpoints. Each has these options:

- **Name**: Label for this webhook (for your reference only)
- **Endpoint URL**: The URL to send form data to
- **Data format**: Choose how the data is sent:
  `JSON` or `Form data` (x-www-form-urlencoded)
- **Data**: Optional payload template using dynamic field tags
  Leave empty to send all form fields. Example:

```php
{ "name": "{{43f295}}", "email": "{{a5c626}}" }
```

**Headers**: Optional custom headers in JSON format. Example:

```php
{ "Authorization": "Bearer token" }
```

#### Setting: Max payload size (KB)

Set the max size of the request payload.
Default: `1024` (1 MB)

#### Setting: Rate limiting

- **Rate limiting**
  Enable to limit requests per hour
- **Max requests per hour**
  Set the limit (default: `60`)

#### Setting: Error handling

- **Continue on error**
  If enabled, form submission succeeds even if the webhook fails
- **Error message**
  Message shown if the webhook fails and "Continue on error" is off

**Example: Zapier**

To trigger a Zap from a form submission, follow these steps:

1. In [Zapier](https://zapier.com/), create a new Zap
2. Choose **Webhooks by Zapier** as the trigger
3. Select **Catch Hook**
4. Copy the webhook URL Zapier gives you

![](https://academy.bricksbuilder.io/assets/zapier-webhook-url.png)

1. In Bricks, edit your form and add a **Webhook** action
2. Paste the Zapier URL into the **Endpoint URL** field

![](https://academy.bricksbuilder.io/assets/bricks-webhook-zapier-url.png)

1. Set the **Data format** to `JSON` (recommended)
2. Optionally define the payload or leave it empty to send all fields
3. Save and test your form

For full setup instructions, see [Zapier’s webhook guide](https://help.zapier.com/hc/en-us/articles/8496288690317-Trigger-Zaps-from-webhooks).

### Create & update posts (@since 2.1)

It is also possible to create powerful frontend forms with Bricks using the "Create post" and "Update post" actions.

More information and examples can be found at [/builder/features/create-update-posts-on-the-frontend/](https://academy.bricksbuilder.io/builder/features/create-update-posts-on-the-frontend/)

### Custom {#custom-action}

The custom action will allow you to hook into the action `bricks/form/custom_action` and run your custom code.

Please ensure you have included the **Custom** in the "Actions after successful form submit" field on your form element when using this hook.

![](https://academy.bricksbuilder.io/assets/custom-action-form-element.png)

The action callback will receive the `$form` object which exposes the following methods to get the form settings, the form fields, and the form uploaded files (if needed):

**Settings**: `**$form->get_settings()**`

This method exposes an associative array with the form settings (fields and actions settings) similar to this:

```php
Array
(
    [fields] => Array
        (
            [0] => Array
                (
                    [type] => text
                    [label] => Name
                    [placeholder] => Your Name
                    [id] => 15bc57
                )

            [1] => Array
                (
                    [type] => email
                    [label] => Email
                    [placeholder] => Your Email
                    [required] => 1
                    [id] => 3db633
                )

            [2] => Array
                (
                    [type] => textarea
                    [label] => Message
                    [placeholder] => Your Message
                    [required] => 1
                    [id] => f65f2c
                )
            ...

        )

    [submitButtonStyle] => primary
    [actions] => Array
        (
            [0] => email
            ...
        )

    [successMessage] => Message successfully sent. We will get back to you as soon as possible.
    [emailSubject] => Contact form request
    [emailTo] => admin_email
    [fromName] => bricks
    [emailErrorMessage] => Submission failed. Please reload the page and try to submit the form again.
    [htmlEmail] => 1
    [mailchimpPendingMessage] => Please check your email to confirm your subscription.
    [mailchimpErrorMessage] => Sorry, but we could not subscribe you.
    [sendgridErrorMessage] => Sorry, but we could not subscribe you.
    ...
)

```

**Fields values**: `**$form->get_fields()**`

This method exposes an associative array with the submitted values for each form field, together with the post Id and the form Id:

```php
Array
(
    [form-field-15bc57] => John Doe
    [form-field-3db633] => john.doe@example.com
    [form-field-f65f2c] => Thank you for using Bricks!
    ...
    [postId] => 167
    [formId] => yrnkmt
    ...
    [referrer] => https://example.com/contact
)
```

**Submitted files**: `**$form->get_uploaded_files()**`

This method exposes an associative array with the properties of the submitted files, grouped by the form field Id:

> **Note**
>
> ['file'] => Physical saved location
> ['url'] => Might not be accessible if not save to media or save to custom directory.

```php
Array
(
    [form-field-sajbjc] => Array
        (
            [0] => Array
                (
                    [file] => /.../public/wp-content/uploads/2022/03/my-uploaded-file.png
                    [url] => https://example.com/wp-content/uploads/2022/03/my-uploaded-file.png
                    [type] => image/png
                )

            [1] => Array
                (
                    [file] => /.../public/wp-content/uploads/2022/03/my-other-file.png
                    [url] => https://example.com/wp-content/uploads/2022/03/my-other-file.png
                    [type] => image/png
                )
            ...

        )

)
```

**Example #1** Basic setup

```php
<?php
function my_form_custom_action( $form ) {
  // $fields = $form->get_fields();
  // $formId = $fields['formId'];
  // $postId = $fields['postId'];
  // $settings = $form->get_settings();
  // $files = $form->get_uploaded_files();

  // Perform some logic here...

  // Set result in case it fails
  $form->set_result([
    'action' => 'my_custom_action',
    'type'    => 'success', // or 'error' or 'info'
    'message' => esc_html__('Oh my custom action failed', 'bricks'),
  ]);
}
add_action( 'bricks/form/custom_action', 'my_form_custom_action', 10, 1 );
```

**Example #2** Trigger a second email after the form is submitted.

With the current Bricks version, you can only set one email notification. With this code snippet, you may trigger a second one.

```php
<?php
function my_form_custom_action_sending_email( $form ) {
  $fields = $form->get_fields();
  // $formId = $fields['formId'];
  // $postId = $fields['postId'];
  $settings = $form->get_settings();
  // $files = $form->get_uploaded_files();

  $to = 'recipient@example.com'; // Replace this
  $from = 'sender@example.com'; // Replace this
  $subject = 'Your Subject'; // Replace this

  if ( ! empty( $settings['emailContent'] ) ) {
    $message = $form->render_data( $settings['emailContent'] );
    $message = isset( $settings['htmlEmail'] ) ? nl2br( $message ) : $message;
  } else {
    $email = new Bricks\Integrations\Form\Actions\Email('email');
    $message = $email->get_default_message( $settings, $fields );
  }

  $headers[] = 'From: Your Name <'.$from.'>';
  $headers[] = 'Reply-to: '. $from;
  if ( isset( $settings['htmlEmail'] ) ) {
    $headers[] = 'Content-Type: text/html; charset=UTF-8' . "\r\n";
  }

  $result = wp_mail( $to, $subject, $message, $headers );

  // $form->set_result([
  //  'action' => 'my_custom_action',
  //  'type'    => 'success', // or 'error' or 'info'
  //  'message' => esc_html__('Oh my custom action failed', 'bricks'),
  // ]);
}
add_action( 'bricks/form/custom_action', 'my_form_custom_action_sending_email', 10, 1 );
```

<span id="custom-redirect-to-hidden-field"></span>

**Example #3** Custom redirect to a hidden field URL

In certain cases, you would like to redirect user to a page based on certain URL parameter values. In such scenario, you are not able to use `{url_parameter:key}` on the Custom redirect URL field. This is because the form was submitted in AJAX and the current page URL param will not be sent along the AJAX call.

**Method 1**
Since 1.10, Ridirect action is supporting dynamic form field. You can choose Redirect action and configure like this.

![](https://academy.bricksbuilder.io/assets/form-redirect-support-dynamic-field-tag.png)

**Method 2**
You can use Custom action with some PHP code for more complicated logic. You can first place the url parameter into a hidden field.

![](https://academy.bricksbuilder.io/assets/store-url-param-into-hidden-field.png)

<figcaption>

Store url parameter into hidden key, and choose Custom action

</figcaption>

Then choose Custom action, and follow below code as an example

```php
<?php
add_action( 'bricks/form/custom_action', 'redirect_to_my_key', 10, 1 );

function redirect_to_my_key( $form ) {
  $form_fields   = $form->get_fields();
  $form_id       = $form_fields['formId'];

  // Check if the form id is the one you want
  if( $form_id !== 'cyrozb' ) return;

  // oeckxw is the hidden field Id where I placed the {url_parameter:my_key}
  $my_key = isset( $form_fields['form-field-oecdxz'] ) ? $form_fields['form-field-oecdxz'] : '';

  if( $my_key ) {
    // Now you get the hidden field value and redirect to the page you want, for example:
    $redirect_to = get_site_url() . '/?key=' . $my_key;

    // If the hidden field value is a URL, just redirect to it instead of following my code
    // $redirect_to = $my_key;

    $form->set_result(
      [
        'action'          => 'my_custom_redirect', // This is the action name, you can set it to anything you want
        'type'            => 'redirect', // Must be set to 'redirect'
        'redirectTo'      => $redirect_to,
        'redirectTimeout' => 0 // Need to delay ? Set a timeout in milliseconds
      ]
    );
  }
}
```

### Custom form actions {#custom-form-actions}

Since Bricks 1.12.2, you can extend the functionality of Bricks forms by adding multiple **custom form actions**. This allows seamless integration with external services like CRMs, email marketing providers, notification systems, or any custom workflows you require.

To create custom actions, you use three key filters:

- **[`bricks/elements/{element_name}/controls`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-controls/)**: Add new actions and their settings to the form builder.
- **[`bricks/elements/{element_name}/control_groups`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-control_groups/)**: Group settings for better organization in the builder.
- **[`bricks/form/action/{form_action}`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-action-form_action/)**: Handle the logic for the custom action when the form is submitted.

These filters give you complete control over how custom actions are configured and executed.

#### Example: Creating a custom Slack notification action

**1 - Add the action to form actions setting:**

```php
add_filter(
    'bricks/elements/form/controls',
    function( $controls ) {
        $controls['actions']['options']['slack-notification'] = esc_html__( 'Send to Slack', 'bricks' );

        $controls['slackFields'] = [
            'group'       => 'slack',
            'label'       => esc_html__( 'Fields to include', 'bricks' ),
            'type'        => 'select',
            'multiple'    => true,
            'options'     => [], // Auto-populated with form fields with 'map_fields' => true
            'map_fields'  => true,
            'description' => esc_html__( 'Select which form fields to include in the Slack notification', 'bricks' ),
        ];

        return $controls;
    }
);
```

**2 - Add a new control group:**

```php
add_filter(
    'bricks/elements/form/control_groups',
    function( $control_groups ) {
        $control_groups['slack'] = [
            'title' => esc_html__( 'Slack notification', 'bricks' ),
            'required' => [ 'actions', '=', 'slack-notification' ],
        ];

        return $control_groups;
    }
);
```

1.

**3 - Handle the action logic on form submission:**

```php
add_action(
    'bricks/form/action/slack-notification',
    function ( $form ) {
        $settings = $form->get_settings();
        $fields   = $form->get_fields();

        // Custom Slack notification implementation
    }
);
```

## Form validation {#form-validation}

Bricks 1.7.1 provides a new filter named `bricks/form/validate` that allows you to validate every form submission and return error messages if your custom validation fails. The first `$errors` param is an array with each item being an error message. And the second `$form` param is the instance of the form that has been submitted.

The following code example validates the submitted email address for the form field ID `7e30aa`.

If no user account with this email address exists on this site, the validation fails, an error message is displayed, and no email will be sent.

```php
add_filter( 'bricks/form/validate', function( $errors, $form ) {
  $form_settings = $form->get_settings();
  $form_fields   = $form->get_fields();
  $form_id       = $form_fields['formId'];

  // Skip validation: Form ID is not 'kfbqso'
  if ( $form_id !== 'kfbqso' ) {
    // Early return the $errors array if it's not target form
    return $errors;
  }

  // Get submitted field value of form field ID '7e30aa'
  $email_address = $form->get_field_value( '7e30aa' );

  // Error: Email from registered user (show error message, and don't send email)
  if ( ! email_exists( $email_address ) ) {
    // Add error message to the $errors message array
    $errors[] = esc_html__( 'This email address is not in our system, sorry.', 'bricks' );
  }

  // Make sure to always return the $errors array
  return $errors;
}, 10, 2 );.
```

## Immediate input validation {#input-validation}

![](https://academy.bricksbuilder.io/assets/form-error-message-582x1024.png)

<figcaption>

Form field: Error message

</figcaption>

Bricks can show an error message directly below a field while the visitor types and when the field loses focus.

To utilize this feature:

1. Add an "Error Message" to a specific form field.
2. On input and when the field loses focus, the form will evaluate the user input to determine if the "Error Message" should be displayed based on the following criteria:

- **Required:** Checks if mandatory fields have data.
- **Min/Max number:** Ensures entered numbers fall within a defined range.
- **Email:** Confirms the correctness of the email format.
- **URL:** Validates the structure of inputted URLs.

Fields without an "Error Message" do not show this inline message. The browser's own validation message appears on submit instead, unless **Don't use browser validation** is enabled under **Fields**.

### Disabling immediate input validation

Sometimes, we don’t want error messages to appear immediately. Instead, we may want to display them only on specific events. This is now possible (@since 1.12) with the new **"Disable Form Validation"** control.

You can choose to disable validation on input, on blur, or both. However, the form will still be validated upon submission.

![](https://academy.bricksbuilder.io/assets/CleanShot-2024-12-17-at-11.38.32@2x.png)

## Pattern attribute validation {#pattern-validation}

With the new `pattern` attribute (`@since 2.0.2`), you can now validate form input natively before submission. Combined with the `title` attribute (also `@since 2.0.2`), you can display custom error messages directly from the browser. Make sure the "Don't use browser validation" toggle it not enabled.

The `pattern` attribute works with the following field types: `text`, `tel`, `email`, `url`, and `password`.

**Example:**
To require a simple phone number in the `###-###-###` format, you can use the pattern `^\d{3}-\d{3}-\d{3}$`.
Additionally, you can use the `title` attribute to guide users or show a helpful message if the input doesn’t match the pattern:

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-07-30-at-15.38.08@2x.png)

## Spam protection (Google reCaptcha V3) {#spam}

The Bricks form element supports the latest [Google reCaptcha V3](https://developers.google.com/recaptcha/docs/v3) mechanism. To enable it, first, [create](https://g.co/recaptcha/v3) a site key and a site secret key and then add both in your admin area under "Bricks > Settings > API keys".

After adding the keys, enable the reCaptcha setting when editing the Form element in the builder under the "Spam Protection" control group.

The reCAPTCHA, hCaptcha, and Turnstile settings only appear once their keys are saved. Until then, the **Spam protection** group shows a note that links to **Bricks > Settings > API keys**. A [honeypot field](#honeypot) needs no keys.

If you still get a lot of spam, you might need to tweak the score threshold level. The threshold is configured to 0.5 by default. Google reCaptcha V3 API returns a value between 0.0 and 1.0, where 0.0 is very likely a bot, and 1.0 is very likely a human interaction. To increase the Bricks threshold, please use the following PHP snippet:

```php
add_filter( 'bricks/form/recaptcha_score_threshold', function( $score ) {
    // Bricks default is 0.5
    $score = 0.8;
    return $score;
}, 10, 1 );
```

Setting the threshold to 0.8 means Bricks will only accept form submissions with higher scores (more likely to be human interactions).

## Spam protection (hCaptcha) {#hcaptcha}

Bricks integrates with hCaptcha. To utilize it, add your hCaptcha Sitekey and hCaptcha Secret Key under "Bricks > Settings > API keys".

After adding the keys, enable the hCaptcha setting when editing the Form element in the builder under the "Spam Protection" control group. You'll find options to select either "Invisible" or "Visible" hCaptcha. For the "Visible" hCaptcha:

- **Theme:** Choose between a `dark` or `light` theme.
- **Size:** Pick from `compact` or `normal`.

For detailed setup instructions, refer to the [hCaptcha documentation](https://docs.hcaptcha.com/switch/#get-your-hcaptcha-sitekey-and-secret-key).

### Automated form testing

For automated tests on a staging or test site, use [hCaptcha's test keys](https://docs.hcaptcha.com/#integration-testing-test-keys). Test keys do not provide anti-bot protection and must not be used on a production form.

Keep production monitoring separate from the public form, for example by testing the same setup on staging or using a dedicated protected monitoring form.

## Spam Protection (Cloudflare Turnstile) {#turnstile}

Beginning with version 1.9.2, Bricks has introduced support for Cloudflare Turnstile. To leverage its capabilities, first, add your Cloudflare Turnstile site key & secret key under "Bricks > Settings > API keys".

After registering the necessary details, go to the Form element in the builder and look for the “Spam Protection” control group. Here, you can toggle the Cloudflare Turnstile setting on or off.

Once enabled, you will have the ability to customize the following:

- **Theme:** Select between a "dark", "light", or the default "auto" theme.
- **Size:** Opt for either "compact" or "normal".

For more details about getting your site key and secret key, refer to the [Cloudflare Turnstile documentation](https://developers.cloudflare.com/turnstile/get-started/).

## Honeypot {#honeypot}

![](https://academy.bricksbuilder.io/assets/bricks-1.12.2-form-field-honeypot.png)

Another spam protection layer, available since Bricks 1.12.2 is the ability to turn any form field (except "Files", "Remember me", "HTML" and "Hidden") into a honeypot field. This won't affect or interrupt actual website visitors, but it'll prevent bot form submissions if they fill out any of your honeypot fields.

## Date and time picker fields {#datepicker}

Use a **Datepicker** field to let visitors select a date, a date with a time, or a time on its own. Bricks 2.5 adds **Disable calendar** for time-only selection and **24-hour time** to control the hour display in the picker.

Select the Form element, open a field under **Fields**, and set **Type** to **Datepicker**.

| Selection | Field settings |
| --- | --- |
| Date only | Leave **Enable time** off. |
| Date and time | Turn **Enable time** on and leave **Disable calendar** off. |
| Time only (Bricks 2.5) | Turn both **Enable time** and **Disable calendar** on. |

Existing datepicker fields keep their date selection behavior unless you enable **Disable calendar**.

### Time-only selection (@since 2.5) {#timepicker}

To collect an appointment time separately from its date:

1. Add a **Datepicker** field and give it a label such as `Appointment time`.
2. Turn on **Enable time**.
3. Turn on **Disable calendar**. This setting appears after you enable time.
4. Set **24-hour time** to **Enabled** if you want hours from `00` to `23` without an AM/PM selector.
5. Optionally enter **Min. time** and **Max. time**, such as `09:00` and `17:00`, to limit the times visitors can select in the picker.

<div className="screenshot screenshot--control-panel">

![Datepicker settings with Enable time and Disable calendar on, 24-hour time enabled, and time limits of 09:00 and 17:00.](https://academy.bricksbuilder.io/assets/form-timepicker-settings.webp)

</div>

<figcaption>

Time-only field settings with 24-hour selection and time limits of 09:00 to 17:00.

</figcaption>

<div className="screenshot screenshot--control-panel">

![Frontend appointment field showing 14:30 with a time picker open and no calendar.](https://academy.bricksbuilder.io/assets/form-timepicker-frontend.webp)

</div>

On the frontend, this field opens a time picker without a calendar. To collect the appointment date, add a second **Datepicker** field and leave **Enable time** off. Each field has its own value and field ID.

### 24-hour time (@since 2.5) {#24-hour-time}

The **24-hour time** setting appears when **Enable time** is on. It applies to both date-and-time and time-only pickers.

| Setting | Picker behavior |
| --- | --- |
| **Default** | Uses the WordPress time format under **Settings > General** to choose the hour display. |
| **Enabled** | Uses 24-hour selection without an AM/PM selector. |
| **Disabled** | Uses 12-hour selection with an AM/PM selector. |

This setting changes the controls inside the picker, not the format of the value shown in the form field or submitted with the form. A time-only field uses `H:i` (24-hour hours and minutes), so selecting `2:30 PM` still fills and submits `14:30`. A date-and-time field uses the WordPress date format followed by `H:i`.

These are the built-in formats. Custom code using the [datepicker options filter](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-form-datepicker_options/) can override them.

### Saving time values to post meta

When mapping a time-only field through **Create post** or **Update post**, set **Sanitization method** to **Text (sanitize_text_field)** to preserve a value such as `14:30`. Integer or float sanitization will not preserve the full time string.

With **Update post**, time-only fields bypass the date conversion used for datepicker fields that include a calendar. Those calendar fields still use the existing `Ymd` conversion when saving mapped post meta. For example, a date-only selection of October 15, 2026 is saved as `20261015`.

See [Create & Update Posts on the Frontend](https://academy.bricksbuilder.io/builder/features/create-update-posts-on-the-frontend/#date-and-time-meta) for a mapping example and custom-field integration details.

### Customize the picker options {#datepicker-options}

Bricks uses the [Flatpickr](https://flatpickr.js.org/) JavaScript library for date and time selection. Extend or customize the picker using its [available options](https://flatpickr.js.org/options/).

To change the library initialization options, use the `bricks/element/form/datepicker_options` filter, like so:

```php
add_filter( 'bricks/element/form/datepicker_options', function( $options, $element ) {
    $options['locale'] = [
        'firstDayOfWeek' => 1 // Set Monday as the first week day
    ];

    return $options;
}, 10, 2 );
```

The filter callback function accepts two arguments:

- $options - an array of [Flatpickr options](https://flatpickr.js.org/options/)
- $element - the Bricks element object

### Localize the date picker strings {#datepicker-l10n}

Flatpickr supports [l10n](https://flatpickr.js.org/localization/) for a variety of languages. You would need to load the language package by placing the following instructions into the Bricks Settings > Custom Code > Body (footer) scripts:

```php
<script src="https://npmcdn.com/flatpickr/dist/l10n/XX.js"></script>

<script>
   window.flatpickr.localize(window.flatpickr.l10ns.XX)
</script>
```

Replace the XX with the language code you need (e.g. **de** for German, **pt** for Portuguese, ...).

If you need to adjust the language on a specific form, you would need to load the language package as explained in the first line of the code above but then you may use the Bricks filter to load the language for a specific form element

```php
add_filter( 'bricks/element/form/datepicker_options', function( $options, $element ) {
    if ( $element->id === 'abcdef' ) {
      // localize the form "abcdef" element
      $options['locale'] = 'XX';
    }

    return $options;
}, 10, 2 );
```

## Define options value & label {#options}

Starting at Bricks 1.10.2 you can define the value & label for the checkbox, radio, and select field types by separating the option through a colon (:) like this:

![](https://academy.bricksbuilder.io/assets/bricks-form-options-value-label.png)

## Integrations {#integrations}

The Form element integrates with Mailchimp & Sendgrid. Allowing you to add new contacts to your email lists. Make sure you've added your Mailchimp/Sendgrid API keys as described below.

When editing your form element, you have to select Mailchimp or Sendgrid under "Actions" so the form knows to add the submitted email address to your list.

Once you've selected the proper action, a new "Mailchimp" or "Sendgrid" control group should appear. There you have to select the list you want to add this new contact to and the "Email field" of your form that contains the email address.

### Mailchimp {#mailchimp}

The Mailchimp form action allows you to automatically communicate your form data (email, first name, and last name) to a Mailchimp list and group.

To use the Mailchimp action, you need to create a Mailchimp account and then [get an API key](https://mailchimp.com/help/about-api-keys/).

To use this form action, add the API key under "Bricks > Settings > API keys > Mailchimp API key".

### SendGrid {#sendgrid}

The SendGrid form action allows you to automatically communicate your form data (email, first name, and last name) to a SendGrid list.

To use the SendGrid action, you need to create a SendGrid account and then [get an API key](https://docs.sendgrid.com/ui/account-and-settings/api-keys#creating-an-api-key).

To use this form action, add the API key under "Bricks > Settings > API keys > SendGrid API key".

## How to create a multi-column form {#multi-column}

To create a multi-column form, we first need to set the "Width" of the form fields in percentage.

**Example: Two-column layout**

Creating a two-column form is as simple as setting the width of the individual form fields to 50%.

To add some spacing between our form fields, let's set the "Width" of the first two form fields in our example to 49%. Those fields now take up 98% of the horizontal width. Creating a 2% gap between our columns. Set the bottom "Spacing" value to "2%" to apply the same spacing in all directions.

Lastly, set the "Alignment" to "space-between" to ensure our fields horizontally align with the outer edges of our form.

![](https://academy.bricksbuilder.io/assets/form-element-multi-column-layout-1024x539.png)

<figcaption>

Two-column form layout

</figcaption>

---

# Icon box

Source: https://academy.bricksbuilder.io/builder/elements/general/icon-box/

*The Icon Box element combines an icon with content in a flexible layout.*

The Icon Box element combines an icon with content in a flexible layout.

## Settings

- **Direction** (direction) - Layout direction of the icon and content.

- **Spacing** (number with units) - Gap between the icon and content.

### Icon

- **Icon** (icon) - The icon to display. Default: WordPress icon from Themify library.

- **Align** (align-items) - Vertical alignment of the icon.

- **Link** (link) - Make the icon clickable with a link.

- **Margin** (spacing) - Margin around the icon.

- **Padding** (spacing) - Padding inside the icon container.

- **Size** (number with units) - Font size of the icon.

- **Height** (number with units) - Height of the icon container.

- **Width** (number with units) - Minimum width of the icon container.

- **Color** (color) - Color of the icon.

- **Background color** (color) - Background color of the icon container.

- **Border** (border) - Border styling for the icon container.

- **Box shadow** (box-shadow) - Shadow effect for the icon container.

### Content

- **Content** (rich text) - The text content to display alongside the icon. Supports rich text and dynamic data.

- **Align** (align-items) - Vertical alignment of the content.

- **Margin** (spacing) - Margin around the content.

- **Padding** (spacing) - Padding inside the content container.

- **Heading typography** (typography) - Font settings for heading elements (h1-h6) in the content.

- **Body typography** (typography) - Font settings for the content text.

- **Background** (color) - Background color of the content container.

- **Border** (border) - Border styling for the content container.

- **Box shadow** (box-shadow) - Shadow effect for the content container.

> **Developer reference**
>
> See the [Icon Box Schema](https://academy.bricksbuilder.io/developer/schema/elements/icon-box/) for the full JSON schema of this element's settings and controls.

---

# Icon list

Source: https://academy.bricksbuilder.io/builder/elements/general/icon-list/

*The Icon List element creates a list of social media icons or custom icons with customizable styling, labels, and links.*

The Icon List element creates a list of social media icons or custom icons with customizable styling, labels, and links.

## Settings

- **Icons** (repeater) - Add and configure icons. Each icon has:
  - **Icon** (icon) - Icon selection. Default: `ion-logo-twitter`.
  - **Icon: Color** (color) - Individual icon color.
  - **Icon: Size** (number with units) - Individual icon size.
  - **Label** (text) - Text label for the icon.
  - **Label: Size** (number with units) - Label text size.
  - **Color** (color) - Text color for the icon/label combination.
  - **Background** (color) - Background color for the icon item.
  - **Link** (link) - Link destination for the icon.

- **Icon: Color** (color) - Global icon color for all icons.

- **Icon: Size** (number with units) - Global icon size for all icons.

### Alignment

- **Direction** (direction) - Layout direction. Options: `row`, `column`.

- **Align items** (align-items) - Vertical alignment of icons. Options: `flex-start`, `center`, `flex-end`, `baseline`.

- **Justify content** (justify-content) - Horizontal alignment of icons. Options: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly`.

- **Spacing (Items)** (number with units) - Spacing between icon items. Default: 0.

- **Spacing (Item)** (number with units) - Internal spacing within each icon item. Default: 5px.

> **Developer reference**
>
> See the [Icon List Schema](https://academy.bricksbuilder.io/developer/schema/elements/social-icons/) for the full JSON schema of this element's settings and controls.

---

# Map Connector

Source: https://academy.bricksbuilder.io/builder/elements/general/map-connector/

*Connect query-loop items to Google or Leaflet map markers using coordinates, per-item marker settings, and Info Box templates.*

The **Map Connector** works with the Google [Map](https://academy.bricksbuilder.io/builder/elements/general/map/) element and, starting with **Bricks 2.5**, [Map (Leaflet)](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/) when **Sync with query** is enabled. Place **one Map Connector inside each item** of the query loop that should produce a marker.

It renders an invisible **`<template>`** node that stores latitude, longitude, and/or address plus optional **Info Box** popup template data and **per-item marker overrides**. The Map reads these nodes to build markers when the query updates (pagination, filters, load more, etc.).

See [Google Map: Sync with query](https://academy.bricksbuilder.io/builder/elements/general/map/#3-sync-with-query) or [Leaflet: Sync with query](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#sync-with-query) for setup. External controls target the results loop containing the connectors, rather than the map itself.

Leaflet requires both **Latitude** and **Longitude**. It ignores address-only connectors. Google Maps can geocode an **Address** when coordinates are not supplied.

For [Geolocation filtering](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geolocation-element), the filter's data source must contain saved coordinates. Geocoding a connector's Address for a Google marker does not create coordinates in the filter index. Use the same location fields for the filter and connector so the radius search and markers agree.

Both map types preview the connected loop's markers in the builder. Test filters and pagination on the frontend.

## Active Marker State {#active-marker-state}

Starting with **Bricks 2.5**, a connector synced to a **Google Map** or **Map (Leaflet)** receives `map-marker-active` when its marker is selected by a click or an **Open address (Map)** interaction. This works without an Info Box. The class is removed when another marker is selected or the marker state is reset.

The connector itself is invisible. To highlight a card, assign a class such as `property-card` to the repeated item and use `.property-card:has(.map-marker-active)` in your CSS. See the [active connected item example](https://academy.bricksbuilder.io/builder/elements/general/map/#active-connected-item).

Both Google Map and Map (Leaflet) support **Scroll active item into view** in Sync mode. Bricks finds the loop item and scroll container automatically. See the [Google Map scroll settings](https://academy.bricksbuilder.io/builder/elements/general/map/#scroll-active-item) or [Leaflet scroll settings](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#scroll-active-item).

The `infobox-opened` class on interaction elements follows the Info Box's open/close state. Use `map-marker-active` on the connector to style the selected result independently of whether it has an Info Box.

## Settings

- **Latitude** (text) - Use dynamic data from the looped post (placeholder shows Berlin-area example).

- **Longitude** (text).

- **Address** (text) - Google Maps only: alternative to coordinates, resolved through geocoding. Leaflet requires latitude and longitude.

An error notice appears when all three fields are empty. For Leaflet, fill in both coordinate fields even if an Address is already set.

### Info Box (Popup)

- **Info Box: Template (Popup)** (select) - Popup template with **Template Settings > Popup > Info Box (Map)** enabled.

- **Info** - Reminds you to enable the Info Box option on the popup template.

### Markers

An **info** control notes that **Marker: Type** (text vs image) is configured on the connected map element, while fields here **override** that map’s defaults for **this** loop item.

Use the connector to set values for each loop item. Set global marker typography and image dimensions on the connected map element.

- **Label** (text) - Screen reader label (`aria-label`) for the marker.

- **Marker: Text** - Text for the default text marker.

- **Marker: Text (Active)** - Text for the active text marker.

- **Marker: Image** - Image for the default image marker.

- **Marker: Image (Active)** - Image for the active image marker.

> **Developer reference**
>
> See the [Map Connector Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-connector/) for the full JSON schema of this element's settings and controls.

---

# Map (Leaflet)

Source: https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/

*Display tile-based maps, populate markers from a query, or sync them with a filterable listing using Map Connectors.*

**Map (Leaflet)** displays maps using tile layers such as OpenStreetMap. Configure the tile provider under **Layers**, add locations under **Markers**, and set the center, zoom, and interactions under **Map**. It does not require a Google Maps API key. Tile providers may have their own access and attribution requirements.

Starting with **Bricks 2.5**, the element supports query-generated markers, **Sync with query**, clustering, text and image markers with active styles, and custom Info Boxes.

## Layers

Add a row to **Layers** for each tile source visitors should be able to select. Each row has:

- **Name**: Label in the layer switcher.
- **URL**: Tile URL template, such as `https://tile.openstreetmap.org/{z}/{x}/{y}.png`.
- **Min Zoom** and **Max Zoom**: Zoom levels supported by the tile provider.
- **Error Tile URL**: Fallback image for failed tiles.
- **Attribution**: Credits required by the provider.

The default layer uses OpenStreetMap. See the [Leaflet integration guide](https://academy.bricksbuilder.io/integrations/map-leaflet/#layers) for tile URL placeholders and provider examples.

## Choose the marker source {#marker-source}

| Mode | Use it for | Location data comes from |
| --- | --- | --- |
| Static | A fixed set of locations | Rows in the **Markers** repeater |
| Query loop | Markers generated from posts, terms, or other query results | Dynamic data in the first marker row |
| Sync with query | A map beside a listing that changes through filters, AJAX pagination, or Load More | Map Connectors inside a separate query loop |

Leaflet requires latitude and longitude. It does not convert street addresses into coordinates. Address-only Map Connectors are ignored.

### Static markers {#static-markers}

Add a row under **Markers** for each location. Enter **Coordinates** as `latitude, longitude`, for example `52.5164, 13.3776`. Dynamic data is supported. Static and query markers with missing, nonnumeric, or out-of-range coordinates are skipped.

Use **Label** to distinguish rows in the builder. It is separate from the screen reader **Label** in the marker settings. Add **Popup (Text)** for content shown when the marker is clicked. Each row can override the map's text or image marker defaults.

### Query loop {#query-loop}

Use the map's own query when you need markers without a separate visible results listing.

1. Under **Markers**, enable **Query loop**.
2. Open **Query** and choose the content to retrieve.
3. In the first marker row, use dynamic data for **Coordinates** and any marker text, images, or **Popup (Text)** that should change for each result.
4. For a custom popup design, select an **Info Box: Template (Popup)**. See [Info Boxes](#info-boxes).

Bricks uses the first marker row as the template for every query result. The screenshots below use a Publisher terms query with an ACF Google Map field named `map_location`. Its **Coordinates** value is:

```text
{acf_map_location:array_value|lat}, {acf_map_location:array_value|lng}
```

<div className="screenshot screenshot--control-panel">

![The first Leaflet marker row uses dynamic latitude and longitude from an ACF map field.](https://academy.bricksbuilder.io/assets/leaflet-query-marker-coordinates-2x.webp)

</div>

<div className="screenshot screenshot--control-panel">

![Leaflet Query loop enabled with a Terms query targeting the Publishers taxonomy.](https://academy.bricksbuilder.io/assets/leaflet-query-source-settings-2x.webp)

</div>

To update markers through filters, pagination, or Load More, create a separate results loop and use [Sync with query](#sync-with-query).

### Sync with query {#sync-with-query}

Use this mode to keep markers connected to a visible listing, such as property cards beside a map.

1. Create a [Query Loop](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) on a layout element, such as a Block or Div.
2. Place one [Map Connector](https://academy.bricksbuilder.io/builder/elements/general/map-connector/) inside the repeated item.
3. Set the connector's **Latitude** and **Longitude** using dynamic data from each result. Add marker overrides or an Info Box template if needed.
4. On Map (Leaflet), leave **Query loop** off. Under **Markers > Sync with query**, select the results loop.
5. Point filters, AJAX Pagination, Load More, and any Query Results Summary at that same results loop.
6. Enable **Map > Fit map on markers change** if the map should adjust its view after the results change.

Markers refresh when the connected loop changes on the frontend. Set **Text: No results** under **Markers** to customize the message when there are no locations. The default is `No locations found`. **No results typography** styles the message, and **No results position** places it at the top, bottom, or center of the map.

![Publisher cards beside Leaflet markers populated from the same Terms query.](https://academy.bricksbuilder.io/assets/leaflet-synced-publisher-list-2x.webp)

The builder previews the connected loop's markers. Test visitor filtering, pagination, and Load More on the frontend.

### Geolocation filtering {#geolocation-filtering}

Starting with **Bricks 2.5**, a [Filter - Geolocation](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geolocation-element) can limit the connected Posts, Terms, or Users listing to a radius around a location. Set its **Target query** to the results loop containing the Map Connectors, then select that same loop under the map's **Sync with query** control. The map's own query and static markers are not filter targets.

The filter connects automatically when exactly one Geolocation filter and one matching map use the query. For multiple filters or maps, select **Map (Optional)** on the filter. Each filter connects to one map, and each map can be controlled by one filter.

Device-location searches and **Search on map drag** work without Google APIs. Optional address search uses Google Maps JavaScript API and Geocoding API, and autocomplete additionally requires Places API (New). These services are separate from Leaflet's tile provider.

The map shows the applied search origin and radius, including when no locations match. Configure their appearance on the filter. Enable **Search on map drag** on the filter to search around the map center after a visitor finishes panning. Dragging must be enabled on the map. In **Visitor controlled** mode, visitors choose whether to search using a **Search as I move the map** checkbox; **Automatic** mode searches after every qualifying drag. Zooming alone does not trigger a search. **Apply on: On submit** stages the new location until submitted.

### Scroll the active item into view {#scroll-active-item}

In Sync mode, enable **Scroll active item into view** under **Markers** to scroll to a marker's connected result when the marker is clicked or selected through an **Open address (Map)** interaction. This works even when the marker has no Info Box. It is off by default.

- **Scroll behavior**: **Follow site setting** (default), **Smooth**, or **Instant**.
- **Scroll position**: **Nearest** (default), **Start**, or **Center**.

Bricks finds the result's nearest vertically scrollable parent, or scrolls the page when there is none. **Nearest** leaves an already visible item in place. No scroll-container selector is needed.

The selected result's Map Connector also receives `map-marker-active`, including when no Info Box is configured. Use this class to [style the connected card](https://academy.bricksbuilder.io/builder/elements/general/map-connector/#active-marker-state).

<div className="screenshot screenshot--control-panel">

![Leaflet synced to Publishers (Terms), with Scroll active item into view enabled, Smooth behavior, and Center positioning.](https://academy.bricksbuilder.io/assets/leaflet-sync-query-settings-2x.webp)

</div>

## Marker appearance {#marker-appearance}

Under **Markers > Marker**, choose **Type: Image** (default) or **Text**. Settings on individual marker rows or Map Connectors override the map's defaults.

### Text markers

Set the marker text and its active text, then style typography, background, border, box shadow, and padding for each state. **Max. width** limits the text marker's width. Dynamic data can display a property's price or a location's name.

### Image markers

Choose the normal and active marker images. Each state has height, width, border, and box shadow controls. Existing Leaflet **Icon** and **Marker (Default)** settings remain supported for saved maps.

Use the marker's screen reader **Label** to describe its location or purpose.

### Clustering

Enable **Cluster: Markers** to group nearby markers. Set **Cluster: Background color** and **Cluster: Text color** to style the cluster icons. The clustering library loads only when clustering is enabled.

![Publisher-name text markers and purple clusters showing marker counts on a Leaflet map.](https://academy.bricksbuilder.io/assets/leaflet-text-markers-clustering-2x.webp)

## Info Boxes and interactions {#info-boxes}

Static markers use **Popup (Text)**. Query and Sync modes support custom Bricks popup templates:

1. Create a Popup template and enable **Template Settings > Popup > Info Box (Map)**.
2. Design and publish the template. Use dynamic data for the current query result.
3. In Query mode, select it under **Markers > Info Box: Template (Popup)** on the map. In Sync mode, select it on the Map Connector instead.

Info Box templates support **Fetch content via AJAX** and its loader animation. See the [Info Box template guide](https://academy.bricksbuilder.io/builder/elements/general/map/#info-box-popup-template) for template setup.

Use **Open address (Map)** on an element inside the connected result to select its marker and open its Info Box. Use **Close address (Map)** on a button or icon inside the Info Box to close it. These actions are available under [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/#action).

![A custom publisher Info Box showing Hachette Book Group, Saint Joseph, MO, a View publisher link, and a close button.](https://academy.bricksbuilder.io/assets/leaflet-custom-infobox-detail.webp)

## Map view and behavior {#map-view}

| Setting | Behavior |
| --- | --- |
| Height | Map height. The placeholder is `300px`. |
| Map center | Center coordinates as `latitude, longitude`. |
| Disable initial fit map | Keep the configured center and zoom on page load. Off by default. |
| Fit map on markers change | Adjust the view after synced query results change. Off by default. |
| Zoom level (Initial) | Starting zoom. Defaults to `13`. Used when centering a single marker automatically. |
| Zoom level (Min) / (Max) | Constrain how far the map can zoom. |

By default, the initial view centers a single marker at the configured zoom or fits multiple markers.

**Disable initial fit map** and **Fit map on markers change** are independent. Enable the first to preserve the view on page load, and the second if later query updates should fit the current markers.

An active Geolocation search keeps its origin and radius visible instead of fitting the view to the result markers. A successful search with no matching locations retains the search area.

> **Existing Leaflet maps**
>
> Starting with Bricks 2.5, existing static Leaflet maps also use automatic initial fitting. To retain a manually configured center and zoom, enable **Map > Disable initial fit map**, including for maps with one marker.

<div className="screenshot screenshot--control-panel">

![Leaflet Map settings with Disable initial fit map enabled, Fit map on markers change disabled, and the center and zoom controls visible.](https://academy.bricksbuilder.io/assets/leaflet-initial-fit-settings-2x.webp)

</div>

The Map group also includes zoom snapping and increments, double-click and scroll wheel zoom, box zoom, zoom and attribution controls, closing popups on map clicks, dragging, and resize tracking. See [Leaflet's map options](https://leafletjs.com/reference.html#map) for the underlying behavior.

> **Developer reference**
>
> See the [Map (Leaflet) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-leaflet/) for the element's settings and controls.

---

# Map

Source: https://academy.bricksbuilder.io/builder/elements/general/map/

*Display Google Maps, sync markers with a query loop, style the connected active item, and scroll it into view when a marker is selected.*

The **Map** element in Bricks allows you to display Google Maps with a range of capabilities, from showing a single location to dynamically rendering multiple markers based on queries.

You can get started quickly by adding a Google Maps API key. Follow this guide to set it up: [How to set up your Google Maps API key](https://academy.bricksbuilder.io/integrations/how-to-set-up-your-google-maps-api-key/).

Without an API key, the Map element is still functional but limited to displaying **a single marker** only.

![](https://academy.bricksbuilder.io/assets/map-without-google-maps-api.png)

To ensure a marker is shown, simply enter a pair of coordinates (latitude and longitude, separated by a comma) in the **Address** field.

## Choose how the map renders

With an API key saved, **Render mode** lets you choose **Google Maps JavaScript API** (the default) or **Iframe embed**. Use Iframe embed when the map only needs a single address and you do not need API-only features such as multiple markers, clustering, query syncing, or custom Info Boxes. The iframe mode does not load the Google Maps JavaScript API for that map. Set its **Loading** option to `lazy` (the default) or `eager`.

Without an API key, the map uses the single-address iframe mode automatically. The Render mode selector appears only when an API key is saved.

## Displaying multiple addresses

To unlock advanced features such as multiple locations, clustering, and custom Info Boxes, save a valid **Google Maps API key** and use the **Google Maps JavaScript API** render mode. You will then see more controls on the element.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-addresses.png)

Bricks supports three address input modes:

### 1) Static

Manually define multiple locations using the "Addresses" **Repeater** control of the Map element. This mode supports only the default Google Maps Info Box.

### 2) Query loop

Use this mode to populate map markers with addresses or coordinates from a query.

For example, if you have a **custom post type** like "Properties" where each property contains an address, enabling the Query loop allows you to show markers of all property addresses on the map. `(@since 2.0)`

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-query-loop.png)

You can also define a [custom Info Box](#info-box-popup-template) using a popup template.

In our example above, we selected the custom post type `property`, where each address is stored in a custom field (ACF). Providing the latitude & longitude coordinates will be more accurate than a physical address.

The map's own query only populates markers. To update markers through filters, pagination, or Load More, use a separate results loop containing [Map Connectors](#map-connector-element) and sync the map to it.

### 3) Sync with query

Ideal for use cases where the map is shown alongside a dynamic query loop such as a directory, Sync with query allows the map to update live with the query as users interact via **AJAX Pagination**, **Load More**, or **Query Filters**.

This mode requires adding a [Map Connector](#map-connector-element) element inside the target query loop. Point filters, pagination, Load More, and any results summary at that loop.

The builder previews the connected loop's markers. Test filtering and pagination on the frontend. [Map (Leaflet)](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#sync-with-query) also supports this workflow.

It also supports [custom Info Boxes](#info-box-popup-template) using popup templates.

**Example setup:** You want to display a query loop on the same page as your map and connect the two. If this query loop uses **AJAX Pagination**, **Query Filters**, or **Load More**, enabling Sync with query allows the map markers to update dynamically in real-time as users interact with those features.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-sync-with-query.png)

**Map markers update according to query results**:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-sync-with-query-filters.png)

### Geolocation filtering {#geolocation-filtering}

Starting with **Bricks 2.5**, use a [Filter - Geolocation](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geolocation-element) to search the connected listing within a radius of an address, device location, or map center. Target a Posts, Terms, or Users results loop containing Map Connectors, and select the same loop under **Addresses > Sync with query**. The map must use **Google Maps JavaScript API** rendering. Static maps and the map's own query are not filter targets.

The filter reads saved coordinates from its configured data source. It does not geocode stored street addresses during indexing. Use matching location fields on the Map Connectors.

One matching Geolocation filter and one synchronized map connect automatically. If several filters or maps use the query, select **Map (Optional)** on the filter. Each filter connects to one map, and each map can be controlled by one filter.

The map shows the applied search origin and radius, including searches with no matching locations. Configure the origin marker and circle on the filter. Address search requires Maps JavaScript API and Geocoding API; autocomplete additionally requires Places API (New).

Enable **Search on map drag** on the filter to use the map center after the visitor finishes panning. Dragging must be enabled on the map. **Visitor controlled** mode displays a **Search as I move the map** checkbox; **Automatic** mode searches after every qualifying drag. Zooming alone does not trigger a search. **Apply on: On submit** stages the new location until submitted.

Under **Addresses**, use **No results text**, **No results typography**, and **No results position** to configure the empty-state message. Position it at the top or bottom to keep the origin marker visible.

### Scroll the Active Item Into View {#scroll-active-item}

Starting with **Bricks 2.5**, selecting a marker can scroll its connected query-loop item into view. This works when clicking a marker or selecting it through an **Open address (Map)** interaction, including markers without an Info Box.

1. Save a Google Maps API key and use **Google Maps JavaScript API** render mode.
2. Add a [Map Connector](https://academy.bricksbuilder.io/builder/elements/general/map-connector/) inside the target query loop and configure its location data.
3. On the Map element, select the loop under **Addresses > Sync with query**.
4. Enable **Scroll active item into view**. It is off by default.
5. Choose the scrolling behavior and position, then save and test the frontend.

| Setting | Options |
| --- | --- |
| Scroll behavior | **Follow site setting** (default) uses the scroll container's or page's CSS scroll behavior. **Smooth** animates scrolling. **Instant** scrolls immediately. |
| Scroll position | **Nearest** (default) moves only as far as needed to bring the item into view. **Start** aligns its top with the scroll area. **Center** centers it vertically. |

Bricks finds the connected loop item automatically and scrolls its nearest vertically scrollable parent. If there is no such parent, it scrolls the page. You do not need an interaction on each result, a target selector, or a scroll-container selector. With **Nearest**, an item already visible, or an oversized item spanning the scroll area, stays in place.

<div className="screenshot screenshot--control-panel">

![Map settings targeting the Publisher card query, with Scroll active item into view enabled, Smooth behavior, and Center positioning.](https://academy.bricksbuilder.io/assets/map-scroll-active-item-settings.webp)

</div>

## Markers

![](https://academy.bricksbuilder.io/assets/markers-control.png)

### Cluster markers

Enable this option to automatically group nearby markers into a cluster. `(@since 2.0)`

![](https://academy.bricksbuilder.io/assets/cluster-markers.png)

## General Settings

### Map ID

![](https://academy.bricksbuilder.io/assets/map_id-control.png)

Enter your **Google Maps ID** (available in your Google Cloud Console) to enable the latest Maps features `(@since 2.0)`  
When set:

- Bricks uses Google's modern `AdvancedMarker` API.
- Map styles are managed via your Google Console (style settings in Bricks are disabled).
- Deprecated browser console warnings are avoided.

### Map Center

![](https://academy.bricksbuilder.io/assets/map-center-control.png)

Set the default center point of the map. With **Sync with query**, AJAX updates preserve the current view unless **Fit map on markers change** is enabled. When fitting is enabled and no locations remain, the map returns to its configured center and zoom. An active Geolocation search preserves its search origin and radius when there are no results.

### Initial view and marker updates {#map-fitting}

By default, the initial view centers a single marker at the configured zoom or fits multiple markers. Enable **Disable initial fit map** to retain the configured center and zoom on page load.

**Fit map on markers change** separately controls whether the view adjusts after synced-query updates. It is off by default.

### Others

![](https://academy.bricksbuilder.io/assets/general-settings.png)

## Map Connector (element)

**The Map Connector element `(@since 2.0)` is required when using Sync with query.**

Place it inside the target query loop that you want to sync with your map. It generates an invisible `<template>` node containing location data, which is then read by the map to dynamically render the markers.

**Note:** It's strongly recommended to provide **latitude and longitude** values whenever available. If you rely solely on addresses and require geocoding every time markers are rendered, you may incur charges from the Google Maps Platform Geocoding API.

![](https://academy.bricksbuilder.io/assets/map-connector.png)

You can also define the Info Box (popup template) that should show when a marker is clicked. Make sure the selected popup template has the **"Info Box (Map)"** option enabled in its settings.

## Info Box (Popup template)

Introduced in version 2.0, the **Info Box (Map)** option is available in Popup template settings.

![](https://academy.bricksbuilder.io/assets/infobox-popup.png)

- Once enabled, the popup will display with a default width of 300px in the builder and remove the backdrop for preview.
- You can customize the design of the Info Box in the builder.
- Supports **Fetch content via AJAX**.
- Supports **AJAX loader** animation when loading dynamically.
- It is recommended to set **Populate Content** to the post or term being looped so dynamic data displays correctly in the builder.

![](https://academy.bricksbuilder.io/assets/infobox-popup-preview.png)

## Map Interactions

Two new map interaction actions are introduced in Bricks 2.0:

- Open address (Map)
- Close address (Map)

![](https://academy.bricksbuilder.io/assets/interaction.png)

Use cases:

- Use a button or element inside the query loop to **open** the Info Box for the corresponding marker.
- Add a close icon inside the Info Box popup to allow users to manually **close** it.

These interactions provide greater control and flexibility over how Info Boxes behave in dynamic mapping scenarios.

When an Info Box opens, Bricks adds the `infobox-opened` class to the interaction elements associated with that marker. The class is removed when the Info Box closes. You can use this class to style the open state or a parent element that contains the interaction element:

```css
.looping-div:has(.infobox-opened) {
  background-color: blue;
}
```

### Style the Active Connected Item {#active-connected-item}

Starting with **Bricks 2.5**, Bricks adds `map-marker-active` to the **Map Connector** associated with the selected marker. The class updates when a marker is clicked or selected through **Open address (Map)**, even if the marker has no Info Box. Bricks removes it when another marker is selected or the marker state is reset, including when query updates rebuild the markers.

Because the connector is an invisible `<template>` node, style the visible loop item that contains it. For example, assign the `property-card` class to the repeated card and add:

```css
.property-card:has(.map-marker-active) {
  outline: 2px solid currentColor;
  outline-offset: 4px;
}
```

The active connector class and **Scroll active item into view** work independently. Use `map-marker-active` to style the selected location's card. Continue using `infobox-opened` on interaction elements for the Info Box's open/close state.

![Selecting a map marker scrolls the publisher list to Penguin Random House and outlines its connected card.](https://academy.bricksbuilder.io/assets/map-active-connected-item.webp)

## Resolving Google Maps Script Conflicts with Other Plugins

Starting with **Bricks 2.5**, Bricks reuses a Google Maps API runtime that another integration has loaded or is loading. It preserves that integration's key, language, and callbacks. A manual script-dequeue workaround is usually unnecessary.

If the map or address search fails, check that the key used by the shared Google loader permits the APIs your page needs. A key configured by another plugin can have different service or website restrictions from the key saved in Bricks. Consent tools and script optimizers can also control when Google becomes available.

After upgrading, review custom code that deregisters `bricks-google-maps` or starts the map on a fixed timer. Test the map and address search together on the frontend before removing an existing workaround.

## Settings

### Addresses

- **Addresses** (repeater) - Add map locations. Each address has:
  - **Latitude** (text) - Latitude coordinate. Placeholder: `52.5164154966524`.
  - **Longitude** (text) - Longitude coordinate. Placeholder: `13.377643715349544`.
  - **Address** (text) - Address for geocoding (alternative to coordinates). Placeholder: `Berlin, Germany`.
  - **Info Box template** (select) - Template for infobox popup.
  - **Title** (text) - Infobox title.
  - **Subtitle** (text) - Infobox subtitle.
  - **Content** (textarea) - Infobox content.
  - **Images** (image-gallery) - Images for infobox.
  - **Width** (number) - Infobox width. Placeholder: `300`.
  - **Label** (text) - Screen reader label for accessibility.
  - **Marker: Text** (text) - Text marker content. Placeholder: `Marker`.
  - **Marker: Text (Active)** (text) - Active text marker content. Placeholder: `Marker`.
  - **Marker: Image** (image) - Image marker.
  - **Marker: Image (Active)** (image) - Active image marker.

### Query loop

- **Has loop** (checkbox) - Enable query loop for dynamic addresses.
- **Query** (query) - Configure which posts to display.
- **Info Box: Template** (select) - Template for infobox popup in query loop.

### Sync with query

- **Sync with query** (query-list) - Connect to existing query loop for dynamic markers.
- **Text: No results** (text) - Message when no locations found. Placeholder: `No locations found`.
- **Scroll active item into view** (checkbox, Bricks 2.5) - Scroll to the connected loop item when its marker is selected. Off by default. Requires a selected query and JavaScript API rendering.
- **Scroll behavior** (select) - Follow site setting (default), Smooth, or Instant. Available when scrolling is enabled.
- **Scroll position** (select) - Nearest (default), Start, or Center. Available when scrolling is enabled.

### Markers

- **Cluster: Markers** (checkbox) - Enable marker clustering.
- **Cluster: Background color** (color) - Cluster background color.
- **Cluster: Text color** (color) - Cluster text color.

- **Marker** (separator) - Global marker settings.
- **Type** (select) - Marker type. Options: `image`, `text`. Default: `image`.

#### Marker: Text

- **Max. width** (number with units) - Maximum text marker width.
- **Typography** (typography) - Text marker font settings.
- **Background color** (color) - Text marker background.
- **Border** (border) - Text marker border styling.
- **Box shadow** (box-shadow) - Text marker shadow.
- **Padding** (spacing) - Text marker padding.

#### Marker: Text (Active)

- **Typography** (typography) - Active text marker font settings.
- **Background color** (color) - Active text marker background.
- **Border** (border) - Active text marker border styling.
- **Box shadow** (box-shadow) - Active text marker shadow.
- **Padding** (spacing) - Active text marker padding.

#### Marker: Image

- **Marker** (image) - Default marker image.
- **Height** (number) - Marker height in pixels. Placeholder: `40`.
- **Width** (number) - Marker width in pixels. Placeholder: `40`.
- **Border** (border) - Marker border styling.
- **Box shadow** (box-shadow) - Marker shadow.

#### Marker: Image (Active)

- **Marker (Active)** (image) - Active marker image.
- **Height** (number) - Active marker height in pixels. Placeholder: `40`.
- **Width** (number) - Active marker width in pixels. Placeholder: `40`.
- **Border** (border) - Active marker border styling.
- **Box shadow** (box-shadow) - Active marker shadow.

### Map

- **Map ID** (text) - Google Maps ID from Cloud Console for advanced features.
- **Render mode** (select) - With an API key saved, choose Google Maps JavaScript API or Iframe embed. Default: Google Maps JavaScript API.
- **Loading** (select) - For iframe rendering, choose `lazy` or `eager`. Default: `lazy`.

#### Map center

- **Latitude (Center)** (text) - Map center latitude. Placeholder: `52.5164154966524`.
- **Longitude (Center)** (text) - Map center longitude. Placeholder: `13.377643715349544`.
- **Address (Center)** (text) - Map center address. Placeholder: `Berlin, Germany`.

#### General settings

- **Height** (number with units) - Map container height. Placeholder: `300px`.
- **Zoom level** (number) - Initial map zoom level. Range: 0-20. Placeholder: `12`.
- **Map type** (select) - Map style. Options: `roadmap`, `satellite`, `hybrid`, `terrain`. Default: `roadmap`.
- **Map style** (select) - Predefined map styles. Requires roadmap type.
- **Custom map style** (code) - JSON code for custom styling from Snazzy Maps.
- **Apply: Custom map style** (apply) - Apply custom style changes.
- **Disable initial fit map** (checkbox) - Preserve the configured center and zoom on page load. Off by default.
- **Fit map on markers change** (checkbox) - Adjust the view after synced query results change. Off by default.
- **Scroll** (checkbox) - Enable scroll wheel zooming. Default: true.
- **Draggable** (checkbox) - Enable map dragging. Default: true.
- **Fullscreen Control** (checkbox) - Show fullscreen button.
- **Map Type Control** (checkbox) - Show map type selector.
- **Street View Control** (checkbox) - Show street view button. Default: true.
- **Disable Default UI** (checkbox) - Hide all default controls.
- **Disable clickable POI** (checkbox) - Disable clicking on points of interest.
- **Zoom Control** (checkbox) - Show zoom controls. Default: true.
- **Zoom level (Min)** (number) - Minimum zoom level.
- **Zoom level (Max)** (number) - Maximum zoom level.

### No API Key Mode

When no Google Maps API key is configured, the element falls back to Google Maps Embed API with limited functionality:

- **Address** (text) - Single address for embedded map. Placeholder: `Berlin, Germany`.
- **Loading** (select) - Loading behavior. Options: `eager`, `lazy`. Default: `lazy`.

> **Developer reference**
>
> See the [Map (Google) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map/) for the full JSON schema of this element's settings and controls.

---

# Nav (Nestable)

Source: https://academy.bricksbuilder.io/builder/elements/general/nav-nested/

*The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports.*

The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports nested menu structures and can be used to build complex navigation systems.

## Settings

### HTML Tag & Accessibility

- **HTML tag** (text) - HTML tag for the navigation element. Supports dynamic data. Default placeholder: `nav`. Validates HTML tag format.

- **aria-label** (text) - Accessibility label for the navigation. Supports dynamic data. Default placeholder: "Menu".

### Top Level (Item)

- **Gap** (number with units) - Gap between top-level navigation items. Controls `gap` property for `.brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of top-level items. Deprecated since version 1.10. Description suggests using "Align items" under "Mobile menu" instead. Direction: row. Excludes space options.

- **Padding** (spacing) - Padding for top-level navigation items. Controls `padding` property for multiple selectors including `.brx-nav-nested-items > li > a`, text links, icons, SVG elements, and submenu toggles.

- **Background color** (color) - Background color for top-level items. Controls `background-color` property for links, text links, icons, SVG elements, and submenu toggles.

- **Border** (border) - Border styling for top-level items. Controls `border` property for links, text links, icons, SVG elements, and submenu toggles.

- **Typography** (typography) - Typography settings for top-level items. Controls `font` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transform** (transform) - Transform settings for top-level items. Controls `transform` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transition** (text) - Transition settings for top-level items. Supports dynamic data. Controls `transition` property for list items, links, text links, icons, SVG elements, submenu toggles, and submenu toggle children.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Background color** (color) - Background color for active/current page items. Controls `background-color` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Border** (border) - Border styling for active items. Controls `border` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Typography** (typography) - Typography settings for active items. Controls `font` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current > *` selectors.

#### Dropdown (Top Level Only)

- **Dropdown** (separator) - Separator for top-level dropdown controls. Description: "Only applies to top level dropdown elements."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle > span` selector.

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-nav-nested-items > li > .brx-submenu-toggle` selector.

### Dropdown

#### Text

- **Text** (separator) - Separator for dropdown text controls. Description: "Control dropdown element text."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-submenu-toggle span` selector (applies to all dropdowns).

#### Icon

- **Icon** (separator) - Separator for dropdown icon controls. Description: "Edit dropdown to set icon individually."

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-submenu-toggle` selector.

- **Icon position** (select) - Position of the dropdown icon. Options from icon position control options. Default placeholder: "Right". Controls `flex-direction` property for `.brx-submenu-toggle` selector (sets to `row-reverse` when left).

- **Icon size** (number with units) - Size of the dropdown icon. Controls `font-size` property for `.brx-submenu-toggle button` selector.

- **Icon color** (color) - Color of the dropdown icon. Controls `color` property for `.brx-submenu-toggle button` selector.

- **Icon transform** (transform) - Transform settings for dropdown icons. Controls `transform` property for `.brx-submenu-toggle button > *` selector (targets icon only).

- **Icon transform (Open)** (transform) - Transform settings for dropdown icons when open. Controls `transform` property for `.brx-submenu-toggle button[aria-expanded="true"] > *` selector (targets icon only).

- **Icon transition** (text) - Transition settings for dropdown icons. Supports dynamic data. Controls `transition` property for `.brx-submenu-toggle button[aria-expanded] > *` selector (targets icon only). Uses `!important` to override other transitions.

#### Content

- **Content** (separator) - Separator for dropdown content controls. Description: "Sub menu, mega menu, or multilevel area."

- **Min. width** (number with units) - Minimum width for dropdown content. Controls `min-width` property for `.brx-dropdown-content` selector. Triggers re-render.

- **Background color** (color) - Background color for dropdown content. Controls `background-color` property for `.brx-dropdown-content` selector.

- **Border** (border) - Border styling for dropdown content. Controls `border` property for `.brx-dropdown-content` selector.

- **Box shadow** (box-shadow) - Box shadow for dropdown content. Controls `box-shadow` property for `.brx-dropdown-content` selector.

- **Typography** (typography) - Typography settings for dropdown content. Controls `font` property for `.brx-dropdown-content` selector.

- **Transform** (transform) - Transform settings for dropdown content. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown > .brx-dropdown-content` selector.

- **Transform (Open)** (transform) - Transform settings for dropdown content when open. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown.open > .brx-dropdown-content` selector.

- **Transition** (text) - Transition settings for dropdown content. Supports dynamic data. Controls `transition` property for `.brx-dropdown-content` selector.

- **Z-index** (number) - Z-index for dropdown elements. Controls `z-index` property for `.brxe-dropdown` selector. Default placeholder: 1001.

#### Item

- **Item** (separator) - Separator for dropdown item controls.

- **Padding** (spacing) - Padding for dropdown items. Controls `padding` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content :where(.brx-submenu-toggle > *)` selectors.

- **Background** (color) - Background color for dropdown items. Controls `background-color` property for `.brx-dropdown-content > li` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for dropdown items. Controls `border` property for `.brx-dropdown-content > li:not(.brxe-dropdown)` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Typography** (typography) - Typography settings for dropdown items. Controls `font` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content .brx-submenu-toggle > *` selectors.

- **Transition** (text) - Transition settings for dropdown items. Supports dynamic data. Controls `transition` property for dropdown content items, links, submenu toggles, and megamenu elements.

#### Multilevel

- **Multilevel** (separator) - Separator for multilevel controls. Description: "Show only active dropdown. Toggle on click. Inner dropdowns inherit multilevel."

- **Enable** (checkbox) - Enable multilevel dropdown functionality.

- **Back: Text** (text) - Text for the back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for the back button. Only available when multilevel is enabled. Controls `font` property for `.brx-multilevel-back` selector.

- **Back: Background** (color) - Background color for the back button. Only available when multilevel is enabled. Controls `background-color` property for `.brx-multilevel-back` selector.

### Mobile Menu

- **Mobile menu** (separator) - Separator for mobile menu controls. Description: "Insert "Toggle" element after "Nav items" to show/hide your mobile menu."

- **Keep open while styling** (checkbox) - Keep mobile menu open during styling in the builder. Adds `brx-open` class. Not saved as setting.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Width** (number with units) - Width of the mobile menu. Controls `width` property for `&.brx-open .brx-nav-nested-items` selector.

- **Height** (number with units) - Height of the mobile menu. Controls `height` property for `&.brx-open .brx-nav-nested-items` selector.

- **Padding (Dropdown)** (spacing) - Padding for dropdown content in mobile view. Controls padding for `&.brx-open .brx-dropdown-content > *` selector. Description: "Used to create visual hierarchy between nested dropdowns."

- **Align items** (align-items) - Vertical alignment of mobile menu items. Controls `align-items` property for `&.brx-open .brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of mobile menu items. Controls `justify-content` property for `&.brx-open .brx-nav-nested-items` selector.

- **Position** (dimensions) - Position settings for the mobile menu. Controls multiple position properties.

- **Background color** (color) - Background color for the mobile menu. Controls `background-color` property for mobile menu selectors.

#### Item

- **Item** (separator) - Separator for mobile menu item controls.

- **Align items** (align-items) - Vertical alignment of mobile menu items. Excludes `stretch` option. Controls `align-items` property for various mobile menu item selectors.

> **Developer reference**
>
> See the [Nav (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/nav-nested/) for the full JSON schema of this element's settings and controls.
