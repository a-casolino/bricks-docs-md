*Understand how saving and publishing work in Bricks, including drafts, updates, and when frontend changes go live.*

Bricks, by default, automatically creates an autosave every 60 seconds when the current builder area has unsaved element changes.

Autosave creates a backup copy of the elements on the canvas. It does not save global data such as components, classes, or variables. Autosaves can be restored under **Manage > History / Revisions** from the builder toolbar.

To adjust or disable the autosave interval go to **Bricks > Settings > Builder** in your WordPress admin area. The default interval is 60 seconds, and the minimum interval is 15 seconds.

Bricks detects unsaved changes and will show you a prompt to help prevent data loss in case you reload the builder by accident.

To manually save your changes, click the **Save** (disk) icon in the builder toolbar or use the default `CMD/CTRL + S` shortcut. Save writes to the version you are editing: Live, a Bricks page draft, or a named site version. In Bricks 2.5, you can change the shortcut under **Manage → Keyboard shortcuts**. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/).

For live page changes, **Bricks creates a revision/snapshot** when changed Bricks data or page settings are saved using the standard WordPress Revisions API ([learn more about revisions](https://academy.bricksbuilder.io/builder/interface/revisions/)). Saving into a Bricks draft keeps pending changes separate from that live-page save.

Customize the save messages with the [bricks/builder/save_messages](https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages/) filter.

## Save pending changes without publishing {#drafts}

Bricks 2.5 offers experimental [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/), disabled by default. Enable **Bricks > Settings > Builder > Drafts > Enable drafts**, then open **Live** beside Save and choose **Save page as draft**. The label follows the post type.

While the switcher shows **Draft**, Save continues saving into that draft. Select **Publish** to review its changes before making them live, or **Discard** to remove its pending changes. On narrower screens, these actions appear in the version menu. Save while **Live** is selected still saves directly to the live version.

Changes to shared items already used on live pages stay in the draft until publication. Reusable items that do not affect live content become available across the site immediately, so you can use a new class on other pages and templates while working. Read [what stays in a draft](https://academy.bricksbuilder.io/builder/interface/drafts/#shared-data) for the full rules and examples.

Use a named [site version](https://academy.bricksbuilder.io/builder/interface/site-versions/) for work across several pages, and [review links](https://academy.bricksbuilder.io/builder/interface/review-links/) to let someone without a login preview pending work.

## Saving shared data from multiple Builder sessions {#save-conflicts}

Since Bricks 2.5, conflict-safe saving is always active for shared data such as global classes, components, Theme Styles, variables, palettes, global queries and filters, and custom fonts. There is no setting to enable it.

If two people edit different shared items, Bricks merges those changes when they save. For example, one person can update a button class while another updates a card component. Saving from an older Builder session does not replace the other person's unrelated update.

If both sessions change the same shared item, Bricks pauses the save and asks which version to keep. This can also happen when you have the Builder open in two tabs. Resolve the conflicts before treating the page or shared-data changes as saved.

### Resolving a conflict

1. In the conflict notification, click **Overview changes** to open **Conflict details**.
2. Select a resource group or expand an item to compare its **Saved version** with **My version**. The saved version is the version currently on the site; your version is the one in this Builder session.
3. Choose which version to keep for each item. The dialog initially selects **Saved version**. Use **All items** only when you want the same choice for every item in the dialog.
4. Click **Use selected**. Resolve any other conflict notifications. After the final conflict is resolved, Bricks retries the save automatically.

![Conflict details comparing the demo global class: the saved typography color is white, while My version uses orange.](https://academy.bricksbuilder.io/assets/builder/save-publish/conflict-details-global-class.webp)

The notification also offers **Use saved version** and **Use my version** for applying one choice to its listed conflicts. Choosing your version can replace another person's work on those items. If you need changes from both versions, agree on the version to keep and reapply the remaining changes afterward.

If another session saves again while you are resolving conflicts, Bricks may ask you to review the updated conflicts. Wait for the save to finish before leaving the Builder.

Conflict-safe saving protects shared data such as global classes and components. It does not merge changes made by two people editing the same page at the same time. Legacy global elements are outside this protection. Autosave still backs up canvas elements rather than shared data, so keep your normal site backups.

## Publishing a WordPress draft post

Saving a page or post whose WordPress status is **Draft** does not publish that post. While editing its **Live** version, use the **Publish** action in the toolbar when it is ready to go public.

If you are editing a Bricks page draft, its **Publish** action first reviews and applies the pending Bricks changes. After returning to Live, publish the WordPress post separately if it is still unpublished. See [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) for the distinction.