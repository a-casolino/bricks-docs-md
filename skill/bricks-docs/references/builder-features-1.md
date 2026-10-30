# How to add a custom animation in interaction

Source: https://academy.bricksbuilder.io/builder/features/add-custom-animation-to-interaction/

*Add a custom GSAP animation to a Bricks interaction and connect it to triggers, timelines, and interaction events.*

## Step 1: Add a new option via bricks/setup/control_options hook

Hook documentation: [/developer/hooks/filters/filter-bricks-setup-control_options/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/)

```php
add_filter( 'bricks/setup/control_options', function( $options ) {
  // Add custom animation into animationTypes
  // Note that the key is very important, must be unique
  $options['animationTypes']['myAnim1'] = esc_html__( 'My animation 1', 'bricks' );

  return $options;
}, 10 );
```

![](https://academy.bricksbuilder.io/assets/custom-animation-added.png)

Custom animation added to the interaction "Animation" dropdown

## Step 2: Add animation CSS

When the interaction is set, Bricks will assign a class to the element using your animation key (`myAnim1` in our example), and it will be prefixed with `brx-animate-`.

All you have to do is create a CSS class that sets the animation name for your element, along with the corresponding keyframes for your animation. You can place these CSS inside `Bricks > Settings > Custom Code > Custom CSS`.

![](https://academy.bricksbuilder.io/assets/custom-css-code-for-animation.png)

```php
.brx-animate-myAnim1 {
  animation-name: my-anim-1;
}

@keyframes my-anim-1 {
  0% {
    animation-timing-function: ease-in;
    opacity: 0;
    transform: translateY(-250px);
  }
  38% {
    animation-timing-function: ease-out;
    opacity: 1;
    transform: translateY(0);
  }
  55% {
    animation-timing-function: ease-in;
    transform: translateY(-65px);
  }
  72% {
    animation-timing-function: ease-out;
    transform: translateY(0);
  }
  81% {
    animation-timing-function: ease-in;
    transform: translateY(-28px);
  }
  90% {
    animation-timing-function: ease-out;
    transform: translateY(0);
  }
  95% {
    animation-timing-function: ease-in;
    transform: translateY(-8px);
  }
  100% {
    animation-timing-function: ease-out;
    transform: translateY(0);
  }
}
```

Now, you can use this new animation on any element from the "Interactions" panel.

---

# Accessibility

Source: https://academy.bricksbuilder.io/builder/features/accessibility/

*Improve accessibility in Bricks with better semantic structure, keyboard support, contrast, and other practical checks for templates and content.*

Accessibility (short: **a11y**), is the fine art of making your website as usable as possible by as many people as possible.

No matter your drive to improve the accessibility of your website, making your website as inclusive as possible is the most ethical approach and will benefit your business in the long term.

According to the [WHO](https://www.who.int/disabilities/world_report/2011/report.pdf) around 15% of the world’s population has some sort of disability. Your time is better invested in improving your site accessibility than optimizing it for IE (which has only 2% global usage). In some countries, this is a legal requirement.

## How Bricks Helps To Address Accessibility

Bricks provides the tools for you to generate the most semantic HTML possible and approach a11y requirements & best practices without the need to code.

Making sure the content is understandable by the majority of your site's target visitors. The [HTML is valid](https://validator.w3.org/nu/) with an appropriate semantic structure. Links and buttons are descriptive enough. Images have relevant `alt` descriptions, etc. Just to mention some of the relevant aspects of **a11y**.

## ARIA landmarks

Bricks, by default, creates three different [landmark regions](https://www.w3.org/TR/wai-aria-practices/examples/landmarks/HTML5.html) for you: Header, Main, and Footer.

Bricks elements use the most semantic tags whenever possible. For example, the **Form** element and the **Nav Menu** element use the correct HTML tag: `form` and `nav`, respectively. If you need to add more landmarks to your page, or any other semantic tag, you may do it using the Container element, selecting the **HTML tag** needed. You can specify a custom HTML tag, too.

![Select a semantic HTML tag to a container.](https://academy.bricksbuilder.io/assets/container-landmark-tags.jpg)

Bricks 1.3 also introduces [Custom Attributes](https://academy.bricksbuilder.io/builder/features/custom-attributes/). Those allow you to add other attributes to any Bricks element.

A common example: If you want to assign the **role** attribute to a container, to go "Style > Attributes", add a new attribute by clicking the "+" icon, and set the "Name" to "role" and the "Value" to the appropriate value:

![Add custom attributes to a Bricks element](https://academy.bricksbuilder.io/assets/custom-attributes.jpg)

## Images

Images in Bricks are rendered using the alternative text provided in the image media attributes (WordPress Media). The `alt` attribute is the place where site owners should provide a description of the image for people that are not able to view it. Bricks will also allow you to provide a custom `alt` attribute if you are using the Image element inside the builder.

Background images are output as CSS background images. Use them for decorative imagery. If an image carries meaning, prefer the Image element so the image can use proper alternative text, or add the necessary supporting text or custom attributes manually.

## Links

Set `aria-label` (and `title`) attributes to links using the builder if the link description is empty or not clear enough. These attributes will improve how assistive technology like screen readers interpret your website and should be used to provide better context to the link in case the link content is not semantic enough.

It is also important to mention that it is a good practice to avoid using links with terms like "Read more" or "Click here" as these labels do not provide any context to the visitors. If you still want to use these terms, make sure your links contain the `aria-label` attribute to provide context to the navigation.

## Forms

The Form element lets you add or remove field labels. Field labels are important to comply with a11y guidelines as they provide a description of what is expected to be input in each field. If you prefer to not present field labels, Bricks automatically adds the `aria-label` attribute to the field input using the label defined for each field in the builder.

## Keyboard navigation

One of the main a11y requirements is to make sure your website can be operated/navigated using the keyboard only.  Assuring good keyboard navigation not only will allow people that cannot use a mouse to navigate through your website but also people using other assistive technologies.

One of the key aspects of keyboard navigation is to have a visual hint of where the focus is. Bricks 1.3 introduces default CSS to style the `:focus` property.

You can set your own focus style under "Settings > Theme Styles > Typography > Focus Outline". Although not recommended, if you want to remove this focus outline default, simply set it to "none".

### Skip navigation links

When using the keyboard navigation it can be frustrating having to navigate through all the menu links before arriving at the page's main content. To overcome this, one of the best practices, together with semantic ARIA landmarks (as described above), is to insert links on the top of the page to bypass the navigation.

Bricks 1.3 introduces two skip links by default: one to skip to the content and another to skip to the footer (if the footer exists). These skip links are added automatically to your website and will only appear if you press the TAB key on your keyboard.

### Menus

One of the most used elements in websites is the navigation menu. This element makes the website content more approachable to everyone and therefore deserves special attention to allow people without a mouse to also be able to navigate and open links inside menus.

Bricks also covers this need. All menus generated by Bricks are wrapped inside a `<nav>` tag and are fully keyboard-accessible according to the typical behavior of the keys when the focus is inside a menu element:

- TAB: Selects the next menu item
- SHIFT TAB: Select the previous menu item
- ENTER: Follows the link (similar to click)
- SPACE: Toggles the submenu (if exists)

Bricks implements the keyboard menu navigation using the [fly-out menu](https://www.w3.org/WAI/tutorials/menus/flyout/) approach.

> **Note**
>
> As accessibility requirements and best practices evolve, so does Bricks. If you spot any potential accessibility improvements, [please let us know](https://bricksbuilder.io/contact/).

---

# AI Abilities and Skills

Source: https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/

*Use Bricks AI abilities through MCP-compatible clients or WP-CLI, manage which actions are available, and install optional Bricks skills.*

https://www.youtube.com/watch?v=DcmoqqXWGcs

Bricks 2.4 introduces experimental AI abilities for Bricks. Abilities are actions registered with the WordPress Abilities API that an AI agent can run through an MCP-compatible client. Developers can also inspect and run the same registered abilities from WP-CLI when the `wp ability` command is available.

With abilities enabled, a connected agent can read and update parts of a Bricks site: design system, templates, elements, [dynamic data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/), media, WooCommerce templates, and [revisions](https://academy.bricksbuilder.io/builder/interface/revisions/).

Bricks skills are optional companion instructions for AI clients that support skills, rules, or reusable project guidance. They do not add new site permissions or new Bricks actions. They teach the agent how to work with Bricks more carefully, for example when to inspect the existing design system, avoid duplicate classes or variables, preview before saving, and choose the right ability for the task.

Use `Bricks > AI` to set up the MCP connection, choose which abilities are available on the site, create credentials, and install optional Bricks skills.

> **Experimental feature**
>
> AI abilities can write to your site. Test on a local or staging site first. Keep this feature off on production sites while it is experimental.

## Where to find it

Visit the `Bricks > AI` screen in your WordPress dashboard.

The AI screen is split into three tabs:

| Tab             | What it does                                                                                                                                        |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Configuration` | Installs or detects the WordPress MCP Adapter, enables Bricks abilities, creates an application password, and generates client-specific MCP config. |
| `Abilities`     | Lets you choose which Bricks MCP abilities are available on this site.                                                                              |
| `Skills`        | Helps you install and verify the optional Bricks skills package in your AI client.                                                                  |

![](https://academy.bricksbuilder.io/assets/bricks-ai-admin-screen.png)

## How the connection works

The connection has three parts:

| Piece                 | Lives in         | Purpose                                                                                                  |
| --------------------- | ---------------- | -------------------------------------------------------------------------------------------------------- |
| WordPress MCP Adapter | WordPress plugin | Adds the MCP endpoint that exposes registered WordPress abilities.                                       |
| Bricks abilities      | Bricks           | Registers Bricks actions with the WordPress Abilities API.                                               |
| Bricks skills         | AI client        | Adds optional Bricks workflow guidance for clients that support skills, rules, or reusable instructions. |

Bricks generates MCP config that runs `npx -y @automattic/mcp-wordpress-remote@latest` locally. That command connects the AI client to the WordPress MCP endpoint and authenticates with a WordPress application password.

Every request uses the WordPress user behind that application password. Bricks then checks that user's WordPress capabilities, builder access, and builder permissions before abilities can read or write.

## Setup

Use an administrator account for setup. Installing the adapter, activating it, saving settings, and creating credentials can require WordPress permissions such as `manage_options`, `install_plugins`, `activate_plugins`, and permission to edit the selected user account.

### 1. Enable Bricks abilities

Go to `Bricks > AI > Configuration`. Under `Enable Bricks abilities`, turn on the toggle and save your settings.

The WordPress Abilities API must be available. The screen recommends WordPress 6.9 or later if the API is missing. The toggle is also disabled when `BRICKS_DISABLE_MCP` is truthy. Remove that constant or set it to `false` to allow admin control.

You can enable abilities without installing or connecting the MCP Adapter. For a WP-CLI workflow, continue with [WP-CLI access](#wp-cli-access). To connect an MCP client, complete the remaining setup steps below.

### 2. Set up the MCP server

Under `Connect AI client to MCP`, use `Set up MCP server` to install or activate the WordPress MCP Adapter.

| MCP server status | Meaning | What to do |
| --- | --- | --- |
| `Not installed` | The adapter plugin is not installed. | Click `Install plugin`, or download the release ZIP through `View on GitHub`. |
| `Inactive` | The adapter is installed but not active. | Click `Activate plugin`, or activate it from `Plugins`. |
| `Connected` | The adapter is active and its REST route is registered. | Create a credential and connect your client. |
| `Route missing` | The adapter is loaded, but the MCP REST route did not register. | Check REST API routing, permalinks, plugin conflicts, and PHP error logs. |

If the one-click installer is unavailable, download `mcp-adapter.zip` from the [WordPress MCP Adapter releases](https://github.com/WordPress/mcp-adapter/releases) and upload it under `Plugins > Add New Plugin > Upload Plugin`.

Once connected, Bricks shows the MCP endpoint URL. It usually looks like this:

```text
https://example.com/wp-json/mcp/mcp-adapter-default-server
```

If pretty permalinks are unavailable, the endpoint can use the REST route format:

```text
https://example.com/?rest_route=/mcp/mcp-adapter-default-server
```

An MCP server connection makes enabled abilities accessible to an MCP client. It does not control whether Bricks can register abilities with WordPress.

### Optional: Enable PHP abilities {#optional-enable-php-execution}

PHP abilities cover two security-sensitive workflows: the `bricks/execute-php` ability runs one-off PHP without storing the submitted snippet, and authorized agents can write and sign persistent PHP in supported Bricks code fields. Both workflows use the same PHP opt-in and safeguards.

`bricks/execute-php` gives an agent access to the same WordPress and PHP runtime as the site, including functions and data that are not covered by a dedicated Bricks ability.

PHP abilities are disabled by default and cannot be enabled from wp-admin or a database setting. Define the constant in one of these PHP locations before Bricks evaluates the ability:

- `wp-config.php`, before the "That's all, stop editing" line
- A must-use plugin
- A plugin
- A child theme's `functions.php`

Do not edit the Bricks parent theme because theme updates overwrite those changes. Define the constant only once:

```php
define( 'BRICKS_ENABLE_PHP_ABILITIES', true );
```

In a child theme's `functions.php` or a plugin, use a guard to avoid redefining the constant:

```php
if ( ! defined( 'BRICKS_ENABLE_PHP_ABILITIES' ) ) {
	define( 'BRICKS_ENABLE_PHP_ABILITIES', true );
}
```

Use the boolean value `true`. Bricks 2.4 beta and release candidate builds used `BRICKS_ENABLE_EXECUTE_PHP_ABILITY`. Replace that constant with `BRICKS_ENABLE_PHP_ABILITIES` before updating. The old constant is not an alias and does not enable PHP abilities.

> **Use on trusted development environments**
>
> Enable PHP abilities only on a local, staging, or otherwise trusted development environment. Remove the constant or set it to `false` when they are no longer needed.

On a local or staging site, an agent can use this ability to:

- Inspect active plugins, theme and plugin versions, PHP extensions, WordPress configuration, registered hooks, scheduled events, and other runtime state.
- Reproduce a plugin or theme function with the site's actual data instead of reasoning from an error message alone.
- Read PHP-accessible files and logs, check paths and permissions, or inspect a plugin or child theme implementation.
- Make an explicitly approved file or data repair, then rerun the failing operation to verify the result.
- Run one-off maintenance, migration, or setup tasks without installing a permanent code-snippet plugin.

File access is limited by the permissions of the PHP process. The ability is not sandboxed, so it can also edit or delete files and data that PHP can access. Keep the site backed up and use version control when testing file changes.

Every PHP action must still meet all of these conditions:

- Bricks abilities are enabled, and `BRICKS_DISABLE_MCP` is not forcing them off.
- The request is authenticated with a WordPress application password.
- The application-password user has the WordPress `manage_options` capability.
- The application-password user has the Bricks `Execute code` capability.
- Bricks code execution is enabled under `Bricks > Settings > Custom code`.
- `BRICKS_LOCK_CODE_SIGNATURES` is not enabled. The signature lock overrides the PHP execution constant.

Persistent PHP is stored only when the agent is authorized to edit the target and the code can be signed. Bricks validates supported HTML and PHP Code field paths before accepting an update, so a field that normally accepts HTML cannot be used to bypass the PHP checks.

Keeping activation in PHP configuration means the ability cannot be enabled through a WordPress option or database setting alone. The permission and configuration checks above run again for every call.

To disable PHP abilities, remove the constant or change it to:

```php
define( 'BRICKS_ENABLE_PHP_ABILITIES', false );
```

The highlighted `bricks/execute-php` row appears first under `Bricks > AI > Abilities`. Select `View setup` to expand the configuration instructions inside the row. Its status shows whether `BRICKS_ENABLE_PHP_ABILITIES` is undefined, `true`, `false`, or invalid, without exposing an unexpected constant value. When the constant is `true`, a second status shows whether the ability is callable or blocked by another requirement.

### 3. Create a credential

Under `Connect AI client to MCP > Create a credential`, select the WordPress user the AI client should act as, enter a credential name, and click `Generate password`.

Use a name that identifies the client or workflow, for example `Codex staging`, `Claude local`, or `Cursor design review`.

Copy the generated application password before leaving the page. WordPress only shows it once.

For shared local or staging environments, create a dedicated WordPress user for the AI client instead of using your personal admin account. Give that user only the [builder access](https://academy.bricksbuilder.io/builder/interface/builder-access/) and WordPress capabilities it needs.

### 4. Connect your AI client

Under `Connect AI client to MCP`, choose the client you use. Bricks shows a config block, a command, or a prompt depending on the client.

Use `Paste config` when the client supports config files. It keeps the setup explicit and keeps credentials out of the chat prompt.

`Copy a prompt` asks the AI client to help install the MCP server using the same connection details. Use it only in a local or staging workflow, and only with a client you trust with the credential.

Bricks generates client-specific config for many tools. The examples below show the shape of that config, but use the values generated on your site. The generated config includes:

- `WP_API_URL`: the MCP endpoint URL.
- `WP_API_USERNAME`: the selected WordPress username.
- `WP_API_PASSWORD`: the generated application password.
- `NODE_TLS_REJECT_UNAUTHORIZED=0`, only when Bricks detects a local development HTTPS domain that likely uses a self-signed certificate.
- `npx -y @automattic/mcp-wordpress-remote@latest` as the local command that connects your AI client to WordPress.

Do not put the application password in the endpoint URL, command arguments, or global shell config. Keep it in the MCP server environment for that client.

**Codex**

Paste the generated block into `~/.codex/config.toml`, or merge it with your existing MCP server config:

```toml
[mcp_servers.example-com]
command = "npx"
args = ["-y", "@automattic/mcp-wordpress-remote@latest"]

[mcp_servers.example-com.env]
WP_API_URL = "https://example.com/wp-json/mcp/mcp-adapter-default-server"
WP_API_USERNAME = "mcp-service-user"
WP_API_PASSWORD = "xxxx xxxx xxxx xxxx"
```

Start a new Codex chat after saving the config so Codex reloads the MCP server.

**Claude Code**

Run the generated command in your terminal:

```bash
claude mcp add example-com \
  --env WP_API_URL='https://example.com/wp-json/mcp/mcp-adapter-default-server' \
  --env WP_API_USERNAME='mcp-service-user' \
  --env WP_API_PASSWORD='xxxx xxxx xxxx xxxx' \
  -- npx -y @automattic/mcp-wordpress-remote@latest
```

Start a new Claude Code chat after adding the server.

**Generic JSON**

Many clients use a JSON config shape like this:

```json
{
  "mcpServers": {
    "example-com": {
      "command": "npx",
      "args": ["-y", "@automattic/mcp-wordpress-remote@latest"],
      "env": {
        "WP_API_URL": "https://example.com/wp-json/mcp/mcp-adapter-default-server",
        "WP_API_USERNAME": "mcp-service-user",
        "WP_API_PASSWORD": "xxxx xxxx xxxx xxxx"
      }
    }
  }
}
```

Use the exact file path and wrapper key shown in `Bricks > AI`, because each client names its MCP config differently.

> **Local HTTPS**
>
> For local domains such as `.local`, `.test`, `.localhost`, `.ddev.site`, `localhost`, or `127.0.0.1`, Bricks may add `NODE_TLS_REJECT_UNAUTHORIZED=0` to the generated MCP server environment. Keep that setting scoped to this MCP server only. Do not set it globally.

### 5. Test the connection

Start a new chat in your AI client and ask:

```text
Call bricks-start-here, then bricks-get-mcp-version, then bricks-list-ability-status.
Tell me whether Bricks abilities are available, which Bricks version is connected, and whether any abilities are disabled.
```

If `bricks-start-here` is not visible as a direct tool, ask the client to call the MCP Adapter dispatcher:

```json
{
  "ability_name": "bricks/start-here",
  "parameters": {}
}
```

If the client cannot list Bricks abilities, fix the MCP connection before installing skills or trying a build task.

## Managing abilities

Open `Bricks > AI > Abilities` to control which Bricks abilities AI clients can use on this site.

> **User permissions still apply**
>
> The Abilities tab controls site-level availability. It does not grant permissions to the WordPress user behind the MCP connection. An ability can be enabled here and still not be callable for that user if they do not have the required WordPress capability, builder access, or Bricks builder permission.

### Scope abilities by user or role

Ability toggles are site-wide. Per-user and per-role access comes from the WordPress account used by the MCP connection:

1. Go to `Bricks > Settings > Builder access` and create a custom builder capability.
2. Enable only the actions that account needs, including the relevant post types and element editing permissions.
3. Assign the capability to a WordPress role or to one user from that user's WordPress profile.
4. In `Bricks > AI > Configuration`, generate the application password for that user and use it in the AI client's MCP config.

For example, a `Client editor` capability can allow content and element editing while leaving every permission under `Components` disabled. An AI client connected with that user's application password can edit the permitted content, but component abilities and component operations inside element writes are rejected.

WordPress capabilities still apply alongside Builder access. Avoid using an administrator account for a restricted client workflow because users with `manage_options` receive full builder access. See [Builder Access & Capabilities](https://academy.bricksbuilder.io/builder/interface/builder-access/) for every permission and the steps for assigning capabilities to roles and individual users.

You can:

- Search abilities by name or description.
- Filter by category, enabled state, disabled state, and default-off state.
- Enable all, disable all, or reset to defaults.
- Review badges such as `Default off` and `Destructive`.

Some diagnostic abilities are always available so clients and admins can understand the connection state:

- `bricks/start-here`
- `bricks/get-mcp-version`
- `bricks/list-ability-status`

Most abilities are enabled by default once Bricks abilities are enabled. Sensitive categories, such as builder permission management, are default-off until an admin enables them. Abilities marked destructive can remove data or make changes that are not easy to reverse, so treat them as actions that need clear user approval.

![](https://academy.bricksbuilder.io/assets/bricks-ai-abilities.png)

## Fast-path tools and dispatcher tools

Bricks registers many abilities, but only common abilities appear directly in an MCP client's tool list.

Direct MCP tool names use hyphens:

```text
bricks-get-design-context
bricks-get-page-elements
bricks-set-page-elements
```

Ability names use slashes:

```text
bricks/get-design-context
bricks/get-page-elements
bricks/set-page-elements
```

If a Bricks ability is not visible as a direct tool, call it through the MCP Adapter dispatcher:

```json
{
  "ability_name": "bricks/get-mcp-version",
  "parameters": {}
}
```

Use `bricks-list-ability-status` to see which abilities are enabled, which are disabled, and which are default-off.

### Add a direct tool

If your integration frequently calls an ability through the dispatcher, you can expose it as a direct tool on the default MCP server. Add this filter to a custom plugin or your child theme's `functions.php`:

```php
add_filter( 'bricks/abilities/named_tools', function( $tools ) {
    $tools[] = 'bricks/get-element-schema';

    return $tools;
} );
```

Use slash-separated ability names. Bricks removes duplicates, disabled abilities, and unregistered names once the ability registry is available. Reconnect your MCP client or refresh its tools after changing the list.

This changes tool discovery only. Removing a direct tool does not disable its ability: it remains callable through the dispatcher. Use **Bricks > AI > Abilities** to disable an ability. User permissions still apply.

## Code authoring and HTML/CSS imports

Agents can create and edit Bricks content through the same permissions that apply in the builder. An agent does not receive PHP access merely because it can edit HTML, CSS, or JavaScript.

- HTML authoring requires permission to edit the target and its content settings.
- CSS authoring follows the target resource and style-editing permissions, such as access to the Class Manager and permission to edit global classes.
- JavaScript authoring requires permission to edit the target and the WordPress `unfiltered_html` capability.
- PHP authoring and signing require the PHP abilities opt-in and every safeguard listed above, including `manage_options`, Bricks **Execute code**, enabled code execution, application-password authentication, and unlocked code signatures.

Code elements retain their existing **Execute code** permission, global execution setting, and PHP/HTML signing requirements. These abilities do not change how Code elements render or how the builder authorizes them. Writing the signed PHP/HTML field in execution mode uses the PHP abilities safeguards, including when that field contains only HTML.

When an agent imports HTML or CSS, Bricks checks the imported structure and its permissions. Content the connected user is not allowed to create is omitted automatically. A one-call import can apply the retained content and returns a prominent partial result with the omitted elements and the reason for each omission. An explicit preview is also available before applying an import.

Bricks rejects an import when the retained tree is empty or invalid. It also rejects a nonempty replacement when any source content was omitted or invalid, because it could remove existing content incompletely. Review the reported omissions, adjust the source or permissions, and run the import again.

## Settings Abilities and Remote Libraries

The settings abilities use an allow-list rather than exposing the entire `bricks_global_settings` option:

- `bricks/list-settings-schema` lists supported keys and their value types.
- `bricks/get-global-settings` reads allowed settings.
- `bricks/set-global-settings` updates only the keys sent in the request.
- `bricks/list-credential-status` reports whether known credentials are configured without returning their values.

The Remote Templates and Remote Components settings use these keys:

| Setting key | Ability behavior |
| --- | --- |
| `myTemplatesAccess` | Readable and writable boolean for exposing this site's templates. |
| `myComponentsAccess` | Readable and writable boolean for exposing this site's components. |
| `myTemplatesWhitelist` | Readable and writable newline-separated URL whitelist shared by templates and components. Its stored key keeps the older name for compatibility. |
| `remoteTemplates` | Reads and writes remote-library URLs and optional display names. Stored passwords are preserved but never returned or written through the abilities. |
| `myTemplatesPassword` | Excluded from settings reads and writes. `bricks/list-credential-status` reports only whether the shared **Remote access password** is configured and identifies it as used by remote template and component access. |

The `myTemplatesPassword` key also keeps its older internal name for compatibility. AI and MCP clients cannot read, replace, or clear the password. Manage it in **Bricks > Settings > Templates & components > Remote access**.

## Installing Bricks skills

Skills are optional. Get the MCP connection working first.

Open `Bricks > AI > Skills` and copy the install prompt. Paste it into the AI client you want to use. The prompt points the client to the [Bricks skills repository](https://github.com/codeerhq/bricks-skills), asks it to install the matching skills or rules format, and asks it to report which Bricks skills were installed.

Then copy the verification prompt from the same tab. Start a new chat and ask the client to list loaded Bricks skills.

If no Bricks skills are loaded, the MCP connection can still work. The client can call `bricks-start-here` at the beginning of a session to get the core Bricks workflow rules, fast-path tool names, and dispatcher example.

Skills help with workflows such as:

- Designing or auditing a design system.
- Creating pages and templates.
- Working with [query loops](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) and [dynamic data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/).
- Writing element conditions and interactions.
- Converting HTML and CSS into Bricks element data.
- Verifying frontend output with screenshots or browser automation.

## WP-CLI access

Bricks abilities are registered with the WordPress Abilities API, so they are not limited to MCP clients.

For developer checks, WP-CLI can access the same registered abilities from the command line. The WordPress Developer Resources page for [`wp ability`](https://developer.wordpress.org/cli/commands/ability/) describes it as the command for abilities registered through the WordPress Abilities API.

Useful checks:

```bash
wp ability list --namespace=bricks --user=admin
wp ability get bricks/get-mcp-version --user=admin
wp ability run bricks/get-mcp-version --user=admin
wp ability run bricks/list-ability-status --user=admin --format=json
```

Use `--user` so permission checks run in the same WordPress user context your MCP connection would use.

This is separate from the Bricks-specific `wp bricks ...` commands, and it is not required for the MCP setup above. It is a WordPress Abilities API surface for any registered ability, including abilities from Bricks and other plugins.

## Security model

Treat an MCP-connected AI client like a real WordPress user.

- Each call runs as the authenticated WordPress user, for example the application-password user or the `--user` passed to WP-CLI.
- Bricks checks WordPress capabilities, builder access, and Bricks builder permissions before abilities can read or write.
- The Abilities tab controls which Bricks abilities are available on the site.
- `BRICKS_DISABLE_MCP` in `wp-config.php` prevents Bricks from registering abilities, including for WP-CLI use.
- PHP execution and persistent PHP authoring share a strict boolean opt-in in PHP configuration. Each action rechecks application-password authentication, `manage_options`, Bricks **Execute code**, enabled code execution, and the code-signature lock.
- Application passwords can be revoked from the selected user's WordPress profile.
- Post and template element writes create Bricks [revisions](https://academy.bricksbuilder.io/builder/interface/revisions/) where supported. Global data writes, such as classes, variables, theme styles, and components, are not covered by post revisions.

Recommended defaults:

- Use local or staging for first tests.
- Use a dedicated WordPress user for the AI client in shared testing environments.
- Disable abilities that are not needed for the workflow.
- Review destructive actions before approving them in the AI client.
- Revoke old application passwords.

## Troubleshooting

| Symptom                                                    | Likely cause                                                               | What to do                                                                                                                                    |
| ---------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| The Bricks abilities toggle is disabled | The WordPress Abilities API is unavailable, or `BRICKS_DISABLE_MCP` is truthy | Use WordPress 6.9 or later if the API is missing, or remove the constant/set it to `false`. A connected MCP Adapter is not required to enable abilities. |
| `MCP server enabled but endpoint did not register`         | The adapter loaded, but the REST route is missing                          | Check `/wp-json/`, permalink settings, plugin conflicts, and PHP error logs.                                                                  |
| The client cannot connect                                  | Wrong endpoint, wrong credential, or the client did not reload config      | Confirm the endpoint in `Bricks > AI`, regenerate or re-copy the application password, then start a new chat.                                 |
| Application passwords are unavailable on a local HTTP site | WordPress enables application passwords by default only over HTTPS or when the environment type is `local` | Use HTTPS when possible. For a local HTTP site, add `define( 'WP_ENVIRONMENT_TYPE', 'local' );` to `wp-config.php`.                            |
| Application passwords are unavailable for one user         | A security plugin, filter, or user-level restriction disabled application passwords | Check the selected user, security plugins, and filters that control WordPress application password availability.                              |
| The client only shows `mcp-adapter-*` tools                | Bricks direct tools are not loaded or the ability is outside the fast path | Use `mcp-adapter-discover-abilities`, call long-tail abilities through `mcp-adapter-execute-ability`, and check `bricks-list-ability-status`. |
| A Bricks ability returns disabled                          | The ability is off in `Bricks > AI > Abilities`                            | Enable the ability or reset abilities to defaults.                                                                                            |
| `bricks/execute-php` is unavailable                        | `BRICKS_ENABLE_PHP_ABILITIES` is missing, a required permission is missing, code execution is disabled, or code signatures are locked | Open `Bricks > AI > Abilities`, select `View setup` for `bricks/execute-php`, and follow the blocked requirement shown there. |
| Local HTTPS fails                                          | The local certificate is not trusted by the local `npx` process            | Use the scoped `NODE_TLS_REJECT_UNAUTHORIZED=0` generated by Bricks for local development, or trust the local certificate.                    |
| The AI client keeps asking for approval on every tool call | The client has per-tool approval settings                                  | Approve the Bricks MCP server or adjust that client's MCP approval settings if you trust the workflow.                                        |

### Upload or conversion exceeds a size limit

If an ability rejects a file or HTML/CSS input as too large, reduce its size before retrying. Bricks uses these defaults unless a site customization changes them:

| Operation | Default limit |
| --- | --- |
| Media upload (`bricks/upload-media`) | The site's WordPress upload limit; remote downloads have a 30-second timeout |
| Font upload (`bricks/upload-custom-font-file`) | 8 MiB per decoded font file |
| SVG icon upload (`bricks/upload-custom-icon`) | 1 MiB of SVG markup |
| HTML/CSS conversion (`bricks/convert-html-css-to-bricks-data`) | 2 MiB of combined HTML and CSS, including CSS-only input |

1 MiB is 1,048,576 bytes. Base64 encoding makes an upload request larger than the file itself. If the request fails before Bricks returns an error, check your hosting, proxy, and MCP client's request limits as well.

## Example prompts

Start with explicit instructions. Ask the client to inspect the site before writing.

```text
You are connected to a Bricks site through MCP.
Call bricks-start-here, then inspect the design system and the current page before making changes.
Do not create duplicate global classes or variables.
Preview or read back your changes before reporting that the task is done.
```

Build a first pass of a page:

```text
Create an About page for this Bricks site. Use the existing design system, keep the style consistent with the homepage, and show me the plan before saving.
```

Replace static content with dynamic data:

```text
Find the static listing cards on the homepage and replace them with a query loop that pulls the Listing post type. Use the existing card styling.
```

Audit before changing:

```text
Audit the site's global classes, variables, and templates for naming drift or duplicated patterns. Show me the report first. Do not change anything yet.
```

---

# An Intro To Templates

Source: https://academy.bricksbuilder.io/builder/features/an-intro-to-templates/

*Learn how Bricks templates work, which template types are available, and how conditions determine where each template is rendered.*

Templates are reusable Bricks layouts that can render in specific parts of your site. They are different from ordinary pages because Bricks can choose them automatically for the current request: the site header, site footer, blog posts, archives, search results, error pages, popups, password gates, and WooCommerce routes.

A template can be a small reusable section, a global header or footer, or the full main layout for a page type. The most common starting set is:

- A **Header** template for the site header.
- A **Footer** template for the site footer.
- A **Single** template for blog posts or another post type.
- An **Archive** template for archive views.

Templates are also used by the Template Library, remote template sources, the Template element, popups, WooCommerce layouts, and password protection.

https://www.youtube.com/watch?v=x0hHUXzk3wg

## The template mental model

Bricks separates a rendered page into template areas:

- **Header:** the active header template.
- **Content:** the active content template, such as a Single, Archive, Search Results, Error Page, Password Protection, or WooCommerce template.
- **Footer:** the active footer template.
- **Popups:** matching popup templates that are loaded for the current page.

When a visitor opens a frontend URL, Bricks checks the current WordPress context. For example, it can detect a single post, the front page, a search results page, an author archive, a category archive, a 404 page, or a WooCommerce route. Bricks then looks through published templates and picks the most suitable template for each area.

That choice is controlled by:

1. The template type.
2. The template conditions.
3. Whether the template is published.
4. Whether default templates are enabled.
5. Page settings such as **Disable header** and **Disable footer**.

## Template type

Every template should have a template type. The type tells Bricks what kind of layout the template is and which settings or elements should be available while editing it.

| Template type | Use it for | Notes |
| --- | --- | --- |
| Header | Site header layouts | Can be used by default when published. Has Header settings. |
| Footer | Site footer layouts | Can be used by default when published. |
| Single | Single posts, pages, or custom post type entries | Needs conditions for predictable frontend use. |
| Section | Reusable sections, hook-injected sections, or templates inserted manually | Inserted copies do not stay synced. Use Components for linked reusable structures. |
| Popup | Popup layouts | Rendered through popup conditions/interactions or through the Template element. |
| Archive | Blog, author, date, post type, taxonomy, and term archives | Can be used by default for archive contexts. |
| Search Results | Native search results pages | Can use Search Criteria settings. |
| Error Page | 404 pages | Can be used by default for error contexts. |
| Password Protection | Password gate templates | Available only when password protection is enabled. |
| WooCommerce templates | Product, product archive, cart, checkout, account, thank-you, and related routes | Visible when WooCommerce is active. Product archive and single product templates can use conditions; the other WooCommerce route templates render automatically on their route. |

## Template conditions {#template-conditions}

Template conditions determine where a template applies.

Open a template in Bricks, click the **Settings** icon, then go to **Template Settings > Conditions**.

![](https://academy.bricksbuilder.io/assets/docs-template-conditions-builder-1024x782.png)

<figcaption>

Template Conditions are located under Settings > Template Settings

</figcaption>

Condition types include:

- **Entire website:** broad condition for the whole site.
- **Front page:** the page configured as the WordPress front page.
- **Post type:** posts, pages, products, or custom post types.
- **Archive:** all archives, post type archives, author archives, date archives, or term archives.
- **Search results:** native WordPress search results.
- **Error page:** the 404 page.
- **Terms:** single entries assigned to selected terms.
- **Individual:** selected posts, pages, custom post type entries, or child pages.

Conditions can be broad or specific. A header with **Entire website** can cover the whole site. A Single template with **Post type: Posts** can cover every blog post. Another Single template with **Individual: About Us** can target only one page.

## How Bricks chooses between matching templates

More than one template can match the same page. Bricks scores matching conditions and uses the highest-scoring match.

In practical terms:

- **Individual** conditions are the most specific.
- **Front page** is more specific than a general post type match.
- **Term**, selected archive, and child-page matches are more specific than broad archive or post type matches.
- **Post type** is more specific than **Entire website**.
- **Entire website** is a broad fallback.
- **Exclude** conditions can disqualify a template when the excluded context matches.

If two templates target the same area with similar conditions, make the intended winner more specific or remove the competing condition. Avoid relying on template creation order as your template strategy.

## Include and exclude conditions

Each condition can be an include condition or an exclude condition.

Use include conditions to say where the template should render. Use exclude conditions to remove specific areas from a broad rule.

Example:

1. Header template condition: **Entire website**
2. Header template exclude condition: **Individual > Landing Page**

The header renders across the site except on the selected landing page.

For terms and individual entries, Bricks also supports child matching. You can apply a condition to child terms or child pages when the relationship should inherit the same template behavior.

## Default templates

Bricks can use some published templates even when no conditions are set. This is controlled by **Bricks > Settings > Templates & components > Disable default templates**.

When default templates are enabled, Bricks can use published templates of supported types as fallbacks. This commonly affects headers and footers, and also applies to supported archive, search, error, and WooCommerce route templates.

When default templates are disabled, templates need matching conditions or route-specific WooCommerce behavior to render on the frontend.

For production sites, explicit conditions are usually easier to audit and maintain.

## Preview content is not a condition

Template editing often needs a preview context. A Single template needs a real post to show post title, content, featured image, and other dynamic data. An Archive template needs an archive context. A Search Results template needs a search term.

Use **Template Settings > Populate Content** to choose what Bricks shows on the canvas while editing.

Populate Content does not decide where the template renders on the frontend. Conditions do that.

## Page settings can still affect templates

A page rendered through a template can still disable its header or footer.

Open the page, go to **Settings > Page Settings > General**, and use **Disable header** or **Disable footer**. This is useful for landing pages, splash pages, checkout-style flows, or isolated campaign pages.

This does not delete the header or footer template. It only disables that template area for the current page.

## Pre-Designed Templates {#community-templates}

Browse Bricks' built-in Wireframes and Design sets right from within the builder.

Access pre-designed templates by clicking the folder icon in the builder's top toolbar. Then, under **Source**, select **Wireframes**, **Design sets**, or a configured remote site.

Insert the template of your choice with a single click and tweak it from there.

> **Note**
>
> **TIP:** When you start with Bricks, inspecting a template is a great way to learn how a certain layout is structured.

## My Templates {#my-templates}

You can view, create, import, and export your own templates by clicking the Templates (folder) icon in the builder toolbar or directly from the WordPress dashboard:

![](https://academy.bricksbuilder.io/assets/docs-my-templates-wp-dashboard-1024x861.png)

<figcaption>

My Templates in WordPress Dashboard

</figcaption>

The dashboard view shows template type, template conditions, template bundles, template tags, and the featured image used as the template screenshot.

## Inject Section templates via hooks {#hook}

Section templates can be injected at a WordPress action hook.

When editing a Section template, add a condition and enter the action hook name under **Hook: Name**. You can also set **Hook: Priority**. Bricks evaluates the condition first, then renders the section when that hook runs.

For example, a Section template with condition **Entire website** and hook name `bricks_before_header` renders at that hook across the site.

![](https://academy.bricksbuilder.io/assets/bricks-1.9.2-section-template-condition-hook-name.png)

<figcaption>

Section template rendered at the `bricks_before_header` hook

</figcaption>

> **Note**
>
> Templates with a hook name are injected on the actual frontend.

## Template Types {#template-types}

Use the table below as a quick reference when choosing a template type.

| Template type | Description | Default or route behavior |
| --- | --- | --- |
| Header | Site header area | Can be used by default. |
| Footer | Site footer area | Can be used by default. |
| Single | Main layout for posts, pages, or CPT entries | Needs conditions for predictable use. |
| Section | Reusable section or hook-injected layout | Render manually, insert into content, or inject through hooks. |
| Popup | Popup layout | Loaded through popup conditions/interactions or Template element usage. |
| Archive | Blog, author, date, post type, taxonomy, and term archives | Can be used by default for archive contexts. |
| Search Results | Native search results page | Can be used by default for search results. |
| Error Page | 404 page | Can be used by default for error pages. |
| Password Protection | Password gate template | Available when password protection is enabled. |
| WooCommerce - Product archive | Shop, product category, product tag, and product attribute archives | Uses WooCommerce archive routing and can use conditions. |
| WooCommerce - Single product | Single product pages | Uses WooCommerce product routing and can use conditions. |
| WooCommerce - Cart | Cart page with items | Automatically rendered on the cart route when the cart has items. |
| WooCommerce - Empty cart | Empty cart page state | Automatically rendered on the cart route when the cart is empty. |
| WooCommerce - Checkout | Checkout page | Automatically rendered on the checkout route. |
| WooCommerce - Pay | Order payment page | Automatically rendered on the order-pay route. |
| WooCommerce - Thank you | Post-checkout thank-you page | Automatically rendered on the order-received route. |
| WooCommerce - Order receipt | Order receipt page | Automatically rendered on the matching WooCommerce route. |
| WooCommerce - Account - Login | Account login form | Automatically rendered on the matching account route. |
| WooCommerce - Account - Lost password | Lost password form | Automatically rendered on the matching account route. |
| WooCommerce - Account - Lost password (Confirmation) | Lost password confirmation | Automatically rendered on the matching account route. |
| WooCommerce - Account - Reset password | Reset password form | Automatically rendered on the matching account route. |
| WooCommerce - Account - Dashboard | Account dashboard | Automatically rendered on the matching account route. |
| WooCommerce - Account - Orders | Account orders | Automatically rendered on the matching account route. |
| WooCommerce - Account - View order | Account view-order endpoint | Automatically rendered on the matching account route. |
| WooCommerce - Account - Downloads | Account downloads | Automatically rendered on the matching account route. |
| WooCommerce - Account - Addresses | Account addresses | Automatically rendered on the matching account route. |
| WooCommerce - Account - Edit address | Account edit-address endpoint | Automatically rendered on the matching account route. |
| WooCommerce - Account - Edit account | Account edit-account endpoint | Automatically rendered on the matching account route. |
| WooCommerce - Account - Payment methods | Account payment methods | Automatically rendered on the matching account route. |
| WooCommerce - Account - Add Payment method | Account add-payment-method endpoint | Automatically rendered on the matching account route. |

> **Note**
>
> Section templates do not sync inserted copies between pages. If you need linked reusable structures, use [Components](https://academy.bricksbuilder.io/builder/features/components/).

## Template Bundles & Template Tags {#bundles}

These two Bricks template taxonomies can be used to organize and group your templates together. They are 100% optional.

For example, Bricks template sources can use **Template Bundles** to group individual templates of the same website design together. Feel free to use template bundles in any other way.

**Template Tags** are simple tags. The "My Templates" screenshot above uses template tags such as "Dark" and "Light". Again, they are completely optional but often very useful. Especially as your template library grows over time.

## Troubleshooting template assignment

**Nothing renders:** Confirm the template is published, has the correct type, and has matching conditions. If it has no conditions, check whether default templates are disabled.

**The wrong layout renders:** Look for another template with a more specific condition. Individual, front page, selected term, and selected archive conditions can outrank broader conditions.

**A header or footer is missing only on one page:** Check that page's **Page Settings > General** for **Disable header** or **Disable footer**.

**The builder preview looks unrelated to the frontend:** Adjust **Populate Content**. Preview content controls the editing canvas, not the frontend assignment.

**WooCommerce conditions are missing:** Product archive and single product templates can use conditions. Other WooCommerce route templates, such as cart, checkout, thank-you, and account templates, render automatically on the correct WooCommerce page, so Bricks hides normal Conditions and Populate Content controls for those types.

---

# Builder Browser

Source: https://academy.bricksbuilder.io/builder/features/builder-browser/

*Use the Builder Browser to browse and manage templates, components, posts, pages, media, and builder managers from one popup.*

The **Builder Browser**, introduced in Bricks 2.4, is the folder popup in the builder toolbar. It brings templates, components, public post types, media, and builder managers into one browser-style popup.

Use it when you want to insert a template, manage components, jump to another page or post, inspect media, or open a related manager without leaving the builder.

https://www.youtube.com/watch?v=f9LH7xihkc0

## Open the Builder Browser

Click the folder icon in the builder toolbar.

You can also use these keyboard shortcuts:

- `CMD / CTRL + SHIFT + .` toggles the Builder Browser.
- `CMD / CTRL + SHIFT + L` opens the Browser directly on the Templates view when your user has template access.

The **Manage: Browser** action is also available from the [Command Palette](https://academy.bricksbuilder.io/builder/interface/command-palette/).

The Browser remembers the last section you opened for your user account. If that section is still available, Bricks opens it again the next time you open the Browser.

Use the expand icon in the upper-right corner to switch to full-screen mode. Bricks remembers the full-screen setting in your browser.

## What appears in the sidebar

The sidebar can show:

- **Templates**, when your builder role can create, edit, or insert templates.
- **Components**, when your builder role can insert, edit, or import/export components.
- Public registered post types, including pages, posts, custom post types, and Media.
- **Style Manager**, when your user has Style Manager access.
- **Font Manager**, **Icon Manager**, and **Query Manager**, when your builder role has access to those managers.

Templates, Components, and Managers use your [builder permissions](https://academy.bricksbuilder.io/builder/interface/builder-access/). Post-type sections come from the public post types registered on the site. Builder support and post-type permissions determine whether an item shows the **Edit with Bricks** action.

## Templates

The Templates view replaces the older standalone Template Library popup.

It lets you browse these template sources:

- **My Templates**
- **Wireframes**
- **Design sets**
- Configured **Remote sites**

You can search templates, switch between grid and list view, filter by source, bundle, tag, and type, and use the available template actions.

Available actions depend on the selected source and your builder permissions:

- **Create template**
- **Save as template**
- **Import template** from JSON or ZIP files
- **Import to templates**, for saving a non-local template under My Templates
- **Generate screenshots**, for local My Templates when screenshot generation is enabled
- **Reload**, for remote template sources
- **Insert**, **edit**, **export**, **delete**, and **preview** on individual templates

The Templates view also includes **Import images** and **Replace content** controls.

**Import images** downloads template images into the Media Library when inserting or importing template data. If disabled, Bricks uses placeholder images.

**Replace content** replaces the current canvas with the inserted template. If disabled, Bricks inserts the template into the existing content.

When a template import contains related data, Bricks may ask you to review imported theme styles, color palettes, global variables, global classes, or Style Manager settings before the template is inserted.

![](https://academy.bricksbuilder.io/assets/bricks-browser-template-manager.webp)

Learn more about template sources in [Template Library](https://academy.bricksbuilder.io/builder/features/template-library/) and [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/).

## Components

The Components view gives you a Component Manager inside the Browser.

You can:

- Switch between **My components** and configured remote sites under **Source**.
- Search components.
- Filter by category.
- Filter by usage: all usage, used on current page, used elsewhere, or unused.
- Switch between grid and list view.
- Import component JSON or ZIP files.
- Edit, duplicate, export, delete, or generate a screenshot for a component.
- Generate screenshots for the currently filtered component list.

When a remote site is selected, the manager shows the remote catalog instead of local usage filters and editing actions. Use **Refresh** to request the catalog again and **Load more** when another page is available. Importing a remote component opens a review for nested components, global classes, global variables, and color palettes before anything is saved locally.

Save pending component, class, variable, and color changes before starting a remote import. Bricks returns to **My components** and refreshes the imported design-system data after a successful import.

Component screenshots are generated from a standalone component preview and saved as component thumbnail metadata. Generating screenshots requires the **Edit components** builder permission.

The usage badge shows component instances as `Instances: current page / total`. For example, `Instances: 2/5` means the component is used twice on the page you are editing and five times across the site. The **Used elsewhere** filter only shows components that are not used on the current page but are used on another page or template.

Click the usage badge to see current-page instances and other pages where the component is used. Current-page items take you to the matching instance in the builder. Other-page items open the matching page or template in Bricks in a new browser tab.

![](https://academy.bricksbuilder.io/assets/bricks-browser-component-manager.webp)

For the local component workflow, see [Components](https://academy.bricksbuilder.io/builder/features/components/).

## Posts, pages, and custom post types

The Browser lists public registered post types from the current WordPress site. Select a post type to browse its content. A post type can appear here even when it is not enabled for editing with Bricks.

For regular post types, you can:

- Search entries.
- Create a new item from the search field when your role can edit posts and access that post type in the builder.
- Filter by post status.
- Sort by newest, oldest, title A-Z, title Z-A, or recently edited.
- Switch between grid and list view.
- Edit with Bricks, edit in WordPress, duplicate, or view the item when the action is available.

**Edit with Bricks** appears only when the post type is enabled for Bricks and the user has builder access to that post type. The other available actions depend on the item and the user's WordPress capabilities.

The post type settings button lets you set **Posts per page** and toggle visible metadata such as author and date.

By default, regular post types use the WordPress **posts per page** value. If that value is missing, Bricks falls back to `10`. You can override the Browser value per post type, from `1` to `100`.

### Organize posts and pages with folders

In Bricks 2.4, Browser folders also work with posts, pages, and custom post types when a compatible folder integration supports that post type. The included HappyFiles integration uses the folders already configured in HappyFiles.

Enable the relevant post type in HappyFiles and give your user folder access. Open that post type in the Browser to browse its folders and uncategorized items. Drag an item or a selection into a folder to assign it.

Assigning existing items requires full folder access in HappyFiles, permission to edit that post type, and permission to edit each selected item. Folder management also requires full folder access. If a post type has no folders in the Browser, check that it is enabled in HappyFiles and that your user has access.

## Media

The Media view is a media-management workspace for attachments in the WordPress Media Library.

You can:

- Search attachment IDs, file names, titles, captions, descriptions, and alternative text.
- Filter by media type, MIME subtype, uploader, attachment status, upload date, dimensions, file size, missing alternative text, and Media Health status.
- Upload local files or import public files from URLs.
- Switch between grid, masonry, and list views.
- Inspect files and edit attachment metadata.
- Select files across result pages for bulk metadata, download, folder, image-size, and deletion actions.
- Audit common accessibility and file problems with Media Health.
- Organize files with folders when a compatible media-folder integration is active.

The Bricks Media Browser is also the default picker for Image, Image Gallery, Video, Audio, SVG, and File controls. Change the picker under **Bricks > Settings > Builder > Media** if you prefer the standard WordPress Media Library interface. Both interfaces use the same WordPress attachments.

Media defaults to `50` items per page. The settings popover lets you change the pagination between `1` and `100` and choose whether attachment details open beside the results or in an overlay.

## Managers

The Managers section gives quick access to builder-wide managers when your user has permission:

- **Style Manager**
- **Font Manager**
- **Icon Manager**
- **Query Manager**

The Style Manager opens its dedicated popup. Font Manager, Icon Manager, and Query Manager open inside the Browser content area.

For reusable queries, see [Global Queries](https://academy.bricksbuilder.io/builder/dynamic-content/global-queries-query-manager/).

## Troubleshooting

### A Template, Component, or Manager Section Is Missing

Check the user's [builder permissions](https://academy.bricksbuilder.io/builder/interface/builder-access/). Templates, Components, Font Manager, Icon Manager, and Query Manager are permission-gated.

### A Post Type Is Missing

The Browser lists public registered post types by default. Check how the post type is registered. Developers can change the registry query with the [`bricks/registered_post_types_args`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-registered_post_types_args/) filter.

### Edit With Bricks Is Missing

Enable the post type under **Bricks > Settings > General > Post types** and confirm that the user's builder capability allows access to that post type.

### The Create Button Does Not Appear

The create action appears only for regular post types when the search field has a value, the user can edit posts, and the user has builder access for that post type. It is not available for Media.

### Template Images Do Not Import

Enable **Import images** before inserting or importing the template. When disabled, Bricks uses placeholder images instead of downloading template images into the Media Library.

### Inserted template replaced the page

Check **Replace content**. When enabled, Bricks replaces the current canvas with the inserted template data. When disabled, Bricks inserts the template into the existing content.

---

# Recovering a compromised Bricks or WordPress site

Source: https://academy.bricksbuilder.io/builder/features/bricks-rce/

*Inspect, clean, and recover a Bricks or WordPress site after a suspected compromise.*

This article was originally published after the February 2024 Bricks security incident. That incident has passed, but the recovery workflow below remains useful for any Bricks or WordPress site that may have been compromised.

The specific February 2024 Bricks RCE vulnerability was addressed in **Bricks 1.9.6.1**, released on February 13, 2024. Sites running Bricks 1.9.6.1 or later are not affected by that specific vulnerability. However, updating Bricks does not automatically clean a site that was already compromised before the update.

> **Note**
>
> If you suspect a site is compromised, update Bricks, WordPress, plugins, and themes to their latest versions, preserve evidence, and involve your host or a security professional when you are unsure.

## Before you start

These are general recovery steps. The right cleanup path depends on your hosting environment, backups, plugins, custom code, and the type of compromise.

Work from a recent backup or a cloned copy whenever possible. Keep notes of what you find, including suspicious users, files, redirects, cron jobs, changed credentials, and timestamps.

## Immediate containment

1. **Take a fresh backup:** Before changing anything, capture the current files and database so your host or security team can review evidence if needed.
2. **Restrict public traffic:** If the site appears actively compromised, temporarily restrict access using your host's tools, maintenance mode, firewall rules, or IP allowlisting.
3. **Update everything:** Update Bricks, WordPress core, plugins, and themes to their latest versions.
4. **Disable suspicious access:** Remove unknown administrator accounts, revoke unfamiliar API keys, and disable plugins or custom code you do not recognize.
5. **Contact your host:** Ask your hosting provider to check server logs, malware scans, file changes, outgoing mail, and suspicious processes.

### Restrict public traffic while cleaning {#block-incoming-traffic}

If you must clean the live site instead of a local or staging copy, keep public access restricted until the cleaned site is deployed and checked. Prefer your host's maintenance mode, firewall controls, password protection, or temporary IP allowlist.

On Apache hosts, one possible temporary `.htaccess` restriction is:

```apache
Order Deny,Allow
Deny from all
Allow from YOUR_IP_ADDRESS
```

Replace `YOUR_IP_ADDRESS` with your public IP address. Remove the rule when the site is clean and ready to reopen. If you are unsure which method fits your host, ask the hosting provider before editing server rules.

## Check for signs of compromise {#check}

Review the site carefully before deciding that it is clean.

1. **Review user accounts**
  - Go to `Users` in the WordPress dashboard.
  - Look for accounts you do not recognize, especially users with the `Administrator` role.
  - Check recent profile changes and reset passwords for all trusted administrators.
2. **Inspect themes and plugins**
  - Go to `Appearance > Themes` and `Plugins`.
  - Remove anything you did not install or no longer need.
  - Reinstall trusted themes and plugins from clean sources instead of keeping possibly modified files.
3. **Examine server files**
  - Use your host's file manager, SFTP, SSH, or a local copy of the site files.
  - Look for unfamiliar PHP files, random file names, recently modified files, and executable files in upload directories.
  - On SSH, a command such as `find . -type f -mtime -14` can help list files changed in the last 14 days. Adjust the time window to match the suspected incident.
4. **Review redirects and server rules**
  - Check `.htaccess`, web server redirects, CDN redirects, firewall rules, and any redirect plugins.
  - Look for rules that send visitors to unfamiliar domains or only affect certain user agents.
5. **Check cron jobs and scheduled tasks**
  - Review host-level cron jobs in your hosting control panel.
  - Review WordPress cron events with a trusted tool such as [WP Crontrol](https://wordpress.org/plugins/wp-crontrol/).
  - Remove unknown recurring tasks.
6. **Review posts, pages, and templates**
  - Check posts, pages, custom post types, Bricks templates, reusable content, and custom code areas.
  - Look for injected scripts, unfamiliar links, hidden content, or changed embeds.
7. **Review logs and performance anomalies**
  - Ask your host for access logs, error logs, and malware scan results.
  - Look for unusual login attempts, unexpected CPU usage, outgoing mail spikes, 500 errors, or repeated requests to suspicious files.

## Clean the site {#fix}

If you find evidence of compromise, clean from a trusted environment instead of editing a live, actively compromised site.

1. **Restore or rebuild from a clean point**
  - Restore a backup from before the compromise, or rebuild the site from clean WordPress, plugin, theme, and Bricks files.
  - If you are not sure which backup is clean, restore locally and repeat the checks above before deploying it.
2. **Reinstall WordPress core**
  - In the dashboard, use `Dashboard > Updates > Re-install version` where available.
  - Or reinstall WordPress core files from a clean WordPress download.
3. **Reinstall plugins and themes**
  - Update or reinstall every plugin and theme from trusted sources.
  - For premium plugins and themes, download clean copies from the vendor.
  - Remove abandoned or unnecessary plugins.
4. **Update Bricks**
  - Update Bricks to the latest available version through `Dashboard > Updates` or your Bricks account workflow.
  - Do not restore an old Bricks version as part of cleanup.
5. **Rotate secrets and credentials**
  - Change WordPress administrator passwords.
  - Change hosting, SFTP, SSH, database, email, SMTP, payment, and API credentials.
  - Generate new WordPress authentication salts using the [WordPress secret-key generator](https://api.wordpress.org/secret-key/1.1/salt/).
  - Replace exposed license keys or ask vendors to rotate them when needed.
6. **Replace `wp-config.php` if needed**
  - If you suspect file tampering, create a fresh `wp-config.php` from a clean `wp-config-sample.php`.
  - Re-enter database details and any required custom settings manually.
7. **Check permissions**
  - Confirm your file and folder permissions match your host's recommendations.
  - Common defaults are `755` for directories and `644` for files, but managed hosts may use different settings.
8. **Deploy the clean site**
  - Move the cleaned local or staging site back to production.
  - Keep public access restricted until the cleaned site is live, updated, and checked again.

## After cleanup

Continue monitoring the site after it is back online.

- Run a server-level malware scan through your host.
- Run an application-level scan with a trusted WordPress security plugin if appropriate.
- Review new user registrations and administrator accounts.
- Watch error logs, redirects, outgoing mail, and performance.
- Keep Bricks, WordPress, plugins, and themes updated.
- Schedule regular off-site backups.
- Review the [WordPress Hardening Guide](https://developer.wordpress.org/advanced-administration/security/hardening/) for broader server and WordPress hardening practices.

## Historical note

This page was created after a February 2024 vulnerability affecting Bricks versions before 1.9.6.1. Bricks 1.9.6.1 included the security patch for that vulnerability. For current sites, the guidance is simpler: keep Bricks on the latest available version and follow the recovery checklist above if you suspect compromise.

---

# Code review

Source: https://academy.bricksbuilder.io/builder/features/code-review/

*Review custom code in Bricks before signing it globally or investigating a security issue.*

The **Code review** screen helps you find and inspect custom code stored in Bricks before you sign code globally or investigate a security issue.

It is a reporting and inspection tool. It does not store an approval state and does not mark code as permanently "reviewed". Use it to inspect code instances, check signature status, and decide what should be fixed, removed, allowlisted, or signed.

> **Note**
>
> Run a Code review before regenerating code signatures globally. Global signature regeneration signs all eligible code that Bricks finds, so you should review the code first.

## Start a Code review

Go to **Bricks > Settings > Custom code** and click **Start: Code review**.

![](https://academy.bricksbuilder.io/assets/bricks-settings-code-review.png)

<figcaption>

Code review results

</figcaption>

## What Bricks reviews

The Code review screen can show:

- **Code elements** that contain PHP/HTML code. If **Execute code** is enabled, the review also checks the code signature.
- **SVG elements** where **Source** is set to **Code**.
- **Query editor** code used in Query loops.
- **Component query properties** that contain Query editor code.
- **Global query records** that contain Query editor code.
- **Dynamic `echo:` tags** found in Bricks element settings.

The review scans Bricks data in pages, templates, components, global elements, and global queries. It groups results by page/template where possible, and groups component and global query results separately.

## Filters and navigation

Use the Code review filter to inspect:

- **All code instances**
- **Code elements**
- **SVG elements**
- **Query editor**
- **Echo tags**

The review screen includes **Show all**, **Individual**, **Previous**, and **Next** controls so you can inspect code one item at a time or review the full result list.

## Signature statuses

For code types that require signatures, Bricks shows one of these statuses:

- **Valid signature**: The stored signature matches the stored code. The code can run if code execution is enabled and the runtime gate allows it.
- **Invalid signature**: The stored signature does not match the current code. Bricks blocks execution.
- **No signature**: No signature is stored. Bricks blocks execution.

When available, Bricks also shows who signed the code and when it was signed.

## Location details

Each review item can include:

- The page, post type, template, component, or global query location.
- The element label.
- The element ID.
- Whether the item is a global element, component, global query, query, echo tag, or executable code item.
- The stored code in a read-only editor.

If the item belongs to a regular page or template, click the title to open it in the builder and edit the code there.

## Echo tag allowlist helper

Dynamic `echo:` tags can call PHP functions only when those function names pass the [`bricks/code/echo_function_names`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-echo_function_names/) allowlist check.

When the Code review finds `echo:` tags, Bricks collects the function names and shows a starter snippet that you can place in a child theme, custom plugin, or code-management plugin. The helper can also include function names detected in theme styles, global classes, and raw color palette values:

```php
add_filter( 'bricks/code/echo_function_names', function() {
  return [
    'my_allowed_function',
  ];
} );
```

Review the generated list before using it. Remove any functions you do not want Bricks dynamic data to call.

## Advantages of centralized code monitoring

- **Centralized code oversight:** Review Bricks-managed executable code from one settings screen instead of opening each page manually.
- **Signature visibility:** Find missing and invalid signatures before code fails on the frontend.
- **Safer global signing:** Inspect code before using the global **Regenerate code signatures** action.
- **Echo tag hardening:** See which function names are being requested through `echo:` tags and allowlist only the functions you trust.

## Security checklist

Before regenerating code signatures globally:

- Review every Code, SVG, Query editor, component, and global query item.
- Remove code you do not recognize.
- Fix invalid signatures by reviewing and signing the intended code again.
- Do not copy the full `echo:` allowlist snippet without checking each function.
- Back up the site before global signature regeneration.

---

# Code signatures

Source: https://academy.bricksbuilder.io/builder/features/code-signatures/

*Use Bricks code signatures to protect executable custom code from silent database changes.*

Code signatures protect executable Bricks code from being changed silently in the database.

> **Note**
>
> Code that requires a signature will not run when the signature is missing or invalid.

When code is signed, Bricks hashes the code with WordPress' `wp_hash()` function and stores the signature with the Bricks data. When the code runs, Bricks hashes the stored code again and compares it with the saved signature. If the values do not match, Bricks blocks execution.

## Elements that require code signatures

The following Bricks code locations require valid signatures to run:

- Code element PHP/HTML when **Execute code** is enabled
- SVG element with **Source** set to **Code**
- Query loop editor code
- Component query properties
- Global query records

Direct CSS and JavaScript in the Code element are rendered as CSS/JS output when the Code element executes. The signature gate applies to the executable PHP/HTML code field and the other executable code locations listed above.

## Required permissions

Code signatures are tied to the code execution security model:

- **Code execution** must be enabled under **Bricks > Settings > Custom code**.
- The user must have the Bricks **Execute code** capability.
- Manual signature generation in the builder is an administrator-level action in Bricks. Global signature regeneration requires WordPress `manage_options`.
- If `BRICKS_LOCK_CODE_SIGNATURES` is set to `true`, Bricks blocks new signature generation regardless of user permissions.
- Dangerous automatic builder signing is a separate opt-in flow. It is not recommended for normal production sites. It still requires code execution to be enabled, the Bricks **Execute code** capability, and unlocked code signatures.

If the Sign code action does not create or update a signature, confirm that code execution is enabled, your user has the Execute code capability, your user has administrator-level access, and code signatures are not locked.

AI clients can store and sign PHP in supported Bricks Code fields only when PHP abilities are explicitly enabled with `BRICKS_ENABLE_PHP_ABILITIES`. The connected user must use an application password and have `manage_options` and the Bricks **Execute code** capability. The same code execution and signature-lock checks still apply. See [AI Abilities and Skills](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/#optional-enable-php-execution).

## How to generate code signatures

You can generate code signatures for individual elements when editing them in the builder, view unsigned code for the current page, or regenerate signatures globally via the Bricks settings.

### Generate code signatures in the builder

Inside the builder, elements with unsigned executable code are highlighted in red. You'll also see a red fingerprint icon at the top of the structure panel.

![](https://academy.bricksbuilder.io/assets/bricks-query-editor-unsigned-code.png)

<figcaption>

Builder: Code, SVG, and Query editor with unsigned code

</figcaption>

#### Sign code for an individual element

![](https://academy.bricksbuilder.io/assets/bricks-builder-panel-sign-code.png)

To generate a code signature for an individual element while you edit it, click the **Sign code** button above the code editor. If your cursor is inside the code editor, you can also use `CMD/CTRL + R`. This action is available only when the required permissions are satisfied.

After signing, save the page so the updated code and signature are stored together.

### View and sign unsigned code in bulk

You can view and sign all elements with unsigned code on the current page by clicking the fingerprint icon at the top of the structure panel. The same icon is also available on individual unsigned elements in the structure panel.

![](https://academy.bricksbuilder.io/assets/bricks-builder-popup-unsigned-code.png)

### Sign all code globally via Bricks settings

To generate code signatures for your entire site, navigate to **Bricks > Settings > Custom code > Code signatures** in your WordPress dashboard.

Click **Regenerate code signatures**. This generates code signatures for all pages, templates, global elements, component element trees, component query properties, and global query records built with Bricks.

This action requires a nonce-verified admin request, `manage_options`, code execution capability, and unlocked code signatures. If CSS file loading is enabled, Bricks regenerates CSS files after successful global signature regeneration.

## Locking code signature generation {#lock-code-signatures}

In Bricks 1.11.1, the `BRICKS_LOCK_CODE_SIGNATURES` constant adds another layer of control for high-security environments.

When `BRICKS_LOCK_CODE_SIGNATURES` is set to `true`, Bricks prevents new code signatures from being generated, regardless of user permissions.

To enable this lock, define the constant before signing code:

```php
if ( ! defined( 'BRICKS_LOCK_CODE_SIGNATURES' ) ) {
    define( 'BRICKS_LOCK_CODE_SIGNATURES', true );
}
```

With this constant enabled, any attempt to generate a new code signature returns a "Code signatures are locked" error.

## When to regenerate signatures

> **Note**
>
> When updating Bricks from a version before 1.9.7, generating code signatures via **Bricks > Settings > Custom code** is mandatory for signed code locations to run. Perform a Code review first.

**After changing your WordPress salts or secret keys:** If the salts in `wp-config.php` change, existing Bricks code signatures become invalid.

**After site migration:** When moving a site to a new domain or server, regenerate signatures if the new environment uses different WordPress salts.

**After editing signed code:** Editing executable Bricks code changes the signed content. Review and sign the updated code before expecting it to run.

## Why code signatures?

Code signatures limit what an attacker can do with database-only access.

If someone can edit Bricks data in the database but cannot generate signatures, they can add malicious code, but Bricks will not execute it because the signature will be missing or invalid.

### Understanding WordPress salts

WordPress salts are secret values stored in `wp-config.php`. Bricks uses WordPress' hashing system, which depends on those salts, so signatures generated on one site environment may not match another environment with different salts.

If salts change, Bricks has to regenerate signatures from the current trusted code.

### Bricks code integrity verification process

1. **Code and signature generation:** When you sign code, Bricks stores a hash generated from the code.
2. **Code retrieval for execution:** When the code is loaded, Bricks retrieves the stored code and signature.
3. **Verification:** Bricks hashes the retrieved code again and compares it with the stored signature.
4. **Execution decision:** If the hashes match, the code can continue through the execution flow. A missing or mismatched signature blocks execution and returns a "No signature" or "Invalid signature" error.

## Why rotating WordPress salts regularly is a bad idea {#rotating-salts}

If you rotate the salts in your `wp-config.php` file, all existing Bricks code signatures become invalid. You need to manually regenerate them from **Bricks > Settings > Custom code > Code signatures** before signed code can run again.

Some plugins offer automatic salt rotation with the claim that it makes cracking passwords harder. That claim is incorrect. WordPress salts are not used for hashing user passwords. Rotating them provides no added protection against password theft or brute-force attacks.

What salt rotation does cause:

- Logs out all users by invalidating authentication cookies.
- Breaks nonces, which can disrupt form submissions and AJAX requests.
- Can break plugins that use salts for encryption or data integrity.
- Invalidates all Bricks code signatures.

Unless your site has been compromised, there is usually no practical reason to rotate salts. It introduces unnecessary breakage and instability.

## Why isn't code automatically signed by default? {#no-automatic-code-signing}

Bricks requires manual code signing to prevent a database-only compromise from becoming full code execution.

If someone gains access to your database, for example through another plugin vulnerability or compromised credentials without code execution capability, they could inject malicious code into Bricks data. That is serious, but it does not automatically mean they can run PHP on your server.

Because Bricks uses signatures tied to your site's WordPress salts, that attacker cannot make the code executable with database access alone. The injected code remains unsigned and Bricks blocks it.

If Bricks automatically signed code by default whenever an authorized user opened the builder, this protection would collapse. The attacker could plant malicious code and wait for an authorized user to load the builder. Manual signing forces a review checkpoint before code becomes executable.

## Dangerous automatic signing constants {#dangerous-automatic-signing}

Bricks includes two opt-in constants for controlled builder workflows where you deliberately accept the risk of automatic signing.

These constants are disabled by default. Define them as the boolean `true`, not as the string `'true'`.

> **Danger**
>
> We do not recommend enabling these constants on normal production sites. Do not enable them just to avoid the manual Sign code step.
>
> Automatic signing reduces the protection that code signatures are designed to provide. If an attacker, vulnerable plugin, compromised integration, or database-level process can change Bricks data, they may be able to store malicious executable code and wait for a trusted user to open, rerender, or save the builder. With automatic signing enabled, that builder action can turn the stored code into signed code.
>
> Use these constants only when you fully accept that tradeoff, for example in a local development site, disposable sandbox, or tightly controlled internal workflow with additional hardening around database writes, plugins, integrations, users, and deployment access.

| Constant | What it signs |
| --- | --- |
| `BRICKS_DANGEROUSLY_AUTO_SIGN_CODE_ON_BUILDER_SAVE` | Eligible executable code included in a builder save request, including page or template elements, global elements, component element trees, component query properties, and global query records. |
| `BRICKS_DANGEROUSLY_AUTO_SIGN_CODE_ON_BUILDER_RERENDER` | Eligible executable code included in builder preview and rerender requests. Bricks returns the generated signature metadata to the builder so it can update the in-memory element data. A later builder save persists that updated data. |

Example:

```php
if ( ! defined( 'BRICKS_DANGEROUSLY_AUTO_SIGN_CODE_ON_BUILDER_SAVE' ) ) {
    define( 'BRICKS_DANGEROUSLY_AUTO_SIGN_CODE_ON_BUILDER_SAVE', true );
}

if ( ! defined( 'BRICKS_DANGEROUSLY_AUTO_SIGN_CODE_ON_BUILDER_RERENDER' ) ) {
    define( 'BRICKS_DANGEROUSLY_AUTO_SIGN_CODE_ON_BUILDER_RERENDER', true );
}
```

Neither constant bypasses code execution permissions or `BRICKS_LOCK_CODE_SIGNATURES`. If code execution is disabled, the current user cannot execute code, or code signatures are locked, Bricks will not generate signatures automatically.
