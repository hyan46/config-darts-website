---
title: 'Rapid Detection of Hot-Spots via Tensor Decomposition with Applications to Crime Rate Data'
authors:
  - Yujie Zhao
  - Hao Yan
  - Sarah Holte
  - Yajun Mei
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
date: '2021-01'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['2']

# Publication name and optional abbreviated publication name.
publication: '*Journal of Applied Statistics*'
publication_short: ''

abstract: "We propose an efficient statistical method (denoted as SSR-Tensor) to robustly and quickly detect hot-spots that are sparse and temporal-consistent in a spatial-temporal dataset through the tensor decomposition. Our main idea is to first build an SSR model to decompose the tensor data into a Smooth global trend mean, Sparse local hot-spots and Residuals. Next, tensor decomposition is utilized as follows: basis are introduced to describe within-dimension correlation and tensor products are used for between-dimension interaction. Then, a combination of LASSO and fused LASSO is used to estimate the model parameters, where an efficient recursive estimation procedure is developed based on the large-scale convex optimization, where we first transform the general LASSO optimization into regular LASSO optimization and apply FISTA to solve it with the fastest convergence rate. Finally, a CUSUM procedure is applied to detect when and where the hot-spot event occurs. We compare the performance of the proposed method in a numerical simulation and a real-world dataset, which is a collection of three types of crime rates for U.S. mainland states during the year 1965-2014. In both cases, the proposed SSR-Tensor is able to achieve the fast detection and accurate localization of the hot-spots."



# Summary. An optional shortened abstract.
summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
  - Source Themes
featured: false

links:
- name: 'Publication link'
url: 'www.public.asu.edu/~hyan46/publication/zhao-rapid-2021/'
url_pdf: 'www.public.asu.edu/~hyan46/publication/zhao-rapid-2021/zhao-rapid-2021.pdf'


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides:
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

Supplementary notes can be added here, including [code and math](https://wowchemy.com/docs/content/writing-markdown-latex/).
