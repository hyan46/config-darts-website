---
title: Crime in US
date: 2020-12-02
image:
  focal_point: 'top'
---

Our DARTS methodology has been used in identifying how crime hotspots have emerged throughout the US over time.

Abstract: We propose an efficient statistical method (denoted as SSR-Tensor) to robustly and quickly detect hot-spots that are sparse and temporal-consistent in a spatial-temporal dataset through the tensor decomposition. Our main idea is to first build an SSR model to decompose the tensor data into a Smooth global trend mean, Sparse local hot-spots and Residuals. Next, tensor decomposition is utilized as follows: basis are introduced to describe within-dimension correlation and tensor products are used for between-dimension interaction. Then, a combination of LASSO and fused LASSO is used to estimate the model parameters, where an efficient recursive estimation procedure is developed based on the large-scale convex optimization, where we first transform the general LASSO optimization into regular LASSO optimization and apply FISTA to solve it with the fastest convergence rate. Finally, a CUSUM procedure is applied to detect when and where the hot-spot event occurs. We compare the performance of the proposed method in a numerical simulation and a real-world dataset, which is a collection of three types of crime rates for U.S. mainland states during the year 1965-2014. In both cases, the proposed SSR-Tensor is able to achieve the fast detection and accurate localization of the hot-spots.



<!--more-->

Publications: https://www.public.asu.edu/~hyan46/publication/zhao-rapid-2021/

<iframe
    src="https://30days.streamlit.app/?embed=true"
    height="450"
    style="width:100%;border:none;"
></iframe>