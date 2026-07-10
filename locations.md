---
layout: page
title: "Collection Locations"
permalink: /locations/
---

This archive contains geospatial and habitat data for all collected algal specimens.

## Specimen Logs by Location
{% for post in site.tags["Collection locations"] %}
### [{{ post.title }}]({{ post.url }})
* **Locality:** {{ post.locality }}
{% endfor %}
