---
title: ''
summary: ''
date: 2026-11-18
type: landing

sections:
  - block: resume-biography-3
    id: about
    content:
      username: me
      text: |-
        I am an Associate Professor in the PCSAS-accredited Clinical Science PhD program at the University of New Mexico, an Investigator at the [Center on Alcohol, Substance use, And Addictions (CASAA)](https://casaa.unm.edu/), and a licensed clinical psychologist. I direct the [Behavioral Addictions And Associated Disorders (BAAAD) Lab](lab/).

        My research focuses on addictive behaviors that are reshaping public health: the rapid spread of legal sports betting and newer products such as prediction markets, compulsive sexual behavior, and alcohol use that co-occurs with both. Much of this work uses large, nationally representative longitudinal panels and intensive daily methods to understand who develops problems, how problems change over time, and how policy and social context shape those trajectories. A long-running line of work examines moral incongruence, or how people's moral beliefs shape whether they see their own behavior as an addiction.

        I am committed to open, transparent, and reproducible science, and I regularly share findings with clinicians, policymakers, regulators, and the public. I am available for [speaking, training, consultation, and expert witness work](speaking/).
      button:
        text: View CV
        url: https://drive.google.com/open?id=1FHGTXObvEooYboxzVN7rRlxbRhQlTk4p&usp=drive_fs
      headings:
        about: 'About'
        education: 'Education'
        interests: 'Research Interests'
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: research-areas
    id: research
    content:
      title: Research Areas
      subtitle: ''
      text: ''
      items:
        - name: Gambling & Sports Betting
          description: Problem gambling in the era of legal sports wagering, including policy effects, betting behavior tracked over time, and whether prediction markets function as gambling.
          icon: hero/presentation-chart-bar
          topics:
            - Sports betting
            - Gambling policy
            - Prediction markets
          cta:
            text: Learn more
            url: projects/sports-betting/
        - name: Compulsive Sexual Behavior
          description: Assessment, classification, and course of compulsive sexual behavior disorder and problematic pornography use, studied in national and international samples.
          icon: hero/light-bulb
          topics:
            - CSBD
            - Pornography use
            - Assessment
          cta:
            text: Publications
            url: tags/compulsive-sexual-behavior/
        - name: Moral Incongruence & Religion
          description: How conflict between moral or religious beliefs and behavior shapes distress, self-perceived addiction, and help-seeking.
          icon: hero/scale
          topics:
            - Moral incongruence
            - Religion & spirituality
            - Self-perception
          cta:
            text: Learn more
            url: projects/moral-incongruence/
        - name: Alcohol & Co-occurring Addictions
          description: How drinking and other substance use travel with gambling, from daily links between betting and drinking to population trends after sports betting legalization.
          icon: hero/beaker
          topics:
            - Alcohol use
            - Daily (EMA) methods
            - Comorbidity
          cta:
            text: Learn more
            url: projects/sports-betting-alcohol-center/
        - name: Veterans' Behavioral Health
          description: Gambling disorder, substance use, and related problems among U.S. veterans, including a dedicated initiative on gambling in women veterans.
          icon: hero/user-group
          topics:
            - Veterans
            - Gambling disorder treatment
            - Women veterans
          cta:
            text: Learn more
            url: projects/veterans-gambling/
        - name: Longitudinal & Open Science
          description: Large, nationally representative panels followed over years, daily diary and EMA designs, and a commitment to transparent, reproducible methods.
          icon: hero/chart-bar
          topics:
            - Panel studies
            - EMA
            - Open science
    design:
      layout: cards

  - block: stats
    content:
      items:
        - statistic: '190+'
          description: Peer-reviewed journal articles
          icon: hero/document-text
        - statistic: '13,800+'
          description: Citations (Google Scholar)
          icon: hero/chart-bar
        - statistic: '60'
          description: h-index
          icon: hero/academic-cap
    design:
      layout: compact

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
      count: 9
    design:
      view: citation

  - block: collection
    content:
      title: Recent Publications
      text: ''
      count: 8
      filters:
        folders:
          - publications
        exclude_featured: false
        exclude_future: false
    design:
      view: citation

  - block: cta-card
    content:
      title: Speaking, Training & Consultation
      text: |-
        I give keynotes, continuing education workshops, and trainings on gambling, sports betting, and compulsive sexual behavior, and I consult with organizations, regulators, and attorneys.
      button:
        text: Learn more
        url: speaking/
    design:
      card:
        css_class: 'bg-primary-100 dark:bg-primary-900'
---
