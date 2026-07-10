---
layout: page
title: "Associated Literature"
permalink: /literature/
---

A compiled bibliography of peer-reviewed journal articles, books, and references associated with my repository. I have several physical copies of some of the older literature.

## References by Taxon
{% for post in site.tags["Associated Literature"] %}
### {{ post.title }} References
{{ post.literature_citations }}
{% endfor %}
