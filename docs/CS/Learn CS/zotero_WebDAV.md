---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 10min
publish_date: 2024.09.28
---

I'm trying to set-up a WebDAV server on my own MAC computer for my zotero synchronization.

Using the Apache Web Server.

Start Apache:

```bash 
sudo apachectl start
```

Enable WebDAV functionality by modifying the configuration file.

```bash
sudo vim /etc/apache2/httpd.conf
```

And delete the `#` in front of the two following lines:

```bash
LoadModule dav_module libexec/apache2/mod_dav.so
LoadModule dav_fs_module libexec/apache2/mod_dav_fs.so
```

Then create a directory to store the files to be shared via WebDAV. Apache also requires access to the parent directory of the WebDAV directory.

```bash
mkdir /Users/lumizhang/zotero_webdav
sudo chown -R _www:_www /Users/lumizhang/zotero_webdav
sudo chmod -R 755 /Users/lumizhang/zotero_webdav
sudo chmod 755 /Users/lumizhang
```

Then add the following lines to the configuration file:

```bash
<Directory "/Users/lumizhang/zotero_webdav">
    Dav On
    AuthType Basic
    AuthName "WebDAV login"
    AuthUserFile /etc/apache2/users.password
    Require valid-user
</Directory>
```

Then create a password file:

```bash
sudo htpasswd -c /etc/apache2/users.password lumizhang
```

Remember to add a lock database for Apache WebDAV implementation. This is done by adding the following line to the configuration file:

```bash
DAVLockDB "/Users/lumizhang/zotero_webdav/locks/DAVLockDB"
```

The lock database doesn't necessarily have to be in the webdav folder, but I put it there since Apache have the access. 


Then restart the Apache server:

```bash
sudo apachectl restart
```

Then you can access the WebDAV server via the following URL: http://chocolate-icecream.local/zotero/.

Then you go to Zotero and set up the sync location.



