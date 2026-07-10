---
layout: page
title: "Strain Information"
permalink: /strains/
---

Access comprehensive strain IDs, taxonomic lineages, and morphology metadata. All the taxonomic names I may put on these strains are strictly to describe what it looks most like. There is a lot more diversity in species than previously anticipated and will need to be verified in the future with genetic data.

## Catalogued Strains
{% for post in site.tags["Strain information"] %}
* [{{ post.title }}]({{ post.url }}) - *Strain: {{ post.strain_id }}*
{% endfor %}
