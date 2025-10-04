# Setup Cloudflare domain on Github Page

1. Register and buy a domain on Cloudflare.
2. In DNS tab, adding CNAME records to the Github Page URL.
   - type: `CNAME`, name: `@`, target: `<github-page-url>`
   - type: `CNAME`, name: `www`, target: `<github-page-url>`
3. In SSL/TLS tab, setting SSL/TLS encryption mode to `Full`.
4. In SSL/TLS tab, enabling `Always Use HTTPS`.
5. In SSL/TLS tab, enabling `Automatic HTTPS Rewrites`.
6. In Github repository settings, adding a custom domain.
7. In Github repository settings, enabling `Enforce HTTPS`.
