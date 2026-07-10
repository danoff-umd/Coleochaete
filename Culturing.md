---
layout: page
title: "Culturing Notes"
permalink: /culturing/
---

Growth media requirements, light regimes, and protocols for maintaining viable strains. Most media preparation can also be found on https://utex.org/pages/algal-culture-media

## Active Culture Protocols
{% for post in site.tags["Culturing notes"] %}
### [{{ post.title }} Culture Protocol]({{ post.url }})
{{ post.culture_brief }}
{% endfor %}
