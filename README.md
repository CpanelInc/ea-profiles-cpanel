# Making different profiles available based on the server’s current state

## Goal

Make different EA4 profiles available to the EA4 UI/CLI based on some factor like license type or if a plugin is installed (anything really).

## Situation

Doing the logic in ULC would be complicated and would hit the “ULC update problem”.

Since the pkg built for an OS will own the same files we can’t simply munge them in post because it’d look like the pkg’s files were modified. Making them config files compounds the problem.

## Solution

Instead of installing directly to `/etc/cpanel/ea4/profiles/cpanel/` we:

1. Install directly to `/opt/cpanel/ea-profiles-cpanel/`.
2. Have a script that ensures `/etc/cpanel/ea4/profiles/cpanel/` contains the correct symlinks to `/opt/cpanel/ea-profiles-cpanel/` for the server based on its state **at that moment**.
   * `/opt/cpanel/ea-profiles-cpanel/bin/update-available-profiles`
3. Call that script in post (install and upgrade).
4. On uninstall remove `/etc/cpanel/ea4/profiles/cpanel/`
   * Because the pkg does not own this directory (and can’t because deb has no equiv to RPM’s `%DIR`)
5. When the servers state changes that script will need run also.
   * We don’t really support license type changes so that is moot.

Other vendors can do the same, just need to `s/cpanel/your-name/g` in the info above 👍
