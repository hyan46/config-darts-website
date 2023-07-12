---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Detecting Anomalies in Real-Time Survelliance
      image:
        filename: welcome.jpg
      text: |
        <br>
        
        The **Detecting Anomalies in Real-Time Research Group** has been a center of excellence for Artificial Intelligence research, teaching, and practice since its founding in 2016.

  - block: hero
    content: 
      title: Methods
      image:
        filename: TST_Data.png
      cta:
        label: Get Started
        url: ../config-darts-website/methods
    # link: ../methods/

  - block: hero
    content: 
      title: Current Project
      image:
        filename: US_over_time_gon.png
      cta:
        label: View
        url: ../config-darts-website/current/
    # link: ../methods/


  
  - block: collection
    content:
      title: Past Projects
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: past
    design:
      view: card
      columns: '1'
  
  # - block: slider
  #   content:
  #     slides:
  #     - title: Our Methods
  #       content: Tensor Spatial-temporal Data Decomposition Method
  #       align: center
  #       background:
  #         image:
  #           filename: TST_Data.png
  #           filters:
  #             brightness: 1
  #         position: right
  #         color: '#666'
  #     - title: View our results on our most recent project
  #       content: 'Tensor Decomposition for Anomaly Detection with Gonorrhea'
  #       align: right
  #       background:
  #         image:
  #           filename: US_over_time_gon.png
  #           filters:
  #             brightness: 1
  #         position: center
  #         color: '#333'
  #       link:
  #         icon: graduation-cap
  #         icon_pack: fas
  #         text: Join Us
  #         url: ../current/
  # - block: markdown
  #   content:
  #     title: Past Projects
  #     subtitle: 'COVID in WA'
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

  # - block: markdown
  #   content:
  #     title: 
  #     subtitle: 'Crime in NYC'
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
