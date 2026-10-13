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